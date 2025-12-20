def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2   

def divide(n1,n2):
    return n1 / n2

operations = {"+": add, 
              "-": subtract,
              "*": multiply, 
              "/": divide   }

def calculator():
    should_continue = True
    num1 = int(input("Enter first number: "))
    while should_continue:
        for symbol in operations:
            print(symbol)

        operational_symbol = input("Enter operation (+, -, *, /) : ")
        num2 = int(input("Enter second number: "))

    
        print(f"{num1} {operational_symbol} {num2} = {operations[operational_symbol](num1,num2)}")

        choice =input(" Y or y to continue ; N or n to exit : ")
        if choice == 'Y' or choice == 'y':
            num1 = operations[operational_symbol](num1,num2)
        else:
            should_continue = False
            
            calculator()
            
calculator()