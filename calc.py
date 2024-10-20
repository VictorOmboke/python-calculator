#Prompt user to enter a mathematical operator
operator = input("Please enter an operator (+ - * /): ")
#Variable to store the first number
num1 = float(input("Please enter a number: "))
#Variable to store the second number
num2 = float(input("PLease enter another number: "))

#If statement that verifies what operator the user chose and uses it to calculate a result
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    #Condition that handles if a user does not enter a valid operator
    print(f"{operator} is not a valid operator")

print(f"Your result is: {result}")
