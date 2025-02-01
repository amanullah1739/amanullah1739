import random
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
command = int(input("What do you choose ? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))
if command == 0:
    print(Rock)
elif command == 1:
    print(Paper)
elif command == 2:
    print(Scissors)
else:
    print("Invalid input!")
print("Computer choose : \n")
random_play = random.randint(0, 2)
if random_play == 0:
    print(Rock)
elif random_play == 1:
    print(Paper)
else:
    print(Scissors)

if command == 0 and random_play == 1:
    print("Computer Wins")
elif command == 0 and random_play == 2:
    print("You Wins")
elif command == 1 and random_play == 0:
    print("You Wins")
elif command == 1 and random_play == 2:
    print("Computer Wins")
elif command == 2 and random_play == 0:
    print("Computer Wins")
elif command == 2 and random_play == 1:
    print("You Wins")
else:
    print("Draw")
