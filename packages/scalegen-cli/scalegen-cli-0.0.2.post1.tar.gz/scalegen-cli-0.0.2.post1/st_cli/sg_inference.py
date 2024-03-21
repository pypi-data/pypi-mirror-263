# Standard modules
import os
from typing import Any, Dict, List, Union
from datetime import datetime

# Third-party modules
import click
from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import yaml

# Product modules
from .utils import print_to_string
from .client import get_garb, send_request
from .datamodels.datamodels.api import InferenceDeploymentIn, InferenceDeploymentStatus


def get_deployment(inf_id: str) -> Dict[str, Any]:
    console = Console()

    with console.status(
            f"[bold green]Getting deployment with inf_id {inf_id}..."
    ) as status:

        resp = send_request("GET", f"/sg_inf/{inf_id}")

    if resp.status_code == 204:
        click.echo(
            click.style(f"Deployment with inf_id {inf_id} not found", fg="red"),
            err=True,
        )
        exit()

    elif resp.status_code != 200:
        click.echo(click.style(f"Could not fetch deployment", fg="red"), err=True)
        exit()

    deployment = resp.json()
    return deployment


def get_deployments(should_exist: bool = True):
    console = Console()

    with console.status("[bold green]Getting existing deployments...") as status:

        resp = send_request("GET", "/sg_inf/list")

    if resp.status_code == 204:
        if should_exist:
            click.echo(
                click.style(
                    f"No deployments found. Create one with 'scalegen infer create'",
                    fg="blue",
                ),
                err=should_exist,
            )
        return []

    elif resp.status_code != 200:
        click.echo(click.style(f"Could not fetch deployments", fg="red"), err=True)
        exit()

    deployments = resp.json()
    deployments.sort(key=lambda dep: dep["name"])

    return deployments


def print_inference_deployments(
    deployments: List[Dict[str, Any]],
    table_title: str = "Inference Deployments",
    plain: bool = False,
):
    table = Table(
        show_header=True,
        # header_style='bold #2070b2',
        # title='[bold] Jobs',
        title=table_title,
        box=None if plain else box.DOUBLE_EDGE,
    )

    col_names = [
        "Inference ID",
        "Name",
        "Model",
        "Allow Spot Instances",
        "Current Price Per Hour",
        "Status",
        # "API Gateway",
    ]

    for col in col_names:
        table.add_column(col)

    provisioning = sorted([d for d in deployments if d['status'] == InferenceDeploymentStatus.PROVISIONING],
                          key=lambda dep: datetime.strptime(dep["timestamp"], '%Y-%m-%d %H:%M:%S.%f'), reverse=True)
    active = sorted([d for d in deployments if d['status'] == InferenceDeploymentStatus.ACTIVE],
                    key=lambda dep: datetime.strptime(dep["timestamp"], '%Y-%m-%d %H:%M:%S.%f'), reverse=True)
    inactive = sorted([d for d in deployments if d['status'] == InferenceDeploymentStatus.INACTIVE],
                      key=lambda dep: datetime.strptime(dep["timestamp"], '%Y-%m-%d %H:%M:%S.%f'), reverse=True)
    deleted = sorted([d for d in deployments if
                      d['status'] not in [InferenceDeploymentStatus.PROVISIONING, InferenceDeploymentStatus.ACTIVE,
                                          InferenceDeploymentStatus.INACTIVE]],
                     key=lambda dep: datetime.strptime(dep["timestamp"], '%Y-%m-%d %H:%M:%S.%f'), reverse=True)

    deployments = provisioning + active + inactive + deleted

    for depl in deployments:
        row = [
            depl["id"],
            depl["name"],
            depl["model"],
            str(depl["allow_spot_instances"]),
            str(depl["current_price_per_hour"]),
            depl["status"],
            # depl["link"],
        ]
        # if row[-1] is None:
        #     row[-1] = "Unavailable"
        # else:
        #     row[-1] = print_to_string(
        #         f"[link={depl['link'] + '/inference'}]Inference link[/link]\n"
        #         f"[link={depl['link'] + '/metrics'}]Metrics link[/link]",
        #         end="",
        #     )

        table.add_row(*row)

    console = Console()

    if table.row_count <= 15 or plain:
        console.print(table, justify="left")
    else:
        with console.pager():
            console.print(table, justify="left")


@click.group(name="infer", chain=True)
def infer():
    """
    ScaleGen commands for managing inference deployments
    """
    pass


def create_inf_dep(inf_dep_req_data: InferenceDeploymentIn, quiet: bool = False, force: bool = False):

    console = Console()

    with console.status("[bold green]Creating new deployment...") as status:
        resp = send_request("POST", "/sg_inf/create", data=inf_dep_req_data.model_dump(mode="json"))
        inf_id = ""

    if resp.status_code == 200:
        resp_data = resp.json()
        inf_id = resp_data["message"]["inf_id"]  # P-API returns dict for CREATE request
        click.echo(click.style(f"Created deployment - Id: {inf_id}", fg="green"))

    elif resp.status_code == 500:
        resp_data = resp.content.decode("utf-8")
        click.echo(
            click.style(
                f"Something went wrong: {resp_data}. Please try creating deployment later",
                fg="red",
            ),
            err=True,
        )
        exit()

    else:
        try:
            resp_data = resp.json()
            click.echo(
                click.style(f"Couldn't not create deployment: {resp_data}", fg="red"),
                err=True,
            )
        except Exception as e:
            click.echo(
                click.style(f"Couldn't not create deployment", fg="red"), err=True
            )
        exit()

    # Exit if quiet was passed
    if not quiet:
        print_inference_deployments(
            [get_deployment(inf_id)],
            table_title="New Deployment Added",
        )


