from foto.models import Like
from aiogram import types


async def health(message):
    like = Like.objects.get(id=1)
    like.like = like.like + 1
    like.save()
    dif = like.like%2
    if dif == 1:
        await message.answer_sticker('CAACAgIAAxkBAAID8GZnBmIVdsua6X05tE5ht7TUj35zAAKfHgACOkkpSXXiamE21BzyNQQ')
        await message.answer(
            f'🤖💬:\n_ - я набрал "{like.like}" ♥️\n - Что будет, если лайки будут кратны 10 ??? Попробуй)_',
            parse_mode="Markdown"
            )
    if dif == 0:
        await message.answer(
            '🤖💬:\n_ - Попробуй лайкнуть еще раз)_',
            parse_mode="Markdown"
            )
    dif10 = like.like%10
    if dif10 == 0:
        bt_ok = types.KeyboardButton('♥️ DA ♥️')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(bt_ok)
        await message.answer(
            f'🤖💬:\n_- я набрал "{like.like}"   ♥️_',
            reply_markup=keyboard,
            parse_mode="Markdown"
            )
