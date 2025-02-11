import asyncio
import gtts

from aiogram import Bot, Router, F, types
from aiogram.filters import Command

router = Router()

@router.message(Command('say'), F.text)
async def echo_voice(message: types.Message):
    _, text_to_voice = message.text.split('say', maxsplit=1)
    voice = gtts.gTTS(text_to_voice, lang='ru')
    voice.save('voice.mp3')
    voice_file = types.FSInputFile('voice.mp3')
    await message.answer_voice(voice_file)
    await message.reply('Ваш текст:' + text_to_voice)