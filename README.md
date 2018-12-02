# SentiBot
Research project comparing different methods (specifically word- and subword-based vector embeddings) to create more empathetic chatbot responses to natural language input using sentiment analysis.

Read a summary of this project's methodology and results: https://www.overleaf.com/read/jvwwgbcsywht

## Use the demo
This project features a demo of a chatbot that detects the sentiment of the user's input, and responds with an appropriate statement of similar sentiment. The chatbot is built on the Chatterbot framework by Gunther Cox, available under the BSD 3-Clause License: https://github.com/gunthercox/ChatterBot

Note: the demo requires the Chatterbot library, the gensim Python library, as well as the FastText wiki corpus with subword vectors, which can be found here: https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki-news-300d-1M-subword.vec.zip

Instructions:

1. Clone this repo
2. Install gensim using pip, and unzip the FastText wiki corpus in the same folder as 'SentiBot-demo.py'.
3. Unzip the 'Chatterbot.zip' file and copy it into the location of the Chatterbot library, overwriting any duplicate files.
3. Run the SentiBot-demo.py script to interact with the chatbot
