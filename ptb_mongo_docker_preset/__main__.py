from telegram.ext import Application, CommandHandler, MessageHandler, filters

from utils import commands
from utils.const import Commands as CommandNames
from utils.commodities import env_files_count

from dotenv import load_dotenv
from sys import stderr
import logging
import os


# Configure logging
logging.getLogger('apscheduler').setLevel(logging.WARNING)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger('telegram').setLevel(logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.WARNING)
logging.getLogger('httpcore').setLevel(logging.WARNING)

logger = logging.getLogger()

logger.removeHandler(logger.handlers[0])

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

stdout_handler = logging.StreamHandler(stderr)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


def main() -> None:
    env_files = env_files_count("../")
    if env_files == 0:
        logging.critical("Can't find .env file")
        return
    elif env_files == 1:
        logging.info("Env file found")
    elif env_files > 1:
        logging.warning("Found more than one .env files")

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

    # Run the bot until the admin presses Ctrl-C
    logging.warning("Bot started")
    application.run_polling()


if __name__ == "__main__":
    main()
