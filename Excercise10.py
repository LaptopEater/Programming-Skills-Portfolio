def check(number): #In this line of code I made a function to check the number if its odd or even.
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function to get input and print the result
def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))  
    # Call the function and print the result
    result = check(num)
    print(result)

# Run the main function
if __name__ == "__main__":
    main()