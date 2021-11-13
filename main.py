import json
import time
import random

user = []

def play():
    print("\n *******QUIZ STARTING*******")
    score = 0
    user_name = input("Enter your name ")
    if user_name in user:
        print("This name has been used")
    else:
        user.append(user_name)
        print("Game starting...")
        time.sleep(0.5)
        with open("questions.json", "r+") as f:
            j = json.load(f)
            for i in range(10):
                no_of_questions = len(j)
                ch = random.randint(0, no_of_questions-1)
                print(f'\nQ{i+1} {j[ch]["question"]}\n')
                for option in j[ch]["options"]:
                    print(option)
                answer = input("\nEnter your answer: ")
                if j[ch]["answer"][0] == answer[0].upper():
                    print("\nYou are correct")
                    score+= 1
                else:
                    print("\nYou are incorrect")
                del j[ch]
            print(f'\nFinal Score {score} ')

def rules():
	print('''\n*******RULES*******
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
	''')

def about():
	print('''\n*******ABOUT US*******
This project has been created by KorayGnsl.
It is a basic Python Project for my learning path.''')


choice = 1
while choice != 3:
	print('\n*******WELCOME TO QUIZ MASTER*******')
	print('****************************************')
	print('1. PLAY QUIZ')
	print('2. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
	print('3. EXIT')
	print('4. ABOUT US')
	choice = int(input('ENTER YOUR CHOICE: '))
	if choice == 1:
		play()
	elif choice == 2:
		rules()
	elif choice == 3:
		break
	elif choice == 4:
		about()
	else:
		print('WRONG INPUT. ENTER THE CHOICE AGAIN')
