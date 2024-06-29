from aiogram import types
from aiogram import Bot
from dotenv import load_dotenv
import os
from aiogram.types.web_app_info import WebAppInfo
from foto.models import Client


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)

#url = "https://lyhatik.github.io/clicker.github.io/"
url = "https://lyhatik.github.io/"

web_app = WebAppInfo(url=url)

bt_restart = types.KeyboardButton(text='♻️ restart ♻️')
bt_photoalbum = types.KeyboardButton(text='📷 Фотоальбом')
bt_pay = types.KeyboardButton(text='💵 Оплата')
bt_zakaz = types.KeyboardButton(text='🤖 Заказ бота', web_app=web_app) # ccылка на приложение "заказать бот"
bt_like = types.KeyboardButton(text='♥️ Лайк') # просто лайк, в ответ кол-во лайков, запись в базу лайков.
bt_otziv = types.KeyboardButton(text='📝 Отзывы') # выдает список отзывов, и кнопка добавить отзыв
bt_profile = types.KeyboardButton(text='👛 Кошелек')
bt_clean = types.KeyboardButton(text='🗑 Очистить')
prime_keyboard = types.ReplyKeyboardMarkup(row_width=3)
prime_keyboard.add(bt_restart)
prime_keyboard.add(bt_photoalbum)
prime_keyboard.add(bt_pay)
prime_keyboard.add(bt_zakaz)
prime_keyboard.add(bt_like)
prime_keyboard.add(bt_otziv)
prime_keyboard.add(bt_profile)
prime_keyboard.add(bt_clean)


async def menu(chat_id):
    await bot.send_message(
        chat_id=chat_id,
        text='*Главно меню*:\n   - 📷 *Фотоальбом* _для ознакомления с навигацией_\n   - 💵 *Оплата*, _круто что можно платить в пару кликов_\n   - 🤖 *Заказ БОТа*, _если вы просто смотрите возможности, напишите в комметарии заказа:_ тест\n   - _♥️ Если Вам понравилось)_\n   - 📝 *Отзывы*, _хотелось бы увидеть конструктивно-негативные), это позволит мне делать продукт лучше!_\n   - 🗑 *Очистить*, _если Тебе надоел бесконечный столб сообщений._',
        reply_markup=prime_keyboard,
        parse_mode="Markdown"
        )