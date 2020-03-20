import os

# Data directory
data_dir_path = os.path.dirname(__file__) + "/../data/"

# Formats
JSON_FORMAT = "json"
TABLE_FORMAT = "table"
SOURCE_FORMAT = "source"

# Alias attributes names
NAME_ATTRIBUTE = "name"
COMMAND_ATTRIBUTE = "command"
DESCRIPTION_ATTRIBUTE = "description"
TAGS_ATTRIBUTE = "tags"
IS_ACTIVE_ATTRIBUTE = "is_active"
SET_NAME_ATTRIBUTE = "set_name"

# Display columns
ALIAS_COLUMNS = [NAME_ATTRIBUTE, COMMAND_ATTRIBUTE, DESCRIPTION_ATTRIBUTE, TAGS_ATTRIBUTE, IS_ACTIVE_ATTRIBUTE]

# Alias attributes defaults
ALIAS_ATTRIBUTES_DEFAULTS = {
    NAME_ATTRIBUTE: "",
    COMMAND_ATTRIBUTE: "",
    DESCRIPTION_ATTRIBUTE: "",
    TAGS_ATTRIBUTE: None,
    IS_ACTIVE_ATTRIBUTE: "false",
    SET_NAME_ATTRIBUTE: ""
}

# Manager sets operations
LIST_OP = "list"
SHOW_OP = "show"
DELETE_OP = "delete"
CREATE_OP = "create"
EXPORT_OP = "export"
IMPORT_OP = "import"

# Manager aliases operations
CURRENT_OP = "current"
ADD_OP = "add"
REMOVE_OP = "remove"
EDIT_OP = "edit"
SET_OP = "set"
GENERATE_OP = "generate"

# args names
DESTINATION_ARG = "destination"
SOURCE_ARG = "source"
FORMAT_ARG = "format"
VALIDITY_ARG = "validity"
NAME_ARG = "name"
COLUMNS_ARG = "columns"
ALL_ARG = "all"
YES_ARG = "yes"
PACKAGE_ARG = "package"
IGNORE_CONFLICT_ARG = "ignore_conflict"
OVERWRITE_ARG = "overwrite"
REPLACE_ARG = 'replace'
STDOUT_ARG = 'stdout'
COMMAND_ARG = "command"
DESCRIPTION_ARG = "description"
TAGS_ARG = "tags"
IS_ACTIVE_ARG = "is_active"
SET_NAME_ARG = "set_name"
ALIAS_NAME_ARG = "alias_name"
KEEP_TAGS_ARG = "keep_tags"
KEEP_DESCRIPTION_ARG = "keep_description"
# args groups
PATHS_GROUP = [DESTINATION_ARG, SOURCE_ARG, STDOUT_ARG]
