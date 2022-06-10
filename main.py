import random

while True:

    user = input("Enter your choice('R','S','P'): ")
    user = user.upper()
    computer = random.choice(['R','S','P'])

    if (user == computer):
        print("Its a Tie \n play again")
    elif(user == 'R' and computer== 'S') or (user == 'P' and computer== 'R') or (user == 'S' and computer == 'P'):
        print("you win")
    elif(user != ['R', 'S', 'P']):
        print("invalid input \n Try again")
    elif(input != ['R','S','P']):
        print("invalid number \n Try again")
    else:
        print("You loose")