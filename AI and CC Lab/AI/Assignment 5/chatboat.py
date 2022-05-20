import nltk
from nltk.chat.util import Chat, reflections

reflections = {
"i am" : "you are",
"i was" : "you were",
"i" : "you",
"i'm" : "you are",
"i'd" : "you would",
"i've" : "you have",
"i'll" : "you will",
"my" : "your",
"you are" : "I am",
"you were" : "I was",
"you've" : "I have",
"you'll" : "I will",
"your" : "my",
"yours" : "mine",
"you" : "me",
"me" : "you"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by TechHotel. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"services?",
        ["Room Booking system , Swimming Pool available , Big hall is available for function and many more..",]
    ],
    [
        r"Types of Rooms?",
        ["1. Single Bed Room \n 2. Double Bed Room \n 3. AC Room \n 4. Non AC Room" ,]
    ],
    [
        r"Price of Rooms?",
        ["1. Single Bed Room : 500 \n 2. Double Bed Room : 700 \n 3. AC Room : 1000 \n 4. Non AC Room : 600;",]
    ],
    [
        r"Food?",
        ["Food \t\t Time \t\tPrice \nBreakfast \t9.00 A.M, \t150Rs \nLunch \t\t1.00 P.M, \t350Rs \nDinner \t\t7.00 P.M, \t550Rs ",]
    ],
]


def chat():
    print("Hi! I am a chatbot created by TechHotel for your service")
    chat = Chat(pairs, reflections)
    chat.converse()

#initiate the conversation
if __name__ == "__main__":
    chat()