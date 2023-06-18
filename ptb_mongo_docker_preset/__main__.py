from telegram import __version__ as tg_ver
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)
if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {tg_ver}. To view the "
        f"{tg_ver} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{tg_ver}/examples.html"
    )


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
logger = logging.getLogger(__name__)


# Get bot token from .env file
load_dotenv()
bot_token = os.getenv("TG_BOT_TOKEN")


def main() -> None:
    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler(CommandNames.start.value, commands.start))
    application.add_handler(CommandHandler(CommandNames.help.value, commands.help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, commands.unknown_text))

    # Run the bot until the admin presses Ctrl-C
    logger.warning("Bot started")
    application.run_polling()


if __name__ == "__main__":
    main()
