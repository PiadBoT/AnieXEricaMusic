from typing import Union
from AnieXEricaMusic.misc import SUDOERS
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message
from AnieXEricaMusic import app

@app.on_message(filters.command(["admins", "admin"]) & ~BANNED_USERS)
@LanguageStart
async def admis(client, message: Message, _):
    # Retrieve user information
    sudo_users_info = []
    for user_id in SUDOERS:
        try:
            user = await client.get_users(user_id)
            # Construct mention string using user.username or user.mention
            mention = user.mention or f"[@{user.username}](tg://user?id={user.id})"
            sudo_users_info.append(mention)
        except Exception as e:
            print(f"Error retrieving user {user_id}: {e}")
            sudo_users_info.append(f"User {user_id}")

    if sudo_users_info:
        sudo_users_list = "\n".join(sudo_users_info)
        response_message = f"The following users are Bot admins:\n{sudo_users_list}"
    else:
        response_message = "No admins found."
    await message.reply_text(response_message, parse_mode="Markdown")

