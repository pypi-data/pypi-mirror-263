import json
import click

from .engines.engines import ENGINE

config_global = None

def get_config():
    global config_global
    if config_global is None:
        with open('.proj.config', 'r') as config_file:
            config_global = json.load(config_file)
    return config_global

@click.group()
def cli():
    pass

@cli.command()
@click.argument('project_name', type=str, required=True)
@click.option('--engine', '-e', type=click.Choice([ENGINE.PYPI]), default=ENGINE.PYPI, help='Choose the engine to use for packaging')
def init(project_name, engine):
    '''
    <project_name> - Name of the project to be setup
    '''
    from .init import init
    init(project_name, engine)

@cli.command()
@click.argument('script_name', type=str, required=True)
def run(script_name):
    '''
    <script_name> - Name of the script to be run
    '''
    from .run import run
    run(script_name)

if __name__ == '__main__':
    cli()
