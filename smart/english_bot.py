"""Smart Chatbot(english)
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    "smart",
    storage_adapter={
        "import_path": "chatterbot.storage.SQLStorageAdapter",
        "database_uri": "sqlite:///smart.db"
    }
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
