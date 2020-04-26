from random import choice


def check_letter(letter, word, guess_word):
    for i in word:
        if i == letter:
            guess_word[word.index(i)] = i
            word[word.index(i)] = '*'
    return guess_word


used = []
tries = 1
comp_lan = ['python', 'java', 'kotlin', 'javascript']
selection = list(choice(comp_lan))
hidden = ['-' for x in selection]
print('H A N G M A N')
while True:
    action = input('Type "play" to play the game, "exit" to quit:')
    if action == 'play':
        print('')
        print(''.join(map(str, hidden)))
        while tries <= 8:
            if selection.count('*') != len(selection):
                letter_guess = input('Input a letter:')
                if len(letter_guess) != 1:
                    print('You should print a single letter')
                    print('')
                    print(''.join(map(str, hidden)))
                elif letter_guess.islower():
                    if letter_guess in selection:
                        used.append(letter_guess)
                        check_letter(letter_guess, selection, hidden)
                        print('')
                        print(''.join(map(str, hidden)))
                    elif letter_guess not in selection:
                        if letter_guess in used:
                            print('You already typed this letter')
                            print('')
                            print(''.join(map(str, hidden)))

                        else:
                            if tries == 8:
                                print('No such letter in the word')
                                print('You are hanged!')
                                break
                            elif tries < 8:
                                used.append(letter_guess)
                                print('No such letter in the word')
                                print('')
                                print(''.join(map(str, hidden)))
                                tries += 1
                else:
                    print('It is not an ASCII lowercase letter')
                    print('')
                    print(''.join(map(str, hidden)))
            else:
                hid = ''.join(map(str, hidden))
                print(f'You guessed the word {hid}!')
                print('You survived!')
                break
    if action == 'exit':
        break
