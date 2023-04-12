import importlib.metadata

from basekit.infosources.distribution import get_distribution_name, get_distribution_version, distribution_install_editable, caller_info, call_order, get_distribution_files, get_distribution_filepaths

from bridgepilot import settings

def cli():
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
