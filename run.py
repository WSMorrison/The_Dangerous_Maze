# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
GET NAME
    validate
    length
        not blank

EXPLAIN RULES
    start with 4hp
    25 positions, one has garage door
    relatives randomly throughout
    ready (y/n)
        validate
            y or n only

FIRST RENDER
    decide what position garage door is
    DISPLAY BOARD

GAMEPLAY
    user input
        validate
            format
            on board
            not chosen
    change board dictionary

    check if garage door
        WIN
            access spreadsheet for <win copy>

    check if opponent door, ROLL D6
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
