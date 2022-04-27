###################################
# Description: Main Functionality - Main program runs here
# Team: Matthew Stroble and Hannah Reinbolt
# Date: 4-24-2022
#
# How to Run:
# >> python3 main.py
###################################

# libraries
import menu.program_logic as lc

# main menu cycle
def crack():
    # variables
    end = False
    file_path = ""
    result = []

    # step 1: start program and request file
    while (end != True):

        result = lc.step_1()
        end = result[0]

    # step 2: start fingerprinting and return results
    end = False
    while (end != True):
        file_path = result[1]
        result = lc.step_2(file_path)
        end = result[0]

    # step 3: choose decryption method and start decryption
    end = False
    while (end != True):
        result = lc.step_3(file_path, result[1])
        end = result[0]

    # step 4: return results for decryption method
    end = False
    while (end != True):
        result = lc.step_4("msg", "key")
        end = result[0]

    # end program
    return None


# main menu
def main():

    # user prompts program quit
    while(True):
        crack()

    return None

# run main program
main()





