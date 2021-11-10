"""Use adapters in chatterbot
"""
from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

storage_adapter = {
    "import_path": "chatterbot.storage.SQLStorageAdapter",
    "database_uri": "sqlite:///dori.db"
}

bestmatch = {
    "import_path": "chatterbot.logic.BestMatch",
    "excluded_words": [
        "fuck",
    ]
}

timelogic = {
    "import_path": "chatterbot.logic.TimeLogicAdapter",
    "negative": [
        "How are you?",
        "How old are you?",
        "What is 2 + 2",
        "What is 4 / 4",
        "What is 5 plus 5"
    ]
}


logic_adapters = [
    bestmatch,
    timelogic,
    "chatterbot.logic.MathematicalEvaluation",
]

bot = ChatBot(
    "dori",
    storage_adapter=storage_adapter,
    logic_adapters=logic_adapters,
)

while True:
    user_message = input("You> ")
    try:
        bot_message = bot.get_response(user_message)
    except Exception as error:
        print("Bot>", "I don't understand you!")
    else:
        print("Bot>", bot_message)
