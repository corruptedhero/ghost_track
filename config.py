import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GOAL_HOURS_PER_DAY = 6  # можно будет менять из настроек