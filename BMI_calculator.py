print("""
  _____       _      _      __  __  _____   _      ____  _       _             
 / ____|     (_)    | |    |  \\/  |/ ____| | |    / __ \\| |     | |            
| (___  _ __  _  ___| | __ | \\  / | (___   | |   | |  | | |_   _| |__   ___ _ __ 
 \\___ \\| '_ \\| |/ __| |/ / | |\\/| |\\___ \\  | |   | |  | | | | | | '_ \\ / _ \\ '__|
 ____) | | | | | (__|   <  | |  | |____) | | |___| |__| | | |_| | | | |  __/ |   
|_____/|_| |_|_|\\___|_|\\_\\ |_|  |_|_____/  |______\\____/|_|\\__, |_| |_|\\___|_|   
                                                         __/ |                  
                                                        |___/                   
                        Sulex BMI Calculator
""")

weight= int(input("Enter your weight:"))
height = int(input("Enter your height:"))
bmi= weight / height **2

if bmi <= 18.4:
    print(f"Your BMI is : {round(bmi)} \n You are Underweight 😒")
elif bmi in range(18.5 , 24.9):
    print(f"Your BMI is : {round(bmi)} \n You are Normal 😊")
elif bmi in range(25.0, 39.9):
    print(f"Your BMI is : {round(bmi)} \n You are overweight 😞")
else:
    print(f"Your BMI is : {round(bmi)} \n You are Obsese 🥲")




