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

#problem 2
#sales tracking program for a 5day week

target = float(input("Enter total sales target: "))

#cumulative sales
cumulative_sales = 0

#loop for 5days
for day in range(1, 6):
    sales= float(input(f"Enter the day {day} sales: "))
    cumulative_sales += sales
    percent =(cumulative_sales / target) * 100
    print(f"The cumulative sales is: {cumulative_sales:.1f} ({percent:.1f}%)")




