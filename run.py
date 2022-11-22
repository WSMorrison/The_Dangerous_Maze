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


# Basic functions ------------------------------------------------------
def short_string(string):
    """
    Makes sure input string isn't blank,
    then shortens user input to one character,
    and makes sure the string is lowercase
    as part of defensive design.
    """
    nonblank_string = string + 'x'
    shortened_string = nonblank_string[0]
    good_string = shortened_string.lower()
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
    user_input = input('Y/N/E E for exit.\n')
    play = short_string(user_input)
    if play == 'y':
        attempts = 0
        clear_screen()
        if next_function == 'rules':
            game_rules()
        elif next_function == 'first':
            first_render()
        elif next_function == 'oppo':
            oppo_or_not()
        elif next_function == 'rere':
            re_render()
        elif next_function == 'dice':
            dice_roll()
        else:
            error_end()
    elif play == 'n':
        clear_screen()
        game_quit()
    elif play == 'e':
        clear_screen()
        game_quit()
    else:
        attempts = attempts + 1
        if attempts < 5:
            print('Input must be Y or N or E.')
            continue_game(next_function)
        elif attempts == 5:
            print('Too many attempts.')
            game_quit()
        else:
            error_end()


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


def game_over_lose():
    """
    Ends game when user loses game.
    """
    print("You didn't make it, better luck next time.")


# Game play functions ---------------------------------------------------
def start_game():
    """
    Introduces game and passes user to begin_game function.
    """
    clear_screen()
    print('Welcome to Christmas Vacation.\n')
    print('Your entire family has been in your house for a month,')
    print('and you just want to get out to the garage to relax.')
    print('Can you get some valuable alone time')
    print('before having a meltdown?')
    print('\nPlay the game?')

    continue_game('rules')


def game_rules():
    """
    Explains game rules, gets user name, and begins gameplay.
    """
    print('You are in your house.')
    print('There are Christmas decorations everywhere,')
    print('and you are disoriented by the blinking, colored lights')
    print('and the strong smells from the scented candles.\n')
    print('All the doors in the house are closed,')
    print('and like this is a bad dream,')
    print('they all look the same.')
    print('Try a door, and see if it leads to the garage.\n')
    print('Behind the door, you may find freedom...')
    print('...or you may find a needy family member.\n')
    print('...loading...')
# DONT FORGET TO CHANGE THE SLEEP TO 10 FOR 10 SECONDS!!!!!!!!
    sleep(1)
    clear_screen()
    print('You will get to roll a D6\n')
    print('1-4, you lose a health point!')
    print('5, you escape unscathed,')
    print('and if you roll a 6, family love and the holiday spirit')
    print('will restore you one health point.\n')
    print('Are you ready to go out into the house?')

    continue_game('first')


def first_render():
    """
    Does the initial gameboard render.
    """
    global health_points
    health_points = 5
    print('SYSTEM: First render happens here.')
# Skipping ahead for funtion testing.
# Will need to advance to selecting a door from here.
    print('SYSTEM: Skipping to opponent selector.\n')

    oppo_or_not()


def oppo_or_not():
    """
    Decides if there is an opponent behind the door,
    or if door is clear.
    """
    global attempts
    roll = random.randint(1, 6)
    if roll < 6:
# Opponent copy goes here!
        print('There is an opponent!')
        print('\nReady to battle?')
        continue_game('dice')
    elif roll == 6:
        print('Room is clear! Take a breath and get back out there.')
        print('\nChoose another door?')
        continue_game('oppo')
    else:
        attempts = attempts + 1
        if attempts < 5:
            print('Error rolling.')
            oppo_or_not()
        elif attempts == 5:
            print('Too many attempts.')
            error_end()
        else:
            error_end()


def dice_roll():
    """
    Rolls the D6.
    """
    global health_points
    global attempts
    roll = random.randint(1, 6)
    print(f'You rolled a {roll}.')
    if roll < 5:
        health_points = health_points - 1
# Outcome copy goes here!
        print(f'You lose one health point! You have {health_points}.')
        print('\nChoose another door?')
    elif roll == 5:
# Outcome copy goes here!
        print(f'Your health points remain the same. You have {health_points}.')
        print('\nChoose another door?')
    elif roll == 6:
# Outcome copy goes here!
        health_points = health_points + 1
        print(f'You gain one health point! You have {health_points}.')
        print('\nChoose another door?')
    else:
        attempts = attempts + 1
        if attempts < 5:
            print('Error rolling.')
            dice_roll()
        elif attempts == 5:
            print('Too many attempts.')
            error_end()
        else:
            error_end()

    did_you_die_though()


def did_you_die_though():
    """
    Decides if player has lost or will continue playing.
    """
    global health_points
    if health_points > 0:
        continue_game('rere')
    elif health_points == 0:
        game_over_lose()
    else:
        print('Fatal error')
        game_quit()

def re_render():
    print('Rerender happens here!')
    oppo_or_not()


# First call ------------------------------------------------
start_game()
