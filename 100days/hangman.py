# hangman

word1 = "hidden"

def play(hiddenWord):
    # setup board
    revealedWord = "_" * len(hiddenWord)
    revealedArr = list(revealedWord)

    guessesLeft = 10
    # guessesMade = [] # option to save string of letters that have been used already

    # take user input
    while guessesLeft > 0:
        print("loop")
        print("revealedArr", revealedArr)
        guess = input()
        # print("guess", guess)
        print(f"let's see if there are any {guess}'s...")
        
        # check input and update board
        found = False 
        for i in range(len(hiddenWord)):
            if guess == hiddenWord[i]:
                revealedArr[i] = guess
                found = True
        if not found: # if found != True:
            guessesLeft -= 1
            print("guesses left", guessesLeft)

        # check game status
        if "_" not in revealedArr:
            print("YOU WIN!!!")
            return

                
            


play(word1)



# ============== Pythonic Terminal Hangman ===================
# def play(word: str, max_guesses: int = 10) -> None:
#     revealed = ["_"] * len(word)
#     guesses_left = max_guesses
#     guessed_letters = set()

#     while guesses_left > 0:
#         print("\nWord:", " ".join(revealed))
#         print("Guesses left:", guesses_left)
#         print("Guessed letters:", ", ".join(sorted(guessed_letters)))

#         guess = input("Guess a letter: ").lower()

#         # --- input validation ---
#         if len(guess) != 1 or not guess.isalpha():
#             print("Please enter a single letter.")
#             continue

#         if guess in guessed_letters:
#             print("You already guessed that letter.")
#             continue

#         guessed_letters.add(guess)

#         # --- game logic ---
#         if guess in word:
#             for i, letter in enumerate(word):
#                 if letter == guess:
#                     revealed[i] = guess
#         else:
#             guesses_left -= 1
#             print("Nope!")

#         # --- win condition ---
#         if "_" not in revealed:
#             print("\n🎉 You win!")
#             print("The word was:", word)
#             return

#     # --- loss condition ---
#     print("\n💀 Game over!")
#     print("The word was:", word)
