from colorama import Fore, Back, Style
print(Fore.GREEN + "welcome to my bmi calculator")
height = float(input("enter your height in m:\n"))
weight = float(input("enter your weight in m:\n"))
bmi = round(weight / height **2)
if bmi < 18.5:
 print(f"your bmi is {bmi} , you are underweight")
elif bmi < 25:
 print(f"your bmi is {bmi}, you have a normal weight")
elif bmi < 30:
 print(f"your bmi is {bmi}, you are a fatass.")
elif bmi < 35:
 print(f"your bmi is {bmi}, you are freaking obese. ")

