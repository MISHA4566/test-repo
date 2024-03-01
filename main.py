import random


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display


def main():
    words = ["apple", "orange", "banana"]
    word = random.choice(words)
    attempts = int(input("Введість кількість спроб: "))
    guessed_letters = []

    while attempts > 0:
        print("\nСлово: ", display_word(word, guessed_letters))
        guess = input("Введіть літеру або слово: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("Така літера є в цьому слові !")
            elif guess in word:
                print("Такої літери немає!")
                guessed_letters.append(guess)
            else:
                print("Такої літери немає.")
                attempts -= 1
        else:
            if guess == word:
                print("Вітаємо!!!")
                break
            else:
                print("Неправильне слово!")

        attempts -= 1

        if attempts == 0:
            print("Ви програли. Спроби закінчилися. Слово було загадано:", word)


main()
