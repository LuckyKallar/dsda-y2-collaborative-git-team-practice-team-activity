def greet_user(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")


def calculate_square(number):
    """Calculates the square of a number."""
    return number * number


def save_to_log(name, square):
    """Saves user data to a log file."""
    with open("log.txt", "a") as log_file:
        log_file.write(f"Hello, {name}!: Your square number is {square}.\n")


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_number = int(input("Enter a number: "))
    result = calculate_square(user_number)
    greet_user(user_name)
    save_to_log(user_name, result)

# Changes here for testing the process
