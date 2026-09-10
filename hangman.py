import random

# List of predefined words
words = ["python", "computer", "programming", "keyboard", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_wrong_guesses = 6
wrong_guesses = 0

# Display the hidden word
display_word = ["_"] * len(word)

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)

print("\nGuess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add letter to guessed letters
    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:

        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:

        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in display_word:

    print("\n" + "=" * 40)
    print("🎉 CONGRATULATIONS!")
    print("You guessed the word:", word)
    print("You won the game!")
    print("=" * 40)

else:

    print("\n" + "=" * 40)
    print("GAME OVER!")
    print("The correct word was:", word)
    print("Better luck next time!")
    print("=" * 40)