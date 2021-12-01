import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 
dcbot = Client(
    "DC ID Tracker TG Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@dcbot.on_message(filters.private & filters.text & filters.command(["start"]))
async def start(bot, message):
    button =[[ InlineKeyboardButton("📢 Join Channel", url="t.me/Mo_Tech_YT") ],[ InlineKeyboardButton("⛏️ Open Source", url="https://github.com/PR0FESS0R-99/DC-Tracker-TG-Bot") ]]
    text = """Hello <b>{}</b>, Your Telegram DC ID Is : <b>{}</b>"""
    await message.reply_text(
        text=text.format(message.from_user.mention, message.from_user.dc_id),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(button)
    )

dcbot.run()
