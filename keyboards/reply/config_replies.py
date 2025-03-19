from telebot import types  # noqa
from database.default_values_config.default_getter import GetDefaultValues


def get_start_config_reply() -> types.ReplyKeyboardMarkup:
    """
    A function to initialize a reply keyboard markup with two buttons for changing settings and exiting.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(types.KeyboardButton('Change Settings'), types.KeyboardButton('Exit'))  # Изменить настройки -> Change Settings, Выход -> Exit
    return markup


def get_options_to_config_button() -> types.ReplyKeyboardMarkup:
    """
    A function to initialize a reply keyboard markup with buttons for different configuration options.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(types.KeyboardButton('Reset All Settings'))  # Сбросить все настройки -> Reset All Settings
    markup.row(types.KeyboardButton('Crypto Exchanges'), types.KeyboardButton('Cryptocurrencies'))  # Криптобиржи -> Crypto Exchanges, Криптовалюты -> Cryptocurrencies
    markup.row(types.KeyboardButton('Profit'), types.KeyboardButton('Exit'))  # Профит -> Profit, Выход -> Exit
    return markup


def go_exit_button() -> types.ReplyKeyboardMarkup:
    """
    A function to initialize a reply keyboard markup with an exit button.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(types.KeyboardButton('Exit'))  # Выход -> Exit
    return markup


def get_go_exit_or_clear_buttons() -> types.ReplyKeyboardMarkup:
    """
    A function to initialize a reply keyboard markup with buttons to clear the blacklist and exit.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(types.KeyboardButton('Clear Blacklist'), types.KeyboardButton('Exit'))  # Очистить черный список -> Clear Blacklist, Выход -> Exit
    return markup


def get_exchanges_buttons() -> types.ReplyKeyboardMarkup:
    """
    A function to initialize a reply keyboard markup with buttons for selecting cryptocurrency exchanges.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(types.KeyboardButton('binance'), types.KeyboardButton("bybit"), types.KeyboardButton("okx"))
    markup.row(types.KeyboardButton("kucoin"), types.KeyboardButton("upbit"), types.KeyboardButton("gateio"))
    markup.row(types.KeyboardButton("gemini"), types.KeyboardButton("zonda"), types.KeyboardButton("cryptocom"))
    markup.row(types.KeyboardButton('Exit'))  # Выход -> Exit
    return markup
