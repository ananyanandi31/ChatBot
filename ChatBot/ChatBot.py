from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"how are you ?",
        ["I'm doing great. How about you ?", ]
    ],
    [
        r"i'm (.*) doing (.*)|i am (.*) doing (.*)",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"what is your name ?|what's your name ?",
        ["My name is ChatBot,R2D2. What's your name ?", ]
    ],
    [
        r"(my name is|i'm|i am) (.*)",
        ["Hello %2, that's a nice name", ]
    ],
    [
        r"thank you (.*)|thank you!",
        ["You're welcome" ]
    ],
    [
        r"quit|good bye|bubye|ok bye",
        ["Goodbye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]
