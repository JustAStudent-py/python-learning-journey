# Program to convert meters to centimeters
try:
    meters = float(input("Write the distance in meters: "))

    centimeters = meters * 100

    print(f"The distance in centimeters is {centimeters:.2f} cm")

#Handle invalid input
except ValueError:
    print("Write a valid distance... ") 