# WORDLE GAME
import fontstyle
import random  # Used to generate a random number which is used to select key

print(" " * 50, fontstyle.apply("WELCOME TO WORDLE", "BOLD/BLACK/GREEN_BG"))
print(fontstyle.apply("RULES:", "BOLD"))
print(
    "1.The player has to guess the Wordle in six attempts or less.\n2.Every word, which is entered should be in the word list.\n3.If the letter is correct, the color would turn green.\n4.If the letter is correct but placed wrong then it would turn yellow.\n5.An incorrect letter turns gray.\n6.Letters can be used more than one time.")


def read_word_list(file_path):  # To read the file containing the wordlist
    word_list = []

    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Split the content into a list of words
    word_list = content.split()

    return word_list


file_path = 'wordleinput.txt'
words = read_word_list(file_path)


def random_word():
    # This function chooses a random word from the list words
    x = random.randint(0, 2309)
    key_word = words[x]
    return key_word


def listToString(s):
    # This function is used to convert a given list to a string

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


key = random_word().upper()  # Used to store the key


def word_in_engdict(word):
    # This function is used to check if the guess exists in the word list
    return word.lower() in words


i = 0
# This block is for inputing the user's guesses
while i < 6:
    guess = input("enter your guess: ").upper()
    if len(guess) == 5:
        if word_in_engdict(guess):  # Checks if guess is in words
            i += 1
            guess1 = list(guess)  # Storing guess in the form of a list
            key1 = list(key)  # Storing key in the form of a list
            if guess == key:  # Checks if the guess is correct
                print(fontstyle.apply(guess.upper(), "BOLD/GREEN_BG"))
                print(fontstyle.apply("!!!!!YOU WON!!!!!", "BOLD/GREEN"))
                exit()
            else:
                for x in range(5):
                    if guess1[x] == key1[x]:  # Checks if the letter is in the key and in correct position
                        guess1[x] = fontstyle.apply(guess1[x].upper(), "green_bg")
                        key1[x] = ''  # Removing letter from the key

                for x in range(5):
                    if guess1[x] in key1:  # Checks if letter is in key
                        guess1[x] = fontstyle.apply(guess1[x].upper(), "yellow_bg")
                        key1[key1.index(guess[x])] = ''  # Removing letter from the key

                print(listToString(guess1))  # Converts guess1 to a string and prints it
        else:
            print('Word not found!!!')
    else:
        print("enter only 5 letters")
print('You ran out of guesses')
print('Word is:', key)
