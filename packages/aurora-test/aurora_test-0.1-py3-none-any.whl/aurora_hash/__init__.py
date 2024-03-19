import click
import pyperclip
from .main import random_password, hash

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-l', '--length', type=int, help='Length of password to be generated')
@click.option('-o', '--option', type=click.Choice(['1', '2', '3', '4']), default = '4',
    help='''Options\n
    1 - alphabetic lowercase\n
    2 - alphabetic both cases\n
    3 - alphanumeric\n
    4 - alphanumeric + special characters'''
)
def generate(length, option):
    """generates a random password of length and type"""
    logo = """
    +--------------------+
    | Testing for aurora |
    +--------------------+
    """

    # generate random password
    password = random_password(int(length), int(option))

    # copy password to clipboard
    try:
        pyperclip.copy(password)
        click.echo('Password has been copied to clipboard\n')
    except Exception:
        click.echo('Could not copy password to clipboad\n')

    # output password and info to terminal
    click.echo(password)
    click.echo(logo)
