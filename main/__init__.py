#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "13750040"
API_HASH = "6553ea819bb17098b0e3c62530823328"
BOT_TOKEN = "6052295632:AAG3SR53VHX66YdMz0YMa8-DSzypwRT5leA"
SESSION = "BQBnFfyHF-PhuexNUyPkwt5Y2UkDQg8eCOtBidb39UomEQxdqE75b9K1VuNrhDwvENSvdt-jBfbK9v-fgWyFnbzjae4HcGIBgfZQjn_K6-Sijw4gFvwGUSWGfE3AgVGygm4amJGOfr1hykdUZFZkAuVnHPLBcoais1CPjFPYD8jdy5eeD67nSt8NxNRls23nMelp4h_cs0hwljNugWkHC9_oOVoYdC0Cc-IAMsD1M_03mJLC3iHPH5hncuVswCORrd_OXakUDQS8u5wZBVfwuG27rhUVK4oT6k__N9m5zcgHOctlUDQ05pv-cSBClAq3vOV0O8yDBGmepanGSN0V5bwrAAAAAXUZulgA"
FORCESUB = "amthespy"
AUTH = "5842877813"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
