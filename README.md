# Number Guessing Game

This Python program is an interactive number guessing game where the user guesses a randomly generated number within a specified range. The game provides hints for each incorrect guess, ensuring a fun and engaging experience.

## Features
- User specifies the range of numbers to guess from.
- Random number generation using Python's `random` module.
- Interactive feedback to guide the player:
  - "Too low" for guesses smaller than the random number.
  - "Too high" for guesses larger than the random number.
- Keeps track of the number of guesses made.
- Input validation ensures robust handling of invalid or out-of-range inputs.

## How to Use

### Prerequisites
- Python 3.x installed on your system.

### Running the Program
1. Clone the repository or download the program file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the program file.
4. Run the program using:
   ```
   python guessing_game.py
   ```

### Gameplay
1. The program prompts you to enter a start number and an end number to define the range.
2. A random number will be generated within the specified range.
3. Guess the number by entering an integer. The program provides hints if your guess is too high or too low.
4. Continue guessing until you find the correct number. The program will display the total number of guesses made.

### Example Run
```
Type a start number: 1
Type an end number: 100
Make a guess: 50
Too low number
Make a guess: 75
Too high number
Make a guess: 60
You got it in 3 guesses.
```

## Error Handling
- **Invalid Range**: If the end number is not greater than the start number, the program exits with a message.
- **Non-integer Input**: If you enter a non-integer, the program prompts you to try again.
- **Out-of-range Guess**: If your guess is outside the specified range, the program requests a valid input.

## Program Flow
1. **Input Phase**:
   - Prompts for start and end numbers to define the range.
   - Generates a random number within the range.
2. **Guessing Phase**:
   - Repeatedly prompts for guesses until the correct number is guessed.
   - Provides feedback for incorrect guesses.
3. **Exit Phase**:
   - Displays the number of guesses made.
   - Gracefully exits the program.

## Dependencies
- **random**: Used for random number generation.
- **sys**: Used for clean program termination.

## Contribution
Feel free to fork the repository and submit pull requests for improvements or new features. Suggestions and feedback are always welcome!

