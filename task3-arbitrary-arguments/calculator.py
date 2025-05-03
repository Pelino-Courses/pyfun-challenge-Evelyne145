def add(*numbers):
    """Adds all the numbers together."""
    return sum(numbers)

def subtract(*numbers):
    """Subtracts all numbers from the first one."""
    if not numbers:
        raise ValueError("We need at least one number to subtract.")
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(*numbers):
    """Multiplies all numbers together."""
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(*numbers):
    """Divides the first number by each of the others, in order."""
    if not numbers:
        raise ValueError("We need at least one number to divide.")
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ZeroDivisionError("Careful! You can't divide by zero.")
        result /= num
    return result

def calculate(*args, **kwargs):
    """
    A friendly calculator that handles multiple numbers and operations.

    What you pass:
    - Any amount of numbers (like: 5, 10, 2)
    - Keywords:
        - operation: 'add', 'subtract', 'multiply', or 'divide' (default is 'add')
        - round: True if you want the result rounded to 2 decimal places (optional)

    What you get:
    - A number that’s the result of your operation

    Examples:
    >>> calculate(5, 10, 2, operation='divide', round=True)
    0.25
    >>> calculate(1, 2, 3, operation='add')
    6
    """

    operation = kwargs.get('operation', 'add')  # default is 'add'
    round_result = kwargs.get('round', False)

    if not args:
        raise ValueError("You need to give me at least one number to work with!")

    # Pick the right math function
    if operation == 'add':
        result = add(*args)
    elif operation == 'subtract':
        result = subtract(*args)
    elif operation == 'multiply':
        result = multiply(*args)
    elif operation == 'divide':
        result = divide(*args)
    else:
        raise ValueError(f"Sorry, I don't know how to '{operation}'. Try: add, subtract, multiply, divide.")

    # Round the result if asked nicely
    if round_result:
        result = round(result, 2)

    return result


# Let’s try it out!
if __name__ == "__main__":
    try:
        print("Adding some numbers:", calculate(1, 2, 3, 4, operation='add'))
        print("Taking some away:", calculate(20, 5, 3, operation='subtract'))
        print("Multiplying a few things:", calculate(2, 3, 4, operation='multiply'))
        print("Doing some division:", calculate(100, 2, 5, operation='divide', round=True))

        # Uncomment to try some errors:
        # print(calculate(operation='add'))  # No numbers
        # print(calculate(5, 0, operation='divide'))  # Division by zero

    except Exception as err:
        print(f"Oops, something went wrong: {err}")
        