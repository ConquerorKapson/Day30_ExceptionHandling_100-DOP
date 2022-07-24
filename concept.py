fruits = ["apple", "banana", "orange"]
try:
    file = open("abc.txt")
    print(fruits[2])
except FileNotFoundError:
    file = open("abc.txt", 'w')
    file.write("something")
except IndexError as index:
    print(f"{index} out of range incurred")
else:
    print("In the else block \nNo error Found")
    something = file.readlines()
    print(something)
finally:
    file.close()
