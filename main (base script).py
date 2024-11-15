def greet_user(name, age):
    """Greets the user by name and age."""
    if age >= 18:
        print(f"Hello, {name}! Welcome!")
    else:
        print(f"Hi, {name}! How can I help you today?")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    greet_user(user_name, user_age)