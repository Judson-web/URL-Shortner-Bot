# Made with python3
# (C) @Judson-web
# Copyright permission under MIT License
# All rights reserved by Mickey
# License -> https://github.com/Judson-web/URL-Shortner-Bot/blob/main/LICENSE

import os
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyshorteners import Shortener

BITLY_API = os.environ.get("BITLY_API", None)
CUTTLY_API = os.environ.get("CUTTLY_API", None)
SHORTCM_API = os.environ.get("SHORTCM_API", None)
GPLINKS_API = os.environ.get("GPLINKS_API", None)
POST_API = os.environ.get("POST_API", None)
OWLY_API = os.environ.get("OWLY_API", None)

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text='ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ', url='https://t.me/storytym')
        ]]
    )

@Client.on_message(filters.private & filters.regex(r'https?://[^\s]+'))
async def reply_shortens(bot, update):
    message = await update.reply_text(
        text="`Aɴᴀʟʏsɪɴɢ ʏᴏᴜʀ ʟɪɴᴋ...`",
        disable_web_page_preview=True,
        quote=True
    )
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    await message.edit_text(
        text=shorten_urls,
        reply_markup=BUTTONS,
        disable_web_page_preview=True
    )

@Client.on_inline_query(filters.regex(r'https?://[^\s]+'))
async def inline_short(bot, update):
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    answers = [
        InlineQueryResultArticle(
            title="Sʜᴏʀᴛ Lɪɴᴋs",
            description=update.query,
            input_message_content=InputTextMessageContent(
                message_text=shorten_urls,
                disable_web_page_preview=True
            ),
            reply_markup=BUTTONS
        )
    ]
    await bot.answer_inline_query(
        inline_query_id=update.id,
        results=answers
    )

async def short(link):
    shorten_urls = "**sʜᴏʀᴛᴇᴅ ᴜʀʟ's**\n"
    
    # Bit.ly shorten
    if BITLY_API:
        try:
            s = Shortener(api_key=BITLY_API)
            url = s.bitly.short(link)
            shorten_urls += f"\n**Bɪᴛ.ʟʏ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"Bit.ly error :- {error}")
    
    # Chilp.it shorten
    try:
        s = Shortener()
        url = s.chilpit.short(link)
        shorten_urls += f"\n**Cʜɪʟᴘ.ɪᴛ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
    except Exception as error:
        print(f"Chilp.it error :- {error}")
    
    # Clck.ru shorten
    try:
        s = Shortener()
        url = s.clckru.short(link)
        shorten_urls += f"\n**Cʟᴄᴋ.ʀᴜ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
    except Exception as error:
        print(f"Click.ru error :- {error}")
    
    # Cutt.ly shorten
    if CUTTLY_API:
        try:
            s = Shortener(api_key=CUTTLY_API)
            url = s.cuttly.short(link)
            shorten_urls += f"\n**Cᴜᴛᴛ.ʟʏ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"Cutt.ly error :- {error}")
    
    # Da.gd shorten
    try:
        s = Shortener()
        url = s.dagd.short(link)
        shorten_urls += f"\n**Dᴀ.ɢᴅ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
    except Exception as error:
        print(f"Da.gd error :- {error}")
    
    # Git.io shorten
    if "github.com" in link or "github.io" in link:
        try:
            s = Shortener()
            url = s.gitio.short(link)
            shorten_urls += f"\n**Gɪᴛ.ɪᴏ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"Git.io error :- {error}")
    
    # Is.gd shorten
    try:
        s = Shortener()
        url = s.isgd.short(link)
        shorten_urls += f"\n**Is.ɢᴅ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
    except Exception as error:
        print(f"Is.gd error :- {error}")
    
    # Osdb.link shorten
    try:
        s = Shortener()
        url = s.osdb.short(link)
        shorten_urls += f"\n**Osᴅʙ.ʟɪɴᴋ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
    except Exception as error:
        print(f"Osdb.link error :- {error}")
    
    # Ow.ly shorten
    if OWLY_API:
        try:
            s = Shortener(api_key=OWLY_API)
            url = s.owly.short(link)
            shorten_urls += f"\n**Oᴡ.ʟʏ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"Ow.ly error :- {error}")
    
    # Po.st shorten 
    if POST_API:
        try:
            s = Shortener(api_key=POST_API)
            url = s.post.short(link)
            shorten_urls += f"\n**Pᴏ.sᴛ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"Po.st error :- {error}")
    
    # Qps.ru shorten
    try:
        s = Shortener()
        url = s.qpsru.short(link)
        shorten_urls += f"\n**Qᴘs.ʀᴜ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
    except Exception as error:
        print(f"Qps.ru error :- {error}")
    
    # Short.cm shorten
    if SHORTCM_API:
        try:
            s = Shortener(api_key=SHORTCM_API)
            url = s.shortcm.short(link)
            shorten_urls += f"\n**Sʜᴏʀᴛ.ᴄᴍ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"Short.cm error :- {error}")
    
    # TinyURL.com shorten
    try:
        s = Shortener()
        url = s.tinyurl.short(link)
        shorten_urls += f"\n**TɪɴʏURL.ᴄᴏᴍ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
    except Exception as error:
        print(f"TinyURL.com error :- {error}")
    
    # NullPointer shorten
    try:
        # 0x0.st shorten
        try:
            s = Shortener(domain='https://0x0.st')
            url = s.nullpointer.short(link)
            shorten_urls += f"\n**0x0.st :-** [Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"0x0.st :- {error}")
        # ttm.sh shorten
        try:
            s = Shortener(domain='https://ttm.sh')
            url = s.nullpointer.short(link)
            shorten_urls += f"\n**ᴛᴛᴍ.sʜ :-**[Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"ttm.sh :- {error}")
    except Exception as error:
        print(f"NullPointer error :- {error}")
    
    # GPLinks shorten
    if GPLINKS_API:
        try:
            api_url = "https://gplinks.in/api"
            params = {'api': GPLINKS_API, 'url': link}
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url, params=params, raise_for_status=True) as response:
                    data = await response.json()
                    url = data["shortenedUrl"]
                    shorten_urls += f"\n**GPLɪɴᴋs.ɪɴ :-** [Cʟɪᴄᴋ Mᴇ]({url})"
        except Exception as error:
            print(f"GPLink error :- {error}")
    
    # Send the text
    try:
        shorten_urls += "\n\nMᴀᴅᴇ ʙʏ [Tᴇʀʀᴏʀ Mɪᴄᴋᴇʏ](https://t.me/VAMPIRE_KING_NO_1)"
        return shorten_urls
    except Exception as error:
        return error
