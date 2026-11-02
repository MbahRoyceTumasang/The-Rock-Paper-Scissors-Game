rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Welcome to the Rock Paper Scissors game! The place were we can test your luck stat...")
Game_Start = input("To be begin the game please type start\n").lower()
Computer_Choice = random.randint(0,2)
if Game_Start == "start":
    Player= input("Please type 0 for rock, 1 for paper, and 2 scissors\n")
    if Player == "0":
        print(rock)
        if Computer_Choice == 0:
            print("The computer chose:")
            print(rock)
            if Player and Computer_Choice == 0:
                print("Its a draw")
        elif Computer_Choice == 1:
            print("The computer chose:")
            print(paper)
            print("You lose")
        elif Computer_Choice == 2:
            print("The computer chose:")
            print(scissors)
            print("You win")
    elif Player == "1":
        print(paper)
        if Computer_Choice == 0:
            print("The computer chose:")
            print(rock)
            print("You Win")
        elif Computer_Choice == 1:
            print("The computer chose:")
            print(paper)
            if Player and Computer_Choice == 1:
                print("Its a draw")
        elif Computer_Choice == 2:
            print("The computer chose:")
            print(scissors)
            print("You lose")
    elif Player == "2":
        print(scissors)
        if Computer_Choice == 0:
            print("The computer chose:")
            print(rock)
            print("You lose")
        elif Computer_Choice == 1:
            print("The computer chose:")
            print(paper)
            print("You win")
        elif Computer_Choice == 2:
            print("The computer chose:")
            print(scissors)
            if Player and Computer_Choice == 2:
                print("Its a draw")
    else:
        print("Invalid Input")
else:
    print("Ahh it seems your luck stat is not high enough")

