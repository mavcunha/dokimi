import click
from lib.utils import log

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    log.DEBUG=debug

@cli.command()
def parse():
    log(f"parsing log")
