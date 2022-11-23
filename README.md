clearing screen and timing information from: https://www.geeksforgeeks.org/clear-screen-python/

Bugs
Bug caused the game_over_lose() function to print "You lose" once for every time the dice_roll() function was called. Troubleshooting found I used an if statement instead of an elif statement for the losing condition, which apparently holds all of the print() commands until it's finally called. Replaced with an elif, problem solved.

Unfixed bugs
There is a bug where the global attempts variable resets between most functions, but not between the door_row() and door_pos() functions. 

When getting door_row() and door_pos(), if user gives a bad input the resulting values for door[] are none,none even if a good input is ultimately given.