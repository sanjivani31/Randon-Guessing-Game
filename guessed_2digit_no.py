import random # Built-in module that you can use to make random numbers.

nump = random.randint(10,99) # Returns a random number between the given range
print(nump)

num = int(input("Enter a two digit number : "))

while num != 100 :
    if num == nump :
        print("You guessed it right!!!")
        break
    elif num > nump :
        print("Number is too large.")
        num = int(input("Enter a two digit number : "))
    elif num < nump :
        print("Number is too small")
        num = int(input("Enter a two digit number : "))
else :
    print("You quit the game!!!")
