from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"

API_KEY = "YOUR_TMDB_API_KEY"
TMDB_BASE_URL = "https://api.themoviedb.org/3"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! اسم یک فیلم یا سریال رو برام بفرست تا اطلاعاتش رو بگم 🎬")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    response = requests.get(
        f"{TMDB_BASE_URL}/search/movie",
        params={"api_key": API_KEY, "query": query, "language": "fa"}
    )
    data = response.json()
    if data["results"]:
        movie = data["results"][0]
        title = movie["title"]
        overview = movie.get("overview", "خلاصه‌ای موجود نیست.")
        rating = movie.get("vote_average", "بدون امتیاز")
        await update.message.reply_text(f"🎬 {title}\n⭐ امتیاز: {rating}\n📖 خلاصه: {overview}")
    else:
        await update.message.reply_text("متاسفم، چیزی پیدا نکردم.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("search", start))
    app.add_handler(CommandHandler("film", start))
    app.add_handler(CommandHandler("movie", start))
    app.add_handler(CommandHandler("سریال", start))
    app.add_handler(CommandHandler("فیلم", start))
    app.add_handler(CommandHandler("شروع", start))
    app.add_handler(CommandHandler("راهنما", start))
    app.add_handler(CommandHandler("جستجو", start))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("search", start))
    app.add_handler(CommandHandler("film", start))
    app.add_handler(CommandHandler("movie", start))
    app.add_handler(CommandHandler("سریال", start))
    app.add_handler(CommandHandler("فیلم", start))
    app.add_handler(CommandHandler("شروع", start))
    app.add_handler(CommandHandler("راهنما", start))
    app.add_handler(CommandHandler("جستجو", start))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("search", start))
    app.add_handler(CommandHandler("film", start))
    app.add_handler(CommandHandler("movie", start))
    app.add_handler(CommandHandler("سریال", start))
    app.add_handler(CommandHandler("فیلم", start))
    app.add_handler(CommandHandler("شروع", start))
    app.add_handler(CommandHandler("راهنما", start))
    app.add_handler(CommandHandler("جستجو", start))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("search", start))
    app.add_handler(CommandHandler("film", start))
    app.add_handler(CommandHandler("movie", start))
    app.add_handler(CommandHandler("سریال", start))
    app.add_handler(CommandHandler("فیلم", start))
    app.add_handler(CommandHandler("شروع", start))
    app.add_handler(CommandHandler("راهنما", start))
    app.add_handler(CommandHandler("جستجو", start))
    app.run_polling()

if __name__ == "__main__":
    main()
