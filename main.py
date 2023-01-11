from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
from random import choice


load_dotenv()

bot= Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=f'''Ну здрасивуй человечина я рад тебя видеть {message.from_user.first_name},
хоть кто-то ко мне пришел за эти 100 лет''')
    await message.delete()

    
    
@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await message.answer(text='''
start - Начало
help - Список команд
myinfo - Получение все информации о себе   
picture - случайные картинки''')
    await message.delete()

    
    
@dp.message_handler(commands=['myinfo'])
async def start_command(message: types.Message):
    await message.answer(text=f'''
Я знаю все о тебе и что ты делаешь 
Твой id в мои руках: {message.from_user.id}
Твоё имя в моих руках: {message.from_user.first_name}
Твой ник в моих руках: {message.from_user.username}.''')
    await message.delete()

    
    
@dp.message_handler(commands=['picture'])
async def start_command(message: types.Message):
    photo =open('images/'  + choice(os.listdir('images')), 'rb')
    await bot.send_photo(message.chat.id,photo )
    await message.delete()

    
    
@dp.message_handler()
async def upper(message: types.Message):
    if len(message.text.split()) >=3:
        await message.reply(text=message.text.upper())
    else:
        await message.answer(text='Нам нечем разговаривать')


        
if __name__ == '__main__':
    executor.start_polling(dp)

