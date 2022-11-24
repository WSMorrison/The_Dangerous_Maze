# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from os import system, name
from time import sleep
# Sleep(x) x is number of seconds.
import random


# Global variables -----------------------------------------------------
health_points = 0
attempts = 0
turn = 0
selected_row = ''
selected_pos = 0
user_door = []
exit_door = []
board = {}
guessed_doors = []


# Basic functions ------------------------------------------------------
def short_string(string):
    """
    Makes sure input string isn't blank,
    then shortens user input to one character,
    and makes sure the string is lowercase
    as part of defensive design.
    """
    nonblank_string = string + 'X'
    shortened_string = nonblank_string[0]
    good_string = shortened_string.upper()
    return good_string


def clear_screen():
    """
    Clears the screen, often used between rendering text.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def continue_game(next_function):
    """
    Y/N/E input asking user if user wants
    to advance to the next activity.
    """
    global attempts
    user_input = input('Y/N/Q Q for Quit.\n')
    play = short_string(user_input)
    if play == 'Y':
        attempts = 0
        clear_screen()
        if next_function == 'rules':
            game_rules()
        elif next_function == 'first':
            first_render()
        elif next_function == 'door':
            get_door()
        elif next_function == 'oppo':
            oppo_or_not()
        elif next_function == 'dice':
            dice_roll()
        else:
            error_end()
    elif play == 'N':
        clear_screen()
        game_quit()
    elif play == 'Q':
        clear_screen()
        game_quit()
    else:
        attempts = attempts + 1
        if attempts < 5:
            print('Input must be Y or N, or Q for Quit.')
            continue_game(next_function)
        elif attempts == 5:
            print('Too many attempts.')
            game_quit()
        else:
            error_end()


def board_render():
    """
    Renders game board
    """
    print(f'HP: {health_points}         Turn: {turn}')
    for row in board:
        print(f'Row {row}: {board[row]}')


def error_end():
    """
    Ends game due to an error.
    """
    print('\nThere was an unrecoverable error.')

    game_quit()


def game_quit():
    """
    Ends game when user selects to quit.
    """
    print('\nThank you, goodbye!\n')
    exit()


def game_over_lose():
    """
    Ends game when user loses game.
    """
    print("You didn't make it, better luck next time.")
    exit()


# Game play functions ---------------------------------------------------
def start_game():
    """
    Introduces game and passes user to begin_game function.
    """
    clear_screen()
    print('Welcome to Christmas Vacation.\n')
    print('Intro')
    print('Intro')
    print('Intro')
    print('Intro')
    print('Intro')
    print('Intro')
    print('\nPlay the game?')

    continue_game('rules')


def game_rules():
    """
    Explains game rules, gets user name, and begins gameplay.
    """
    print('Intro\n')
    print('Intro')
    print('Intro')
    print('Intro')
    print('Intro')
    print('Intro')
    print('Intro')
    print('\n...loading...')
# DONT FORGET TO CHANGE THE SLEEP TO 10 FOR 10 SECONDS!!!!!!!!
    sleep(1)
    clear_screen()
    print('You will get to roll a D6\n')
    print('1-4, you lose a health point!')
    print('5, you escape unscathed,')
    print('and if you roll a 6,')
    print('one health point will be restored.')
    print('Rules')
    print('Rules')
    print('\nAre you ready to go out into the house?')

    continue_game('first')


def first_render():
    """
    Does the initial gameboard render.
    """
    global health_points
    health_points = 5
    global turn
    turn = 1
    global board
    global exit_door
    exit_row = chr(random.randint(65, 69))
    exit_pos = random.randint(1, 5)
    exit_door = [exit_row, exit_pos]
    board = {'A': [1, 2, 3, 4, 5], 'B': [1, 2, 3, 4, 5],
                'C': [1, 2, 3, 4, 5], 'D': [1, 2, 3, 4, 5], 'E': [1, 2, 3, 4, 5]}
    board_render()
    print('Behind the door, you may find an opponent,')
    print('and empty room, or the exit.')
    print('\nWould you like to choose a door?')

    continue_game('door')


def door_row():
    """
    Gets row assignment for door selection
    """
    global attempts
    global selected_row
    rows = ['A', 'B', 'C', 'D', 'E']
    user_row = input('Input row. Q for Quit.\n')
    row_string = short_string(user_row)
    if row_string in rows:
        selected_row = row_string
    elif row_string == 'Q':
        clear_screen()
        game_quit()
    else:
        attempts = attempts + 1
        if attempts < 5:
            print('Pick a valid row, or Q for quit.')
            door_row()
        elif attempts == 5:
            clear_screen()
            print('Too many attempts.')
            game_quit()
        else:
            error_end()


def door_pos():
    """
    Gets position assignment for door selection
    """
    global attempts
    global selected_pos
    user_pos = input('Input position. Q for Quit.\n')
    if user_pos.isdigit():
        pos_num = int(user_pos)
        if 1 <= pos_num <= 5:
            selected_pos = pos_num
        else:
            print('Enter valid position, or Q for Quit.')
            door_pos()
    elif user_pos.isalpha():
        if short_string(user_pos) == 'Q':
            clear_screen()
            game_quit()
        else:
            attempts = attempts + 1
            if attempts < 5:
                print('Enter valid position or Q for Quit.')
                door_pos()
            elif attempts == 5:
                clear_screen()
                print('Too many attempts.')
                game_quit()
            else:
                error_end()
    else:
        attempts = attempts + 1
        if attempts < 5:
            print('Enter valid position or Q for Quit.')
            door_pos()
        elif attempts == 5:
            clear_screen()
            print('Too many attempts.')
            game_quit()
        else:
            error_end()


def get_door():
    """
    User selects door to open
    """
    global user_door
    global selected_row
    global selected_pos
    global guessed_doors
    board_render()
    print("You're back in the hall.")
    print('\nSelect a door.')
    door_row()
    door_pos()
    row = selected_row
    pos = selected_pos
    user_door = [row, pos]
    if user_door in guessed_doors:
        print(f'You have already tried {user_door}.')
        print('Give it another try?')
        continue_game('door')
    else:
        guessed_doors.append(user_door)
        clear_screen()

    check_door()


def check_door():
    """
    Checks if user guessed the exit door.
    """
    global user_door
    global exit_door
    global guessed_doors
    print(f'User door: {user_door}')
    print(f'Exit door: {exit_door}')
    print(f'Guessed: {guessed_doors}')
    sleep(5)
    if user_door == exit_door:
        clear_screen()
        print('*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
        print("You win! You win! You legend!")
        print('*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
        game_quit()
    else:
        clear_screen()

        oppo_or_not()


def oppo_or_not():
    """
    Decides if there is an opponent behind the door,
    or if door is clear.
    """
    global turn
    global attempts
    global user_door
    board_render()
    print(f'You chose {user_door}.')
    roll = random.randint(1, 6)
    if roll < 6:
        # Opponent copy goes here!
        print('There is an opponent!')
        print('\nReady to battle?')
        continue_game('dice')
    elif roll == 6:
        print('Room is empty! Get back out there.')
        print('\nChoose another door?')
        turn = turn + 1
        continue_game('door')
    else:
        attempts = attempts + 1
        if attempts < 5:
            print('Error rolling.')
            oppo_or_not()
        elif attempts == 5:
            print('Too many attempts.')
            game_quit()
        else:
            error_end()


def dice_roll():
    """
    Rolls the D6.
    """
    global health_points
    global attempts
    global turn
    roll = random.randint(1, 6)
    if roll < 5:
        health_points = health_points - 1
        board_render()
        print(f'You rolled a {roll}.')
        # Outcome copy goes here!
        print(f'You lose one health point! You have {health_points}.')
        print('\nChoose another door?')
    elif roll == 5:
        board_render()
        print(f'You rolled a {roll}.')
        # Outcome copy goes here!
        print(f'Your health points remain the same. You have {health_points}.')
        print('\nChoose another door?')
    elif roll == 6:
        health_points = health_points + 1
        board_render()
        print(f'You rolled a {roll}.')
        # Outcome copy goes here!
        print(f'You gain one health point! You have {health_points}.')
        print('\nChoose another door?')
    else:
        attempts = attempts + 1
        if attempts < 5:
            print('Error rolling.')
            dice_roll()
        elif attempts == 5:
            print('Too many attempts.')
            game_quit()
        else:
            error_end()
    turn = turn + 1
            
    did_you_die_though()


def did_you_die_though():
    """
    Decides if player has lost or will continue playing.
    """
    global health_points
    if health_points > 0:
        continue_game('door')
    elif health_points == 0:
        game_over_lose()
    else:
        error_end()


# First call ------------------------------------------------
start_game()
