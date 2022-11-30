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
selected_pos = 0
calc_oppo = 0
exit_pos = 0
selected_row = ''
exit_row = ''
user_door = []
exit_door = []
guessed_doors = []
opponents_list = []
minus_one_list = []
no_change_list = []
run_away_list = []
plus_one_list = []
opponents_past = []
hint_row = []
hint_pos = []
board = {}


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


def diagnostic_prints():
    """
    Code that allows the user to see the doors selected
    as well as the winning door for code testing use.
    """
    print('Diagnostics:\n')
    print(f'User door: {user_door}')
    print(f'Exit door: {exit_door}')
    print(f'Guessed: {guessed_doors}')
    sleep(5)


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
        elif next_function == 'lose':
            game_over_lose()
        elif next_function == 'scared':
            game_over_lose()
        elif next_function == 'over':
            start_game()
        else:
            error_end()
    elif play == 'N':
        if next_function == 'rules':
            clear_screen()
            n_quit()
        elif next_function == 'first':
            clear_screen()
            n_quit()
        elif next_function == 'dice':
            run_away()
        elif next_function == 'door':
            stay_in_hall()
        elif next_function == 'scared':
            get_door()
        elif next_function == 'over':
            clear_screen()
            print('\nUntil the next cave, goodbye!')
            exit()
        else:
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
        elif next_function == 'run':
            run_away()
        else:
            stay_in_hall()
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


def give_hint():
    """
    Gives user a hint after every third turn.
    """
    global hint_row, hint_pos
    len_row = len(hint_row) - 1
    len_pos = len(hint_pos) - 1
    if len_pos > 0:
        if turn % 2 == 0:
            hint = hint_row[random.randint(0, (len_row))]
            print(f'You see an old sign that says "Row {hint} leads to doom!"')
            hint_row.remove(hint)
        elif turn % 2 == 1:
            hint = hint_pos[random.randint(0, (len_pos))]
            print(f'A carving in the wall reads "Fear position {hint}!"')
            hint_pos.remove(hint)
        else:
            error_end()
    elif len_pos == 0:
        print('You see an old sign but the writing is illegible.')
    else:
        error_end()


def stay_in_hall():
    clear_screen()
    board_render()
    print('\nIf you choose no doors, you have no chance for escape.')
    print('Your rotting bones will be left for the next sad soul.')
    print('\nAre you sure?')
    continue_game('scared')


def error_end():
    """
    Ends game due to an error.
    """
    print('\nThere was an unrecoverable error.')

    game_quit()


def n_quit():
    """
    Ends game after an N selection.
    """
    print('\nMaybe you will grow up to be brave.\n')
    exit()


def game_quit():
    """
    Ends game when user selects to quit.
    """
    print('\nQuitters never win.\n')
    exit()


