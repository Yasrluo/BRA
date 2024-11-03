import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/8a8e661753d85cee921f6.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆ 𝕃𝕃𝕋ℍ𝕆ℕ ", url=f"https://t.me/A1DIIU"
            ),
            InlineKeyboardButton(
                text="☆ 𝐋𝐄𝐀𝐃𝐄𝐑 ", url=f"https://t.me/L_Q7I"
            ),
        ],
                [
            InlineKeyboardButton(
                text="☆ 𝐋𝐄𝐀𝐃𝐄𝐑 𝐒𝐀𝐃𝐃𝐀𝐌", url=f"https://t.me/H_8_o"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "✯ اغلاق ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
