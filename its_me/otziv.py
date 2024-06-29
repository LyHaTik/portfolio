from foto.models import Otziv, Client
from aiogram import types
from aiogram import Bot
from dotenv import load_dotenv
import os
from prime_menu import prime_keyboard


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)



async def show_otziv(message):
    
    bt_ok = types.InlineKeyboardButton('📝 Написать', callback_data='otziv')
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    keyboard.add(bt_ok)
    
    otziv_list = Otziv.objects.filter()
    if not otziv_list:
        await message.answer(
            f'🤖💬: _Отзывов пока нет.._',
            parse_mode="Markdown",
            reply_markup=keyboard
            )
    text = ''
    for otziv_obj in otziv_list:
        otziv = otziv_obj.text
        otziv_author = otziv_obj.username
        text = text + f' "{otziv}"    @{otziv_author}\n\n'
    await message.answer(text)
        
    await message.answer(
        '🤖💬: _-Напиши свой отзыв!_',
        reply_markup=keyboard,
        parse_mode="Markdown"
        )


async def write(chat_id):
    
    bt_cancel = types.KeyboardButton('❌ Отмена')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(bt_cancel)
    await bot.send_message(
        chat_id=chat_id,
        text="🤖💬: - _Напишите отзыв в поле ввода сообщений..._",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


async def create(message):
    username = message['from']['username']
    chat_id = message.chat.id
    text = message.text
    Otziv.objects.create(username=username, text=text)
    client = Client.objects.get(id=chat_id)
    
    keyboard = prime_keyboard
    if client.dacoin_otzivi == False:
        bt_da = types.KeyboardButton(
            text='💬 DA 💬'
        )
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt_line1 = [bt_da]
        keyboard.add(*bt_line1)

    await message.answer(
        text="🤖💬: _- Спасибо. Отзыв добавлен в БД_",
        parse_mode="Markdown",
        reply_markup=keyboard
    )