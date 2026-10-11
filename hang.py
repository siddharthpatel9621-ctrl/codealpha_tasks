import random

words = ["python", "apple", "mango", "school", "hangman"]
word = random.choice(words).lower()

guesses = 0
wrong_guesses = 0
max_wrong = 6

guessed = ["_"] * len(word)
used_letters = []

print("====== Hangman Game ======")

while wrong_guesses < max_wrong and "_" in guessed:

    print("\nWord:", " ".join(guessed))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)
    print("Used letters:", used_letters)

    letter = input("Enter a letter: ").lower()

    if letter in used_letters:
        print("You already guessed this letter.")
        continue

    used_letters.append(letter)
    guesses += 1

    if letter in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter

    else:
        print("Wrong guess!")
        wrong_guesses += 1

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)

print("Total guesses:", guesses)