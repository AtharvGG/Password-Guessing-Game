import random

easy_words = ["apple","train","tiger","money","india"]
medium_words = ["python","bottle","planet","laptop"]
hard_words = ["elephant","silver","umbrella","computer","treking"]

print("welcome to the password guessing game!!!")
print("choose a Game Levels: easy,medium,hard")

level =input("Enter the level:").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level =="medium":
    secret = random.choice(medium_words)
elif level =="hard":
    secret = random.choice(hard_words)
else:
    print("Invalid Choice...Defulting to easy level")
    secret = random.choice(easy_words)

attempt = 0
print("\n Guess the secret password")

while True:
    guess = input("Enter your guess:").lower()
    attempt += 1

    if guess == secret:
        print(f"Congratulation!! you guessed it in {attempt}")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:",hint)
print("GAME OVER")




