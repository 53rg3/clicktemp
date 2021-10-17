import click

from commands.hello import hello
from models.Config import somePassedObject


@click.group()
@click.option("--verbose", "-v", is_flag=True)
@somePassedObject
def main(config, verbose):
    # main.add_command(say)
    click.secho("In main...")
    if verbose:
        config.mode = "VERBOSE"


main.add_command(hello)


if __name__ == '__main__':
    main()
