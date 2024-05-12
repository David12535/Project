import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice: ")

        result = roll_dice()
        print(f"You rolled: {result}")

        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
------------------------------------------------------------------------
import random

def choose_word():
    words = ["cheese", "cheesburger", "burger", "hot dog", "watermelon", "kiwi", "carrot"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to Hangman!")

    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while True:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")
            if attempts == 0:
                print("You've run out of attempts! The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break

if __name__ == "__main__":
    main()
..