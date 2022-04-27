#########################################
# Description: Menu configuration - all visual menues generated here
# Team: Matthew Stroble and Hannah Reinbolt
# Date: 4-24-2022
#
# ascii art words (font=Small): https://patorjk.com/software/taag/#p=display&f=Small&t=Automatic%20Encryption%20Breaker%20 
# ascii art key1: https://ascii.co.uk/art/key
# ascii art key2: https://textart.sh/topic/key
#########################################

# libraries
import os
import time


# welcome menu
def welcome_menu():
    # variables
    bar = """##################################################################################################################################"""
    authors = "By Matthew Stroble and Hannah Reinbolt"
    date = "4.24.2022 - Auburn University"
    title = """    _       _                  _   _      ___                       _   _            ___              _            
   /_\ _  _| |_ ___ _ __  __ _| |_(_)__  | __|_ _  __ _ _ _  _ _ __| |_(_)___ _ _   | _ )_ _ ___ __ _| |_____ _ _  
  / _ \ || |  _/ _ \ '  \/ _` |  _| / _| | _|| ' \/ _| '_| || | '_ \  _| / _ \ ' \  | _ \ '_/ -_) _` | / / -_) '_| 
 /_/ \_\_,_|\__\___/_|_|_\__,_|\__|_\__| |___|_||_\__|_|  \_, | .__/\__|_\___/_||_| |___/_| \___\__,_|_\_\___|_|   
                                                          |__/|_|                                                  """
    keys = """
           ___________ @ @
          /         (@\   @
          \___________/  _@
                    @  _/@ \_____
                     @/ \__/-="="`
                      \_ /
                       <|
                       <|
                       <|
                       `"""

    keys2 = """                                                                           
                                                                                        
                                ██████████████████████                                  
                              ████                  ████                                
                              ██    ░░░░░░░░░░░░░░  ░░██                                
                              ██    ░░██████████    ░░██                                
                              ██    ░░██▓▓▓▓▓▓██    ░░██                                
                              ██    ░░██████████    ░░██                                
                              ██                    ░░██                                
                              ████░░░░░░░░░░░░░░░░░░████                                
                                ██████████████████████                                  
                                      ██    ░░██                                        
                                      ██    ░░████████                                  
                                      ██    ░░██    ██                                  
                                      ██    ░░████████                                  
                                      ██    ░░██    ██                                  
                                      ██░░░░░░██░░░░██                                  
                                      ████████████████                                  
                                                                                                                                                                
    """

    # initial welcome menu
    os.system("clear")
    print(bar)
    print(title)
    print(keys)
    print(bar)
    print(authors)
    print(date)
    print(bar)


# main menu printout
# options:
# 1 = initial welcome
# 2 = end program
# 3 = custom multi-choice menu
# 4 = custom single-choice menu
# 5 = custom error menu
# var option: int, menu option
# var status: str, program status
# var choices: list of str, descriptive menu choices
def main_menu_printout(option, status, choices):
    # variables

    goodbye = """   ___              _ _               _ 
  / __|___  ___  __| | |__ _  _ ___  | |
 | (_ / _ \/ _ \/ _` | '_ \ || / -_) |_|
  \___\___/\___/\__,_|_.__/\_, \___| (_)
                           |__/         """


    # end program menu
    if option == 2:
        # clear and setup
        welcome_menu()
        
        # menu
        print("STATUS: "+str(status))
        print("Thank you for using Automatic Encryption Breaker!!")
        print(goodbye)
        print("\n")

    # custom multi-choice menu
    if option == 3:
        # clear and setup
        welcome_menu()

        # menu
        print("STATUS: " + str(status))
        print("Please choose a menu option:")
        count = 1
        
        for choice in choices:
            print(str(count) + ": " + str(choice))
            count += 1
        print("\n")


    # custom single-choice menu
    if option == 4:
        # clear and setup
        welcome_menu()

        # menu
        print("STATUS: " + str(status))
        print(str(choices[0]))
        print("\n")


    # custom error menu
    if option == 5:
        # clear and setup
        welcome_menu()

        # menu
        print("STATUS: " + str(status))
        print(str(choices[0]))
        print("\n")
        time.sleep(2)



