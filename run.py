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
    elif begin == 'n':
        game_quit()
    else:
        print('Input must be Y or N\n')


start_game()


"""
GET NAME
    validate
        length
        not blank

EXPLAIN RULES
    start with 4hp
    25 positions, one has exit door
    opponents randomly throughout
    ready (y/n)
        validate
            y or n only

FIRST RENDER
    decide what position exit door is
    DISPLAY BOARD

GAMEPLAY
    user input
        validate
            format
            on board
            not chosen
    change board dictionary

    check if exit door
        WIN
            access spreadsheet for <win copy>

    check if door is ALLY, CLEAR or OPPONENT, ROLL D6
        6 ALLY
            unless two allies chosen, then CLEAR
            access spreadsheet for <ally copy>
        4-5 CLEAR
            access spreadsheet for <clear copy>
            NEXT
        1-3 OPPONENT
            access spreadsheet for <opponent info>
            user instigate ROLL D6
            6 - success
                +1 hp
                access spreasheet for <opponent success>
            4-5 - deflect
                access spreadsheet for <opponent deflect>
            1-3 - fail, -1 hp
                -1 hp
                access spreadsheet for <opponent fail>
            NEXT

NEXT
    check player hp
        hp = 0
            LOSE
        hp >= 0
        increment turn total +1
        DISPLAY BOARD
            board a dictionary
            row is key, value is a list,
                so it can be changed by targeting a position in the list
                after a specific key.
"""
