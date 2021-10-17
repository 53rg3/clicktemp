from click.testing import CliRunner


def run(command, args):
    runner = CliRunner()
    return runner.invoke(command, args)
