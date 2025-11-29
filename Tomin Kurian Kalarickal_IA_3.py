#problem 1
#simple calculator

number_1 = float(input("Enter the first number: "))
operator = input("Enter the operator(+, -, *, /): ")
number_2 = float(input("Enter the second number: "))

#calculation using if/elif/else
if operator == "+":
    result = number_1 + number_2
    print("The result is: ", result)

elif operator == "-":
    result = number_1 - number_2
    print("The result is: ", result)

elif operator == "*":
    result = number_1 * number_2
    print("The result is: ", result)

elif operator == "/":
    if number_2 != 0:
        result = number_1 / number_2
        print("The result is: ", result)
    else:
        print ("Error: Cannot divide by zero")
else:
    print ("Error: Invalid operator")








