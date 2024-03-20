import click


@click.group()
def cli():
    """
    Empty CLI group to make it clear we're using Cringelord commands.
    """


@cli.command(help="Helper that initializes your project for using cringelord.")
@click.option(
    "-m", "--mode",
    required=False,
    type=click.Choice(["ALL", "SRC"], case_sensitive=False),
    default="ALL",
    show_default=True,
    help="""
    Do you want cringelord to load all settings in your 
    cringe-config (i.e. "ALL"), or only settings you actually use in 
    your source code (i.e. "SRC")?
    """
)
def init(mode):
    return NotImplemented
