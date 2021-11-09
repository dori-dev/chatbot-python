"""Use adapters in chatterbot
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

storage_adapter = {
    "import_path": "chatterbot.storage.SQLStorageAdapter",
    "database_uri": "sqlite:///dori.db"
}

logic_adapters = [
    {
        "import_path": "chatterbot.logic.BestMatch",
        "excluded_words": ["Fuck"]
    }
]

bot = ChatBot(
    "dori",
    storage_adapter=storage_adapter,
    logic_adapters=logic_adapters,
)

while True:
    user_message = input("You> ")
    bot_message = bot.get_response(user_message)
    print("Bot>", bot_message)
