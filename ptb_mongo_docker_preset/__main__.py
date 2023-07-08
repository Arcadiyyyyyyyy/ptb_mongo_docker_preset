from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ContextTypes,
)
from telegram import Update

from utils import commands
from utils.const import Commands as CommandNames, QueryCategories

from dotenv import load_dotenv
from sys import stderr
import logging
import i18n
import os


# Configure logging
logging.getLogger('apscheduler').setLevel(logging.WARNING)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger('telegram').setLevel(logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.WARNING)
logging.getLogger('httpcore').setLevel(logging.WARNING)

logger = logging.getLogger()

try:
    logger.removeHandler(logger.handlers[0])
except IndexError:
    pass

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s | Line: %(lineno)d | %(name)s | %(message)s')

stdout_handler = logging.StreamHandler(stderr)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


# set up i18n localization/internationalization
locale_path = os.path.abspath('./locale')

i18n.load_path.append(locale_path)
i18n.set("fallback", "en")
i18n.set("locale", "en")


async def callback_query_distributor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Global Callback Query distributor.
    It's much easier to handle callbacks in one place, than in 100 different commands"""

    # Checks for mypy
    if update.callback_query is None or update.callback_query.data is None:
        raise Exception("Input error")

    category = update.callback_query.data.split("*")[0]

    if category == QueryCategories.commands.value:
        return await commands.local_query_handler(update, context)

    logging.warning("Unknown query category type {:}. Some of your commands will work wrong.".format(category))


def main() -> None:
    # Get bot token from .env file
    load_dotenv()
    bot_token = os.getenv("TG_BOT_TOKEN")

    if bot_token is None:
        logging.critical("TG_BOT token not found. Check .env")
        return

    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler(CommandNames.start.value, commands.start))
    application.add_handler(CommandHandler(CommandNames.help.value, commands.help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, commands.unknown_text))

    application.add_handler(CallbackQueryHandler(callback_query_distributor))

    # Run the bot until the admin presses Ctrl-C
    logging.warning("Bot started")
    application.run_polling()


if __name__ == "__main__":
    main()
