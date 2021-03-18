import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist)
lettersGuessed = []


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True        
                
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    new = ""
    for letter in secretWord:
        if letter not in lettersGuessed:
            new += "_ "
        else:
            new += letter + " "
    return new



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc = string.ascii_lowercase
    for letter in lettersGuessed:
        abc = abc.replace(letter,"")# FILL IN YOUR CODE HERE...
    return abc


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    secretWord = chooseWord(wordlist)
    print("Vamos a jugar al AHORCADO")
    print("Estoy pensando en una palabra de", len(secretWord), "letras" )
    counter = 8
    print(f"Tienes {counter} intentos")
    lettersGuessed = []
    print(getGuessedWord(secretWord, lettersGuessed))
    while counter > 0:
        print("Las letras disponibles son:", getAvailableLetters(lettersGuessed))
        intento = input("Elige una letra:").lower()
        if len(intento) != 1 or intento not in string.ascii_lowercase:
            print("Elige UNA letra")
        elif intento in lettersGuessed:
            print("Ya has dicho esa letra")
        else:
            lettersGuessed += intento
            if intento in secretWord:
                print("¡Bien!")
                print(getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print("Has ganado! Vivirás por un tiempo mas")
                    break
            else:
                counter -= 1
                if counter == 4:
                    print("La soga se ajusta sobre tu cuello")
                elif counter == 3:
                    print("Ya te cuesta respirar")
                elif counter == 2:
                    print("Piensa en tus últimas palabras")
                elif counter == 1:
                    print("Estás al borde de la muerte")
                else:
                    print("Mala decisión")
                print(f"Te quedan {counter} intentos")
    if counter == 0:            
        print("")
        print("Has sido ahorcado")
        print("La palabra era", secretWord)



