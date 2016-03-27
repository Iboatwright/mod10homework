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
    option, medium, time, distance = -1, 0, 0, 0

    # Displays an introduction to the program and describes what it does.
    fluffy_intro()

    # The program will continue looping until the user selects 0.
    while option not in ['0']:
        # Get the user's menu selection and assign to the option variable.
        option = display_menu(menuDesign, option,
                             *[x[0].capitalize() for x in meds], 'Exit')
        # Exit the while loop and end the program if the user selects 0.
        if option == '0':
            break

        # Get user inputs.
        medium = meds[int(option) - 1]
        time = get_time()

        # Calculate distance based on time.
        distance = calc_distance(medium[1], time)

        # Display results to the user.
        display_results(medium[0], time, distance)


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Speed of Sound distance calculator.\n'
          'Please select a medium the sound will be traveling through.\n'
          'Then input the time with in seconds the sound will travel.\n'
          'The program will display how far the sound will travel in that\n'
          'time.')
    return None


# Presents the user with a list of options and returns a valid selection.
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


# get_time asks the user to enter a time value.  Once a valid integer is
#   entered, it is returned to the calling module.
def get_time(time=0):
    print('\nPlease enter how many seconds the sound will travel.')
    while True:
        try:
            time = int(input('  >>> '))
            break
        except ValueError:
            print('Invalid entry. Try again.')
    return time


def calc_distance(medium, time):
    return medium * time


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(medium, time, distance):
    print('{4:_<60}\n\n{0}When passing through {1} for {2} seconds,\n'
          '{0}{0}sound will travel {3} feet.'
          '\n{4:_<60}\n'.format(' '*8, medium, time, distance,''))
    return None


# Call main program
main()