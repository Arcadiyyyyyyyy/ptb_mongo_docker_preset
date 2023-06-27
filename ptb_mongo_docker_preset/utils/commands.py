from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when the command /start is issued."""
    if update.message is None:
        return

    await update.message.reply_text("Start!")


async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when the command /help is issued."""
    if update.message is None:
        return

    await update.message.reply_text("Help!")


async def unknown_text(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when user sends unknown text."""
    if update.message is None:
        return

    await update.message.reply_text("Unknown text!")
