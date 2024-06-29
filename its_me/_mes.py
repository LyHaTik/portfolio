from dotenv import load_dotenv
import os
from aiogram import Bot
from aiogram import types
from prime_menu import menu


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)


async def del_mes(message):
    from_mes = message['from']
    chat_id = from_mes['id']
    mes_id = message['message_id']
    error_del_mes = False
    while error_del_mes == False:
        try:
            await bot.delete_message(chat_id=chat_id, message_id=mes_id)
            mes_id = mes_id - 1
        except:
            error_del_mes =True

    await message.answer('Все сообщения удалены.')
    await menu(chat_id)
