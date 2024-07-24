# Cricket Battle Simulator

**Overview**

Cricket Battle Simulator is a Python-based game that simulates a cricket match between a user and the computer. Utilizing the random module, this game allows players to experience both batting and bowling, where they can input their choices and compete against the computer’s random selections. The game includes input validation, score tracking, and a final results display to determine the winner. This project showcases fundamental concepts in Python programming, including loops, conditionals, and basic input/output operations.

## Cricket Battle Simulator Components:

**1. Game Objective ->**
Simulate a cricket match between a user and the computer.
Players take turns batting and bowling with the aim of scoring the highest points.
Gameplay Mechanics:

**2. Batting ->**
User inputs a number between 0 and 5.
Computer randomly generates a number between 0 and 5.
If the user's input matches the computer's number, the user is out.
If not, the score is incremented by the sum of the user's and computer's numbers.

**3. Bowling->**
User inputs a number between 0 and 5.
Computer randomly generates a number between 0 and 5.
If the user's input matches the computer's number, the computer is out.
If not, the score is incremented by the sum of the user's and computer's numbers.

**4. Game Flow:->**
Toss to decide who bats first.
Player goes through batting and bowling phases.
Scores are tracked and displayed after each round.
The game ends when either the user or the computer is out.

**5. Input Validation ->**
Ensures user inputs are within the valid range (0 to 5).
Provides feedback for incorrect inputs.

**6. Score Tracking: ->**
Maintains and updates scores for both the user and the computer.
Displays scores after each input and at the end of the game.

**7. Winning Conditions ->**
Compares the final scores of the user and the computer.
Declares the winner or if the game is a draw.

**8. Technology Used ->**
Python programming language.
random module for generating random numbers.
Basic input/output operations for user interaction.
Demonstrates fundamental programming concepts.

