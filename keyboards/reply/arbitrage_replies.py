from telebot import types  # noqa


def create_start_reply() -> types.ReplyKeyboardMarkup:
    """
    A function to initialize a reply keyboard markup with two buttons for starting and exiting.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(
        types.KeyboardButton('Start \U00002705'),  # Начать = Start
        types.KeyboardButton('Exit \U0000274E')   # Выход = Exit
    )
    return markup
