##############################################################
# Definition: Perform best guess on cipher data
# Team: Matthew Stroble and Hannah Reinbolt
# Date: 4-24-2022
##############################################################

# libraries
from english_words import english_words_set


# check how many english words are in a file
def is_word(word):

    if word in english_words_set:
        return True
    else:
        return False

# count english words
def count_words(text, key, word_dict):
    # variables
    text = text.lower()
    words = text.split(" ")
    count = 0

    # count words
    for word in words:
        if is_word(word) == True:
            count += 1

    # store count
    word_dict[count] = [key, text]
    return word_dict


# calculate best guess
def calc_best_guess(word_dict):
    # put keys in a list
    key_list = []
    for key in  word_dict.keys():
        key_list.append(key)

    # find highest number
    key_list.sort()
    best_key = key_list[-1]
    return [word_dict[best_key][0], word_dict[best_key][1]]

