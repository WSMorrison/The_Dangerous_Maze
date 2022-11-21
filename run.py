# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from os import system, name
from time import sleep
# Sleep(x) x is number of seconds.
import random


# Global variables -----------------------------------------------------
health_points = 0


# Basic functions ------------------------------------------------------
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


def short_string(string):
    """
    Shortens user input to one lowercase character
    as first half of defensive design.
    """
    nonblank_string = string + 'x'
    shortened_string = nonblank_string[0]
    good_string = shortened_string.lower()
    return good_string


def clear_screen():
    """
    Clears the screen between rending text.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Game play functions ---------------------------------------------------
def first_render():
    """
    Does the initial gameboard render
    """
    global health_points
    health_points = 5
    print('First render happens HERE')
# Skipping straight to dice roll for funtion testing.
# Will need to advance to selecting a door from here.
    print('Skipping to dice roll\n')

    dice_roll()


def dice_roll():
    """
    Rolls the D6
    """
    global health_points
    roll = random.randint(1, 6)
    print(f'You rolled a {roll}')
    if roll < 5:
        health_points = health_points - 1
        print(f'HP -1. Your HP are now {health_points}')
    elif roll == 5:
        print(f'HP remain the same. Your HP remain {health_points}')
    elif roll == 6:
        health_points = health_points + 1
        print(f'HP +1. Your HP is now {health_points}')
    else:
        print('Error rolling.')
        dice_roll()

    did_you_die_though()


def did_you_die_though():
    """
    Decides if player has lost or will continue playing.
    """
    global health_points
    if health_points > 0:
        continue_game()
    elif health_points == 0:
        game_over_lose()
    else:
        print('Fatal error')
        game_quit()


def continue_game():
    """
    Ask user if they want to begin, looped in defense.
    Y/N/E INPUT, REFACTOR????????????????????????????
    """
    print('\nContinue?')
    user_input = input('Y/N/E E for exit.\n')
    play = short_string(user_input)
    if play == 'y':
        clear_screen()
        dice_roll()
    elif play == 'n':
        clear_screen()
        game_quit()
    elif play == 'e':
        clear_screen()
        game_quit()
    else:
        print('Input must be Y or N or E')
        continue_game()


# Pregame ----------------------------------------------------------------
def play_game():
    """
    Ask user if they want to begin, looped in defense.
    Y/N/E INPUT, REFACTOR????????????????????????????
    """
    user_input = input('Y/N/E E for exit.\n')
    play = short_string(user_input)
    if play == 'y':
        clear_screen()
        first_render()
    elif play == 'n':
        clear_screen()
        game_quit()
    elif play == 'e':
        clear_screen()
        game_quit()
    else:
        print('Input must be Y or N or E')
        play_game()


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
    print('...loading...')
# DONT FORGET TO CHANGE THE SLEEP TO 10 FOR 10 SECONDS!!!!!!!!
    sleep(1)
    clear_screen()
    print('Try a door, and see if it leads to the garage.')
    print('Behind the door, you may find freedom....\n')
    print('...or you may find a needy family member.\n')
    print('You will get to roll a D6')
    print('1-4, you lose a health point!')
    print('5, you escape unscathed,')
    print('and if you roll a 6, family love and the holiday spirit')
    print('will restore you one health point.\n')
    print('Are you ready to go out into the house?')

    play_game()


def begin_game():
    """
    Ask user if they want to begin, looped in defense.
    Y/N/E INPUT, REFACTOR????????????????????????????
    """
    user_input = input('Y/N/E E for exit.\n')
    play = short_string(user_input)
    if play == 'y':
        clear_screen()
        game_rules()
    elif play == 'n':
        clear_screen()
        game_quit()
    elif play == 'e':
        clear_screen()
        game_quit()
    else:
        print('Input must be Y or N or E')
        begin_game()


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

    begin_game()

# First call ------------------------------------------------
start_game()
