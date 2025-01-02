import random # import the random module to generate random numbers
import sys # import the sys module for handling system-related operations

def main():
    while True:
        try:
            # Ask the user for the start of the range and convert it to an integer
            start_of_range = int(input("Type a start number: ").strip())
            # Ask the user for the end of the range and convert it to an integer
            top_of_range = int(input("Type an end number: ").strip())

            # Checking if the end of the range is greater than the start of the range
            if top_of_range > start_of_range:
                # Generating a random number between the start and end of the range
                random_number = random.randint(start_of_range, top_of_range)

                guesses = 0 # Initializing the counter to keep track of the number of guesses
                while True:
                    try:
                        # Prompt the user to guess the number and convert it to an integer
                        user_guess = int(input("Make a guess: ").strip())

                        # Validate if the guess is within the specified range
                        if start_of_range <= user_guess <= top_of_range:
                            guesses += 1 # increment the guess counter

                            # Checking if the guess matches the random number
                            if user_guess < random_number:
                                print("Too low number") # Hint if the guess is too low
                            elif user_guess > random_number:
                                print("Too high number") # Hint if the guess is too high
                            else:
                                print(f"You got it in {guesses} guesses.") # Hint for correct guess and exit the program
                                quit()
                        else:
                            # If the guess is out of range, prompt the user with valid range
                            print(f"Please make a guess between {start_of_range} and {top_of_range} of range")
                    except ValueError:
                        # Handling invalid input (non-integer values) for guesses
                        print("Please give an integer for guess next time")
                        continue
            else:
                # Exit the program if the start of the range is not less than the end
                sys.exit("Enter numbers where start is less than end of range")
        except ValueError:
            # Handling invalid input (non-integer values) for the range
            print("Please type a number next time.")
            continue
    
if __name__ == "__main__":
    main()  # Calling the main function to start the program
    

