"""Smart Chatbot(persian)
"""
from time import strftime
from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement


class SimplePersianTimeLogic(LogicAdapter):
    """Simple persian time logic
    """
    positive_words = [
        "ساعت",
        "زمان",
    ]

    def __init__(self, chatbot, **kw):
        super().__init__(chatbot, **kw)
        self.positive = kw.get("positive", self.positive_words)

    def process(self, statement, additional_response_selection_parameters=None):
        for word in self.positive:
            if word in statement.text:
                time = strftime("%H:%M")
                return Statement(text=f"ساعت {time} است", confidence=1.0)
        return Statement(text="!نمیفهمم", confidence=0.0)
