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
    vars = (('air',1100), ('water',4900), ('steel',16400))
    endProgram = 'no'

    # Displays an introduction to the program and describes what it does.
    fluffy_intro()

    # The program will continue looping until the user sets
    #   endProgram == 'yes' when prompted.
    while endProgram.lower() in ['no', 'n', '']:
        input('Menu Selection')



# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Going Green program.\n'
          'This program takes the monthly energy costs from the year prior\n'
          'to going green and the year since going green.  It then calculates'
          'the monthly savings and displays everything in a savings report.')
    return None