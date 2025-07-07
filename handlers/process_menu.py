from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from database import get_processes, toggle_process, delete_process

async def show_processes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    processes = get_processes(user_id)

    if not processes:
        await query.edit_message_text("У тебя нет процессов.")
        return

    buttons = []
    for process in processes:
        pid, name, is_active = process
        status = "⏸" if is_active else "▶️"
        buttons.append([
            InlineKeyboardButton(f"{status} {name}", callback_data=f"toggle_{pid}"),
            InlineKeyboardButton("🗑", callback_data=f"delete_{pid}")
        ])

    keyboard = buttons + [[InlineKeyboardButton("🔙 Назад", callback_data="back_to_menu")]]
    await query.edit_message_text("📋 Твои процессы:", reply_markup=InlineKeyboardMarkup(keyboard))


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("toggle_"):
        pid = int(data.split("_")[1])
        toggle_process(pid)
        await show_processes(update, context)

    elif data.startswith("delete_"):
        pid = int(data.split("_")[1])
        delete_process(pid)
        await show_processes(update, context)
