from os import system, name

print("Welcome to hangman! \n")

secwrd = input("First, someone has to choose a word: ").upper()

print("\nNow, the rest of the persons have to guess the word")
print("The word has " + str(len(secwrd)) + " characters\n")
counter = 6
underscores = '_' * len(secwrd)
display = underscores
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def clear():
    if name == 'nt':
        _ = system('cls')


def draw(c):
    if c == 6:
        print(HANGMANPICS[0])
    if c == 5:
        print(HANGMANPICS[1])
    if c == 4:
        print(HANGMANPICS[2])
    if c == 3:
        print(HANGMANPICS[3])
    if c == 2:
        print(HANGMANPICS[4])
    if c == 1:
        print(HANGMANPICS[5])
    if c == 0:
        print(HANGMANPICS[6])

def guess():

    guessed_letters = []
    guessed = False
    global counter
    global underscores
    global display
    global secwrd

    if counter > 0 and guessed == False:
        letter = input("\nSay a letter, if the letter is not inside the word, you lose a life: ").upper()
        if not letter.isalpha():
            print("[!] Invalid character")
            guess()
        else:
            if letter in secwrd and len(letter) == 1 and guessed == False:
                display_as_list = list(display)
                indices = [i for i, ltter in enumerate(secwrd) if ltter == letter]
                for index in indices:
                    display_as_list[index] = letter
                display = "".join(display_as_list)
                clear()
                draw(counter)
                print(display)

                if display == secwrd:
                    clear()
                    print("Nice, You won!, the correct word was " + secwrd)
                    guessed = True


            elif letter not in secwrd:
                clear()
                print("\nThe letter wasn't in the word, you lost a life!")
                counter -= 1
                draw(counter)
                print(display)
                print("\nYou have " + str(counter) + " lifes left")

            elif len(letter) > 1:
                if letter == secwrd:
                    clear()
                    print("Nice, You won!, the correct word was " + secwrd)
                    guessed = True

                else:
                    clear()
                    print('The word you wrote is incorrect! You lost a life')
                    counter -= 1
                    draw(counter)
                    guess()
            guess()
    elif guessed == True:
        clear()
        print('You guessed the word after ' + str((5 - counter)) + ' attempts')


    else:
        clear()
        print('You ran out of lifes! Game restarts')

guess()
