import os
from dotenv import load_dotenv, find_dotenv

# ✅ Check if .env file is found, otherwise exit
if not find_dotenv():
    exit("Environment variables are not loaded because the .env file is missing.")
else:
    load_dotenv()

# ✅ Get BOT_TOKEN from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ✅ Default commands with descriptions
DEFAULT_COMMANDS = (
    ("start", "Start the bot"),
    ("help", "Usage documentation"),
    ("config", "Configure user settings for arbitrage"),
    ("arbitrage", "Cryptocurrency arbitrage tool"),
    ("developer", "Information about the developer")
)

# ✅ Date and time formats
DATE_FORMAT = "%d.%m.%Y"
TIME_FORMAT = "%H:%M:%S"
DATE_FORMAT_FULL = "%d.%m.%Y, %H:%M:%S"
DATE_FORMAT_IN = "%d.%m.%Y at %H:%M:%S (Moscow Time)")
ROUND_VALUE = 5
TIME = "%H:%M:%S"
DATE = "%d-%m-%Y"
Y = '%Y'
