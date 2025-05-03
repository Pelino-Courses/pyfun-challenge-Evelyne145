from datetime import datetime

def days_between_dates(date1: str, date2: str) -> int:
    """
    Finds how many days are between two dates.

    Parameters:
    - date1: A string representing the first date in 'YYYY-MM-DD' format.
    - date2: A string for the second date in the same format.

    Returns:
    - The number of days between the two dates as a positive integer.

    Raises:
    - ValueError if the input doesn't look like a valid date.

    Examples:
    >>> days_between_dates("2023-04-01", "2023-04-10")
    9
    >>> days_between_dates("2025-01-01", "2024-12-25")
    7
    """

    try:
        # Let's turn those strings into real date objects
        first = datetime.strptime(date1, "%Y-%m-%d")
        second = datetime.strptime(date2, "%Y-%m-%d")

        # Calculate the difference and make sure it's always positive
        difference = abs((second - first).days)

        return difference

    except ValueError:
        # If something goes wrong, let’s explain it kindly
        raise ValueError("Oops! Please enter dates in the 'YYYY-MM-DD' format. For example: '2025-05-01'.")

# Try it out!
if __name__ == "__main__":
    # You can change these to try different dates
    try:
        print("Days between:", days_between_dates("2025-05-01", "2025-05-03"))
        print("Days between:", days_between_dates("2023-04-01", "2023-04-10"))  # Output: 9
    except ValueError as error:
        print("Something went wrong:", error)
