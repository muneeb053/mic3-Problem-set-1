# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Fri Mar 24 02:14:44 2023)---
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Training data
conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.'
]

# Train the chatbot based on the conversation data
trainer.train(conversation)


# Get a response to a user input
response = chatbot.get_response('How are you?')

print(response)

# More training data
more_conversation = [
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]

# Train the chatbot with more conversation data
trainer.train(more_conversation)

# Get a response to a user input
response = chatbot.get_response('What is your name?')

print(response)
pip install pip==21.3.1
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Training data
conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.'
]

# Train the chatbot based on the conversation data
trainer.train(conversation)


# Get a response to a user input
response = chatbot.get_response('How are you?')

print(response)

# More training data
more_conversation = [
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]

# Train the chatbot with more conversation data
trainer.train(more_conversation)

# Get a response to a user input
response = chatbot.get_response('What is your name?')

print(response)
python -m chatterbot --version
pip install --upgrade chatterbot
from chatterbot import ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Training data
conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.'
]

# Train the chatbot based on the conversation data
trainer.train(conversation)


# Get a response to a user input
response = chatbot.get_response('How are you?')

print(response)

# More training data
more_conversation = [
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]

# Train the chatbot with more conversation data
trainer.train(more_conversation)

# Get a response to a user input
response = chatbot.get_response('What is your name?')

print(response)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('MyBot')

chatbot = ChatBot('MyBot')
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('MyBot')
trainer = ListTrainer(chatbot)
conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.'
]
trainer.train(conversation)
response = chatbot.get_response('How are you?')
print(response)
more_conversation = [
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]
trainer.train(more_conversation)
response = chatbot.get_response('What is your name?')
print(response)
response = chatbot.get_response('What do you do?')
print(response)
response = chatbot.get_response('What languages you cna speak')

print(response)
pandas
pip install pandas
C:\ProgramData\Anaconda3\python.exe -m pip install --upgrade pip'
C:\ProgramData\Anaconda3\python.exe -m pip install --upgrade pip
python.exe -m pip install --upgrade pip
python.exe -m pip --upgrade pip
pip install csvreader
C:\ProgramData\Anaconda3\python.exe -m pip install --upgrade pip
df = pd.read_csv('C:\Users\acer1\Downloads\archive\TEDTalks.csv')
print(df)
df = pd.read_csv(r'C:\Users\acer1\Downloads\archive\TEDTalks.csv')
print(df)
import pandas as pd
df = pd.read_csv(r'C:\Users\acer1\Downloads\archive\TEDTalks.csv')
print(df)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
import csvreader as csv


df = pd.read_csv(r'C:\Users\acer1\Downloads\archive\TEDTalks.csv')
print(df)



# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Training data
conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.',
    df['content']
]

# Train the chatbot based on the conversation data
trainer.train(conversation)


# Get a response to a user input
response = chatbot.get_response('How are you?')

print(response)

# More training data
more_conversation = [
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]

# Train the chatbot with more conversation data
trainer.train(more_conversation)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
import csvreader as csv


df = pd.read_csv(r'C:\Users\acer1\Downloads\archive\TEDTalks.csv')
print(df)

df['content'] = df['content'].str.strip('content ')

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Training data
conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.',
    df['content']
]

# Train the chatbot based on the conversation data
trainer.train(conversation)


# Get a response to a user input
response = chatbot.get_response('How are you?')

print(response)

# More training data
more_conversation = [
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]

# Train the chatbot with more conversation data
trainer.train(more_conversation)
df['content'] = df['content'].str.strip('content ')
trainer.train(conversation)
df['content'] = df['content'].str.extract(r'(\d+)')
trainer.train(conversation)

trainer.train(conversation)
df['content'] = df['content'].str.strip()
trainer.train(conversation)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
import csvreader as csv


df = pd.read_csv(r'C:\Users\acer1\Downloads\archive\TEDTalks.csv')
print(df)

df['content'] = df['content'].str.strip()

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Training data
conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.',
    df['content']
]

# Train the chatbot based on the conversation data
trainer.train(conversation)