@infer.command("create")
@click.option("--model", type=click.STRING, required=True, help="Model to use")
@click.option("--max_price_per_hour", type=click.INT, required=True, help="The maximum price you are willing to spend per hour")
@click.option("--allow_spot_instances", type=click.BOOL, required=False, default=False, help="Use spot instances")
@click.option("--name", type=click.STRING, required=True, help="Deployment name to use")
@click.option("--hf_token", type=click.STRING, required=False, default=None, help="Hugging Face token to use")
@click.option("--logs_store", type=click.STRING, required=False, help="Logs store to use")
@click.option("--enable_speedup_shared", type=click.BOOL, required=False, default=False, help="Enable fast auto scaling using shared capacity")
@click.option("--type", type=click.Choice(["embedding", "llm"]), required=True, help="Inference deployment type to use")
@click.option("--min_workers", type=click.INT, required=False, default=0, help="The minimum number of workers to scale down to")
@click.option("-f", "--force", is_flag=True)
@click.option("-q", "--quiet", is_flag=True)
def create_impl(
        model,
        max_price_per_hour,
        allow_spot_instances,
        name,
        hf_token,
        logs_store,
        enable_speedup_shared,
        type,
        min_workers,
        force,
        quiet,
):
    """
    Create an inference deployment
    """

    # Get existing deployments
    deployments = get_deployments(should_exist=False)

    # Check if there is already a deployment with the same model
    similar_deployments = list(
        map(lambda x: x["id"], filter(lambda x: x["model"] == model, deployments))
    )
    if similar_deployments and not force:
        # If exists, Warn the user
        if not click.confirm(
            click.style(
                f"This model is already deployed with id(s): {similar_deployments}. Do you want to continue?",
                fg="yellow",
            )
        ):
            exit()

    # Make request to P-API
            
    if not type in [ "llm", "embedding" ]:
        click.echo(
            click.style(
                f"\nType value must be one of [ llm , embedding ]",
                fg="red",
            ),
            err=True,
        )
        exit()

    data = {
        "name": name,
        "model": model,
        "inf_type": type,
        "hf_token": hf_token,
        "allow_spot_instances": allow_spot_instances,
        "logs_store": logs_store,
        "cloud_providers": [],
        "initial_worker_config": {
            "min_workers": min_workers,
        },
        "autoscaling_config": {
            "enable_speedup_shared": enable_speedup_shared,
        },
        "max_price_per_hour": max_price_per_hour,
    }

    inf_dep_req_data = InferenceDeploymentIn(**data)

    create_inf_dep(inf_dep_req_data, quiet=quiet, force=force)


@infer.command("launch")
@click.argument("config_file", type=click.STRING, required=True)
@click.option("-f", "--force", is_flag=True)
@click.option("-q", "--quiet", is_flag=True)
def launch_impl(config_file, force, quiet):
    """
    Launch an inference deployment using a config YAML file
    """
    # check if config_file is an absolute path
    if not os.path.isabs(config_file):
        config_path = os.path.join(os.getcwd(), config_file)

    if not os.path.exists(config_path):
        click.echo(
            click.style(
                f"{config_path} not found. Please specify a valid config file path",
                fg="red",
            ),
            err=True,
        )
        return

    with open(config_path, "r") as fp:
        config_yaml = fp.read()
        dict_from_yaml = yaml.safe_load(config_yaml)

    try:
        inf_dep_create_req = InferenceDeploymentIn(**dict_from_yaml)  # Valid config
    except Exception as e:
        click.echo(click.style(f"Validation Error: {e}", fg="red"), err=True)
        exit()
    
    create_inf_dep(inf_dep_create_req, quiet, force)



@infer.command("start")
@click.option("--inf_id", type=click.STRING, required=True)

