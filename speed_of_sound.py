# speed_of_sound.py
# Exercise selected: Chapter 11 program 7
# Name of program: Speed of Sound
# Description of program: This program displays a menu allowing the user
#   to select air, water, or steel. After the user has made a selection,
#   he or she should be asked to enter the number of seconds the sound
#   will travel in the selected medium. The program should then display
#   the distance the sound will travel.
#
# Ivan Boatwright
# March 27, 2016

def main():
    # Local variables
    meds = (('air',1100), ('water',4900), ('steel',16400))
    menuDesign = '{0:^4}1) {{0:<10}}\n{0:^4}2) {{1:<10}}\n' \
                 '{0:^4}3) {{2:<10}}\n{0:^4}0) {{3:<10}}\n'.format('')
    option = -1

    # Displays an introduction to the program and describes what it does.
    fluffy_intro()

    # The program will continue looping until the user sets
    #   endProgram == 'yes' when prompted.
    while option not in ['0']:
        option = display_menu(menuDesign, *[x[0].capitalize() for x in vars],'Exit')
        time = input()

# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Speed of Sound distance calculator.\n'
          'Please select a medium the sound will be traveling through.\n'
          'Then input the time with in seconds the sound will travel.\n'
          'The program will display how far the sound will travel in that\n'
          'time.')
    return None

def display_menu(design, option=-1, *labels):
    print('Please select the medium or enter 0 to exit.\n')
    print(design.format(*labels))
    option = input('   >>> ')

    # If the user enters anything other than the list values this
    #   loop requests new/valid input.
    while option not in ['0', '1', '2', '3']:
        option = input("Please enter the number of your menu "
                       "selection.\n    >>> ")
    return option