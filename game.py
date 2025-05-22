# Define the game board
BOARD_SIZE = 100
board = list(range(1, BOARD_SIZE + 1))

# Define snakes and ladders
# Format: {start_square: end_square}
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

# Player data
player_names = ["Player 1", "Player 2"] # Default names
player_positions = [1, 1] # For 2 players, starting at square 1
current_player_index = 0 # Player 0 starts

import random

def roll_die():
    """Simulates rolling a 6-sided die."""
    return random.randint(1, 6)

def play_turn(player_index):
    """
    Simulates a single turn for a player.

    Args:
        player_index (int): The index of the current player (0 or 1).

    Returns:
        bool: True if the current player has won, False otherwise.
    """
    global current_player_index # To modify the global variable
    global player_names # To access player names
    global player_positions # To access player positions

    current_player_name = player_names[player_index]
    print(f"\n--- {current_player_name}'s turn ---")
    input(f"{current_player_name}, press Enter to roll the die...")

    roll = roll_die()
    print(f"{current_player_name} rolled a {roll}")

    player_positions[player_index] = move_player(player_positions[player_index], roll)
    print(f"{current_player_name} is now at {player_positions[player_index]}")

    # Print updated positions of both players
    print(f"Current positions: {player_names[0]}: {player_positions[0]}, {player_names[1]}: {player_positions[1]}")

    if player_positions[player_index] == BOARD_SIZE:
        print(f"\n{current_player_name} has reached {BOARD_SIZE} and wins!")
        return True # Game over, winner found

    # Switch to the other player for the next turn
    current_player_index = 1 - player_index
    return False # No winner yet

def move_player(current_position, die_roll):
    """
    Calculates the new position of a player after a die roll.

    Args:
        current_position (int): The player's current square.
        die_roll (int): The result of the die roll.

    Returns:
        int: The player's new square after movement, including snakes/ladders.
    """
    new_position = current_position + die_roll

    if new_position > BOARD_SIZE:
        return current_position # Player doesn't move if roll exceeds 100

    # Check for snakes
    if new_position in snakes:
        print(f"Oops! Landed on a snake at {new_position}. Going down to {snakes[new_position]}")
        new_position = snakes[new_position]
    # Check for ladders
    elif new_position in ladders:
        print(f"Yay! Found a ladder at {new_position}. Climbing up to {ladders[new_position]}")
        new_position = ladders[new_position]

    return new_position

def main():
    global player_names # To modify global player_names list
    print("Welcome to Snakes and Ladders!")

    # Get player names
    name1 = input("Enter name for Player 1: ").strip()
    name2 = input("Enter name for Player 2: ").strip()
    if name1: player_names[0] = name1
    if name2: player_names[1] = name2

    print(f"\nInitial positions: {player_names[0]}: {player_positions[0]}, {player_names[1]}: {player_positions[1]}")
    
    # Game loop
    max_turns = 200 # To prevent infinite loops during development/testing, can be increased
    for turn_count in range(1, max_turns + 1):
        # The turn header is now part of play_turn
        # print(f"\n--- Turn {turn_count} ---") # Optional: keep for overall turn counting if desired
        
        winner_found = play_turn(current_player_index)
        
        if winner_found:
            print("\nGame Over! Thanks for playing!")
            break
    else: # Executed if the loop completes without a break (no winner in max_turns)
        print(f"\nGame ended after {max_turns} turns. No winner. Thanks for playing!")


if __name__ == "__main__":
    main()
