from aiogram.types import InlineKeyboardMarkup, InputMediaPhoto, ParseMode, MediaGroup, InputMedia
from aiogram import Bot
from dotenv import load_dotenv
import os

from .reply_photo import filter_photo, nav_photo
from .models import ChildPhoto


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)


async def start_photo(chat_id):
    inline_keyboard = await filter_photo()
    await bot.send_message(chat_id,
                         '🤖💬:_ - Также существуют кнопки, которые можно прикрепить к сообщению, они называются "Inline", они более функциональны и несут больше информации внутри_',
                         reply_markup=inline_keyboard, parse_mode="Markdown")


async def future_photo(chat_id, photo_id_prev, photo_id, photo_id_next, command):
    global photo_dict
    photo_dict = {0: ['AgACAgIAAxkBAAIC6GZkdQABYm_14oTOdwSD7Pa0FkbWQwAC4uAxG_edIEuLS3oe1FkkeQEAAwIAA3kAAzUE', 'Комп))'],
                  1: ['AgACAgIAAxkBAAIC6WZkdZtMp__WQIYPbTLbC10SI0WrAALl4DEb950gS-pBJqTbelHBAQADAgADeQADNQQ', 'Город будущего'],
                  2: ['AgACAgIAAxkBAAIC62Zkdku9J29HvT9g377FuVxrCAvSAALo4DEb950gS54htXfLjoXtAQADAgADeQADNQQ', 'Пхукет будущего))']
        }
    global DICT_MES
    inline_keyboard = await nav_photo(chat_id, photo_id_prev, photo_id, photo_id_next)

    mes_media = await bot.send_photo(
        chat_id=chat_id,
        photo=photo_dict[photo_id][0],
        )
    mes_text = await bot.send_message(
        chat_id=chat_id,
        text='🤖💬:_ - Это мой короткий фотоальбом_',
        reply_markup=inline_keyboard,
        parse_mode="Markdown"
        )
    mes_media_id = mes_media.message_id
    mes_text_id = mes_text.message_id
    DICT_MES = {chat_id: {'mes_media_id': mes_media_id, 'mes_text_id': mes_text_id}}


async def now_photo(chat_id, photo_id_prev, photo_id, photo_id_next, command):
    global photo_dict
    photo_dict = {0: ['AgACAgIAAxkBAAICumZkS8-fpMtKBkud5bha29mYuVsFAAKf3zEb950gS95zfjB3h7MoAQADAgADeAADNQQ', '🤖💬: - Я на Пангане))'],
                  1: ['AgACAgIAAxkBAAICu2ZkTAMs5xuqcK4-jjvBW4zSb4fqAAKg3zEb950gS6h8psOVDZoyAQADAgADeAADNQQ', '🤖💬: - Я на Пхукете'],
                  2: ['AgACAgIAAxkBAAICuWZkS6zaRfM1mZnUxXpY1FinivvQAALt3zEbOFB5SjiIz56u2gmjAQADAgADeQADNQQ', '🤖💬: - Я на байке))']
        }
    global DICT_MES
    inline_keyboard = await nav_photo(chat_id, photo_id_prev, photo_id, photo_id_next)
    mes_media = await bot.send_photo(
        chat_id=chat_id,
        photo=photo_dict[photo_id][0],
        )
    mes_text = await bot.send_message(
        chat_id=chat_id,
        text='🤖💬:_ Это мой короткий фотоальбом_',
        reply_markup=inline_keyboard,
        parse_mode="Markdown"
        )
    mes_media_id = mes_media.message_id
    mes_text_id = mes_text.message_id
    DICT_MES = {chat_id: {'mes_media_id': mes_media_id, 'mes_text_id': mes_text_id}}

    
async def child_photo(chat_id, photo_id_prev, photo_id, photo_id_next, command):
    global photo_dict
    photo_dict = {0: ['AgACAgIAAxkBAAIB72Zjd6aVJ92dnLRNHzV0LfM-ce9aAALS3zEb950YS2OZbK4-O32gAQADAgADeQADNQQ', '🤖💬: - Вытащил меч из камня в 2012))'],
                  1: ['AgACAgIAAxkBAAIBrWZjX46Q6ObOtWoSAAEEFAX9yx1xYAACRN0xG8rxGEs7q7IYFmVS3AEAAwIAA20AAzUE', '🤖💬: - Заяц и 92го)'],
                  2: ['AgACAgIAAxkBAAIB8GZjd_k6mbrtJAXyhAABVv8IfKXn9AAC098xG_edGEt7r8PRbEgZmwEAAwIAA3kAAzUE', '🤖💬: - А это не я, это мой племянник)']
        }
    global DICT_MES
    DICT_MES = {}
    inline_keyboard = await nav_photo(chat_id, photo_id_prev, photo_id, photo_id_next)    

    mes_media = await bot.send_photo(
        chat_id=chat_id,
        photo=photo_dict[photo_id][0],
        )
    mes_text = await bot.send_message(
        chat_id=chat_id,
        text='🤖💬:_ - Это мой короткий фотоальбом_',
        reply_markup=inline_keyboard,
        parse_mode="Markdown"
        )
    mes_media_id = mes_media.message_id
    mes_text_id = mes_text.message_id
    DICT_MES = {chat_id: {'mes_media_id': mes_media_id, 'mes_text_id': mes_text_id}}


async def prev_next(chat_id, photo_id_prev, photo_id, photo_id_next, command):
    сomment_photo = {
        0: '🤖💬: - Так удобнее))',
        1: '🤖💬: - Это мой короткий фото-альбом)',
        2: '🤖💬: - Заметили, сообщения не появляются новые, мы изменяем сообщение и не засоряем экран'
    }
    
    inline_keyboard = await nav_photo(chat_id, photo_id_prev, photo_id, photo_id_next)
    await bot.edit_message_media(
        chat_id=chat_id,
        message_id=DICT_MES[chat_id]['mes_media_id'],
        media=InputMediaPhoto(photo_dict[photo_id][0])
    )
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=DICT_MES[chat_id]['mes_text_id'],
        text=сomment_photo[photo_id],
        reply_markup=inline_keyboard,
        parse_mode="Markdown"
        )
    return
    
    

async def switch_child_photo(call_id, photo_id):
    await bot.answer_callback_query(
        call_id,
        show_alert=True,
        text=photo_dict[photo_id][1]
    )