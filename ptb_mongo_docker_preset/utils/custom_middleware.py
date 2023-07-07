from .db import read_chat


def perhaps():
    return 1


def is_chat_exists(chat_id) -> bool:
    return True if read_chat(chat_id) is not None else False
