"""Use adapters in chatterbot
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

storage_adapter = {
    "import_path": "chatterbot.storage.SQLStorageAdapter",
    "database_uri": "sqlite:///dori.db"
}

bot = ChatBot(
    "dori",
    storage_adapter=storage_adapter
)

while True:
    user_message = input("You> ")
    bot_message = bot.get_response(user_message)
    print("Bot>", bot_message)
