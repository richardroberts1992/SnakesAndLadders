# SnakesAndLadders
# Snakes and Ladders Command-Line Game

## Description
This is a classic Snakes and Ladders board game implemented in Python, playable on the command line. Two players take turns rolling a die to advance their positions on a board of 100 squares. The goal is to be the first to reach square 100. The board features snakes that can send you back and ladders that can help you climb faster.

## How to Play
1.  **Run the game:** Open your terminal or command prompt, navigate to the directory containing the game files, and execute the following command:
    ```bash
    python game.py
    ```
2.  **Enter Player Names:** When the game starts, you will be prompted to enter names for Player 1 and Player 2. If you skip this, default names ("Player 1", "Player 2") will be used.
3.  **Roll the Die:** On your turn, the game will prompt you to roll the die. Simply press `Enter` to roll.
4.  **Game Play:** The game will display the die roll, your new position, and any effects from snakes or ladders. The positions of both players will be shown after each turn.
5.  **Winning:** The first player to reach square 100 wins the game.

## Running Tests
The game includes a suite of unit tests to verify its core logic. To run these tests, execute the following command in your terminal from the project directory:
```bash
python -m unittest test_game.py
```
The test results will indicate if all tests passed or if any failures occurred.

## Files
-   `game.py`: This file contains the main game logic, including player movement, snake and ladder effects, turn management, and the command-line interface for playing the game.
-   `test_game.py`: This file contains unit tests written using Python's `unittest` module. These tests cover various aspects of the game, such as die rolling, player movement, snake and ladder interactions, and win conditions.
-   `README.md`: This file, providing information about the game, how to play it, and how to run tests.
