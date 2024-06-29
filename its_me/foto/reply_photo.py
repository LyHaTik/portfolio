from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from foto.models import Client


# Составляет кнопки для поиска авто
async def filter_photo():
    in_child_photo = InlineKeyboardButton('👶 Child 👶', callback_data='child_photo/')
    in_now_photo = InlineKeyboardButton('👱‍♂️ Now 👱‍♂️', callback_data='now_photo/')
    in_future_photo = InlineKeyboardButton('👴 Future 👴', callback_data='future_photo/')
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(in_child_photo)
    inline_keyboard.add(in_now_photo)
    inline_keyboard.add(in_future_photo)

    return inline_keyboard


# Составляет кнопки для поиска авто
async def nav_photo(chat_id, photo_id_prev, photo_id, photo_id_next):

    bt_prev = InlineKeyboardButton(
        text='⬅️prev',
        callback_data=f'prev/{photo_id_prev}'
        )

    bt_next = InlineKeyboardButton(
        text='next➡️',
        callback_data=f'next/{photo_id_next}'
        )

    bt_info = InlineKeyboardButton(
        text='ℹ️ info',
        callback_data=f'info/{photo_id}'
        )
    bt_da = InlineKeyboardButton(
        text='🔆 DA 🔆',
        callback_data=f'da_foto/{photo_id}'
        )
    bt_line1 = [bt_prev, bt_info, bt_next]
    bt_line2 = [bt_da]

    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(*bt_line1)
    client = Client.objects.get(id=chat_id)
    if client.dacoin_foto == False:
        inline_keyboard.add(*bt_line2)
        
    return inline_keyboard
