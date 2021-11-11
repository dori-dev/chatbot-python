"""Smart Chatbot(english)
"""
# Third party imports
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    "smart",
    storage_adapter={
        "import_path": "chatterbot.storage.SQLStorageAdapter",
        "database_uri": "sqlite:///en-smart.db"
    }
)

trainer = ChatterBotCorpusTrainer(bot)
# Use chatterbot corpus data to train bot
trainer.train("chatterbot.corpus.english")

while True:
    user_message = input("You> ")
    bot_message = bot.get_response(user_message)
    print("Bot>", bot_message)
