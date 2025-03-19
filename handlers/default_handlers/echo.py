from telebot.types import Message  # noqa
from loader import bot
from database import userdata_controller as bd_controller
from utils.misc.logger import Logger
from telebot import types  # noqa


@bot.message_handler(state=None)
def bot_echo(message: Message):
    """
    A function that echoes the message without any state or filter.
    Takes a Message object as input.
    """
    bd_controller.create(message)
    Logger(message).log_activity("echo")
    bot.reply_to(
        message, "Command not recognized. Please enter /help to get the list of available commands.",
        reply_markup=types.ReplyKeyboardRemove()
    )
    bd_controller.update_last_request_time(message)
