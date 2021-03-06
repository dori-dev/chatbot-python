"""Smart Chatbot(persian)
"""
# Standard library import
from time import strftime
import logging

# Local imports
from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

# Fix `No value for search_text was available on the provided input`
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


class SimplePersianTimeLogic(LogicAdapter):
    """Simple persian time logic
    """

    def __init__(self, chatbot, **kw):
        super().__init__(chatbot, **kw)
        self.positive = kw.get("positive", [
            "ساعت",
            "زمان",
            "ساعت چند است",
            "ساعت چنده",
            "زمان را بگو"
        ])

    def process(self, statement, additional_response_selection_parameters=None):
        for word in self.positive:
            if word in statement.text:
                time = strftime("%H:%M")
                return Statement(text=f"ساعت {time} است", confidence=1.0)
        return Statement(text="!نمیفهمم", confidence=0.0)


bot = ChatBot(
    "smart",
    storage_adapter={
        "import_path": "chatterbot.storage.SQLStorageAdapter",
        "database_uri": "sqlite:///fa-smart.db"
    },
    logic_adapters=[
        "__main__.SimplePersianTimeLogic",
        "chatterbot.logic.BestMatch"
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
# Use chatterbot corpus data to train bot
trainer.train("chatterbot.corpus.persian")

while True:
    user_message = input("شما: ")
    bot_message = bot.get_response(user_message)
    print("بات:", bot_message)
