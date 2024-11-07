from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
from chat_log import chat_log

load_dotenv()
TOKEN = os.getenv('TOKEN')
SECRET = os.getenv('SECRET')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id)
    text = f"""
        Dear {update.effective_user.first_name},\n
        Welcome to the official chat assistant of __ABC Engineering College__ , XYZ Town.
        \nhttps://www.mgu.ac.in | +91 123456789 | mail@abc_college.in \n\n
        You can chat or use the following commands for interacting with this bot :\n
        /start - Start the bot.\n
        /help - Get help.\n
        /marklist - Get the marklist of your ward.\n
        /attendance - Get the attendance details. \n
        /notifications -  Get the latest notices and updates. \n
        /exams - Get details on upcoming exams. \n
        /events - Get details on upcoming events. \n
        /contact - Get contact details. \n
        /location - Get link to Google Maps Location.
    """

    with open('files/abc_college_cover.jpg', 'rb') as photo:
        await context.bot.send_photo(chat_id=update.effective_chat.id,
                                     photo=photo,
                                     caption=text)


async def bot_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)
    help_text = """
        You can chat with the bot or use the following commands for interacting with this bot :\n
        /start - Start the bot.\n
        /help - Get help.\n
        /marklist - Get the marklist of your ward.\n
        /attendance - Get the attendance details. \n
        /notifications -  Get the latest notices or updates from the College \n
        /exams - Get details on upcoming exams. \n
        /events - Get details on upcoming events. \n
        /contact - Contact details. \n
        /location - Get link to Google Maps Location.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=help_text)


async def mark_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)

    with open('files/sem2-marklist.pdf', 'rb') as file:
        await context.bot.send_document(chat_id=update.effective_chat.id,
                                        document=file,
                                        caption="Mark list for the Second Semester."
                                                "\n Do you need help with anything else?")


async def attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)

    with open('files/sem3-attendance.pdf', 'rb') as file:
        await context.bot.send_document(chat_id=update.effective_chat.id,
                                        document=file,
                                        caption="Attendance details for the Third Semester (current)."
                                                "\n Do you need help with anything else?")


async def notifications(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)
    with open('files/PTA-meeting-notice.pdf', 'rb') as notice:
        await context.bot.send_document(chat_id=update.effective_chat.id,
                                        document=notice,
                                        caption="Latest notice regarding PTA meeting."
                                                "\nWell will notify on further updates."
                                                "\nDo you need help with anything else?")


async def exams(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)

    with open('files/exam-timetable-midterm.pdf', 'rb') as file:
        await context.bot.send_document(chat_id=update.effective_chat.id,
                                        document=file,
                                        caption="Mid-term exams starts at 12-04-2025."
                                                "\n Do you need help with anything else?")


async def events(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="The Tech Fest for the year 2024-2025 is scheduled to be organised on March."
                                        "Further details will be notified later.\n"
                                        "Do you need help with anything else?")


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="https://www.mgu.ac.in\n"
                                        "Call us at +91-0123456789\n"
                                        "E-mail: support@abc_college\n"
                                        "Address: ABC College, XYZ Town\n"
                                   )


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Address: ABC College of Engineering,\nXYZ Town, 666 666"
                                        "\nGoogle Maps link: https://maps.app.goo.gl/ckiWbJir2SaWtx8A6")


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Address: __ABC College of Engineering__,\nXYZ Town, 666 666"
                                        "\nGoogle *Maps* link \- [Location](https://maps.app.goo.gl/ckiWbJir2SaWtx8A6)",
                                   parse_mode='MarkdownV2')


async def other_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    send_sorry = True

    if "marklist" in message or "mark list" in message or "marks" in message:
        send_sorry = False
        await mark_list(update, context)
    if "attendance" in message:
        send_sorry = False
        await attendance(update, context)
    if "exams" in message or "timetable" in message or "exam" in message:
        send_sorry = False
        await exams(update, context)
    if "events" in message or "event" in message:
        send_sorry = False
        await events(update, context)
    if "notifications" in message or "updates" in message or "notice" in message or "meeting" in message:
        send_sorry = False
        await notifications(update, context)
    if "contact" in message or "phone" in message or "mail" in message or "website" in message:
        send_sorry = False
        await contact(update, context)
    if "location" in message or "address" in message or "how to reach" in message:
        send_sorry = False
        await location(update, context)
    if "help" in message or "commands" in message or "feature" in message:
        send_sorry = False
        await bot_help(update, context)
    if "hi" in message or "hello" in message or "hai" in message or "start" in message:
        send_sorry = False
        await start(update, context)

    if send_sorry:
        chat_log(update.effective_user.first_name, update.effective_chat.id, update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Sorry, we could not recognise your command. Please see /help for more.")


bot_app = ApplicationBuilder().token(TOKEN).build()

bot_app.add_handler(CommandHandler('start', start))
bot_app.add_handler(CommandHandler('help', bot_help))
bot_app.add_handler(CommandHandler('marklist', mark_list))
bot_app.add_handler(CommandHandler('attendance', attendance))
bot_app.add_handler(CommandHandler('notifications', notifications))
bot_app.add_handler(CommandHandler('exams', exams))
bot_app.add_handler(CommandHandler('events', events))
bot_app.add_handler(CommandHandler('contact', contact))
bot_app.add_handler(CommandHandler('location', location))
bot_app.add_handler(CommandHandler('test', test))
other_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, other_messages)
bot_app.add_handler(other_message_handler)

print("Starting bot...")
bot_app.run_webhook(listen='0.0.0.0',
                    port=1000,
                    secret_token=SECRET,
                    webhook_url='https://collegedemotelbot.onrender.com:443'
                    )
