import argparse

__version__ = "0.0.1"

from cli.manager_validators import ValidatePath, ValidateNotEmpty
from operations.alias.current import current_aliases
from operations.set.create import create_set
from operations.set.delete import delete_set
from operations.set.export import export_set
from operations.set.import_set import import_set
from operations.set.list import list_sets

from operations.set.show import show_set
from util.constants import *
from util.helpers.print_helper import get_console_width


def setup_parser():
    parser = argparse.ArgumentParser(description="A program to manage aliases", formatter_class=get_costume_formatter())
    parser.add_argument("-v", "--version", action='version', help="Print version number and exit", version=__version__)
    subparsers = parser.add_subparsers(dest="operation", metavar="operation",
                                       help="start with <operation> help for more info about an operation")
    add_subparsers(subparsers)
    return parser


def get_costume_formatter(formatter=argparse.ArgumentDefaultsHelpFormatter):
    """Return a wider HelpFormatter, if possible."""
    try:
        kwargs = {'width': max(min(get_console_width(), 160), 80), 'max_help_position': 40}
        formatter(None, **kwargs)
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        return formatter


def add_subparsers(subparsers):
    """
        Call order determine order in help list
    """
    add_create_alias_set_action(subparsers)
    add_current_aliases_action(subparsers)
    add_delete_alias_set_action(subparsers)
    add_export_alias_set_action(subparsers)
    add_import_alias_set_action(subparsers)
    add_list_aliases_sets_action(subparsers)
    add_show_aliases_set_details(subparsers)


def add_list_aliases_sets_action(subparsers):
    """
        add list operation parser
    """
    formats = [JSON_FORMAT, TABLE_FORMAT]
    parser = subparsers.add_parser(LIST_OP, help="List aliases sets", description="Manager's list operation",
                                   formatter_class=get_costume_formatter())
    parser.add_argument("-f", "--format", dest=FORMAT_ARG, choices=formats, default=TABLE_FORMAT, metavar=FORMAT_ARG,
                        help="View formatting " + str(formats))
    parser.add_argument("--show-validity", dest=VALIDITY_ARG, action="store_true", help="View the set status flag")
    parser.set_defaults(func=list_sets)


def add_show_aliases_set_details(subparsers):
    """
        add show operation parser
    """
    formats = [JSON_FORMAT, TABLE_FORMAT]
    parser = subparsers.add_parser(SHOW_OP, help="Show aliases in a set", description="Manager's show operation",
                                   formatter_class=get_costume_formatter())
    parser.add_argument("-f", "--format", dest=FORMAT_ARG, choices=formats, default=TABLE_FORMAT,
                        help="View formatting " + str(formats), metavar=FORMAT_ARG, )
    parser.add_argument("-a", "--all", action="store_true", dest=ALL_ARG, help="Show all saved sets")
    parser.add_argument("-c", "--columns", dest=COLUMNS_ARG, choices=ALIAS_COLUMNS, metavar=COLUMNS_ARG,
                        action='append',
                        help="Columns to be shown {}".format(ALIAS_COLUMNS))
    parser.add_argument("name", nargs="+", help="The sets name", action=ValidateNotEmpty)
    parser.set_defaults(func=show_set)


def add_create_alias_set_action(subparsers):
    """
        add create operation parser
    """
    parser = subparsers.add_parser(CREATE_OP, help="Create aliases set", description="Manager's create operation",
                                   formatter_class=get_costume_formatter())
    parser.add_argument("name", help="The set name", action=ValidateNotEmpty)
    parser.set_defaults(func=create_set)


def add_delete_alias_set_action(subparsers):
    """
        add delete operation parser
    """
    parser = subparsers.add_parser(DELETE_OP, help="Delete aliases set", description="Manager's delete operation",
                                   formatter_class=get_costume_formatter())
    parser.add_argument("-y", "--yes", dest=YES_ARG, help="The set name", action="store_true")
    parser.add_argument("-a", "--all", dest=ALL_ARG, help="Delete all the stored sets", action="store_true")
    parser.add_argument("name", nargs="+", help="The set name", action=ValidateNotEmpty)
    parser.set_defaults(func=delete_set)


def add_export_alias_set_action(subparsers):
    """
        add export operation parser
    """
    formats = [JSON_FORMAT, TABLE_FORMAT]
    parser = subparsers.add_parser(EXPORT_OP, help="Export aliases set", description="Manager's export operation",
                                   formatter_class=get_costume_formatter())
    parser.add_argument("name", nargs="+", help="The set name", action=ValidateNotEmpty)
    parser.add_argument("-d", "--destination", dest=DESTINATION_ARG, help="The export path", metavar=DESTINATION_ARG,
                        required=True, action=ValidatePath)
    parser.add_argument("-f", "--format", dest=FORMAT_ARG, choices=formats, default=JSON_FORMAT, metavar=FORMAT_ARG,
                        help="Export formatting " + str(formats))
    parser.add_argument("-p", "--package", dest=PACKAGE_ARG, help="Combine all sets into one set",
                        metavar="package_name", action=ValidateNotEmpty)
    parser.add_argument("-i", "--ignore-conflict", dest=IGNORE_CONFLICT_ARG, action="store_true",
                        help="Will drop the conflicting aliases from the export")
    parser.add_argument("-o", "--overwrite", dest=OVERWRITE_ARG, action="store_true",
                        help="Will overwrite files in dest")
    parser.set_defaults(func=export_set)


def add_import_alias_set_action(subparsers):
    """
        add import operation parser
    """
    parser = subparsers.add_parser(IMPORT_OP, help="Import aliases set", description="Manager's import operation",
                                   formatter_class=get_costume_formatter())
    parser.add_argument("name", help="The set name", action=ValidateNotEmpty)
    parser.add_argument("-s", "--source", dest=SOURCE_ARG, help="The set name", metavar=DESTINATION_ARG,
                        required=True, action=ValidatePath)
    parser.add_argument("-o", "--overwrite", dest=OVERWRITE_ARG, action="store_true", help="Overwrite the entire set")
    parser.add_argument("-r", "--replace", dest=REPLACE_ARG, action="store_true",
                        help="Replace repeated aliases content")

    parser.set_defaults(func=import_set)


def add_current_aliases_action(subparsers):
    """
        add current aliases operation parser
    """
    formats = [JSON_FORMAT, TABLE_FORMAT, SOURCE_FORMAT]
    parser = subparsers.add_parser(CURRENT_OP, help="Shows the current user loaded aliases(temp aliases are excluded)",
                                   description="Manager's current operation", formatter_class=get_costume_formatter())
    parser.add_argument("-f", "--format", dest=FORMAT_ARG, choices=formats, default=TABLE_FORMAT, metavar=FORMAT_ARG,
                        help="View formatting " + str(formats))
    parser.add_argument("-S", "--stdout", dest=STDOUT_ARG, help="Redirect output to file", metavar=STDOUT_ARG,
                        action=ValidatePath)
    parser.set_defaults(func=current_aliases)
