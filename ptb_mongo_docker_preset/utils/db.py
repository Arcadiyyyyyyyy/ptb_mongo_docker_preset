from pymongo import MongoClient
from pymongo.database import Database

from dotenv import load_dotenv
from typing import Any, Mapping

import logging
import os


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

try:
    client: MongoClient[Mapping[str, Any] | Any] = MongoClient(MONGO_URI)
    logging.info("Connected to the db successfully")
    bot_db: Database[Mapping[str, Any] | Any] = client["tg_bot"]
except ConnectionError:
    logging.critical("Could not connect to the database.")
    raise ConnectionError("Can't connect to the database, check .env")


chat_collection = bot_db["chat"]


def create_chat(user_id):
    logging.debug("Started creating chat with id {:}".format(user_id))
    logging.debug("Created chat with id {:}".format(user_id))
    raise NotImplementedError


def read_chat(user_id):
    logging.debug("Started reading chat with id {:}".format(user_id))
    logging.debug("Finished reading chat with id {:}".format(user_id))
    raise NotImplementedError
