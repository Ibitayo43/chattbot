import nltk
from nltk.chat.util import Chat, reflections
print(Chat)

reflections

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name?",
        ["You can call me a chatbot ?",]
    ],
    [
        r"how are you ?|how are you doing ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you? ",
        ["i am looking for movies to watch|i am looking for movies|i am looking for movies to download|i'm looking for movies to watch|i'm looking for movies to download|looking for movies to watch|looking for movies to download",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"i am looking for movies to watch|i am looking for movies to download|i'm looking for movies to watch|i'm looking for movies to download|looking for movies to watch|looking for movies to download|looking for movies|i am looking for movies|i'm looking for movies ",
        ["Oh okay, what are your preferences, Action, Romance, Drama or Comedy",]
    ],
    [
        r"Action",
        ["Here are few action movies you can download; Avengers, John Wick, Terminator",]
    ],
    [
        r"Drama",
        ["Here are few drama movies you can download; Gone girl, Almost Christmas, American Outlaws",]
    ],
    [
        r"Comedy",
        ["Here are few comedy movies you can download; Instant family, Think like a man, Why him"]
    ],
    [
        r"Romance",
        ["Here are few romance movies you can watch; The choice, Everything everything, The great gatsby",]
    ],
    [
        r"(.*) thank you so much, that was helpful|thanks|Thanks|thank you|Thank you|Thanks so much",
        ["I am happy to help",]
    ],
    [
        r"quit|bye|Bye",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def chatbot():
        print("Hi, I'm the chatbot you built") 

chatbot()

chat = Chat(set_pairs, reflections)
print(chat)

chat.converse()
if __name__ == "__main__":
    chatbot()
