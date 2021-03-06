#########################################################
# Description: Program Logic, where everything is put together and called, menues and crackers
# Team: Matthew Stroble and Hannah Reinbolt
# Date: 4-24-2022
#
#########################################################

# libraries
import menu.menu as mm
import decryptor.shift.shift_decrypt as ds
import fingerprinting.fingerprint as ff
import os

#################################################################
# step 1: start program and request file
def step_1():
    # variables
    usr_input = ""

    # starting menu
    mm.main_menu_printout(3,"waiting for input.",
            ["enter file location for encrypted plaintext file",
            "end program"])
    usr_input = input(">>")

    # end program
    if (usr_input == '2'):
        mm.main_menu_printout(2, "shutting down...", [""])
        exit(1)

    # get location of file
    elif (usr_input == '1'):
        mm.main_menu_printout(4, "waiting for input.", ["Please enter location of file below."])
        usr_input = input(">>")

        # check if file is valid
        if (os.path.exists(usr_input) == True):
            return [True, usr_input]

        # file is invalid
        else:
            mm.main_menu_printout(5, "error: could not open file", ["Incorrect file location. Please try again."])
            return [False, '']

    # error in input
    else:
        mm.main_menu_printout(5, "error: incorrect input", ["Incorrect input. Please try again."])

    # catchall
    return [False, '']
#####################################################################


#####################################################################
# step 2: start fingerprinting and return results
def step_2(file_path):
    # variables
    usr_input = ""

    # menu
    mm.main_menu_printout(4, "ready to start fingerprinting", ['Successfully loaded file. Press Enter to start the fingerprinting process.'])
    usr_input = input(">>")

    # matthews fingerprinting functionality here
    # perform frequency analysis
    choice = ff.startAnalysis(file_path)
    
    # menu
    mm.main_menu_printout(4, "finished fingerprinting", ['Successfully detected cipher type. Cipher detected is "' + str(choice) + '" cipher. Press Enter to continue.'])
    usr_input = input(">>")


    # catchall
    return [True, choice]
####################################################################


####################################################################
# step 3: choose decryption method and start decryption
def step_3(file_path, best_guess):
    # variables
    usr_input = ""

    # choose decryption method
    mm.main_menu_printout(3, "successfully fingerprinted file. ready to decrypt file.", 
            ["automatic guess decryption",
             "shift cypher decryption",
             "substitution cypher decryption",
             "end program"])
    usr_input = input(">>")

    # end program
    if (usr_input == '4'):
        mm.main_menu_printout(2, "shutting down...", [''])
        exit(1)

    # shift cypher decryption
    elif ((usr_input == '2') or ((usr_input == '1') and (best_guess == 'shift'))):
        mm.main_menu_printout(4, "ready to start decryption", ["Press Enter to start shift cypher brute force decryption."])
        usr_input = input(">>")

        # enter shift cypher decryption here
        ds.decrypt_shift(file_path)
        mm.main_menu_printout(4, "finished decrypting", ["Sucesssfully decrypted shift cipher. Press Enter to continue to results."])
        usr_input = input(">>")

    # substitution cypher decryption
    elif ((usr_input == '3') or ((usr_input == '1') and (best_guess == 'substitution'))):
        mm.main_menu_printout(4, "ready to start decryption", ["Press Enter to start substitution cypher brute force decryption."])
        usr_input = input(">>")

        # enter substitution cypher decryption here
        cmd = "python3 decryptor/substitution/betterSubCrack.py " + file_path + " results/solution.txt"
        os.system(cmd)
        os.system("cp results/solution.txt results/best_guess.txt")
        mm.main_menu_printout(4, "finished decrypting", ["Successfully decrypted substitution cipher. Press Enter to continue to results."])
        usr_input = input(">>")

    # error
    else:
        mm.main_menu_printout(5, "error: incorrect input", ['Incorrect input. Please try again.'])
        return [False, '']

    # catchall
    return [True, '']
##############################################################################


##############################################################################
# step 4: return results for decryption method
def step_4(msg, key):
    # variables
    result = """Decryption Results:
        
        ALL results are located in /results/solution.txt
        BEST GUESS results are located in /results/best_guess.txt

        Note:
        - Brute force solutions will contain all brute force attempts in solution.txt but only a single best guess will be in best_guess.txt
        - Frequency analysis solutions will only have the best solution located in solution.txt and best_guess.txt. All other guesses will not be noted. 

        Please press Enter to continue to main menu. """

    # menu
    mm.main_menu_printout(4, "finished decryption", [result])
    usr_input = input(">>")

    return [True, '']







