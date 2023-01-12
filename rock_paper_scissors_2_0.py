# Importing libraries.
from getpass import getpass as input

# Setting up a score system for each player.
p1_score = 0
p2_score = 0

# Determining the winner
while True:
    
    # The players options
    print("Please enter R(rock), P(paper) or S(Scissor)")
    
    # Both players enter their choice
    player_1 = input(": ")
    player_2 = input(": ")
    if player_1 == player_2:
        print("It's a Tie")
    elif (player_1 == 'r' and player_2 == 's') or (player_1 == 'p' and player_2 == 'r') or (player_1 == 's' and player_2 == 'p'):
        p1_score += 1
    else:
        p2_score += 1

    # Printing out the score each loop so that the players can keep track of score.
    print(f"Player 1: {p1_score} Player 2: {p2_score}")

    # If statements to check if one of the players has reached a score of 3. Therefore ending the game if one has.
    if p1_score == 3 or p2_score == 3:
        print("Score limit reached thanks for playing!")
        exit()
    else:
        continue