def game_over_win():
    """
    Ends game when user wins game.
    """
    clear_screen()
    board_render()
    print('\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
    print('You win! You escape the maze!')
    print('*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n')
    play_again()
    print('\nPlay again?')
    continue_game('over')


def game_over_lose():
    """
    Ends game when user loses game.
    """
    clear_screen()
    board_render()
    print('\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
    print('You lose! You did not escape!')
    print('*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n')
    print('\nPlay again?')
    continue_game('over')


# Game play functions ---------------------------------------------------
def start_game():
    """
    Introduces game and passes user to begin_game function.
    """
    clear_screen()
    print('\nWelcome to...    ___')
    print(' |The\\  |   \\  /   |')
    print(' | |\\ \\ | |\\ \\/ /| |')
    print(' | Dangerous!  Maze!')
    print(' | |/ / | |  \\/  | |')
    print(' |___/  |_|      |_|')
    print('')
    print('\nPlay the game?')

    continue_game('rules')


def game_rules():
    """
    Explains game rules, gets user name, and begins gameplay.
    """
    print()
    print('When prompted, select a door by')
    print('entering coordinates like "A 3"\n')
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
    global opponents_list, minus_one_list, no_change_list, plus_one_list, run_away_list
    opponents_list = SHEET.worksheet('opponents').get_all_values()
    minus_one_list = SHEET.worksheet('minus_one').get_all_values()
    no_change_list = SHEET.worksheet('no_change').get_all_values()
    plus_one_list = SHEET.worksheet('plus_one').get_all_values()
    run_away_list = SHEET.worksheet('run_away').get_all_values()


def first_render():
    """
    Does the initial gameboard render.
    """
    global health_points, turn, board, exit_row, exit_pos, exit_door, hint_row, hint_pos
    health_points = 5
    turn = 1
    hint_row = ['A', 'B', 'C', 'D', 'E']
    hint_pos = [1, 2, 3, 4, 5]
    exit_row = chr(random.randint(65, 69))
    exit_pos = random.randint(1, 5)
    exit_door = [exit_row, exit_pos]
    hint_row.remove(exit_row)
    hint_pos.remove(exit_pos)
    board = {'A': [1, 2, 3, 4, 5], 'B': [1, 2, 3, 4, 5],
             'C': [1, 2, 3, 4, 5], 'D': [1, 2, 3, 4, 5], 'E': [1, 2, 3, 4, 5]}
    board_render()
    print()
    print('Behind these doors is an opponent,')
    print('an empty room, or the exit.')
    print('\nWould you like to choose a door?')

    continue_game('door')


def door_row():
    """
    Gets row assignment for door selection
    """
    global attempts, selected_row
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
    global attempts, selected_pos
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
    User selects door to open.
    """
    global user_door, selected_row, selected_pos, guessed_doors
    clear_screen()
    board_render()
    print()
    print('You are in the maze.')
    if turn > 1:
        if (turn - 1) % 3 == 0:
            give_hint()
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
    global user_door, exit_door, guessed_doors
    # Following function is diagnostic only.
    # diagnostic_prints()
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
    global opponents_past, calc_oppo
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
    global turn, attempts, user_door
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
        print('\nDo you want to fight?')
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
    global health_points, attempts, turn
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
        print('\nContinue?')
    elif roll == 5:
        board_render()
        print()
        print(f'You rolled a {roll}.')
        calc_string = no_change_list[calc_oppo]
        outcome_string = string_debracketer(calc_string)
        print(outcome_string)
        print(f'Your health points remain the same. You have {health_points}.')
        print('\nContinue?')
    elif roll == 6:
        health_points = health_points + 1
        board_render()
        print()
        print(f'You rolled a {roll}.')
        calc_string = plus_one_list[calc_oppo]
        outcome_string = string_debracketer(calc_string)
        print(outcome_string)
        print(f'You gain one health point! You now have {health_points}.')
        print('\nContinue?')
    else:
        input_attempts('roll')
    turn = turn + 1

    did_you_die_though()


def run_away():
    """
    Rolls the dice to see the outcome if the user runs away.
    """
    global health_points, turn
    roll = random.randint(1, 6)
    if roll > 2:
        clear_screen()
        board_render()
        print()
        print(f'You rolled a {roll}.')
        print('You quickly slam the door and run, hopefully undetected.')
        print('\nContinue?')
    elif roll == 2:
        clear_screen()
        board_render()
        health_points = health_points - 1
        calc_string = run_away_list[calc_oppo]
        outcome_string = string_debracketer(calc_string)
        print()
        print(f'You rolled a {roll}.')
        print(outcome_string)
        print(f'You lose one health point. You now have {health_points}.')
        print('\nContinue?')
    elif roll == 1:
        if health_points == 1:
            health_points = health_points - 1
        else:
            health_points = health_points - 2
        clear_screen()
        board_render()
        calc_string = run_away_list[calc_oppo]
        outcome_string = string_debracketer(calc_string)
        print()
        print(f'You rolled a {roll}.')
        print(outcome_string)
        print(f'You lose 2 health points. You now have {health_points}.')
        print('\nContinue?')
    else:
        input_attempts('run')
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
        continue_game('lose')
    else:
        error_end()


# First call ------------------------------------------------
start_game()
