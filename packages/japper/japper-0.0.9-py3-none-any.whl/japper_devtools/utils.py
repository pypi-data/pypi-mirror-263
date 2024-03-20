from re import sub
import os, sys
import subprocess
import yaml
from jinja2 import Environment, FileSystemLoader
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

from rich.console import Console

console = Console()

# jinja2 environment
env = Environment(loader=FileSystemLoader(os.path.dirname(__file__) + '/templates'))

CONFIG_FILENAME = 'japper.yml'
WORKING_DIR = os.getcwd().replace('\\', '/')

JAPPER_DEV = False


class InitConfig:
    # Directories to be created
    DIRS_TO_CREATE = ['app', 'app/assets', 'app/commons', 'app/models', 'app/controllers', 'app/views', 'container']


def run_command(cmd, fail_msg=None, print_cmd=False):
    """
        Run a command in the shell.

        Parameters:
        cmd (str): The command to run.
        fail_msg (str, optional): The message to print if the command fails. Defaults to None.
        print_cmd (bool, optional): Whether to print the command before running it. Defaults to False.

        Returns:
        int: The return code of the command.
    """
    if print_cmd:
        console.print(f'Running command: {cmd}', style='cyan')
    ret = os.system(cmd)
    if ret != 0:
        if fail_msg:
            console.print(fail_msg, style='bold red')
        exit(-1)
    return ret


def save_config(config: dict):
    with open(CONFIG_FILENAME, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)


def load_config():
    if not os.path.exists(CONFIG_FILENAME):
        return None
    with open(CONFIG_FILENAME, 'r') as f:
        return yaml.safe_load(f)


def prompt(text, optional=False, allow_spaces=False, **kwargs):
    """
        Prompt the user for input.

        Parameters:
        text (str): The prompt text.
        optional (bool, optional): Whether the input is optional. Defaults to False.
        allow_spaces (bool, optional): Whether to allow spaces in the input. Defaults to False.

        Returns:
        str: The user's input.
    """
    while True:
        user_input = Prompt.ask(text, **kwargs)
        if not user_input:
            if optional:
                return None
            else:
                console.print('This field is required', style='bold red')
                continue

        if not allow_spaces and ' ' in user_input:
            console.print('This field cannot contain spaces', style='bold red')
            continue

        return user_input


def confirm(text, **kwargs):
    return Confirm.ask(text, **kwargs)


