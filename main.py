#This is a program that allows two users to play a basic hangman game

print("Welcome to Hangman game!")

#The program should prompt user 1 at the beginning for the word and number of guesses.

word = input("Player 1 please enter a word: ")
num = int(input("Player 1 please enter the # of guesses: "))

currentguess = []
for i in range(len(word)):
    currentguess.append("_")
wordList = list(word)

#The program should prompt user 2 to enter a letter

while num != 0 and "_" in currentguess:
    strGuess = "".join(currentguess)
    print("WORD: " + strGuess + "\n" + "GUESSES LEFT: " + str(num))
    num = num - 1
    guess = input("Player 2 please enter a letter: ")

    if len(guess) != 1 or guess in currentguess:
        print("Invalid Input")

    good_guess = False

    if guess in word:
        good_guess = True

    if not good_guess:
        num = num - 1
        print("Incorrect. Letter is not in the word")
    else:
        print("Correct!")
        for index in range(len(wordList)):
            if guess == wordList[index]:
                currentguess[index] = guess

if num == 0 and "_" in currentguess:
    print("You Lost")
if "_" not in currentguess:
    print("You Won!!!")

