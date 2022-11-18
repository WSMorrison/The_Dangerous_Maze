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


def start_game():
    """
    Introduces game and asks user if they want to begin.
    """
    print('        Welcome to Christmas Vacation.\n')
    print('Your entire family has been in your house for a month,')
    print(' and you just want to get out to the garage to relax.')
    print('     Can you get some valuable alone time')
    print('          before having a meltdown?\n')

    begin = input('Begin game? Y/N\n')

    if begin.lower() == 'y':
        game_rules()
    elif begin.lower == 'n':
        game_quit()
    else:
        print('Input must be Y or N\n')


start_game()
