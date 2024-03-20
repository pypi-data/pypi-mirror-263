import os
import shutil
import subprocess
from .utils import prompt, confirm, to_camel_space, get_conda_env_list, create_file, render_template, add_page, \
    run_command, save_config, InitConfig, run_command_with_bottom_msg, JAPPER_DEV
from rich.console import Console

console = Console()

DEV_ENVS_DESC = {
    'docker': 'Recommended for most users if you have Docker installed',
    'conda': 'Recommended for users who are familiar with conda',
    'manual': 'For advanced users who want to set up the environment manually'
}


def copy_static_files(file_path_in_static, dst_path=None):
    # copy files from static folder
    static_path = os.path.dirname(__file__) + '/static/'
    src_path = os.path.join(static_path, file_path_in_static)
    if dst_path is None:
        dst_path = file_path_in_static
    if os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
    else:
        shutil.copy(src_path, dst_path)


def create_docker_related_files(env, project_name):
    copy_static_files(f'container/{env}')
    render_template('container.__name__.docker-compose__name__.yml.jinja2', names=[env, ''],
                    japper_dev=JAPPER_DEV,
                    prod_preview=False,
                    env=env,
                    project_name=project_name)
    if env != 'prod':
        render_template('container.__name__.docker-compose__name__.yml.jinja2', names=[env, '_preview'],
                        japper_dev=JAPPER_DEV,
                        prod_preview=True,
                        env=env,
                        project_name=project_name)


def init_project(config):
    project_name = config['project_name']
    project_title = config['project_title']
    dev_env = config['dev_env']
    mygeohub = 'mygeohub' in config

    console.print("Creating project files...", style="bold cyan")

    # Create a new directory for the project
    for dir_str in InitConfig.DIRS_TO_CREATE:
        console.print(f'Creating directory: {dir_str}', style="white")
        os.makedirs(dir_str, exist_ok=True)

    # copy static files
    copy_static_files('app')
    copy_static_files('gitignore', '.gitignore')

    # create app_main.py
    create_file('app/__init__.py', "from .app_main import AppMain\n")
    render_template('app.app_main.py.jinja2', navigation_mode='top')

    # create config.py
    render_template('app.commons.config.py.jinja2', project_title=project_title)

    # create home page
    render_template('app.controllers.home.py.jinja2')
    render_template('app.views.home.py.jinja2')
    render_template('app.models.home.py.jinja2')

    # create __init__.py files
    create_file('app/controllers/__init__.py', "from .home import HomeController\n")
    create_file('app/views/__init__.py', "from .home import HomeView\n")
    create_file('app/models/__init__.py', "from .home import HomeModel\n")
    render_template('app.commons.__init__.py.jinja2')

    # add tool page
    add_page('Tool', 'mdi-cog')

    # create Readme
    render_template('README.md.jinja2', project_title=project_title)

    # operations based on configs
    if mygeohub:
        console.print(f'\nCreating MyGeoHub Tool structure...', style="bold cyan")
        os.makedirs('middleware', exist_ok=True)
        render_template('middleware.invoke.jinja2', no_file_extension=True,
                        mygeohub_tool_name=config['mygeohub']['tool_name'])
        os.chmod('middleware/invoke', 0o755)

        # create environment.yml
        render_template('environment.yml.jinja2', project_name=project_name, japper_runtime=False)

        # docker-related
        if dev_env == 'docker':
            create_docker_related_files('appmode', project_name)

    else:
        # create environment.yml
        render_template('environment.yml.jinja2', project_name=project_name, japper_runtime=True)

        create_docker_related_files('prod', project_name)
        if dev_env == 'conda':
            conda_env_name = config['conda']['env_name']
            use_existing_conda_env = config['conda']['use_existing_env']

            if not use_existing_conda_env:
                # create conda env
                console.print(f'\nCreating conda environment {conda_env_name}...', style="bold cyan")
                run_command_with_bottom_msg(f'conda env create -f environment.yml -n {conda_env_name}',
                                            f'Creating conda environment {conda_env_name}...',
                                            'Failed to create conda environment')
            console.print(
                f'!! Activate the conda environment by running: [white]conda activate {conda_env_name}[/white]',
                style="bold yellow")
        elif dev_env == 'docker':
            create_docker_related_files('dev', project_name)

    # create app.ipynb
    kernel_name = 'python' if not mygeohub else project_name
    render_template('app.ipynb.jinja2', kernel_name=kernel_name)

    console.print("Project initiated successfully", style="bold green")

    save_config(config)


def init_project_cli(mygeohub=False):
    """Initialize a new Japper project"""
    console.print("\nInitiating a new Japper project", style="bold magenta")

    # get project information
    project_name = prompt("> Enter project name (no spaces) (e.g. japper_project)")
    project_title = prompt("> Enter project title", default=to_camel_space(project_name), allow_spaces=True)

    # get project dev env setup

    # select development environment
    dev_env_list = ['docker', 'conda', 'manual']
    if mygeohub:
        dev_env_list.remove('conda')

    # just to show the choices and descriptions depending on the dev_env_list
    choices = {str(i + 1): dev_env for i, dev_env in enumerate(dev_env_list)}
    choice_desc = [f"{i + 1}. {dev_env.capitalize()}: {DEV_ENVS_DESC[dev_env]}" for i, dev_env in
                   enumerate(dev_env_list)]
    choice_desc = '\n'.join(choice_desc)
    choice_prompt = '([bold cyan]1.docker[/bold cyan], ' + ', '.join(
        [f'{i + 2}.{dev_env}' for i, dev_env in enumerate(dev_env_list[1:])]) + ')'

    console.print("> Choose the development environment:")
    console.print(choice_desc)
    ret = prompt(choice_prompt,
                 choices=choices.keys(), default='1', show_choices=False, show_default=True)

    dev_env = choices[ret]

    config = {
        'project_name': project_name,
        'project_title': project_title,
        'dev_env': dev_env,
    }

    if dev_env == 'conda':
        conda_env_name = prompt("> Enter the new conda environment name", default=project_name, allow_spaces=True)
        conda_env_list = get_conda_env_list()
        use_existing_conda_env = False

        while conda_env_name in conda_env_list:
            ret = confirm(
                f"Conda environment {conda_env_name} already exists. Do you want to create a new one?",
                default=True)
            if ret:
                conda_env_name = prompt("> Enter a different conda environment name",
                                        allow_spaces=True)
            else:
                use_existing_conda_env = True
                break

        config['conda'] = {'env_name': conda_env_name, 'use_existing_env': use_existing_conda_env}

    if mygeohub:
        config['mygeohub'] = {}
        config['mygeohub']['tool_name'] = prompt("> Enter the MyGeoHub tool name", default=project_name)

    init_project(config)
