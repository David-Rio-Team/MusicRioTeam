"""
Rio music Bot, Telegram Voice Chat Userbot
Copyright (C) 2021  ZauteKm <https://telegram.dog/ZauteKm>
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
from pyrogram import Client, filters
from utils import USERNAME
from config import Config
ADMINS=Config.ADMINS
from pyrogram.errors import BotInlineDisabled
@Client.on_message(filters.private & ~filters.bot & filters.incoming & ~filters.service & ~filters.me)
async def reply(client, message): 
    try:
        inline = await client.get_inline_bot_results(USERNAME, "ORU_MANDAN_PM_VANNU")
        await client.send_inline_bot_result(
            message.chat.id,
            query_id=inline.query_id,
            result_id=inline.results[0].id,
            hide_via=True
            )
    except BotInlineDisabled:
        for admin in ADMINS:
            try:
                await client.send_message(chat_id=admin, text=f"مرحبا\nلقد قمت بتعطيل وضع الانلاين @{USERNAME}\n\nقم بتفعيل وضع الانلاين @{USERNAME} من @Botfather للرد عليه")
            except Exception as e:
                print(e)
                pass

    except Exception as e:
        print(e)
        pass
