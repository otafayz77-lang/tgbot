import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv("8323634874:AAFNAA2j3qJHLn4xHgM9S-kdCZu_JiB4OnY")

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

kitoblar = {
    1: {"nomi": "Shum Bola", "muallif": "G'afur G'ulom"},
    2: {"nomi": "O'tgan Kunlar", "muallif": "Abdulla Qodiriy"},
    3: {"nomi": "Mehrobdan Chayon", "muallif": "Abdulla Qodiriy"},
}

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Kitob nomini kiriting yoki /kitoblar deb yozing")

@router.message(Command("kitoblar"))
async def kitoblar_handler(message: Message):
    text = "Mavjud kitoblar:\n"
    for i, k in kitoblar.items():
        text += f"{i}. {k['nomi']} - {k['muallif']}\n"
    await message.answer(text)

@router.message(F.text.regexp(r"^\d+$"))
async def tanlash(message: Message):
    son = int(message.text)
    if son in kitoblar:
        k = kitoblar[son]
        await message.answer(f"{k['nomi']} - {k['muallif']}")
    else:
        await message.answer("Bunday kitob yo'q")

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
