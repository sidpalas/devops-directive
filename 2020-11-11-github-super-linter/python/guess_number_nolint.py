import random

guesses_made = 0
name = input("Hello! What is your name?\n")

number = random.randint(1, 20)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

while guesses_made < 6:
    guess = int(input("Take a guess: "))
    guesses_made += 1

    if guess < number:
      print("Your guess is too low.")

    if guess > number:
      print("Your guess is too high.")

    if guess == number:
      break

if guess == number:
    print(f"Good job, {name}! You guessed my number in {guesses_made} guesses! But this line is way too long!")
else:
    print(f"Nope. The number I was thinking of was {number}")