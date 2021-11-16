# Author: Mickey (https://github.com/Judson-web) (@Judson-web)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
`Hᴇʟʟᴏ {} 😌`
`I ᴀᴍ ᴀ ʟɪɴᴋ sʜᴏʀᴛɴᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ,`

>> `I ᴄᴀɴ sʜᴏʀᴛ ᴀɴʏ ᴛʏᴘᴇ ᴏғ ʟɪɴᴋ`

   `Usɪɴɢ ᴍᴇ ɪs sɪᴍᴘʟᴇ`

>> `Sᴇɴᴅ ᴍᴇ Lɪɴᴋ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sʜᴏʀᴛᴇɴ`
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
        ]]
    )

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
      
      HELP_TEXT = """
`Hɪ {} 😌`
Usɪɴɢ ᴍᴇ ɪs sɪᴍᴘʟᴇ ᴀs Exᴘʟᴀɪɴᴇᴅ ʙᴇʟᴏᴡ

> Sᴇɴᴅ ᴍᴇ Lɪɴᴋ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sʜᴏʀᴛᴇɴ 
• Tʜᴀᴛs Aʟʟ 💜...
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
        ]]
    )

@Client.on_message(filters.private & filters.command(["help"]))
async def start(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
