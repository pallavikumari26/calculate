# calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

def calculator():
    print("Simple CLI Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        again = input("Do you want to calculate again? (y/n): ").lower()
        if again != 'y':
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()

