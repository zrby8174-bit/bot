import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiohttp import web
from database import init_db

# إعدادات البوت
TOKEN = "8907852009:AAG-8AMTwac-2v1iZka5Kdil7Y3hY2iC7lc"
CENTRAL_CHANNEL_ID = -100123456789  # ضع هنا معرف القناة المركزية

bot = Bot(token=TOKEN)
dp = Dispatcher()

# استقبال أي رسالة من القنوات المرتبطة
@dp.message(F.chat.type.in_({'channel'}))
async def forward_message(message: Message):
    # هنا يتم التوجيه للقناة المركزية
    await bot.copy_message(
        chat_id=CENTRAL_CHANNEL_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )

# كود لتشغيل سيرفر بسيط يمنع البوت من التوقف في Render
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080)))
    await site.start()

async def main():
    await init_db()  # تشغيل قاعدة البيانات
    await start_web_server() # تشغيل السيرفر
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
