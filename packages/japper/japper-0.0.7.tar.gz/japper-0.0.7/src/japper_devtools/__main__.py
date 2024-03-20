import os
import subprocess
import rich_click as click
from rich.console import Console
from rich.panel import Panel

console = Console()

from .project_init import init_project_cli
from .utils import save_config, load_config, build_docker_image, check_cur_conda_env, prompt, confirm, run_command

WORKING_DIR = os.getcwd().replace('\\', '/')
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_config():
    config = load_config()
    if config is None or 'project_name' not in config:
        console.print("No project found. Please run 'japper init' first.", style='bold red')
        exit(-1)
    return config


@click.group()
def cli():
    pass


@click.command(help='Initiate a new Japper project')
@click.option('-g', '--gui', help="use GUI mode", default=False, is_flag=True)
@click.option('-mg', '--mygeohub', help="create MyGeoHub Tool structure", default=False, is_flag=True)
def init(gui, mygeohub):
    if gui:
        pass
    else:
        init_project_cli(mygeohub=mygeohub)


@click.command(help='Run this Japper project')
@click.argument('mode', type=click.Choice(['dev', 'preview']))
@click.option('-v', '--verbose', help="verbose mode", default=False, is_flag=True)
def run(env, verbose):
    """
    Run the project in a specified environment.
    """

    # todo: handle preview mode in both dev or appmode

    config = get_config()
    if config['dev_env'] == 'manual':
        console.print("The project is set to run in manual mode. Please run the project manually.", style='bold yellow')
        return

    log_file = f'{WORKING_DIR}/japper_run.log'
    # clean the log
    with open(log_file, 'w') as f:
        f.write('')

    console.print("Running the project in %s mode" % ('production preview' if env == 'prod' else 'development'),
                  style="bold magenta")

    if config['dev_env'] == 'docker':
        # Build the docker image
        build_docker_image(env, quiet=not verbose)
        cmd = f'cd container/{env} && docker-compose up --remove-orphans'

    elif config['dev_env'] == 'conda':
        # check env fist
        check_cur_conda_env(config['conda']['env_name'])
        cmd = "voila ./app.ipynb --no-browser --port=8888 --debug --show_tracebacks=True"
        if env == 'dev':
            cmd = f"""{MODULE_DIR}/parallel_cmd.sh "{cmd}" "jupyter lab --allow-root --no-browser --port=8889 --IdentityProvider.token='' --ServerApp.password=''" """

    console.print(f"Starting the app using {config['dev_env']}", style='bold cyan')
    if not verbose:
        console.print(
            f"  App running logs are being written to file:///{log_file}\n"
            + "  You can use -v or --verbose option to see the logs.", style='yellow')

    # Message for container being up
    container_up_msg = f"[green]Japper App [bold magenta]{config['project_title']}[/bold magenta] is running [{config['dev_env']}]\n\n" + \
                       " - App:   http://localhost:8888/"
    if env == 'dev':
        container_up_msg += "\n - JuptyerLab: http://localhost:8889/lab"
    container_up_msg += "\n\n[yellow]Press Ctrl+C to stop the container"

    voila_running = False
    jupyterlab_running = False
    if env == 'prod':
        jupyterlab_running = True  # no JupyterLab in production
    container_initialized = False

    # Initialize the Docker container
    with console.status("[bold deep_sky_blue1] Initializing the app running environment...") as status:
        process = subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            text = process.stdout.read1().decode("utf-8")
            if verbose:
                print(text, end='', flush=True)
            else:
                with open(log_file, 'a') as f:
                    f.write(text)

            if not container_initialized:
                if '[Voila] Voilà is running at:' in text:
                    voila_running = True
                if 'Jupyter Server' in text and 'is running at:' in text:
                    jupyterlab_running = True
                if voila_running and jupyterlab_running:
                    status.update(Panel(container_up_msg), spinner='dots', speed=0.1)
                    container_initialized = True

            if process.poll() is not None:
                break
        ret = process.poll()

    # Check the return code of the process
    if ret != 0 and ret != 33280 and not verbose:
        console.print(
            f'Failed to start the app. ' +
            f'Please check the logs in file:///{log_file}',
            style='bold red')
        exit(-1)

    console.print("App stopped", style='bold yellow')


@click.command(help="Build this Japper project")
@click.argument('mode', type=click.Choice(['docker', 'hubzero']))
def build(mode):
    config = get_config()
    if mode == 'docker':
        console.print("Building the Docker image in production environment", style='bold cyan')
        build_docker_image('prod')
        console.print(f"Docker image built successfully. Please check the image '{config['project_name']}'",
                      style='bold green')


@click.command(help="Deploy this Japper project")
@click.argument('target', type=click.Choice(['registry']), default='registry')
@click.option('-t', '--tag', help="tag for container image", default='latest')
def deploy(target, tag):
    config = get_config()
    if target == 'registry':
        if 'registry_url' not in config:
            registry_url = prompt("Enter the Docker registry URL", default='docker.io')
            # validate the registry URL
            if registry_url[:4] == 'http':
                registry_url = registry_url.split('//')[1]
            if registry_url[-1] == '/':
                registry_url = registry_url[:-1]

            if registry_url == 'docker.io':
                registry_namespace = prompt("Enter the docker.io username")
            else:
                registry_namespace = prompt("Enter the Docker registry namespace (optional)", optional=True)

            registry_image_name = prompt("Enter the remote image name", default=config['project_name'])

            config['registry_url'] = registry_url
            config['registry_namespace'] = registry_namespace
            config['registry_image_name'] = registry_image_name
            save_config(config)
        else:
            config = load_config()
            registry_url = config['registry_url']
            registry_namespace = config['registry_namespace']
            registry_image_name = config['registry_image_name']

        project_name = config['project_name']

        ret = subprocess.run(['docker', 'images', '-q', config['project_name']], stdout=subprocess.PIPE)
        if ret.stdout.decode('utf-8') == '':
            console.print('No Docker image found. Building the Docker image...')
            build_docker_image('prod')

        console.print("Logging in to the Docker registry...", style='bold cyan')
        run_command(f'docker login {config["registry_url"]}', 'Failed to login to the Docker registry', print_cmd=True)

        console.print("Tagging the Docker image...", style='bold cyan')
        if registry_url == 'docker.io':
            full_image_name = f'{registry_namespace}/{registry_image_name}:{tag}'
        else:
            if registry_namespace:
                full_image_name = f'{registry_url}/{registry_namespace}/{registry_image_name}:{tag}'
            else:
                full_image_name = f'{registry_url}/{registry_image_name}:{tag}'
        run_command(f'docker tag {project_name} {full_image_name}', 'Failed to tag the Docker image', print_cmd=True)

        console.print("Uploading the Docker image to the registry...", style='bold cyan')
        run_command(f'docker push {full_image_name}', 'Failed to upload the Docker image', print_cmd=True)

        console.print(f"Successfully uploaded the Docker image to {full_image_name}", style='bold green')


@click.command(help="Generate documentation")
def doc():
    console.print("Generating documentation", style='bold magenta')
    ret = run_command('pdoc --html --config show_source_code=False -o docs --force app ',
                      'Failed to generate documentation')
    console.print("\nDocumentation generated at docs/app/index.html\n"
                  + f"   Open in browser: file:///{WORKING_DIR}/docs/app/index.html", style='bold green')


cli.add_command(init)
cli.add_command(run)
cli.add_command(build)
cli.add_command(deploy)
cli.add_command(doc)


def main():
    cli()


if __name__ == '__main__':
    main()
