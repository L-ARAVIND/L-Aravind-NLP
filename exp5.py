from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["running", "flies", "happiness"]

for word in words:
    print(word, "->", ps.stem(word))
