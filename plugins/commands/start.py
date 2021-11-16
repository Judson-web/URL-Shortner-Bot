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

HELP_TEXT = """**Hᴇʏ, Fᴏʟʟᴏᴡ ᴛʜᴇsᴇ sᴛᴇᴘs:**

➠ Jᴜsᴛ sᴇɴᴅ ᴀ ʟɪɴᴋ ғᴏʀ sʜᴏʀᴛɪɴɢ.
➠ I ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ sʜᴏʀᴛᴇᴅ ʟɪɴᴋs.
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ', url='https://telegram.me/FayasNoushad'),
        ]]
    )
