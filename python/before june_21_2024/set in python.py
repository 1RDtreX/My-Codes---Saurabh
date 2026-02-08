# first chatbot using dictionary ib python

import time
times = time.strftime("%H:%M:%S")
print(times)
rep={
    "what is your name":"I am RDtreX your personal chatbot",
    "what is the time":times,
    "what is my name":"how could i know",
}
print(rep)
print(rep.items())
# print(rep.type())