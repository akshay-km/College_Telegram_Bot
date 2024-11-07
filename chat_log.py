import datetime

def chat_log(user: str, chat_id: int, message: str = None):
    with open('chat.log', 'a') as file:
        file.write(f"[{datetime.datetime.now()}] {user} <{chat_id}> : {message if message else "New user joined"}\n")