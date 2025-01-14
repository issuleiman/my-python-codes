import random

print("welcome to the sulex-password Generator!")
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","u","s","v","w","x","y","z"]
symbols=["1","2","3","4","5","6","7","8","9"]
numbers=["!","@","#","$","%","&","*","+"]

nr_letters=int(input("How many letter would you like in your password :"))
nr_symbols=int(input("How many symbols would you like :"))
nr_numbers=int(input("How many number would you like:"))

password=[]

for char in range(1,nr_letters + 1):

    password.append(random.choice(letters))

for char in range(1 ,nr_symbols +1):
    password.append(random.choice(symbols))

for char in range(1,nr_numbers +1):
    password.append(random.choice(numbers))

random.shuffle(password)
password= ''.join(password)
print(f"Your passowrd is :{password}")



