'''dictionary'''
from datetime import datetime

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

print(datetime.now())
aliens = [alien_0, alien_1, alien_2]
print(aliens)

print(aliens[0]['color'])
print(datetime.now())

'''input from user'''
prompt = "tell me your name and"
prompt += " I will say it back: "

print(input(prompt))


prompt = "loop will run till you type 'exit'"
message = ""
while message != "exit":
    message = input(prompt)
    print(message)
