from telegram.ext import ContextTypes
from telegram import Update

from .custom_middleware import is_chat_exists
from .db import create_chat


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when the command /start is issued."""

    # Checks for mypy
    if update.message is None or update.effective_chat is None:
        raise Exception("Input error")

    # If user already interacted with the bot before
    if is_chat_exists(update.effective_chat.id):
        await update.message.reply_text("Start!")
    # If user is not in the database (most certainly sent first ever message to the bot)
    else:
        create_chat(update.effective_chat.id)
        await update.message.reply_text("Hello there")


async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when the command /help is issued."""

    # Checks for mypy
    if update.message is None:
        raise Exception("Input error")

    await update.message.reply_text("Help!")


async def unknown_text(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when user sends unknown text."""

    # Checks for mypy
    if update.message is None:
        raise Exception("Input error")

    await update.message.reply_text("Unknown text!")
