def format_text(text: str, width: int = 80, alignment: str = 'left', case: str = 'default') -> str:
    """
    Take a text string and format it in a neat, readable way.

    Parameters:
    - text: The string of text you want to format.
    - width: The total width for the formatted text. Default is 80 characters.
    - alignment: How you want the text aligned. Choose 'left', 'right', or 'center'. Default is 'left'.
    - case: What case you want the text in. 'upper' for uppercase, 'lower' for lowercase, or 'default' for no change. Default is 'default'.

    Returns:
    - The formatted text as a string.

    Errors you might see:
    - If the alignment isn't 'left', 'right', or 'center'.
    - If the case isn't 'upper', 'lower', or 'default'.
    - If the width isn't a positive number.

    Examples:
    >>> format_text("Hello, World!", width=20, alignment='center', case='upper')
    '   HELLO, WORLD!   '
    
    >>> format_text("Python is fun.", width=30, alignment='right', case='lower')
    '            python is fun.'
    
    >>> format_text("Simple formatting.", width=25)
    'Simple formatting.    '
    """

    # First, let's make sure everything looks good.
    if not isinstance(text, str):
        raise TypeError("Oops! The 'text' should be a string, like 'Hello World'.")
    
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Hmm... 'width' needs to be a positive number. Try something like 80.")
    
    if alignment not in ['left', 'right', 'center']:
        raise ValueError("Oops! The 'alignment' can only be 'left', 'right', or 'center'.")
    
    if case not in ['upper', 'lower', 'default']:
        raise ValueError("Ah, 'case' must be either 'upper', 'lower', or 'default'. No surprises here.")

    # Now, let's change the case if needed
    if case == 'upper':
        text = text.upper()
    elif case == 'lower':
        text = text.lower()

    # Align the text as per your choice
    if alignment == 'left':
        formatted_text = text.ljust(width)  # Pad on the right to make the line the right length
    elif alignment == 'right':
        formatted_text = text.rjust(width)  # Pad on the left to make the line the right length
    elif alignment == 'center':
        formatted_text = text.center(width)  # Pad on both sides to center the text
    
    return formatted_text


# Example usage
if __name__ == "__main__":
    try:
        # Let's try a few examples!
        print(format_text("Hello, World!", width=20, alignment='center', case='upper'))  # '   HELLO, WORLD!   '
        print(format_text("Python is fun.", width=30, alignment='right', case='lower'))  # '            python is fun.'
        print(format_text("Simple formatting.", width=25))  # 'Simple formatting.    '

        # If you pass something that doesn't make sense, it'll let you know!
        # Uncomment the line below to see an error in action:
        # print(format_text(12345, width=30))  # This will raise an error

    except (ValueError, TypeError) as error:
        print(f"Oops! Something went wrong: {error}")
        