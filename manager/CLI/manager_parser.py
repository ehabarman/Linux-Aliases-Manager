import argparse

__version__ = "0.0.1"
__set_operations__ = ["list", "show", "create", "delete", "export", "import"]
__alias_operations__ = ["add", "remove", "set"]

from operations.set.create import create_set
from operations.set.delete import delete_set
from operations.set.export import export_set
from operations.set.import_set import import_set
from operations.set.list import list_sets

from operations.set.show import show_set
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
    add_delete_alias_set_action(subparsers)


def add_list_aliases_sets_action(subparsers):
    formats = [JSON_FORMAT, TABLE_FORMAT]
    parser = subparsers.add_parser("list", help="List aliases sets")
    parser.add_argument("-f", "--format", dest="format", choices=formats, default=TABLE_FORMAT,
                        help="View formatting " + str(formats), metavar="")
    parser.add_argument("--show-validity", dest="validity", action='store_true', help="View the set status flag")
    parser.set_defaults(func=list_sets)


def add_show_aliases_set_details(subparsers):
    formats = [JSON_FORMAT, TABLE_FORMAT]
    parser = subparsers.add_parser("show", help="Show aliases in a set")
    parser.add_argument("-f", "--format", dest="format", choices=formats, default=TABLE_FORMAT,
                        help="View formatting " + str(formats), metavar="")
    parser.add_argument("name", help="The name of the set to be shown")
    parser.add_argument("-c", "--columns", dest="columns", choices=ALIAS_COLUMNS, help="Columns to be shown",
                        metavar="", nargs="+")
    parser.set_defaults(func=show_set)


def add_create_alias_set_action(subparsers):
    parser = subparsers.add_parser("create", help="Create aliases set")
    parser.add_argument("name", help="The set name")
    parser.set_defaults(func=create_set)


def add_delete_alias_set_action(subparsers):
    parser = subparsers.add_parser("delete", help="Delete aliases set")
    parser.add_argument("name", help="The set name")
    parser.add_argument("-y", "--yes", dest="yes", help="The set name", action='store_true')
    parser.set_defaults(func=delete_set)


def add_export_alias_set_action(subparsers):
    parser = subparsers.add_parser("export", help="Export aliases set")

    parser.set_defaults(func=export_set)


def add_import_alias_set_action(subparsers):
    parser = subparsers.add_parser("import", help="Import aliases set")

    parser.set_defaults(func=import_set)
