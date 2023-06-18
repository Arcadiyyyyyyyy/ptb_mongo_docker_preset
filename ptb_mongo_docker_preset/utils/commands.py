from telegram import ForceReply, Update
from telegram.ext import ContextTypes


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when the command /help is issued."""
    await update.message.reply_text("Help!")


async def unknown_text(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when user sends unknown text."""
    await update.message.reply_text("Unknown text!")
