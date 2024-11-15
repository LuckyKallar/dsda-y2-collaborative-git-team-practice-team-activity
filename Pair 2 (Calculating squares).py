
# Method to calculate the square of a number
def calculate_to_the_power(number, powerof=2):
    return number**powerof

# user interaction to get the result of increase by the power of x
if __name__ == "__main__":

    # Ask the user for the numbers to calculate
    user_number = int(input("Enter a number: "))
    powerof = int(input("Enter a the power: "))

    #calculate the result
    result = calculate_to_the_power(user_number, powerof) * user_number

    #print the result
    print(f"The square of {user_number} to the power of {powerof} is {result}")
