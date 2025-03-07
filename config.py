# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ 

class Config:
    API_ID = int(environ.get("12097668", ""))
    API_HASH = environ.get("a57f1feaa8b6f507e8431bdd4455be05", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("mongodb+srv://rahulgautam2802:S74pGhoJf7iZyK8Y@cluster0.zofd9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("5442433204", ""))

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
