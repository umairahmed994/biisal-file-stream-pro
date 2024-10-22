# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "Bɪɪsᴀʟ Fɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://telegram.me/bisal_files"
bisal_grp = "https://t.me/+PA8OPL2Zglk3MDM1"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('28671918', ''))
    API_HASH = str(getenv('c92b387142fe889740967b453c28d364', ''))
    BOT_TOKEN = str(getenv('7529441813:AAGwmdjLkzM5oRdpkClbKYz1go1t1alESfA' , ''))
    name = str(getenv('name', '@Martin_Movies_Bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_Channel', '-1002480131358'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '7267485571  6689366151'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "6689366151").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Umair_Ahmed_Panhwer'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('@Martin_Movies_Bot')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('mongodb+srv://UMAIR:UMAIR 123@cluster0.9ehgh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', ''))
    UPDATES_CHANNEL = str(getenv('UBZ_BOTS', 'bisal_files')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002446979598")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ Umair_Ahmed_Panhwer ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
