from hangman_art import stages, logo
from hangman_words import word_list
import random
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
guessed_letters = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You already gussed {guess}")
    guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(
            f'You guessed {guess}, that is not in the word. You lose a life. Lives left: {lives}'
        )
        if lives == 0:
            end_of_game = True
            print("\n\nYou lose.")

    print(f"\n\n{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\n\nYou win!")

    print(stages[lives])
