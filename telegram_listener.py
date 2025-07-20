from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import httpx

TOKEN = "5085990474:AAG0c1bblqX963zl89m7DSSfv-_6tq1frhU"
SERVER_URL = "https://samanet-poll.onrender.com/message"

async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = ' '.join(context.args)
    if not msg:
        await update.message.reply_text("⚠️ اكتب الرسالة بعد الأمر /send")
        return
    
    try:
        async with httpx.AsyncClient() as client:
            await client.post(SERVER_URL, json={"text": msg})
        await update.message.reply_text("✅ تم إرسال الرسالة إلى السيرفر بنجاح")
    except Exception as e:
        await update.message.reply_text(f"❌ حصل خطأ أثناء الإرسال: {e}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("send", send))
app.run_polling()
