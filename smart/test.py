from time import strftime
from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer


class SimplePersianTimeLogic(LogicAdapter):
    def __init__(self, chatbot, **kw):
        super().__init__(chatbot, **kw)
        self.positive = kw.get("positive", [
            "ساعت",
            "زمان",
            "ساعت چند است",
            "ساعت چنده",
            "زمان را بگو"
        ])

    def can_process(self, statement):
        for word in self.positive:
            if word in statement.text:
                return True
        return False

    def process(self, statement, additional_response_selection_parameters=None):
        for word in self.positive:
            if word in statement.text:
                print('*', statement.text, '*')
                t = strftime("%H:%M")
                return Statement(text=f"ساعت {t} است", confidence=1.0)
        return Statement(text="نمی‌فهمم", confidence=0.0)


bot = ChatBot(
    "smart",
    storage_adapter={
        "import_path": "chatterbot.storage.SQLStorageAdapter",
        "database_uri": "sqlite:///smart.db"
    },
    logic_adapters=[
        "__main__.SimplePersianTimeLogic",
        "chatterbot.logic.BestMatch"
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.persian")

while True:
    user = input("شما: ")
    bot_msg = bot.get_response(user)
    print("بات: ", bot_msg)
