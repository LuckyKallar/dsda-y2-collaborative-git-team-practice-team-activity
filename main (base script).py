def greet_user(name, age):
    """Greets the user by name and age."""
    if age >= 18:
        print(f"Hello, {name}! Welcome!")
    else:
        print(f"Hi, {name}! How can I help you today?")


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
    user_age = int(input("Enter your age: "))
    result = calculate_square(user_number)
    greet_user(user_name)
    save_to_log(user_name, result)
