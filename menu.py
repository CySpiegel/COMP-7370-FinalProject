#########################################
# Description: Menu configuration - all visual menues generated here
# Team: Matthew Stroble and Hannah Reinbolt
# Date: 4-24-2022
#
# ascii art words (font=Small): https://patorjk.com/software/taag/#p=display&f=Small&t=Automatic%20Encryption%20Breaker%20 
# ascii art key: https://ascii.co.uk/art/key
#########################################

# libraries
import os
import time

# main menu
def main_menu():
    # variables
    end = False
    usr_input = ""

    # step 1: choose file
    while (end != True):

        # do step 1
        cmd = step_1()
        end = cmd[0]

    # step 2: fingerprint file
    #end = False
    #while (end != True):




        


    # end menu
    return None


# step 1: choose file
def step_1():
    # start program
    main_menu_printout(2)
    usr_input = input()

    # quit program
    if usr_input == 2:
        main_menu_printout(4)

    # choose file for decryption
    elif usr_input == 1:
        main_menu_printout(6)
        usr_input = input()

        # check if path is valid
        try:
            open(usr_input, 'w').close()
            os.unlink(usr_input)
            return [True,usr_input]

        # invalid path
        except OSError:
            main_menu_printout(5)

    # bad input
    else:
        main_menu_printout(5)

    # continue cycle
    return [False,""]


# main menu printout
# options: 
# 1 = initial welcome
# 2 = pre-solve choices
# 3 = post-solve choices
# 4 = end program
# 5 = bad input
# 6 = enter file path
# 7 = solving
def main_menu_printout(choose_menu):
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
    goodbye = """   ___              _ _               _ 
  / __|___  ___  __| | |__ _  _ ___  | |
 | (_ / _ \/ _ \/ _` | '_ \ || / -_) |_|
  \___\___/\___/\__,_|_.__/\_, \___| (_)
                           |__/         """


    # first welcome menu
    if choose_menu == 1:
        print(bar)
        print(title)
        print(keys)
        print(bar)
        print(authors)
        print(date)
        print(bar)

    # pre-solve menu
    if choose_menu == 2:
        # clear screen
        os.system("clear")
        # re-add menu
        main_menu_printout(1)
        
        # menu
        print("STATUS: Waiting for input.")
        print("Please choose a menu option:")
        print("1: enter path to encrypted plaintext file")
        print("2: quit program")
        print("\n\n")
        print(">> ")

    # post-solve menu
    if choose_menu == 3:
        # clear screen
        os.system("clear")
        # re-add menu
        main_menu_printout(1)

        # menu
        print("STATUS: File successfully solved.")
        print("Please choose a menu option:")
        print("3: see recommended solution and key (if any)")
        print("4: see all solutions and keys")
        print("5: solve a new encrypted file")
        print("6: quit program")
        print("\n\n")
        print(">> ")

    # end program menu
    if choose_menu == 4:
        # clear screen
        os.system("clear")
        # re-add menu
        main_menu_printout(1)

        # menu
        print("STATUS: Shutting down.")
        print("Thank you for using Automatic Encryption Breaker!!")
        print(goodbye)
        print("\n\n")

    # bad input menu
    if choose_menu == 5:
        # clear screen
        os.system("clear")
        # re-add menu
        main_menu_printout(1)

        # menu
        print("STATUS: Bad input")
        print("Please try again.")
        print("\n\n")
        time.sleep(1)

    # choose file menu
    if choose_menu == 6:
        # clear screen
        os.system("clear")
        # re-add menu
        main_menu_printout(1)

        # menu
        print("STATUS: Waiting for input.")
        print("Please enter file path.")
        print(">> ")


main_menu()

