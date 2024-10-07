def initialize_variables():
    return 0, ''

def get_user_input():
    while True:
        user_input = input("Enter a number or operator (+, -, *, /) or 'q' to quit: ")
        if user_input.lower() == 'q':
            return None, None
        if user_input in {'+', '-', '*', '/'}:
            return 'operator', user_input
        try:
            return 'number', float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or operator.")

def select_operation(operator, num1, num2):
    if operator == '+':
        return add_numbers(num1, num2)
    elif operator == '-':
        return subtract_numbers(num1, num2)
    elif operator == '*':
        return multiply_numbers(num1, num2)
    elif operator == '/':
        return divide_numbers(num1, num2)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        print("Error: Division by zero!")
        return None
    return a / b

def calculator():
    result, operator = initialize_variables()
    
    while True:
        input_type, value = get_user_input()
        
        if input_type is None:  # User wants to quit
            break
        
        if input_type == 'number':
            if operator:
                result = select_operation(operator, result, value)
                print(f"Result: {result}")
                operator = ''
            else:
                result = value
        else:  # input_type == 'operator'
            operator = value
        
    print("Calculator ended. Goodbye!")

if __name__ == "__main__":
    calculator()