# Get a response to a user input
response = chatbot.get_response('How are you?')

print(response)

# More training data
more_conversation = [
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]

# Train the chatbot with more conversation data
trainer.train(more_conversation)

# Get a response to a user input
response = chatbot.get_response('What languages you cna speak')

print(response)
df['content'] = df['content'].astype(str).str.strip()
trainer.train(conversation)
df['content'] = df['content'].astype(str).str.strip()
trainer.train(conversation)
df['content'] = df['content'].astype(str).str.strip()
df.dropna(subset=['content'], inplace=True)
conversation2 = list(df['content'])
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)
trainer.train(conversation)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
import csvreader as csv


df = pd.read_csv(r'C:\Users\acer1\Downloads\archive\TEDTalks.csv')
print(df)

df['content'] = df['content'].astype(str).str.strip()

# Remove any rows with missing data
df.dropna(subset=['content'], inplace=True)

# Combine all the strings in the 'content' column into one list
conversation = list(df['content'])
chatbot = ChatBot('MyBot')
trainer = ListTrainer(chatbot)
trainer.train(conversation)
more_conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.',
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]

# Train the chatbot with more conversation data
trainer.train(more_conversation)
response = chatbot.get_response('What languages can you speak')

print(response)
response = chatbot.get_response('What is life')

print(response)
response = chatbot.get_response('climate change')

print(response)
response = chatbot.get_response('positivity')

print(response)
response = chatbot.get_response('hi')

print(response)
response = chatbot.get_response('hi, there!')

print(response)
response = chatbot.get_response( 'How old are you?')

print(response)

response = chatbot.get_response( 'How are you?')

print(response)
trainer2 = ListTrainer(chatbot)
trainer.train(more_conversation)
trainer.train(large_conversation)
more_conversation = [
    'Hello',
    'Hi there!',
    'How are you?',
    'I\'m doing great.',
    'That is good to hear',
    'Thank you.',
    'You\'re welcome.',
    'What is your name?',
    'My name is MyBot.',
    'How old are you?',
    'I am one year old.',
    'Where do you live?',
    'I live in your computer.',
    'What do you like to do?',
    'I like to chat with people.'
]
large_conversation = [
'Hello there!',
'Hi, how are you?',
'I\'m doing well, thank you. How about you?',
'I\'m doing pretty good too, thanks for asking.',
'That\'s great to hear.',
'What have you been up to lately?',
'Not too much, just keeping busy with work and hobbies.',
'What kind of hobbies do you have?',
'I enjoy reading, playing video games, and going for walks.',
'That sounds like fun.',
'What about you, what do you like to do for fun?',
'I like to watch movies, listen to music, and spend time with friends.',
'Those are all great activities.',
'What is your favorite type of music?',
'I really enjoy rock music, especially classic rock.',
'What is your favorite band?',
'My favorite band is Led Zeppelin. What about you?',
'I\'m a big fan of The Beatles.',
'Oh, they are one of my favorites too.',
'Do you have any pets?',
'Yes, I have a cat named Whiskers. What about you?',
'I have a dog named Max.',
'That\'s cool. What breed is Max?',
'He is a golden retriever.',
'They are such friendly dogs.',
'Yes, he loves everyone he meets.',
'What do you do for work?',
'I am a software engineer. What about you?',
'I\'m a teacher.',
'That must be a rewarding job.',
'It definitely has its challenges, but it is very fulfilling.',
'What subject do you teach?',
'I teach English.',
'That\'s great. I always loved reading and writing in school.',
'Me too. It\'s a great way to express yourself.',
'Well, it was nice chatting with you.',
'Yes, it was nice chatting with you too. Take care!'
]


