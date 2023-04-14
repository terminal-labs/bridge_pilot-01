import click

from cli_passthrough import cli_passthrough


from basekit.objects import globalconfig
from basekit.infosources.distribution import info
from basekit.settings import VERSION, PROJECT_NAME
from basekit.ops.scaffolding import set_global_bracket_data, get_global_bracket_data
from basekit.ops.scaffolding import get_hydrated_scaffolding_paths, build_scaffolding, test_scaffolding, get_scaffolding_style, scaffolding_styles
from basekit.infosources.distribution import get_distribution_name, get_distribution_version, distribution_install_editable, caller_info, call_order, get_distribution_files, get_distribution_filepaths


from bridgepilot.app import start_main
from bridgepilot.functions.utils import prettyprintdict
from bridgepilot.ux.srv import start_server

context_settings = {"help_option_names": ["-h", "--help"]}

class SpecialHelpOrder(click.Group):

    def __init__(self, *args, **kwargs):
        self.help_priorities = {}
        super(SpecialHelpOrder, self).__init__(*args, **kwargs)

    def get_help(self, ctx):
        self.list_commands = self.list_commands_for_help
        return super(SpecialHelpOrder, self).get_help(ctx)

    def list_commands_for_help(self, ctx):
        """reorder the list of commands when listing the help"""
        commands = super(SpecialHelpOrder, self).list_commands(ctx)
        return (c[1] for c in sorted(
            (self.help_priorities.get(command, 1), command)
            for command in commands))

    def command(self, *args, **kwargs):
        """Behaves the same as `click.Group.command()` except capture
        a priority for listing command names in help.
        """
        help_priority = kwargs.pop('help_priority', 1)
        help_priorities = self.help_priorities

        def decorator(f):
            cmd = super(SpecialHelpOrder, self).command(*args, **kwargs)(f)
            help_priorities[cmd.name] = help_priority
            return cmd

        return decorator


@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=VERSION)
@click.option('-c', '--configfile')
@click.pass_context
def cli(ctx, configfile):
    globalconfig.obj["configfile"] = configfile
    pass

@click.group(name="app")
def app_group():
    pass

@click.group(name="server")
def server_group():
    pass

@click.group(name="system", cls=SpecialHelpOrder)
def system_group():
    pass

@app_group.command("main")
def app_main_cmd():
    start_main()

@server_group.command("serve")
def server_serve_cmd():
    start_server()

@system_group.command("workdirinfo", help_priority=1)
def system_workdirinfo_cmd():
    print(prettyprintdict(info()))

@system_group.command("dottmpinfo", help_priority=5)
def system_workdirinfo_cmd():
    print(prettyprintdict(info()))

@system_group.command("info")
def system_info_cmd():
    print(prettyprintdict(info()))

@system_group.command("moreinfo")
def system_moreinfo_cmd():
    test_scaffolding("workstation")
    print(get_scaffolding_style())
    name = get_distribution_name()
    print(name)
    print(get_distribution_version(name))
    print(distribution_install_editable(name))
    print(call_order())
    print(get_distribution_files(name))
    print(get_distribution_filepaths(name))
    # print(get_distribution_src_path(name))
    # print(get_distribution_pth_path(name))
    # print(get_distribution_pth_content(name))

@system_group.command("allinfo")
def system_workdirinfo_cmd():
    print(prettyprintdict(info()))

cli.add_command(app_group)
cli.add_command(server_group)
cli.add_command(system_group)
