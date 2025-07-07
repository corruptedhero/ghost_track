from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("➕ Добавить процесс", callback_data="add_process")],
        [InlineKeyboardButton("📋 Мои процессы", callback_data="list_processes")],
        [InlineKeyboardButton("📊 Отчёт", callback_data="stats_today")],
        [InlineKeyboardButton("⚙ Настройки", callback_data="settings")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("💀 GhostBot: контроль начат", reply_markup=reply_markup)
