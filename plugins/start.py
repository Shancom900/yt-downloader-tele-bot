
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="https://t.me/SHONU_TOOLS")
      ],
      [ 
        InlineKeyboardButton(
            "Support ", url="https://t.me/SHONU")]
    ])
    welcomed = f"<b> Hey {message.from_user.first_name} , \n\nI'm YouTube DL Bot. I can download video or audio f\n rom Youtube. \n\nMade by @SHONU 🇱🇰/help for More info </b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagatio
