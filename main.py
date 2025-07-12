from rich import print
import platform
import os

number_of_tries = 0
guess = ""
try_counter = 1
word = ""
wrong_letters = set()
correct_letters = []


def settings():
    global number_of_tries
    global guess
    global try_counter
    global word
    number_of_tries = 0
    guess = ""
    try_counter = 1
    word = ""
    wrong_letters.clear()
    correct_letters.clear()
    print("[|] Enter the word: ", end="")
    word = input()
    # print(f"[–] [bold blue]{word} ({len(word)})[/bold blue]")
    for placeholder in range(len(word)):
        correct_letters.append("_")
    print("Clear Screen? [[bold green]Y[/bold green]/[bold red]n[/bold red]] ", end="")
    clear_screen = input()
    if clear_screen.lower() == "n":
        pass
    else:
        if platform.system().lower() == "linux" or "darwin":
            os.system("clear")
        elif platform.system().lower == "windows":
            os.system("cls")
        else:
            try:
                os.system("clear")
            except:
                os.system("cls")

    print("[|] How many tries?: ", end="")

    while number_of_tries <= 1:
        try:
            number_of_tries = int(input())
            break
        except:
            print("[bold red]Enter a Valid Number[/bold red]")
            print("[bold red][|] How many tries?:[/bold red] ", end="")
    # print(f"[–] [bold blue]{number_of_tries}[/bold blue]")


def hanger(guess, word):
    guess_letters = set()
    for letter in guess:
        guess_letters.add(letter)

    word_letters = []
    for letter in word:
        word_letters.append(letter)

    for letter in guess_letters:
        if letter in word_letters:
            correct_letters.pop(word_letters.index(letter))
            correct_letters.insert(word_letters.index(letter), letter)
        else:
            wrong_letters.add(letter)


def game():
    global number_of_tries
    global guess
    global try_counter
    global word

    settings()
    while try_counter <= number_of_tries:
        print(f"[{try_counter}/{number_of_tries}] Guess the word! ", end="")
        guess = input()

        if guess.lower() != word.lower() and try_counter + 1 > number_of_tries:
            try_counter += 1
            print("[-][bold red] You Lost[/bold red]")
            print(
                "[|] Do you want to play again? [[bold green]Y[/bold green]/[bold red]n[/bold red]] ",
                end="",
            )
            want_to_play = input()
            if want_to_play.lower() == "y":
                game()
            else:
                break

        elif guess.lower() != word.lower():
            hanger(guess, word)
            print(f"[bold red]{wrong_letters}[/bold red]")
            print(f"[bold green]{correct_letters}[/bold green]")

            try_counter += 1
        else:
            print("[-][bold green] You Won![/bold green]")
            print(
                "[|] Do you want to play again? [[bold green]Y[/bold green]/[bold red]n[/bold red]] ",
                end="",
            )
            want_to_play = input()
            if want_to_play.lower() == "n":
                break
            else:
                game()


game()
