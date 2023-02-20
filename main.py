import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
art = [Rock, Paper, Scissors]
score = 0
for _ in iter(int, 1):
    answer = int(
        input("Type 0 for Rock, 1 for Paper, and 2 for Scissors "))
    print("You chose:")
    print(art[answer])
    print("Computer chose:")
    computer_answer = random.randint(0, 2)
    print(art[computer_answer])
    if computer_answer == 2 and answer == 0:
        score += 1
        print("You win.")
        print(f"You've won a total of {score} times.")
    elif answer == 2 and computer_answer == 0:
        print("You lose.")
        print(f"You've won a total of {score} times.")
    elif answer > computer_answer:
        score += 1
        print("You win.")
        print(f"You've won a total of {score} times.")
    elif computer_answer > answer:
        print("You lose.")
        print(f"You've won a total of {score} times.")






