# Safe Tools - Week 6 Assignment

def safe_divide():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        result = first / second
        print("Result:", result)
    except ValueError:
        print("Error: Please enter numbers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


safe_divide()

