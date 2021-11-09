"""Simple ChatBot
"""
# Third party imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    "Mohammad",  # Bot name is `Mohammad`
    read_only=True,  # The bot learns in chat with the user
    logic_adapters=[
        # To perform simple mathematical operations.
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.TimeLogicAdapter"  # To work with time.
    ]
)

trainer = ListTrainer(bot)
trainer.train(
    [
        "Hello",
        "Hi",
        "How are you?",
        "I am good. What about you?",
        "I am fine.",
        "Do you like apple?"
    ]
)

while True:
    user_message = input("You> ")
    bot_message = bot.get_response(user_message)
    print("Bot>", bot_message)
