import time
now = time.ctime()
qna ={
    "hello":"hey there",
    "hi":"hey",
    "how are you":"I am fine",
    "what is your name": "My name is Jarvis",
    "how old are you":"I am 20 years old",
    "what is the time now": now,
}

while True:
    qs = input("User : ")

    if (qs == "quit"):
        break
    else:
        if qs in qna:
            print("Bot :",qna[qs.lower()])
        else:
            print("I'm not understanding your lang!")