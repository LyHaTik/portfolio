from aiogram.types import LabeledPrice, Message, PreCheckoutQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot
from dotenv import load_dotenv
import os
import time
from foto.models import Client

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)


async def order(message: Message):
    chat_id = message.chat.id
    await bot.send_message(
        chat_id=chat_id,
        text='🤖💬: _- рекомендую сохранить данные карты для последующего ввода_\n \
        \n \
        Для оплаты используйте данные тестовой карты: 1111 1111 1111 1026, 12/22, CVC 000',
        parse_mode="Markdown"
        )
    await bot.send_invoice(
        chat_id=chat_id,    
        title='Покупка через Telegram бот(ЮКаssa)',
        description=' Тут описание покупаемого продукта(создается автоматически)',
        payload='Patment through a bot',
        provider_token='381764678:TEST:87816',
        currency='rub',
        prices={
            LabeledPrice(
                label='Working Time Machine',
                amount=10000
            ),
            LabeledPrice(
                label='Gift wrapping',
                amount=100
            )
        },
        #max_tip_amount=500,
        #suggested_tip_amounts=[100, 200],
        start_parameter='nztcoder',
        #=None,
        #photo_url=None,
        #photo_size=None,
        #photo_width=None,
        #photo_height=None,
        #need_name=True,
        #need_phone_number=True,
        #need_email=True,
        #nees_shipping_address=False,
        #send_phone_number_to_provider=False,
        #send_email_to_provider=False,
        #is_flexible=False,
        #disable_notification=False,
        #protect_ontent=False,
        #reply_to_message_id=None,
        #allow_sending_without_reply=True,
        #reply_markup=None,
        #request_timeout=15
    )


async def successful_payment(message: Message):
    msg = f'💵 Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.' \
        f'\r\n - Наш менеджер полчил заявку и уже набирает Ваш номер телефона.'
    # Сообщение продавцу об оплате продукта.
    bt_da = InlineKeyboardButton(
        text='🔆 DA 🔆',
        callback_data=f'da_pay/1'
        )
    inline_keyboard = InlineKeyboardMarkup()
    bt_line1 = [bt_da]
    user_id = message.chat.id
    client = Client.objects.get(id=user_id)
    
    if client.dacoin_pay == False:
        inline_keyboard.add(*bt_line1)
    await message.answer(msg)
    await message.answer(
        text='🤖💬: _- Мы протестировали олаты через Юkassa, но возможность приема платежей есть:\n- Сбер\n- ЮКасса\n- Bank 131\n- PayMaster\n- ПСБ\n- Robokassa\n- PayBox.money\n- Redsys\n- Stripe\n- Paycom.Uz\n- CLICK Uzbekistan\n- Tranzzo\n- ECOMMPAY\n- И многое другое.._',
        parse_mode="Markdown",
        reply_markup=inline_keyboard
        )

async def pre_checkout(pre_checkout_query: PreCheckoutQuery):
    # Отправляем запрос продавцу о готовности товара
    # Если получаем положительный ответ, запускаем следующую функцию
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
