"""
Rio music Bot, Telegram Voice Chat Userbot
Copyright (C) 2021  Zaute Km | TGVCSETS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, emoji
from utils import mp
from config import Config
playlist=Config.playlist

HELP = """
**اوامر الاعضاء**
▷/play قم بالرد على الاغنيه او الملف الصوتي
▷/dplay قم بالرد على رابط الاغنيه من Deezer
▷/player: عرض الأغنية الحالية قيد التشغيل.
▷/help: اظهار الاوامر
▷/playlist: عرض قائمه التشغيل

**اوامر الادمنيه:**
▷/skip تخطي الاغنيه
▷/join: انمضام المحادثه الصوتيه
▷/leave: مغادرة المجادثه الصوتيه
▷/vc: تحقق الانضمام للمحادثات الصوتيه
▷/stop: ايقاف التشغيل
▷/radio: تشغيل الراديو
▷/stopradio: ايقاف تشغيل الراديو
▷/replay: اعادة تشغيل من البدايه
▷/clean: قم بإزالة ملفات RAW PCM غير المستخدمة.
▷/pause: ايقاف مؤقت
▷/resume: استئناف التشغيل
▷/volume: اختيار الصوت من (0-200).
▷/mute: كتم بالمحادثات الصوتيه
▷/unmute: الغاء كتم بالمحادثات الصوتيه
▷/restart: اعادة تشغيل البوت
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.from_user.id not in Config.ADMINS and query.data != "help":
        await query.answer(
            "Who the hell you are",
            show_alert=True
            )
        return
    else:
        await query.answer()
    if query.data == "replay":
        group_call = mp.group_call
        if not playlist:
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"{emoji.NO_ENTRY} قائمة تشغيل فارغة"
        else:
            pl = f"{emoji.PLAY_BUTTON} **قائمة تشغيل**:\n" + "\n".join([
                f"**{i}**. **🎸{x[1]}**\n   👤**موصى به:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(
                f"{pl}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="pause"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data == "pause":
        if not playlist:
            return
        else:
            mp.group_call.pause_playout()
            pl = f"{emoji.PLAY_BUTTON} **قائمة تشغيل**:\n" + "\n".join([
                f"**{i}**. **🎸{x[1]}**\n   👤**موصى به:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Paused\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="resume"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    
    elif query.data == "resume":   
        if not playlist:
            return
        else:
            mp.group_call.resume_playout()
            pl = f"{emoji.PLAY_BUTTON} **قائمة تشغيل**:\n" + "\n".join([
                f"**{i}**. **🎸{x[1]}**\n   👤**موصى به:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Resumed\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="pause"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data=="skip":   
        if not playlist:
            return
        else:
            await mp.skip_current_playing()
            pl = f"{emoji.PLAY_BUTTON} **قائمة تشغيل**:\n" + "\n".join([
                f"**{i}**. **🎸{x[1]}**\n   👤**موصى به:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Skipped\n\n{pl}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄", callback_data="replay"),
                        InlineKeyboardButton("⏯", callback_data="pause"),
                        InlineKeyboardButton("⏩", callback_data="skip")
                            
                    ],
                ]
            )
        )
        except:
            pass
    elif query.data=="help":
        buttons = [
            [
                InlineKeyboardButton('قناة المطور', url='https://t.me/w5555'),
            ],
            [
               InlineKeyboardButton('المطور', url='https://t.me/tsttt'),
               InlineKeyboardButton('الححساب المساعد', url='https://t.me/xriomusic'),
            ],
            [
               InlineKeyboardButton('قناة البوت', url='https://t.me/L9L9L'),
        
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            HELP,
            reply_markup=reply_markup

        )

