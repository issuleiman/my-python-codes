weight= int(input("Enter your weight:"))
height = int(input("Enter your height:"))
bmi= weight / height **2


if bmi <= 18.4:
    print(f"Your BMI is : {round(bmi)},you are Underweight")
elif bmi in range(18.5 , 24.9):
    print(f"Your BMI is : {round(bmi)},you are Normal")
elif bmi in range(25.0, 39.9):
    print(f"Your BMI is : {round(bmi)},you are overweight")
else:
    print(f"Your BMI is : {round(bmi)},you are Obsese")




