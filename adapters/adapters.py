"""Use adapters in chatterbot
"""
from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

BAD_WORDS = [
    "fuck",
    "fucking",
]

storage_adapter = {
    "import_path": "chatterbot.storage.SQLStorageAdapter",
    "database_uri": "sqlite:///dori.db"
}

bestmatch = {
    "import_path": "chatterbot.logic.BestMatch",
    "excluded_words": BAD_WORDS
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

specific_response = {
    "import_path": "chatterbot.logic.SpecificResponseAdapter",
    "input_text": "Wow",
    "output_text": "Yes :)"
}

logic_adapters = [
    bestmatch,
    timelogic,
    "chatterbot.logic.MathematicalEvaluation",
    specific_response,
]


def check_bot_response(bot_response: str) -> bool:
    """check the bot response

    Args:
        bot_response (str): text of bot message

    Returns:
        bool: True if is valid and False if its not valid
    """
    for word in BAD_WORDS:
        if word in bot_response:
            return False
    return True


bot = ChatBot(
    "dori",
    storage_adapter=storage_adapter,
    logic_adapters=logic_adapters,
)

while True:
    user_message = input("You> ")
    try:
        while True:
            bot_message = bot.get_response(user_message)
            if check_bot_response(bot_message.text.lower()):
                break
    except Exception as error:
        print("Bot>", "I don't understand you!")
    else:
        print("Bot>", bot_message)
