

try: 
    age =  int(input("Enter age: \n"))
    print(f"You will be {age + 1}, years old next year!")

except ValueError:
    print("Please enter a valid number for age.")