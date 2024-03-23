import os
import click

from functools import wraps

from praetorian_cli.sdk.chaos import Chaos


def handle_api_error(func):
    @wraps(func)
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            click.secho(e.args[0], fg='red')
    return handler


@click.group()
@click.pass_context
def chaos(ctx):
    """ Chaos API access """
    ctx.obj = Chaos(account=ctx.obj)


@chaos.command('seeds')
@click.pass_obj
@handle_api_error
@click.option('-seed', '--seed', default="", help="Filter by seed domain")
def my_seeds(controller, seed):
    """ Fetch seed domains """
    result = controller.my(dict(composite=f'#seed#{seed}'))
    for hit in result.get('seeds', []):
        print(f"{hit['composite']}")


@chaos.command('assets')
@click.pass_obj
@handle_api_error
@click.option('-seed', '--seed', default="", help="Filter by seed domain")
def my_assets(controller, seed):
    """ Fetch existing assets """
    result = controller.my(dict(composite=f'#asset#{seed}'))
    for hit in result.get('assets', []):
        print(f"{hit['composite']}")


@chaos.command('risks')
@click.pass_obj
@handle_api_error
@click.option('-seed', '--seed', default="", help="Filter by seed domain")
def my_risks(controller, seed):
    """ Fetch current risks """
    result = controller.my(dict(composite=f'#risk#{seed}'))
    for hit in result.get('risks', []):
        print(f"{hit['composite']}")


@chaos.command('jobs')
@click.pass_obj
@handle_api_error
@click.option('-seed', '--seed', default="", help="Filter by seed domain")
def my_jobs(controller, seed):
    """ Fetch past, present and future jobs """
    result = controller.my(dict(composite=f'#job#{seed}'))
    for hit in result.get('jobs', []):
        print(f"{hit['composite']}")


@chaos.command('services')
@click.pass_obj
@handle_api_error
@click.option('-port', '--port', default="", help="Filter by port")
def my_services(controller, port):
    """ Fetch recently seen services """
    result = controller.my(dict(composite=f'#service#{port}'))
    for hit in result.get('services', []):
        print(f"{hit['composite']}")


@chaos.command('files')
@click.pass_obj
@handle_api_error
@click.option('-key', '--key', default="", help="Filter by relative path")
def my_files(controller, key):
    """ Fetch all file names """
    result = controller.my(dict(composite=f'#file#{key}'))
    for hit in result.get('files', []):
        print(f"{hit['composite']}")


@chaos.command('threats')
@click.pass_obj
@handle_api_error
@click.option('-source', '--source', type=click.Choice(['kev']), default="kev", help="Filter by threat source")
def my_threats(controller, source):
    """ Fetch threat intelligence """
    result = controller.my(dict(composite=f'#threat#{source}'))
    for hit in result.get('threats', []):
        print(f"{hit['composite']}")


@chaos.command('add-seed')
@click.pass_obj
@handle_api_error
@click.argument('seed')
def add_seed(controller, seed):
    """ Add a new seed domain """
    controller.upsert_seed(seed, 0)


@chaos.command('freeze-seed')
@click.pass_obj
@handle_api_error
@click.argument('seed')
def freeze_seed(controller, seed):
    """ Freeze a seed domain  """
    controller.upsert_seed(seed, 1)


@chaos.command('add-risk')
@click.pass_obj
@handle_api_error
@click.argument('composite')
@click.option('-finding', '--finding', required=True, help="Generic risk identifier")
@click.option('-status', '--status', type=click.IntRange(0, 3), required=False, help="Open (0) Closed (1) Rejected (2) Triaging (3)")
@click.option('-severity', '--severity', type=click.IntRange(0, 4), required=False, help="Info (0) Low (1) Med (2) High (3) Material (4)")
def add_risk(controller, composite, finding, status=0, severity=0):
    """ Apply a risk to an asset composite """
    print(controller.add_risk(composite, finding, status, severity))


@chaos.command('upload')
@click.pass_obj
@handle_api_error
@click.argument('name')
def upload(controller, name):
    """ Upload a file """
    controller.upload(name)


@chaos.command('download')
@click.pass_obj
@handle_api_error
@click.argument('key')
@click.argument('path')
def download(controller, key, path):
    """ Download any previous uploaded file """
    controller.download(key, path)


@chaos.command('trigger')
@click.pass_obj
@handle_api_error
@click.argument('capability', type=click.Choice(['nmap', 'screenshot', 'nuclei', 'masscan', 'whois', 'subfinder']))
@click.argument('composite')
def trigger(controller, composite, capability):
    """ Invoke a capability against an asset composite """
    controller.trigger(capability, composite)


@chaos.command('test')
@click.pass_obj
def trigger_all_tests(controller):
    import pytest
    test_directory = os.path.relpath("praetorian_cli/sdk/test", os.getcwd())
    pytest.main([test_directory])
