from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot( 'SentiBot',
                   storage_adapter='chatterbot.storage.SQLStorageAdapter',
                   output_adapter='chatterbot.data.TerminalAdapter',
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch",
                           "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
                           "response_selection_method": "chatterbot.response_selection.get_sentiment_response"
                       }
                   ],
                   database='./db.sqlite3')

chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train(
    "chatterbot.corpus.english"
)

while True:
    try:
        bot_input = chatbot.get_response( input() )

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
