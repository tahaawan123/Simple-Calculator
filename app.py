
#                Simple Calculator

def calculator():
    num1 =float(input("Enter first number: "))
    operator=input("Enter operation (+, -, *, /): ")
    num2 =float(input("Enter  Second number: "))


    if operator == "+":
        result =f"sum of Your Value is: {num1+num2}"
    elif operator == "-":
        result=f"Subtaction  of Your Value is : {num1-num2}"
    elif operator == "*":
        result=f"Multiplication of Your Value is: {num1*num2}"
    elif operator == "/":
        if num2 == 0:
            result= "Cannot divide by zero"
        else:
            result=f"Division of Your Value is: {num1/num2}"

    else:
        result="Invalid Operator!"

    print("Result:", result)


calculator() 
        


        




