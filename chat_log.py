import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='chat.log',encoding='utf-8', level=logging.DEBUG)


def chat_log(user: str, chat_id: int, message: str = None):
    logger.debug(f"TELBOT >>> [{datetime.datetime.now()}] {user} <{chat_id}> : {message if message else {'New user joined'}}\n")
    with open('chat.log', 'a') as file:
        file.write(f"[{datetime.datetime.now()}] {user} <{chat_id}> : {message if message else {'New user joined'}}\n")