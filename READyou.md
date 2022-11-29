clearing screen and timing information from: https://www.geeksforgeeks.org/clear-screen-python/

generating a random letter a-e was inspired by: https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python but required more research into making it work properly.

code to import Googles sheets is used and implemented as shown and explained in Code Institute lessons, specifically the "Love Sandwiches Walkthrough Project, Getting Set Up, Connecting to our API with Python lesson."

code to remove brackets from strings is from: https://bobbyhadz.com/blog/python-remove-square-brackets-from-list

Bugs
Bug caused the game_over_lose() function to print "You lose" once for every time the dice_roll() function was called. Troubleshooting found I used an if statement instead of an elif statement for the losing condition, which apparently holds all of the print() commands until it's finally called. Replaced with an elif, problem solved.

A bug in door_row() and door_pos() cause the function to return None when user gave a bad input on the first attempt, even if good input was ultimately given. I found that the probelm was that the defensive part of the function called itself again, so the returned value did not get to the original calling location. This issue was fixed by passing around a global variable.

When pulling strings from Google Sheets and trying to display them in an f string literal, the string is surrounted by square brackets and single quotes instead of being seamlessly integrated. Found some code that would remove the brackets and single quotes on https://bobbyhadz.com/blog/python-remove-square-brackets-from-list and adapted it for my use.

Unfixed bugs
There is a bug where the global attempts variable resets between most functions, but not between the door_row() and door_pos() functions. 

