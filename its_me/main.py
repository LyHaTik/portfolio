from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from dotenv import load_dotenv
import os, sys
import json
import hashlib

import start_bd

from foto.models import Client
from foto.foto import start_photo, child_photo, switch_child_photo, prev_next, now_photo, future_photo
from prime_menu import menu, prime_keyboard
from _mes import del_mes
from parse_call import _parse_call
from pay import order, pre_checkout, successful_payment
from like import health
from otziv import show_otziv, write, create
from check_coin import check, change


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class WriteOtziv(StatesGroup):
    choosing_otziv = State()


# СТАРТ
@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    user_id = message.chat.id
    username = message.chat.username
    
    bt_ok = types.KeyboardButton('🔆 DA 🔆')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(bt_ok)
    
    # Проверяем существует ли клиент в БД
    try:
        Client.objects.get(id=user_id)
        await message.answer(
            f'Снова привет, {username}!',
            reply_markup=prime_keyboard
            )
        # Добписать вывод кол-ва ДА
    except:
        Client.objects.create(id=user_id, username=username)
        await message.answer_video_note('DQACAgIAAxkBAANQZliZ2fxHZgx3htUr6-mosHfIZ4gAAqRJAALeKMFKW__2OdhzrNo1BA')

        # Дописать приветственный текст
        await message.answer(
            f' Привет {username},\n я 🤖 БОТ "ДА" v.0.1. \n - Сейчас ты познакомишься с ботами телеграмм\n - За каждое "DA" ты будешь получать "DAcoin" 🤑 \n - 💰 "DAcoin" можно обменять на скидку на мои услуги',
            reply_markup=keyboard
            )
        await bot.send_message(
            chat_id=6382427107,
            text=f'Новый пользователь: @{username}'
            )

# Принимает стикеры
@dp.message_handler(content_types=['video_note'])
async def check_sticker(message: types.Message):
    print(message)


# Принимает фото
@dp.message_handler(content_types=['sticker'])
async def check_photo(message: types.Message):
    print(message)


# Принимает фото
@dp.message_handler(content_types=['animation'])
async def check_photo(message: types.Message):
    print(message)


