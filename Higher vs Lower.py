import random
import sys

from game_data import data
import art

print(art.logo)

def arto():
    print(art.vs)

rand_a = random.choice(data)
print(rand_a)
arto()
rand_b = random.choice(data)
print(rand_b)

a_count = rand_a['follower_count']
b_count = rand_b['follower_count']


def process():
    just = 1
    while just <= len(data):
        guess = input("Who has more followers, Type 'A' or 'B': ").lower()
        if guess == 'a':
            if a_count >= b_count:
                print(f"You are right, current score: {just} ")
                tab = "\n" * 10
                print(tab)
                print(art.logo)
                rand_c = random.choice(data)
                print(rand_c)
                arto()
                rand_d = random.choice(data)
                print(rand_d)
            else:
                print(f"Sorry thats wrong, final score: {just}")
                sys.exit()
            process()
        elif guess == 'b':
            if b_count >= a_count:
                print(f"You are right, current score: {just} ")
                tab = "\n" * 10
                print(tab)
                print(art.logo)
                rand_c = random.choice(data)
                print(rand_c)
                arto()
                rand_d = random.choice(data)
                print(rand_d)
            else:
                print(f"Sorry thats wrong, final score: {just}")
                sys.exit()
            process()
        just += 1

process()





