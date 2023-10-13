# Rock Paper Scissors Simulator

## Description
This is a python script meant to simulate random games of rock, paper, scissors. Random hands are chosen and then compared to determine the winner of the round. The outcome of a round is recorded and stored, which is then either displayed to the user in the terminal, or written to a text file. The number of rounds is determined by the user's input.

## Methods
### pick_hands()
This method creates a tuple of the possible hands (rock, paper, scissors), in which the player and computer variable are assigned a random value from this tuple using `random.choice` from the `random` module.
 
