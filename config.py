import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 21443012
API_HASH = "ae78a60518ea5b9d3043a76ad2c34e5f"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7649501561:AAHuTvTuwz7GBREI-G7ufnsuJNBFaHOUQ14"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://kaarioo:<S6wPreZOHGiETDI8>@cluster0.awhii.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002289124285

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7543230601

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/uren_craft"
SUPPORT_GROUP = "https://t.me/uren_craft"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFHMcQAqROig6zOQTUsYZF0NWTteXMUpSxb7nr8hP7F7PhhfZR568StKtRsSQGODJufNK0PrBCUEW-c4bcVQalLytSN7p-yZKJBOaGNWdD7-mrmoSOIeP7B1OslqjAJ-i2O2LHi-8wf1xpj0py64-3-keT_VDVBHVPr-J0_fBHVH2JP94bznFWc89wr9WNuyNTBeT4nH_BxtsaKZyMM1UtPAQuo4-5LW8l1quIlJZX6ZsotC8j42z0pRBqDGgpThUc32LX7yexmXN1rmlhFqU_E5e2AhSkCUPQTu0H8Mc6BurrcxJHCqrHR4tk0YUQV_MME8-sXyNloX6Hj6QUI7LDi_M8WKQAAAAHNX6eHAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"

PING_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
STATS_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
STREAM_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/9e3c76656f79d96952696-06ba90ce3bce63b6b5.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
