import random

print("Welcome to the head or tall game, "
      "you need to choose any number in between 1 t0 10 , to detemine your guess ")
num=int(input("Enter a number between 1 to 10:"))
rand_num = random.randint(1, 11)

if num == rand_num:
    print("Head")
else:
    print("Tall")
