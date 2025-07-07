from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # TODO: Добавить хендлеры

    print("GhostBot запущен.")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
