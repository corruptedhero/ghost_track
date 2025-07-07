from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from handlers.main_menu import start
from handlers.process_menu import show_processes, handle_callback

async def run():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(show_processes, pattern="^list_processes$"))
    app.add_handler(CallbackQueryHandler(handle_callback, pattern="^(toggle_|delete_)"))
    app.add_handler(CallbackQueryHandler(start, pattern="^back_to_menu$"))

    print("GhostBot запущен.")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())
