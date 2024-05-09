import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 to 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    any_player_rolled = False  # Flag to check if any player chose to roll during their turn
    for player_idx in range(players):
        print("Player", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() == "n":
                break  # Exit the game if any player inputs 'n'
            elif should_roll.lower() == "y":
                any_player_rolled = True  # Set the flag to True if any player chooses to roll
                pass
            else:
                print("Invalid input. Please enter 'y' to roll or 'n' to stop.")

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print('Your total score is:', player_scores[player_idx])

        if should_roll.lower() == "n":
            break  # Exit the game if any player inputs 'n'

    if not any_player_rolled:
        print("No players chose to roll. Game ends without a winner.")
        break  # Exit the game if no player chose to roll

    if should_roll.lower() == "n":
        break  # Exit the game if any player inputs 'n'

max_score = max(player_scores)
if any_player_rolled and max_score >= max_score:
    winning_idx = player_scores.index(max_score)
    print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)


