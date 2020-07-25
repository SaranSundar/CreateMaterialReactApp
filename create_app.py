import os
import platform
import subprocess
import sys

import typer

operating_system = str(platform.system()).lower()

if "window" in operating_system:
    if 'HOME' in os.environ:
        HOME = os.environ['HOME']
    elif 'HOMEPATH' in os.environ:
        HOME = os.environ['HOMEPATH']
    else:
        HOME = "./"
elif "darwin" in operating_system or "linux" in operating_system:
    HOME = os.environ['HOME']
else:
    HOME = os.environ['HOME']


def replace_all_paths(path):
    if path == "":
        return path
    path = path.replace("$HOME", HOME)
    path = path.replace("~", HOME)
    return path


def cmdline(command):
    if "window" in operating_system:
        command = command.split("\n")
        windows_cmdline(command)
    elif "darwin" in operating_system:
        command = command.split("\n")
        macos_cmdline(command)
    else:
        print("Operating system not supported, please use Mac OS or Windows")
        sys.exit(1)


def macos_cmdline(cmds):
    cmds = " && ".join(cmds)
    subprocess.run(cmds, shell=True)


def windows_cmdline(cmds):
    cmds = " & ".join(cmds)
    cmds = cmds.replace("\\", "/")
    subprocess.run(cmds, shell=True)


def create_project(project_path, react_name):
    project_path = replace_all_paths(project_path)
    react_name = react_name.lower()
    cli_commands = [
        "cd " + project_path,
        "npx create-react-app " + react_name,
        "rm -rf " + react_name + "/src",
        "rm -rf " + react_name + "/public",
        "cp rt.py " + react_name + "/rt.py",
        "cp -r public " + react_name + "/public",
        "cp -r src " + react_name + "/src",
        "cd " + react_name,
        "yarn add react-router-dom",
        "yarn add @material-ui/core",
        "yarn add @material-ui/icons",
        "yarn add fontsource-roboto",
        "rm -rf " + "node_modules",
        "yarn install",
        # "npm install --save typescript",
        # "npm install --save @types/node",
        # "npm install --save @types/react",
        # "npm install --save @types/react-dom",
        # "npm install --save @types/jest"
    ]

    cmdline("\n".join(cli_commands))


def create_app(project_name: str, project_path: str):
    # Check if npm, yarn, and npx create-react-app works first, and if python3 and typer is installed
    typer.secho(f"Do you have npm, yarn, python3, and typer (pip package) installed?", fg=typer.colors.BLUE)
    pre_requisites = input("(Y/N) : ")
    if pre_requisites.lower() == "y":
        typer.secho(f"Creating {project_name} under {project_path}", fg=typer.colors.GREEN)
        create_project(project_path, project_name)
    else:
        typer.secho(f"Please install all pre-requisites and enter Y at the prompt above", fg=typer.colors.RED)


if __name__ == "__main__":
    typer.run(create_app)
