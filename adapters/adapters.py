"""Use adapters in chatterbot
"""
# Third party import
from chatterbot import ChatBot

# Local imports
from adapters_list import logic_adapters, storage_adapter
from adapters_list import BAD_WORDS


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
    except Exception:
        print("Bot>", "I don't understand you!")
    else:
        print("Bot>", bot_message)
