import random

print("welcome to number guessing game\n")
n=random.randint(1,100)
game_over=False
chances=0

def level_choosing():
    level=input("Choose the difficulty level\nEnter 'easy' for easy level\nEnter 'difficult' for difficult level\n\n>>>")
    if level=="easy":
        l_n=10
    else:
        l_n=5
    return l_n

level_n=level_choosing()
for _ in range(level_n):
    chances+=1
    g=int(input("Guess the number : "))
    if g>n:
        print(f"Guess a small number than {g}")
    elif g<n:
        print(f"Guess a large number than {g}")
    elif g==n:
        print(f"YES... you guessed the correct number ,that is, {g}\nThe number of chance taken {chances}")
        break
    print(f"number of chances left : {level_n-chances}")
    if chances==level_n:
        print(f"you lost\nThe number was {n}")