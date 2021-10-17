import click


class Config(object):

    def __init__(self):
        self.mode = "SOME_DEFAULT_MODE"


somePassedObject = click.make_pass_decorator(Config, ensure=True)
