import os

API_ID = os.getenv("API_ID", "27823209")
API_HASH = os.getenv("API_HASH", "1d693fcf3bfea119ca1d9057b08a4495")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", "6004928770"))

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001738045764"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://aibotmv28:aibotmv28@cluster0.mkzpuv8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Force Subscribe Enable
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "-1002327045567,-1002414808225") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyDojXqjZT7VvCVIQ2-l3mkmopbMoyo0W7Q")
