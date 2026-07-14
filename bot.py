from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = "YAHAN_APNA_BOT_TOKEN_DALE"

QR = "1000057338.jpg"

HELP = """
🎮 Welcome to Ludo Champions Bot

💰 Deposit / QR / Pay / Payment / UPI
➡️ Get Deposit QR

💸 Withdraw
➡️ @Payment_hub9

👨‍💼 Support
➡️ @Ludo_Champions9
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"🎉 Welcome {user.first_name}!\n"
            "🏆 Welcome to Ludo Champions.\n"
            "Type Help to see all commands."
        )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if any(x in text for x in ["deposit", "qr", "pay", "payment", "upi"]):
        await update.message.reply_photo(
            photo=open(QR, "rb"),
            caption="💰 Scan QR and send payment screenshot."
        )

    elif "withdraw" in text:
        await update.message.reply_text("💸 Withdrawal Admin:\n@Payment_hub9")

    elif "support" in text:
        await update.message.reply_text("👨‍💼 Support:\n@Ludo_Champions9")

    elif "help" in text:
        await update.message.reply_text(HELP)

app = Application.builder().token(TOKEN).build()

app.add_handler
