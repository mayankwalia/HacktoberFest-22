import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()

ans = choose_word(wordlist)
l = len(ans)
guessLeft = 10
userString = '_'*l

print 'Welcome to the game, Hangman !'
print 'I am thinking of a word that is', l, 'letter long'
print '-'*l
print 'You have', guessLeft, 'guesses left'

# function for finding all indices of a charachter in a string
def find_all_index(string, charachter):
    """Takes input as a string and searches for the required charachter in it.
Then returns a list containing all the indices of the charachter appearing in the string.
Returns  a [-1] when charachter is not found in the string"""
    for letter in string: 
            return [i for i,letter in enumerate(string) if letter == charachter]
        
# the game loop    
while ans != userString and guessLeft > 0:
    guessLetter = raw_input('Please guess a letter: ')
    if guessLetter in ans:
        for x in find_all_index(ans, guessLetter):
            userString = userString[:x]+ guessLetter + userString[x+1:] 
        print 'Good Guess:', userString
        print 'You have', guessLeft, 'guesses left'
    else: 
        if guessLetter not in ans:
            print 'Oops! that letter is not in my word: ',userString
            guessLeft -= 1
            print 'You have', guessLeft, 'guesses left'


if ans == userString:
    print'Congratulations! You Won'
    print'Your score', guessLeft*10
    name = raw_input('Enter Your Name: ')
    print name,'copied to Leader Board'

else:
    print'Alas You Lost'
    print'The correct answer is', ans
    print'Your score is 00'




