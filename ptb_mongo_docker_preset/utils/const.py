from enum import Enum


class Commands(Enum):
    start = "start"
    help = "help"


class LanguageCodes(Enum):
    english = "en"


class QueryCategories(Enum):
    commands = "c"


class QueryCommands(Enum):
    lang_code_handle = "l_c_h"