travel_conversation = [
'Have you been on any trips lately?',
'Yes, I went to Japan last month.',
'That sounds amazing. What did you do there?',
'I visited Tokyo, Kyoto, and Osaka. It was a great experience.',
'Did you try any new foods?',
'Yes, I tried sushi for the first time and it was delicious.',
'What was your favorite part of the trip?',
'I really enjoyed visiting the temples and shrines in Kyoto.',
'That sounds like a great trip.',
'Have you been to any interesting places lately?',
'Yes, I went on a hiking trip in the mountains last weekend.',
'That sounds like a lot of fun. How was the scenery?',
'It was breathtaking. We saw a lot of beautiful waterfalls and wildlife.',
'What was the most challenging part of the hike?',
'The steep inclines were definitely a challenge, but it was worth it for the views.',
'I love hiking too. Do you have any favorite hiking spots?',
'I really enjoy hiking in the national parks. Yellowstone is one of my favorites.',
'That\'s on my bucket list. I hope to go there someday.',
'You definitely should. It\'s an amazing experience.',
]


food_conversation = [
'What is your favorite type of cuisine?',
'I love Italian food. What about you?',
'I\'m a big fan of Mexican food.',
'What is your favorite Mexican dish?',
'I really love tacos al pastor. They are so flavorful.',
'That sounds delicious. Have you ever tried making them yourself?',
'Yes, I have a great recipe that I use at home.',
'What is your favorite Italian dish?',
'I love spaghetti carbonara. It\'s so rich and creamy.',
'That\'s one of my favorites too. Have you ever tried making it from scratch?',
'Yes, I learned how to make it when I visited Italy a few years ago.',
'That\'s amazing. I bet it tasted incredible.',
'What other types of cuisine do you enjoy?',
'I also enjoy Japanese cuisine. Sushi and ramen are two of my favorites.',
'Those are great choices. I love the flavors in Japanese food.',
'Me too. It\'s so fresh and flavorful.',
]


sports_conversation = [
'Do you follow any sports?',
'Yes, I\'m a big basketball fan. What about you?',
'I enjoy watching football.',
'What team do you root for?',
'I\'m a fan of the Green Bay Packers. What about you?',
'I\'m a Lakers fan.',
'They have a great team. Who is your favorite player?',
'LeBron James is definitely one of my favorites.',
'He is one of the best players of all time.',
'Who is your favorite basketball player?',
'I really like Steph Curry. He is an amazing shooter.',
'Yes, he is one of the best three-point shooters in the game.',
'Do you play any sports yourself?',
'Yes, I like to play pickup basketball with my friends.',
'That sounds like a lot of fun. Do you play any other sports?',
'I also enjoy playing soccer and tennis.',
'Those are both great sports. I used to play soccer when I was younger.',
]
trainer.train(large_conversation)
trainer.train(travel_conversation)
trainer.train(food_conversation)
trainer.train(sports_conversation)
response = chatbot.get_response( 'what do like ine food?')

print(response)
response = chatbot.get_response( 'what do like in food?')

print(response)
response = chatbot.get_response( 'Do you follow any sports?')

print(response)

## ---(Tue Jun 13 16:33:04 2023)---
runfile('C:/Users/acer1/.spyder-py3/temp.py', wdir='C:/Users/acer1/.spyder-py3')
pip install flask
runfile('C:/Users/acer1/.spyder-py3/appy.py', wdir='C:/Users/acer1/.spyder-py3')
$ curl -X POST -H "Content-Type: application/json" -d '{
  "timestamps": [
    ["Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"],
    ["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"]
  ]
}' http://localhost:5000/time-difference
runfile('C:/Users/acer1/.spyder-py3/appy.py', wdir='C:/Users/acer1/.spyder-py3')
$ curl -X POST -H "Content-Type: application/json" -d '{
  "timestamps": [
    ["Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"],
    ["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"]
  ]
}' http://localhost:5000/time-difference

## ---(Tue Jun 13 18:53:39 2023)---
runfile('C:/Users/acer1/.spyder-py3/app.py', wdir='C:/Users/acer1/.spyder-py3')
runfile('C:/Users/acer1/.spyder-py3/temp.py', wdir='C:/Users/acer1/.spyder-py3')
runfile('C:/Users/acer1/.spyder-py3/app.py', wdir='C:/Users/acer1/.spyder-py3')
runfile('C:/Users/acer1/.spyder-py3/text A.py', wdir='C:/Users/acer1/.spyder-py3')