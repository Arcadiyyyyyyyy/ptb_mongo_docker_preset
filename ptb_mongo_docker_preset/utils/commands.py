from telegram.ext import ContextTypes
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
import i18n

from .custom_middleware import is_chat_exists, main_handler
from .const import LanguageCodes, QueryCommands, QueryCategories
from .db import create_chat, change_chat_language


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when the command /start is issued."""

    # Checks for mypy
    if update.message is None or update.effective_chat is None:
        raise Exception("Input error")

    # Checks that have to be done every update
    main_handler(update.effective_chat.id)

    # If user already interacted with the bot before
    if is_chat_exists(update.effective_chat.id):
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=i18n.t("translation.english", locale=LanguageCodes.english.value),
                        callback_data=QueryCategories.commands.value + "*" +
                        QueryCommands.lang_code_handle.value + "*" +
                        LanguageCodes.english.value,
                    )
                ]
            ]
        )

        await update.message.reply_text(
            i18n.t("translation.start"),
            reply_markup=markup
        )
    # If user is not in the database (most certainly sent first ever message to the bot)
    else:
        create_chat(update.effective_chat.id)
        await update.message.reply_text(i18n.t("translation.start"))


async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when the command /help is issued."""

    # Checks for mypy
    if update.message is None or update.effective_chat is None:
        raise Exception("Input error")

    # Checks that have to be done every update
    main_handler(update.effective_chat.id)

    await update.message.reply_text(i18n.t("translation.help"))


async def unknown_text(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function executes when user sends unknown text."""

    # Checks for mypy
    if update.message is None or update.effective_chat is None:
        raise Exception("Input error")

    # Checks that have to be done every update
    main_handler(update.effective_chat.id)

    await update.message.reply_text(i18n.t("translation.unknown_text"))


async def local_query_handler(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """This function handles any CallbackQuery with the category of QueryCategories.commands.value"""

    # Checks for mypy
    if update.callback_query is None or update.effective_chat is None or update.callback_query.data is None:
        raise Exception("Input error")

    # Checks that have to be done every update
    main_handler(update.effective_chat.id)

    data_list = update.callback_query.data.split("*")[1:]  # Split to attributes and delete query global category
    local_category = data_list[0]

    if local_category == QueryCommands.lang_code_handle.value:
        change_chat_language(update.effective_chat.id, data_list[-1])
        await update.callback_query.answer(i18n.t("translation.success"))
