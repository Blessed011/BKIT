from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot('5882928044:AAHtbnoltpRXNY1VIMKn7lWHsOTNj0_cWhE')
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/description')
b2 = KeyboardButton('/choice')
kb.add(b1).insert(b2)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b4 = KeyboardButton('/red')
b5 = KeyboardButton('/green')
b6 = KeyboardButton('/brown')
b7 = KeyboardButton('/blue')
kb2.add(b4).insert(b5).insert(b6).insert(b7)





@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Приветствую!",
                           parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="👁 Я могу отправить Вам фотографии глаз разного цвета! 👁"
                                "   Для этого выберите цвет, кликнув на '/choice' 😄",
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['red'])
async def photo_command(message: types.Message):
    with open(f'photos/red.png', 'rb') as photo:
        await bot.send_photo(message.from_user.id,
                              photo=photo)
        await message.delete()

@dp.message_handler(commands=['green'])
async def photo_command(message: types.Message):
    with open(f'photos/green.png', 'rb') as photo:
        await bot.send_photo(message.from_user.id,
                              photo=photo)
        await message.delete()

@dp.message_handler(commands=['brown'])
async def photo_command(message: types.Message):
    with open(f'photos/brown.jpg', 'rb') as photo:
        await bot.send_photo(message.from_user.id,
                              photo=photo)
        await message.delete()

@dp.message_handler(commands=['blue'])
async def photo_command(message: types.Message):
    with open(f'photos/blue.jpg', 'rb') as photo:
        await bot.send_photo(message.from_user.id,
                              photo=photo)
        await message.delete()

@dp.message_handler(commands=['choice'])
async def choice_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Выберите, пожалуйста, желаемый цвет",
                           parse_mode="HTML",
                           reply_markup=kb2)
    await message.delete()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
