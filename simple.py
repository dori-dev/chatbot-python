"""Simple ChatBot
"""
# Third party imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    "Mohammad",  # Bot name is `Mohammad`
    read_only=True,  # The bot learns in chat with the user
    logic_adapters=[
        # Selects a response based on the best known match to a given statement.
        "chatterbot.logic.BestMatch",
        # Answer questions about the current time.
        "chatterbot.logic.TimeLogicAdapter",
        # Manage any combination of word and numeric operator for mathematical calculations.
        "chatterbot.logic.MathematicalEvaluation"
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
