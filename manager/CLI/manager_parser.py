import argparse

__version__ = "0.0.1"
__manager_operations__ = ["list", "show", "create", "edit", "remove", "set", "import", "export", "delete"]

from operations.list import list_aliases
from operations.show import show_aliases
from util.constants import JSON_FORMAT, TABLE_FORMAT, ALIAS_COLUMNS


def setup_parser():
    parser = argparse.ArgumentParser(description="A program to manage aliases")
    parser.add_argument("-v", "--version", action='version', help="Print version number and exit", version=__version__)
    subparsers = parser.add_subparsers(title="operation", dest="operation",
                                       description="one of the following operations",
                                       help="start with <operation> help for more info about an operation")
    add_subparsers(subparsers)
    return parser


def add_subparsers(subparsers):
    add_list_aliases_sets_action(subparsers)
    add_show_aliases_set_details(subparsers)
    add_create_alias_set_action(subparsers)


def add_list_aliases_sets_action(subparsers):
    formats = [JSON_FORMAT, TABLE_FORMAT]
    parser = subparsers.add_parser("list", help="list aliases sets")
    parser.add_argument("-f", "--format", dest="format", choices=formats, default=TABLE_FORMAT,
                        help="View formatting " + str(formats), metavar="")
    parser.add_argument("--show-validity", dest="validity", action='store_true', help="View the set status flag")
    parser.set_defaults(func=list_aliases)


def add_show_aliases_set_details(subparsers):
    formats = [JSON_FORMAT, TABLE_FORMAT]
    parser = subparsers.add_parser("show", help="show aliases in a set")
    parser.add_argument("-f", "--format", dest="format", choices=formats, default=TABLE_FORMAT,
                        help="View formatting " + str(formats), metavar="")
    parser.add_argument("name", help="The name of the set to be shown")
    parser.add_argument("-c", "--columns", dest="columns", choices=ALIAS_COLUMNS, help="Columns to be shown",
                        metavar="", nargs="+")
    parser.set_defaults(func=show_aliases)


def add_create_alias_set_action(subparsers):
    parser = subparsers.add_parser("create", help="create alias")
    parser.add_argument("--name", help="alias name")
    parser.add_argument("--command", help="alias name")
    parser.add_argument("--description", help="alias name")
    parser.add_argument("--tags", help="alias name")
    parser.add_argument("--active", help="alias name")
    # parser.set_defaults(func="active")
