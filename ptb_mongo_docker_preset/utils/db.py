from pymongo import MongoClient
from pymongo.database import Database

from dotenv import load_dotenv
from typing import Any, Mapping

from .commodities import env_files_count

import logging
import os


if env_files_count("../") >= 1:
    load_dotenv()
    MONGO_URI = os.getenv("MONGO_URI")

    if MONGO_URI is None:
        logging.critical("DB URI not found. Check .env")
        raise ConnectionError("DB URI not found. Check .env")

    client: MongoClient[Mapping[str, Any] | Any] = MongoClient(MONGO_URI)
    logging.info("Connected to the db successfully")
    bot_db: Database[Mapping[str, Any] | Any] = client["tg_bot"]

    chat_collection = bot_db["chat"]


def create_chat(chat_id: int, **kwargs):
    logging.debug("Checking if chat with id {:} exists".format(chat_id))
    chat = read_chat(chat_id)
    if chat is None:
        logging.debug("Started creating chat with id {:}".format(chat_id))

        arguments = {
            "chat_id": chat_id,
            "language": "en",
        }

        result = chat_collection.insert_one(
            {**arguments, **kwargs}
        )
        logging.debug("Finished creating chat with id {:}".format(chat_id))
    else:
        logging.debug("Chat with id {:} already exists, skipped".format(chat_id))
        return

    return result


def read_chat(chat_id: int):
    logging.debug("Started reading chat with id {:}".format(chat_id))
    result = chat_collection.find_one({"chat_id": chat_id}, {})
    logging.debug("Finished reading chat with id {:}".format(chat_id))

    return result


def change_chat_language(chat_id: int, new_lang_code: str):
    logging.debug("Started changing chat language in id {:} to {:}".format(chat_id, new_lang_code))
    result = chat_collection.update_one({"chat_id": chat_id}, {"$set": {"language": new_lang_code}})
    logging.debug("Finished changing chat language in id {:} to {:}".format(chat_id, new_lang_code))

    return result
