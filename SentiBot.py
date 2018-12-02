from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('SentiBot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  read_only=True,
                  output_adapter='chatterbot.data.TerminalAdapter',
                  database='./db.sqlite3')

chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train(
    "chatterbot.corpus.english"
)

with open('trimmed_twitter_corpus.csv') as f:
    for line in f:
        print(line, end=" ")
        bot_input = chatbot.get_response(line)

