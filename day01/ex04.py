#Body Mass Index (BMI)

weight = float(input("What is your weight (kg)? "))
height = float(input("And your height (meters)? "))

#Calculate BMI using the formula:
# BMI = weight / (height ^ 2)
bmi = weight / (height ** 2)

# Display the BMI result formatted with 2 decimal places
print(f"Your BMI is {bmi: .2f}")