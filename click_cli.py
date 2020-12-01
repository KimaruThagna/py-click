import click

@click.command()
@click.argument('id', type=int, default=1)
def cli_app():
    pass