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

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]
guess = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

bot_guess = random.randint(0, 2)

if guess == bot_guess:
    print(game_images[bot_guess])
    print("\nComputer chose: \n")
    print(game_images[bot_guess])
    print("Its a tie!!!")

# this is rock loosing to paper
if guess == 0 and bot_guess == 1:
    print(rock)
    print("\nComputer chose: \n")
    print(paper)
    print("\n You Loose...\n")

# this is rock winning scissors
if guess == 0 and bot_guess == 2:
    print(rock)
    print("\nComputer chose: \n")
    print(scissors)
    print("\nYou Win!!!\n")

# this is paper winning to rock
if guess == 1 and bot_guess == 0:
    print(paper)
    print("\nComputer chose: \n")
    print(rock)
    print("\nYou Win!!!\n")

# this is paper loosing to scissors
if guess == 1 and bot_guess == 2:
    print(paper)
    print("\nComputer chose: \n")
    print(scissors)
    print("\nYou Loose...\n")

# this is scissors loosing to rock
if guess == 2 and bot_guess == 0:
    print(scissors)
    print("\nComputer chose: \n")
    print(rock)
    print("\nYou Loose...\n")

# this is scissors winning to paper
if guess == 2 and bot_guess == 1:
    print(scissors)
    print("\nComputer chose: \n")
    print(paper)
    print("You Win!!!")