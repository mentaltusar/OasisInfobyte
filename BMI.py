print("_________Welcome to BMI Calculator___________")
weight = int(input("Enter your Weight in Kg : "))
height = float(input("Enter your Height in m : "))
BMI = round(weight / height ** 2 , 2)
print(f"Your BMI is : {BMI}")
if BMI < 18.5:
    print("You are Underweight .")
elif 18.5 <= BMI <= 24.9:
    print("You are Normal in Weight .🤗")
elif 25 <= BMI <= 29.9:
    print("you are Over Weight .")
