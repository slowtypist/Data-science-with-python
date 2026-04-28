import random
num = random.randint(1,10)
tries = 0 
while True:

    guess = int(input("guess the number: ")) 
    if num == guess:
        tries += 1
        print("you win")
        print(f"no of tries: {tries}")class
        break
    else: 
        tries += 1
        print(f"no of tries: {tries}")
        print("you lose")
print(num)