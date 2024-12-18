import random

game = ["kámen", "papír", "nůžky"]

user = int(input("Zadej 0 pro kámen, 1 pro papír, 2 nůžky: "))
bot = random.randint(0, 2)

print(f"Uživatel vybral {game[user]}")
print(f"Bot vybral {game[bot]}")

if user == bot:
    print("remíza")
elif game[bot] == "kámen" and game[user] == "papír":
    print("Uživatel vyhrál")
elif game[bot] == "kámen" and game[user] == "nůžky":
    print("Bot vyhrál")
elif game[bot] == "nůžky" and game[user] == "papír":
    print("Bot vyhrál")
elif game[bot] == "nůžky" and game[user] == "kámen":
    print("Uživatel vyhrál")
elif game[bot] == "papír" and game[user] == "nůžky":
    print("Uživatel vyhrál")
elif game[bot] == "nůžky" and game[user] == "kámen":
    print("Bot vyhrál")
