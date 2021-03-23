import click

global DEBUG

def log(message):
    if (log.DEBUG):
        click.secho(f"debug: {message}", fg='cyan', err=True)

