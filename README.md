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
-

