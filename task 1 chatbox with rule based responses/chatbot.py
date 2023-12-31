# simple chatbot code using module
from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer



chatbot=ChatBot('chatbot project bot')

# Create chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
			"chatterbot.corpus.english.conversations" )

response = chatbot.get_response('What is your Number')
print(response)

response = chatbot.get_response('Who are you?')
print(response)
