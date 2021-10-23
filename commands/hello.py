import click
from click import command

from models.Config import somePassedObject


@click.command()
@click.option('--name', '-n', default='World', help="Name to be greeted")
@click.option('--repeat', '-r', default=1, help="Times to repeat the greeting")
@click.argument('out', type=click.File('w'), default='-')
@somePassedObject
def hello(config, name, repeat, out) -> command:
    """
    This the comment which will be displayed in the --help

    Arguments:
        OUT - File to output to.
    """
    click.secho(f"Running in mode: {config.mode}", fg="yellow")
    for x in range(repeat):
        click.echo(f"Hello, {name}!", file=out)

    return
