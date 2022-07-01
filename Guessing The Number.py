import random
import sys
# from art import logo
# print(logo)
# print("\n")
print("welcome to number guessing game")
rand = random.randint(1,100)

def choose_difficulty():
    choose = input("Choose diffculty 'Easy' or 'hard': ")
    if choose == 'easy':
        num = 1
        print("you have 10 choices")
        while num <= 10:
            choosen_easy = int(input(f"Guess number {num}, Choose value between 1 to 100: "))
            num += 1
            if num > 10:
                print("Guess chances over, You lose")
                sys.exit()
            elif choosen_easy > rand:
                print("Too high")
            elif choosen_easy < rand:
                print("Too low")
            elif choosen_easy == rand:
                print("Guess correct!")
                print(f"Congratulations! you Won at Guess {num}")

    else:
        num = 1
        print("you have 5 choices")
        while num <= 5:
            choosen_hard = int(input(f"Guess number {num}, Choose value between 1 to 100: "))
            num += 1
            if num > 5:
                print("Guess chances over, You lose")
                sys.exit()
            elif choosen_hard > rand:
                print("Too high")
            elif choosen_hard < rand:
                print("Too low")
            elif choosen_hard == rand:
                print("Guess correct!")
                print(f"Congratulations! you Won at Guess {num}")

choose_difficulty()
