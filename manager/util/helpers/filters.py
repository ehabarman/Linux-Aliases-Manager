from util.constants import NAME_ATTRIBUTE, COMMAND_ATTRIBUTE, SET_NAME_ATTRIBUTE


def remove_non_valid_aliases(aliases):
    result = []
    for alias in aliases:
        keys = alias.keys()
        if NAME_ATTRIBUTE in keys and COMMAND_ATTRIBUTE in keys:
            if alias[NAME_ATTRIBUTE] and alias[COMMAND_ATTRIBUTE]:
                result.append(alias)

    return result


def handle_conflict(all_aliases, handler):
    """Find confliction and fix them"""

    # Sort aliases by name
    all_aliases = sorted(all_aliases, key=lambda alias: (alias[NAME_ATTRIBUTE]))

    index = 0
    alias_name = ""
    while index < len(all_aliases):
        if alias_name == all_aliases[index][NAME_ATTRIBUTE]:
            handler(all_aliases, index)
        elif index >= len(all_aliases) - 1:
            break
        elif all_aliases[index][NAME_ATTRIBUTE] == all_aliases[index + 1][NAME_ATTRIBUTE]:
            alias_name = all_aliases[index][NAME_ATTRIBUTE]
        else:
            index += 1

    return all_aliases


def delete_an_element_handler(all_aliases, index):
    del all_aliases[index]


def change_name_handler(all_aliases, index):
    alias = all_aliases[index]
    all_aliases[index][NAME_ATTRIBUTE] = "{}-{}".format(alias[SET_NAME_ATTRIBUTE], alias[NAME_ATTRIBUTE])
