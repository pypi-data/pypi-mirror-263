import click

from praetorian_cli.sdk.account import Account
from praetorian_cli.handlers.backend import chaos


@click.group(invoke_without_command=True)
@click.version_option()
@click.pass_context
@click.option('--profile', default='United States', help='The keychain profile to use', show_default=True)
def cli(ctx, profile):
    ctx.obj = Account(profile=profile)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


cli.add_command(chaos)


if __name__ == '__main__':
    cli()
