from telebot.types import Message
from keyboards.inline import about_developer
from loader import bot


@bot.message_handler(commands=["developer"])
def about(message: Message):
    bot.send_message(message.chat.id, 'Разработчик сервиса Иван Пермяков '
                                      'Основной директ: @DecimalChains\n'
                                      'Сотрудничество:  @Dexiles',
                     reply_markup=about_developer.about_me())
