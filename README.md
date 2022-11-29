# The Dangerous Maze

Porfolio Project 3, Python Essentials.
<br>
Screenshot
<br>
Table of contents
<br>

# Rationale

The Portfolio Project 3 is a terminal based, Python project. It was decided that this format was perfect for a program similar to the text-based, dice-rolling, role-playing games from the developer's childhood before GUI were common. 

The purpose of this project is to display the developer's ability to program a Command Line Interface based program. The game will play with simple keyboard based commands, allowing the user to select wether they want to continue or quit, and the user can select positions on a grid that may trigger an opponent or not, and the user will benefit from a simulated dice roll that will decide the outcome of any opponent encounter. The encounters can result in the loss or gain of a health point, and if the user's health points run out before they find the exit they lose.

The program will exhibit understanding of the Python pogramming language, functions, nested functions, data type, nested data types, methods, object oriented programming, API usage, and deployment strategies. It will also incorporate defensive design, well organized code, and easily readable and understandable user interface.

# User Experience

-The game will be able to be played on a computer browser.
-The game will accept user input.
-The game will react to user inputs, rejecting bad or duplicate inputs in a pleaseing way.
-The game will progress in a logical way, and indicate previous guesses.
-The game will be of appropriate difficulty and duration.
-The game will have engaging copy.

# Project Outcome

The outcome of this project will be a playable, terminal based, command line interface game describing a situation where the user encounters monsters as they try to escape a maze.

# Design

Care was taken to make the game input locations consistent as the game advances. The game uses a function to clear the screen and rebuild the displayed gameboard between user inputs, keeping the terminal tidy and readable. The game was intentionally kept with black text on the black terminal background as an homage to the early games of this type it was inspired by. 

# Technology Implementation

## Language

The program is written in the Python programming language. [Python](https://www.python.org/)

## Technology

The program was built on the Code Institute Python Essentials Templplate. On request.
The program uses Google Sheets for spreadsheet hosting. [Google Sheets](https://www.google.com/sheets/about/)
The spreadsheets are accessed using a credentials API provided by Google Sheets.
The spreadsheets are interpreted for Python using Gspread. [gspread](https://docs.gspread.org/en/v5.7.0/)
Python imports modules from the time and math libraries, and the user's operating system.

## Deployment

Code was written and version control maintained in GitHub. [Github](https://github.com/)
The game was deployed as an app using Heroku. [Heroku](https://www.heroku.com/)

When the code was deployment ready, it was deployed in Heroku by following these steps as outlined in the Code Institute Love Sandwiches Walkthrough Project, Deployment, Deploying our Project Part 1 and Part 2 lessons:

-The run.py file had to have the input() methods modified with a linebreak to work with the Code Institute mock terminal being run by Heroku.
-A requirements.txt file was made to give Heroku the dependencies required by the program. This was done by issuing the command "pip3 freeze > requirements.txt" in the Gitpod terminal.
-In the Heroku dashboard, a new app was created.
-In the new app's page, the settings tab was selected, and the following settings were set:
    -A config var was set as CREDS for the key field, and the creds.json file contents copied and pasted into the value field.
    -A config var was set as PORT for the key field, and 8000 for the value field.
    -heroku/python Buildpack was added to the required buildpacks.
    -heroku/nodejs Buildpack was added to the required buildpacks. The buildpacks must be set in this order.
-In the deploy tab of the app's page, the following selections were made:
    -The app was connected to the developer's appropriate Github repository.
    -Automatic deploys were enabled.
    -Deploy Branch was selected for the initial deploy.
-When Heroku successfully deployed the App, the deployment was checked and tested.

# Features

-The game displays a game board showing rows of doors and selectable positions on each row.
-The game changes positions to a 0 instead of a position number to indicate that it was selected.
-The code defends against selecting a previously selected door to avoid wasted attempts or errors.
-The code defends against bad, empty, or duplicate inputs during gameplay.
-The game accesses a developer expandable list of opponents for the color copy during gameplay.
-The code tracks which opponents have been called and excludes them from duplicate selection.
-Health points are displayed throughout gameplay and remain accurate as gameplay advances.
-A turn counter maintains a count of user turns and indicates how long they have lasted.
-The code clears the screen and rebuilds the game board at each input to maintain a clean look.

# Testing

The game was tested in Gitpod during development, to maintain continuity of functionality and to check that each added development worked properly. 

There is a diagnostic function intentially left in the code, the call for it commented out, that allows the developer and subsequent developers to view the user selected door position, the winning door position, and all previously selected positions in order to allow a developer to see what's going on and quickly test changes in or avoid game winning code. This code is intentionally left in, because it may be useful for assessors as well!

After deployment, the app was shared with friends, family, and Code Institute classmates to test the code.

Some bugs were exposed during initial development and during deployed testing, most were fixed.

## Bugs

During predeployment development, a bug was found that caused the game_over_lose() function to print a line displaying "You lose" once for every time the dice_roll() function had been called during gameplay. Troubleshooting found that developer had used an if statment instead of an elif statement for the losing condition, which apparently heald all of the instances of the game_over_lose() function until it was finally called. Replaced the erroneous if statement with an elif statement, and the code worked properly, only printing the losing message once. (Some of these functions have been refactored or changed, so this may not seem directly applicable to code as it's written now, but the logic and the error would have remained.)

A bug in the initial design of the door_row() and door_pos() functions was revealed in predevelopment testing. When the user gave a bad input on the first attempt at the row or position, the functions would return None even if the user ultimately submitted a good input. The problem was that the defensive part of the function called itself again, so the value returned did not get to the original calling location. The issue was fixed by passing around a global variable instead of passing the function's returned output directly to the position it was called. This allowed the function to write the user's good input to the variable and that information be accessed elsewhere in the program.

Before the code was deployed, the Python code was linked to Google Sheets spreadsheets for the color copy. During the initial build of this functionality, the code was accessed and returned directly into an f'string literal. This caused the string returned with square brackets and single quotes surrounding (see screenshot) instead of a seamless string. Classmate [Adam Boczek](https://github.com/aboczek) suggested a solution described by Borislav Hadzhiev on his [webpage](https://bobbyhadz.com/blog/python-remove-square-brackets-from-list). A new string_debracketer() function was developed using similar code, and printing the returned string to the f'string literal displayed the text properly.

## Unfixed bugs

There is a bug where the global attempts variable resets between most functions, but not between the door_row() and door_pos() functions. This means that the user has a combined 5 attempts to input good values for the door row and the door position.

# Credits

-Code Institute Python Essentials lessons for the bulk of my understanding of how Python works. [Code Institute](https://codeinstitute.net/ie/)
-Code Institute instructor Simen Daehlin for almost everything else. [Simen Daehlin Github](https://github.com/Eventyret)
-Code Institute mentor Jubrile Akolade provided guidance on where to focus time building project and an almost infinite amount of other support.
-Code to import Googles sheets is used and implemented as shown and explained in Code Institute lessons, specifically the "Love Sandwiches Walkthrough Project, Getting Set Up, Connecting to our API with Python lesson." On request.
-W3Schools for help with some data structures and methods. [W3Schools](https://www.w3schools.com/python/)
-Information on clearing the screens on different operating systems found [here.](https://www.geeksforgeeks.org/clear-screen-python/)
-Information and ideas that inspired using ASCII assigments and the random.randint() method in a specific range to return a random letter was found [here.](https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python)
-Information on using the .join() method to creat strings free of brackets and single quotes for use as part of string literals was found [here.](https://bobbyhadz.com/blog/python-remove-square-brackets-from-list)


