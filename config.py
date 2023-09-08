import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME","")
BOT_TOKEN = getenv("BOT_TOKEN","6076293449:AAG2a6mKvrt2COus2O302bEBunSXioWS8K0")
API_ID = int(getenv("API_ID","20165529"))
MONGODB_URL = getenv("MONGODB_URL")
API_HASH = getenv("API_HASH","8df6f871b51473c90c6ada8df53239af")
OWNER_NAME = getenv("OWNER_NAME", "Teto")
MONGODB_URL = getenv("MONGODB_URL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "updateLaith")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5b8270a73a0315ebfd312.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "240"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
FORCE_SUBSCRIBE_TEXT = getenv("SUBSCRIBE_TEXT", f"عليك الاشتراك في قناة البوت لتتمكن من استخدامة \n- @{UPDATES_CHANNEL}")
SUBSCRIBE = getenv("SUBSCRIBE", "no")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6133404544").split()))
