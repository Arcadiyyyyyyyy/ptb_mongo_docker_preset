from telegram.ext import Application, CommandHandler, MessageHandler, filters

from utils import commands
from utils.const import Commands as CommandNames

from dotenv import load_dotenv
import logging
import os


# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARNING
)


# Get bot token from .env file
load_dotenv()
bot_token = os.getenv("TG_BOT_TOKEN")


def main() -> None:
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
