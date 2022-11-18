# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def game_rules():
    """
    Explains game rules, gets user name, and begins gameplay.
    """
    print('Game rules')


def game_quit():
    """
    Ends game when user selects to quit.
    """
    print('Thank you, goodbye!')


def short_string(string):
    """
    Shortens user input to one lowercase character
    as first half of defensive design.
    """
    shortened_string = string[0]
    good_string = shortened_string.lower()
    return good_string


def begin_game():
    """
    Ask user if they want to begin, looped in defense.
    """
    user_input = input('\nBegin game? Y/N\n')
    begin = short_string(user_input)
    if begin == 'y':
        game_rules()
    elif begin == 'n':
        game_quit()
    else:
        print('Input must be Y or N')
        begin_game()


def start_game():
    """
    Introduces game and passes user to begin_game function.
    """
    print('        Welcome to Christmas Vacation.\n')
    print('Your entire family has been in your house for a month,')
    print(' and you just want to get out to the garage to relax.')
    print('     Can you get some valuable alone time')
    print('          before having a meltdown?')

    begin_game()


start_game()
