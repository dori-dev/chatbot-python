"""Simple ChatBot
"""
# Third party imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Mohammad")  # Bot name is `Mohammad`
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
    bot_message = "Bot> ", bot.get_response(user_message)
    print(bot_message)