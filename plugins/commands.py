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

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES, mp
from config import Config
import os
import sys
import subprocess
import asyncio
from signal import SIGINT
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>مرحبا [{}](tg://user?id={})\n\nانا مشغل الاغاني بدون توقف\n\nلاظهار الاوامر ارسل /help</b>"
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



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
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
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
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
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await message.delete()
@Client.on_message(filters.command(["restart", f"restart@{U}"]) & filters.user(Config.ADMINS))
async def restart(client, message):
    await message.reply_text("🔄...جاري اعادة التشغيل")
    await message.delete()
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
    os.execl(sys.executable, sys.executable, *sys.argv)