# Обрабатывает все сообщения
@dp.message_handler()
async def message_dispatcher(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    
    if message.text == '👛 Кошелек':
        total_coin, percent_discount = await check(chat_id)
        
        bt_change = types.InlineKeyboardButton(
            text='Обменять на Скидку',
            callback_data=f'change/{total_coin}'
        )
        bt_line = [bt_change]
        inline_keyboard = types.InlineKeyboardMarkup()
        if percent_discount <= total_coin:
            inline_keyboard.add(*bt_line)
        
        await message.answer(
            f'У вас *{total_coin}* 🔆 DAcoin 🔆\n Найдешь еще? Всего *11*.\nСкидка *{percent_discount}*%',
            parse_mode="Markdown",
            reply_markup=inline_keyboard
            )
        
    if message.text == '🔆 DA 🔆':
        client = Client.objects.get(id=chat_id)
        if client.dacoin_general == False:
            client.dacoin_general = True
            client.save()
            await message.answer_sticker('CAACAgIAAxkBAAIHdmZxTaOzpD5Vq8Gmo5hjzOyMnjJgAAJEAANBtVYMWkioov96ZxQ1BA')
            await message.answer(
                '🤖💬: - _Первый Dacoin!!!_',
                parse_mode="Markdown",
                reply_markup=prime_keyboard
                )
        await menu(chat_id)

    if message.text == '💬 DA 💬':
        client = Client.objects.get(id=chat_id)
        if client.dacoin_otzivi == False:
            client.dacoin_otzivi = True
            client.save()
            await message.answer_sticker('CAACAgIAAxkBAAIIOmZxcsu7zemwPwxtkFXSohJJ4kpeAALpGwAChX8QSdFyHQZ-cUfnNQQ')
            await message.answer(
                '🤖💬: - _Тройной Dacoin получен!!!_',
                parse_mode="Markdown",
                reply_markup=prime_keyboard
                )
        await menu(chat_id)

    if message.text == '♥️ DA ♥️':
        client = Client.objects.get(id=chat_id)
        if client.dacoin_like == False:
            client.dacoin_like = True
            client.save()
            await message.answer_sticker('CAACAgIAAxkBAAIIOmZxcsu7zemwPwxtkFXSohJJ4kpeAALpGwAChX8QSdFyHQZ-cUfnNQQ')
            await message.answer(
                '🤖💬: - _Двойной Dacoin!!!_',
                parse_mode="Markdown",
                reply_markup=prime_keyboard
                )
        await menu(chat_id)
        
    if message.text == '🗑 Очистить':
        await del_mes(message)
        
    if message.text == '📷 Фотоальбом':
        await start_photo(chat_id)
        
    if message.text == '♻️ restart ♻️':
        await menu(chat_id)
        
    if message.text == '💵 Оплата':
        await order(message)
        
    if message.text == '♥️ Лайк':
        await health(message)
        
    if message.text == '📝 Отзывы':
        await show_otziv(message)


# Обрабатывает написание отзыва
@dp.message_handler(state=WriteOtziv.choosing_otziv)
async def tap_otziv(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    if message.text == '❌ Отмена':
        await state.finish()
        await menu(chat_id)
        return
    await create(message)
    await state.finish()


# Обрабатывает коллбек "otziv"
@dp.callback_query_handler(lambda c: c.data=='otziv')
async def callback_otziv(call: types.CallbackQuery, state: FSMContext):
    chat_id = call['from'].id
    await write(chat_id)
    # Устанавливаем пользователю состояние "пишет отзыв"
    await state.set_state(WriteOtziv.choosing_otziv.state)


# Обрабатывает коллбеки
@dp.callback_query_handler(lambda c: c.data)
async def callback_child_photo(call: types.CallbackQuery):
    chat_id = call['from'].id
    # Парсит колбек вызов
    command, photo_id = await _parse_call(call)
    
    if command == 'change':
        total_coin = photo_id
        print(f'Всего {total_coin}')
        discount_percent, discount_password = await change(chat_id, total_coin)
        print(f'Всего {discount_percent, discount_password}')
        await bot.send_message(
            chat_id,
            f'Вы получили скидку: *{discount_percent}%*\n Пароль для скидки: *{discount_password}*',
            parse_mode="Markdown",
        )
        
    if command == 'da_foto':
        # Добавляем ДА
        client = Client.objects.get(id=chat_id)
        client.dacoin_foto = True
        client.save()
        await bot.send_sticker(
            chat_id,
            'CAACAgIAAxkBAAIHdmZxTaOzpD5Vq8Gmo5hjzOyMnjJgAAJEAANBtVYMWkioov96ZxQ1BA')
        await bot.send_message(
            chat_id,
            '🤖💬: - _Еще один Dacoin!!!_',
            parse_mode="Markdown",
            reply_markup=prime_keyboard
            )
        await start_photo(chat_id)
        return
    
    if command == 'da_pay':
        # Добавляем ДА
        client = Client.objects.get(id=chat_id)
        client.dacoin_pay = True
        client.save()
        await bot.send_sticker(
            chat_id,
            'CAACAgIAAxkBAAIHdmZxTaOzpD5Vq8Gmo5hjzOyMnjJgAAJEAANBtVYMWkioov96ZxQ1BA')
        await bot.send_message(
            chat_id,
            '🤖💬: - _Еще один Dacoin!!!_',
            parse_mode="Markdown",
            reply_markup=prime_keyboard
            )
        await menu(chat_id)
        return
    
    if command == 'now_photo':
        photo_id_prev = 0
        photo_id = 1
        photo_id_next = 2
        await now_photo(chat_id, photo_id_prev, photo_id, photo_id_next, command)
    if command == 'child_photo':
        photo_id_prev = 0
        photo_id = 1
        photo_id_next = 2
        await child_photo(chat_id, photo_id_prev, photo_id, photo_id_next, command)
        return
    if command == 'future_photo':
        photo_id_prev = 0
        photo_id = 1
        photo_id_next = 2
        await future_photo(chat_id, photo_id_prev, photo_id, photo_id_next, command)
        return
    if command == 'prev' or command == 'next':
        if photo_id == '0':
            photo_id_prev = 2
            photo_id = int(photo_id)
            photo_id_next = 1
            await prev_next(chat_id, photo_id_prev, photo_id, photo_id_next, command)
            return
        if photo_id == '1':
            photo_id_prev = 0
            photo_id = int(photo_id)
            photo_id_next = 2
            await prev_next(chat_id, photo_id_prev, photo_id, photo_id_next, command)
            return
        if photo_id == '2':
            photo_id_prev = 1
            photo_id = int(photo_id)
            photo_id_next = 0
            await prev_next(chat_id, photo_id_prev, photo_id, photo_id_next, command)
            return
    if command == 'info':
        photo_id = int(photo_id)
        call_id = call.id
        await switch_child_photo(call_id, photo_id)


# Перехватывает сообщения inline режима(доработать)
@dp.inline_handler()
async def inline_handler(inline_query: types.InlineQuery):
    text = inline_query.query or 'Echo'
    link = 'https://ru.wikipedia.org/wiki/'+text
    input_content = types.InputTextMessageContent(link)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    
    item = types.InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        url=link,
        title='Поиск гугл)',
    )
    
    await bot.answer_inline_query(
        inline_query_id=inline_query.id,
        results=[item],
        cache_time=1
    )


# Оплата
@dp.pre_checkout_query_handler(lambda pre_checkout_query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await pre_checkout(pre_checkout_query)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_pay(message: types.Message):
    await successful_payment(message)


# Перехватывает контекст с web_app
@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    # Собираем данные с web_app
    res = json.loads(message.web_app_data.data)
    from_mes = message['from']
    user_id = from_mes['id']
    username = from_mes['username']
    name = res['name']
    email = res['email']
    phone = res['phone']
    comment = res['comment']
    
    client = Client.objects.get(id=user_id)
    if client.dacoin_bot == False:
        client.dacoin_bot = True
        client.save()
        await bot.send_sticker(
            user_id,
            'CAACAgIAAxkBAAIHdmZxTaOzpD5Vq8Gmo5hjzOyMnjJgAAJEAANBtVYMWkioov96ZxQ1BA'
            )
    await bot.send_message(
        chat_id=6382427107,
        text=f'Заказ от @{username}:\n \
            Имя: {name}\n \
            email: {email}\n \
            тел. {phone}\n \
            Комментарий: {comment}'
            )

    await bot.send_message(
        chat_id=user_id,
        text='🤖💬: _- я передал данные разработчику ..._',
        parse_mode="Markdown"
    )

executor.start_polling(dp)
