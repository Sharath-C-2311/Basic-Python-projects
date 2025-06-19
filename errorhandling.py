#simple program to understand try except block
try:
    age = int(input("How old are you?"))
    if age > 18:
        print(f"You can drive at age {age}.")
except ValueError:
    print("invalid input!!..\nInput should be an integer")
    