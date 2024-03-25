import random

print("Guess a number")

start=1
end=100
num = int(random.randint(1, 100))
while True:
    inputt = int(input())
    if inputt == num:
        print("Got it!!! the number is :"+str(num))
        break
    elif inputt > num:
        print("Too high")
    else:
        print("Too low")

