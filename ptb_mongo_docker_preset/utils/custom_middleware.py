import i18n

from .db import read_chat, create_chat


def perhaps():
    return 1


def is_chat_exists(chat_id) -> bool:
    return True if read_chat(chat_id) is not None else False


def main_handler(chat_id):
    create_chat(chat_id)
    return language_handler(chat_id)


def language_handler(chat_id):
    chat = read_chat(chat_id)
    try:
        i18n.set("locale", chat["language"])
    except KeyError:
        pass
    return chat.get("language", "en")
