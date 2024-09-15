from typing import Union
from AnieXEricaMusic.misc import SUDOERS
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message
from AnieXEricaMusic import app
from config import BANNED_USERS
from strings import get_string
from AnieXEricaMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AnieXEricaMusic.utils.decorators.language import LanguageStart
from AnieXEricaMusic.utils.formatters import get_readable_time
from AnieXEricaMusic.utils.inline import help_pannel, private_panel, start_panel

@app.on_message(filters.command(["admins", "admin"]) & ~BANNED_USERS)
@LanguageStart
async def admis(client, message: Message, _):
    sudo_users_info = []
    for user_id in SUDOERS:
        try:
            user = await client.get_users(user_id)
            mention = user.mention or f"[@{user.username}](tg://user?id={user.id})"
            sudo_users_info.append(mention)
        except Exception as e:
            print(f"Error retrieving user {user_id}: {e}")
            sudo_users_info.append(f"User {user_id}")

    if sudo_users_info:
        sudo_users_list = "\n".join(sudo_users_info)
        response_message = f"The following users are admins:\n{sudo_users_list}"
    else:
        response_message = "No admins found."
    await message.reply_text(response_message)
