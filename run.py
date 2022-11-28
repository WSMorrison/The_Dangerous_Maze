"""
Dangerous Maze game, Python Essentials Portfolio Project, PP3.
"""
from os import system, name
from time import sleep
import random
import gspread
from google.oauth2.service_account import Credentials


# Constants ------------------------------------------------------------
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('monsters_master_list')


# Global variables -----------------------------------------------------
health_points = 0
attempts = 0
turn = 0
selected_row = ''
selected_pos = 0
calc_oppo = 0
user_door = []
exit_door = []
board = {}
guessed_doors = []
opponents_list = []
minus_one_list = []
no_change_list = []
plus_one_list = []
opponents_past = []


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


def string_debracketer(string):
    """
    Removes brackets from inported strings.
    """
    no_brackets = ', '.join(string)
    return no_brackets


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
            clear_screen()
            print('Too many attempts.')
            game_quit()
        else:
            error_end()


def input_attempts(next_function):
    """
    Gives the user 5 attempts to give bad input.
    """
    global attempts
    attempts = attempts + 1
    if attempts < 5:
        if next_function == 'row':
            print('Pick a valid row, or Q for quit.')
            door_row()
        elif next_function == 'pos':
            print('Pick a valid postion, or Q for quit.')
            door_pos()
        elif next_function == 'oppo':
            print('Error rolling.')
            oppo_or_not()
        elif next_function == 'roll':
            print('Error rolling')
            dice_roll()
        else:
            error_end()
    elif attempts == 5:
        clear_screen()
        print('Too many attempts.')
        game_quit()
    else:
        error_end()


def board_render():
    """
    Renders game board
    """
    print()
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


def game_over_win():
    """
    Ends game when user wins game.
    """
    clear_screen()
    board_render()
    print('\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
    print('You win! You escape the maze!')
    print('*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
    exit()


def game_over_lose():
    """
    Ends game when user loses game.
    """
    clear_screen()
    board_render()
    print('\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
    print('You lose! You did not escape!')
    print('*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
    exit()


# Game play functions ---------------------------------------------------
def start_game():
    """
    Introduces game and passes user to begin_game function.
    """
    clear_screen()
    print('\n')
    print('')
    print('')
    print('Welcome to the Dangerous Maze!')
    print('')
    print('')
    print('')
    print('\nPlay the game?')

    continue_game('rules')


def game_rules():
    """
    Explains game rules, gets user name, and begins gameplay.
    """
    print()
    print('When prompted, select a door')
    print('by entering coordinates like "A 3"\n')
    print('You have 5 health points to escape!')
    print('Opening a door may reveal the escape,')
    print('the room behind the door may be empty,')
    print('or you may find an oppenent behind it!\n')
    print('If you find an opponent...')
    print('\n...loading...')
    get_opponents()
    sleep(5)
    clear_screen()
    print()
    print('If you find an opponent,')
    print('you will get to roll a D6.\n')
    print('Roll a 1-4, you lose a health point!')
    print('Roll a 5, you escape unscathed,')
    print('and if you manage to roll a 6,')
    print('one health point will be restored.')
    print('\nAre you ready to play the game?')

    continue_game('first')


def get_opponents():
    """
    Get the copy for opponents and outcomes from
    Google Sheets hosted spreadsheet.
    """
    global opponents_list
    global minus_one_list
    global no_change_list
    global plus_one_list
    opponents_list = SHEET.worksheet('opponents').get_all_values()
    minus_one_list = SHEET.worksheet('minus_one').get_all_values()
    no_change_list = SHEET.worksheet('no_change').get_all_values()
    plus_one_list = SHEET.worksheet('plus_one').get_all_values()


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
    print()
    print('Behind these doors is an opponent,')
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
        input_attempts('row')


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
            input_attempts('pos')
    else:
        input_attempts('pos')


def get_door():
    """
    User selects door to open
    """
    global user_door
    global selected_row
    global selected_pos
    global guessed_doors
    board_render()
    print()
    print('You are in the maze.')
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


def indicate_door():
    """
    Changes gameboard to reflect user's selection.
    """
    old_row = (board.get(selected_row))
    print(old_row)
    new_row = old_row
    new_row[selected_pos - 1] = 0
    print(new_row)
    board[selected_row] = new_row


def check_door():
    """
    Checks if user guessed the exit door.
    """
    global user_door
    global exit_door
    global guessed_doors
    # Begin diagnostic code, remove before deployment.
    # print('Diagnostics:\n')
    # print(f'User door: {user_door}')
    print(f'Exit door: {exit_door}')
    # print(f'Guessed: {guessed_doors}')
    sleep(2)
    # End diagnostic code, remove before deployment.
    indicate_door()

    if user_door == exit_door:
        game_over_win()
    else:
        clear_screen()
        oppo_or_not()


def which_opponent():
    """
    Decides which opponent copy to select from
    spreadsheet, while ensuring no duplicates.
    """
    global opponents_past
    global calc_oppo
    calc_oppo = random.randint(0, 24)
    if calc_oppo in opponents_past:
        which_opponent()
    else:
        opponents_past.append(calc_oppo)


def oppo_or_not():
    """
    Decides if there is an opponent behind the door,
    or if door is clear.
    """
    global turn
    global attempts
    global user_door
    board_render()
    print()
    print(f'You chose {user_door}.')
    roll = random.randint(1, 6)
    if roll < 6:
        which_opponent()
        calc_string = opponents_list[calc_oppo]
        literal_string = string_debracketer(calc_string)
        print('There is an opponent!')
        print(f'You have encountered {literal_string}')
        print('\nReady to battle?')
        continue_game('dice')
    elif roll == 6:
        print('Room is empty! Get back out there.')
        print('\nChoose another door?')
        turn = turn + 1
        continue_game('door')
    else:
        input_attempts('oppo')


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
        print()
        print(f'You rolled a {roll}.')
        calc_string = minus_one_list[calc_oppo]
        outcome_string = string_debracketer(calc_string)
        print(outcome_string)
        print(f'You lose one health point! You now have {health_points}.')
        print('\nChoose another door?')
    elif roll == 5:
        board_render()
        print()
        print(f'You rolled a {roll}.')
        calc_string = no_change_list[calc_oppo]
        outcome_string = string_debracketer(calc_string)
        print(outcome_string)
        print(f'Your health points remain the same. You have {health_points}.')
        print('\nChoose another door?')
    elif roll == 6:
        health_points = health_points + 1
        board_render()
        print()
        print(f'You rolled a {roll}.')
        calc_string = plus_one_list[calc_oppo]
        outcome_string = string_debracketer(calc_string)
        print(outcome_string)
        print(f'You gain one health point! You now have {health_points}.')
        print('\nChoose another door?')
    else:
        input_attempts('roll')
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
