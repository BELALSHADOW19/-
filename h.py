from pyrogram import Client

api_id = "15170853"
api_hash = "33f17f7ccfa43fd779489dca8ab67e34"
bot_token = "6291803682:AAHIWpA4xRm9J2XHKA_2xIZGwDHB6PrUtCA"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