def snake(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()


def camel(s):
    return ''.join([word.capitalize() for word in s.split(' ')])


def to_camel_space(s):
    return ' '.join(word.capitalize() for word in s.replace('_', ' ').replace('-', ' ').split())


def create_file(file_path, content=''):
    with open(file_path, 'w') as f:
        f.write(content)


def add_page(page_name: str, icon: str = None, verbose=False):
    snake_page_name = snake(page_name)
    camel_page_name = camel(page_name)

    file_controller, file_view, file_model = (render_template('app.controllers.__name__.py.jinja2',
                                                              name=snake_page_name,
                                                              page_name=camel_page_name),
                                              render_template('app.views.__name__.py.jinja2',
                                                              name=snake_page_name,
                                                              page_name=camel_page_name),
                                              render_template('app.models.__name__.py.jinja2',
                                                              name=snake_page_name,
                                                              page_name=camel_page_name))
    if verbose:
        console.print(f"Adding page files...\n{file_controller}\n{file_view}\n{file_model}")

    # update __init__.py files
    with open('app/controllers/__init__.py', 'a') as f:
        f.write(f"from .{snake_page_name} import {camel_page_name}Controller\n")
    with open('app/views/__init__.py', 'a') as f:
        f.write(f"from .{snake_page_name} import {camel_page_name}View\n")
    with open('app/models/__init__.py', 'a') as f:
        f.write(f"from .{snake_page_name} import {camel_page_name}Model\n")

    # update app_main.py
    with open('app/app_main.py', 'r') as f:
        lines = f.readlines()

    # add controller
    for i in range(len(lines)):
        if 'from .controllers import' in lines[i]:
            lines[i] = lines[i].replace('from .controllers import',
                                        f'from .controllers import {camel_page_name}Controller,')
            break

    # add page by backtracking from the end of the file
    addpage_code = f"self.add_page(Page(name='{page_name}', controller={camel_page_name}Controller()"
    if icon:
        addpage_code += f", icon='{icon}'"
    addpage_code += '))\n'

    for i in range(len(lines) - 1, -1, -1):
        if 'self.add_page(' in lines[i]:
            spaces = len(lines[i]) - len(lines[i].lstrip())
            lines.insert(i + 1, ' ' * spaces + addpage_code)
            break

    with open('app/app_main.py', 'w') as f:
        f.write(''.join(lines))
        f.write('\n')

    if verbose:
        console.print(
            f"Page {page_name} added successfully. " +
            "Please check you app_main.py file to make sure the page is added correctly." +
            " If not, please add it manually the following code:\n\n" + addpage_code)


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def get_yn_input(prompt, default=None):
    while True:
        y_str = 'Y' if default else 'y'
        n_str = 'N' if default is False else 'n'

        print(prompt + f' [{y_str}/{n_str}]', end='', flush=True)
        user_input = getch()
        if user_input.lower() == 'y':
            return True
        elif user_input.lower() == 'n':
            return False
        elif user_input == '\r' and default is not None:
            return default
        else:
            print("Invalid input. Please enter 'y' or 'n'")


def _get_yn_input(question, default=None):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default:
        prompt = " [Y/n] "
    elif default is False:
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return default
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def render_template(template_name, name=None, names=None, no_file_extension=False, **kwargs):
    template = env.get_template(template_name)
    content = template.render(**kwargs)
    tokens = template_name[:-7].split('.')  # remove .jinja2 and split by .
    if no_file_extension:
        file_path = '/'.join(tokens)
    else:
        file_path = '/'.join(tokens[:-1]) + '.' + tokens[-1]

    if name:
        file_path = file_path.replace('__name__', name)
    elif names:
        for name in names:
            file_path = file_path.replace('__name__', name, 1)

    create_file(file_path, content)

    return file_path


def get_conda_env_list():
    ret = subprocess.run(['conda', 'env', 'list'], capture_output=True)
    envs = ret.stdout.decode('utf-8').split('\n')
    envs = [env.split()[0] for env in envs if env and env[0] != '#']
    return envs


def check_cur_conda_env(app_env_name):
    cur_env = os.environ['CONDA_DEFAULT_ENV']
    if cur_env != app_env_name:
        console.print(
            f"Please activate the conda environment {app_env_name} first: [white] conda activate {app_env_name}[/white]",
            style='bold yellow')
        exit(-1)


def build_docker_image(env, quiet=False, preview_mode=False):
    console.print('Build the Docker image', style='bold cyan')
    cmd = f'cd container/{env} && docker-compose'
    if preview_mode:
        cmd += ' -f docker-compose_preview.yml'
    cmd += ' build'
    if quiet:
        cmd += ' -q'

    run_command_with_bottom_msg(cmd, 'Building the Docker image...'
                                , fail_msg='Failed to build the Docker image'
                                , color_err=True)


def run_command_with_bottom_msg(cmd, bottom_msg, fail_msg=None, color_err=False):
    if type(cmd) is not list:
        cmd = ['bash', '-c', cmd]

    err_style = 'red' if color_err else 'white'

    with console.status("[bold deep_sky_blue1]" + bottom_msg) as status:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            text = process.stdout.read1().decode("utf-8")
            err_text = process.stderr.read1().decode("utf-8")
            print(text, end='', flush=True)
            if err_text:
                console.print(err_text, end='', style=err_style)
            if process.poll() is not None:
                break
        rc = process.poll()

    if rc != 0:
        if fail_msg:
            console.print(fail_msg, style='bold red')
        exit(-1)
    return rc


def run_japper_app(cmd, verbose, japper_up_msg, check_voila_running, check_jupyter_running):
    log_file = f'{WORKING_DIR}/japper_run.log'
    # clean the log
    with open(log_file, 'w') as f:
        f.write('')

    console.print(f"Starting the app", style='bold cyan')
    if not verbose:
        console.print(
            f"  App running logs are being written to file:///{log_file}\n"
            + "  You can use -v or --verbose option to see the logs.", style='yellow')

    voila_running = not check_voila_running
    jupyter_running = not check_jupyter_running
    app_initialized = False

    with console.status("[bold deep_sky_blue1] Initializing the app running environment...") as status:
        process = subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            text = process.stdout.read1().decode("utf-8")
            if verbose:
                print(text, end='', flush=True)
            else:
                with open(log_file, 'a') as f:
                    f.write(text)
            if not app_initialized:
                if '[Voila] Voilà is running at:' in text:
                    voila_running = True
                if 'Jupyter ' in text and 'is running at:' in text:
                    jupyter_running = True
                if voila_running and jupyter_running:
                    status.update(Panel(japper_up_msg), spinner='dots', speed=0.1)
                    app_initialized = True

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


def get_docker_up_cmd(env, preview_mode):
    cmd = f'cd container/{env} && docker-compose'
    if preview_mode:
        cmd += ' -f docker-compose_preview.yml'
    cmd += ' up --remove-orphans'

    return cmd
