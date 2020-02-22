import argparse

__version__ = "0.0.1"
__manager_actions__ = ["list", "create", "edit", "remove", "set", "import", "export"]


def setup_parser():
    parser = argparse.ArgumentParser(description="A program to manage aliases")
    parser.add_argument("-v", "--version", action='version', help="Print version number and exit", version=__version__)
    subparsers = parser.add_subparsers(title="operation", dest="operation",
                                       description="one of the following operations",
                                       help="start with <operation> help for more info about an operation")

    add_subparsers(subparsers)

    return parser


def add_subparsers(subparsers):
    add_list_aliases_action(subparsers)
    add_create_alias_action(subparsers)


def add_list_aliases_action(subparsers):
    actions = ["active", "inactive", "all"]
    parser = subparsers.add_parser("list", help="list aliases")
    parser.add_argument("action", help="what aliases to show, options " + str(actions))
    # parser.set_defaults(func="active")


def add_create_alias_action(subparsers):
    parser = subparsers.add_parser("create", help="create alias")
    parser.add_argument("--name", help="alias name")
    parser.add_argument("--command", help="alias name")
    parser.add_argument("--description", help="alias name")
    parser.add_argument("--tags", help="alias name")
    parser.add_argument("--active", help="alias name")
    # parser.set_defaults(func="active")