@click.option('-f', '--force', is_flag=True)
@click.option("-q", "--quiet", is_flag=True)
def start_impl(inf_id, force, quiet):
    """
    Allows user to make the InferenceDeployment Active in case
    its been scaled to zero because of no-requests (status is INACTIVE)
    """

    def _check_if_deployment_already_started(inf_id: str):
        console = Console()

        with console.status(
                f"[bold green]Getting deployment with inf_id {inf_id}..."
        ) as status:

            resp = send_request("GET", f"/sg_inf/{inf_id}/gpu_nodes_ips")
            resp_json = ""

        if resp.status_code == 200:
            # Fetched GPU nodes successfully
            resp_data = resp.json()
            # return True
        elif resp.status_code == 500:
            resp_data = resp.content.decode("utf-8")
            click.echo(
                click.style(
                    f"\nSomething went wrong: {resp_data}. Please try fetching deployment GPU nodes later",
                    fg="red",
                ),
                err=True,
            )
            return False
        else:
            try:
                resp_data = resp.json()
                click.echo(
                    click.style(
                        f"\nCould not fetch deployment GPU nodes: {resp_data}", fg="red"
                    ),
                    err=True,
                )
            except Exception as e:
                click.echo(
                    click.style(f"\nCould not fetch deployment GPU nodes", fg="red"),
                    err=True,
                )
            return False

        if (len(resp_json) > 0) and not force:
            # If there are already existing GPU nodes, Warn the user
            if not click.confirm(
                    click.style(
                        f"Deployment {inf_id} already running with {len(resp_json)} GPU nodes. Do you want to continue scaling up?",
                        fg="yellow",
                    )
            ):
                exit()

    if not _check_if_deployment_already_started(inf_id):
        exit()

    console = Console()

    with console.status(
        f"[bold green]Scaling deployment with inf_id {inf_id}..."
    ) as status:
        
        resp = send_request("POST", f"/sg_inf/{inf_id}/scale/up")

    if resp.status_code == 200:
        resp_data = resp.json()
        click.echo(
            click.style(
                f"\nScaled deployment up with Id: {inf_id} successfully", fg="green"
            )
        )
    elif resp.status_code == 500:
        resp_data = resp.content.decode("utf-8")
        click.echo(
            click.style(
                f"\nSomething went wrong: {resp_data}. Please try scaling deployment later",
                fg="red",
            ),
            err=True,
        )
        exit()
    else:
        try:
            resp_data = resp.json()
            click.echo(
                click.style(
                    f"\nCould not scale up deployment: {resp_data}", fg="red"
                ),
                err=True,
            )
        except Exception as e:
            click.echo(
                click.style(f"\nCould not scale up deployment", fg="red"), err=True
            )
        exit()

    # Exit if quiet was passed
    if not quiet:
        print_inference_deployments(
            [get_deployment(inf_id)], 
            table_title="Deployment started!",
        )


@infer.command("delete")
@click.argument("inf_id", type=click.STRING, required=True)
@click.option("-q", "--quiet", is_flag=True)
def delete_impl(inf_id, quiet):
    """
    Delete an inference deployment
    """

    console = Console()

    with console.status(
            f"[bold green]Deleting deployment with inf_id {inf_id}..."
    ) as status:

        resp = send_request("DELETE", f"/sg_inf/{inf_id}")

    if resp.status_code == 200:
        resp_data = resp.json()
        click.echo(
            click.style(
                f"\nDelete request for deployment with id: {inf_id} is successful",
                fg="green",
            )
        )
    elif resp.status_code == 500:
        resp_data = resp.content.decode("utf-8")
        click.echo(
            click.style(
                f"\nSomething went wrong: {resp_data}. Please try deleting deployment later",
                fg="red",
            ),
            err=True,
        )
        exit()
    else:
        try:
            resp_data = resp.json()
            click.echo(
                click.style(f"\nCould not delete deployment: {resp_data}", fg="red"),
                err=True,
            )
        except Exception as e:
            click.echo(
                click.style(f"\nCould not delete deployment", fg="red"), err=True
            )
        exit()
    
    if not quiet:
        print_inference_deployments(
            [get_deployment(inf_id)], 
            table_title="Deployment deleted!",
        )


@infer.command("list")
@click.option("-p", "--plain", is_flag=True)
def list_impl(plain):
    """
    Print the list of existing inference deployments
    """

    # Get existing deployments
    deployments = get_deployments(should_exist=True)

    print_inference_deployments(deployments, plain=plain)


@infer.command("view")
@click.argument("inf_id", type=click.STRING, required=True)
def view_impl(inf_id):
    """
    Print information about a single inference deployment
    """

    console = Console()
    inf_dep = get_deployment(inf_id)

    markdown_content = (
        f"[bold][orange_red1]ID[/orange_red1] : [cyan]{inf_dep['id']}[/cyan]\n"
    )
    markdown_content += (
        f"[orange_red1]Name[/orange_red1] : [yellow]{inf_dep['name']}[/yellow]\n"
    )
    markdown_content += (
        f"[orange_red1]Status[/orange_red1] : [yellow]{inf_dep['status']}[/yellow]\n"
    )
    markdown_content += f"[orange_red1]Cost[/orange_red1] : [yellow]$ {round(inf_dep['current_price_per_hour'], 3)}[/yellow]\n"
    markdown_content += f"[orange_red1]Model[/orange_red1] : [yellow]{inf_dep['model']}[/yellow]\n"
    markdown_content += f"[orange_red1]Endpoint[/orange_red1] : [yellow]{inf_dep['link']}/inference[/yellow]\n"
    markdown_content += f"[orange_red1]APIKey[/orange_red1] : [yellow]{get_garb('AUTH_ENDPOINT_KEY_' + inf_id)}[/yellow]\n"


    console.print(Panel(markdown_content))
