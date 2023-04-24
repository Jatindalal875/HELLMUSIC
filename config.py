from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900000000000000"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/bd72db7afa8a08a916d49.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/9a246bd831590d22d2582.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EAGLE_MAFIA_CLUB")
CHAT_GROUP = getenv("CHAT_GRP", "https://t.me/EAGLE_MAFIA_CLUB")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5388906652").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
