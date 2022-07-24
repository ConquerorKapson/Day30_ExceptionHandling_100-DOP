# fruits = ["apple", "banana", "orange"]
# try:
#     file = open("abc.txt")
#     print(fruits[2])
# except FileNotFoundError:
#     file = open("abc.txt", 'w')
#     file.write("something")
# except IndexError as index:
#     print(f"{index} out of range incurred")
# else:
#     print("In the else block \nNo error Found")
#     something = file.read()
#     print(something)
# finally:
#     file.close()

# ===================GENERATING YOUR OWN EXCEPTION===============

# Suppose I am calculating the BMI of a person but height of a person can not be greater than 3m so will will handle
# this using exception


height = int(input("What is your height (m) : "))
weight = float(input("What is your weight (Kg) : "))


if height > 3:
    raise ValueError("Height can not be greater than 3 m")

bmi = weight/height**2


print(f"your BMI is: {bmi}")

