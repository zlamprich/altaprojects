import os
import pyfiglet
from os import system  # for windows


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def quiz():
    correct_answers = 0
    question_val = 1
    guesses = []

    for key in questions:
        print("===================================")
        print(key)
        for i in answerbank[question_val - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D)")
        guess = guess.upper()
        guesses.append(guess)

        correct_answers += checkans(questions.get(key), guess)
        question_val += 1

    getscore(correct_answers, guesses)


def checkans(answer, guess):
    if answer == guess:
        print("THAT IS CORRECT! ONE POINT ADDED TO SCORE")
        return 1
    else:
        print("INCORRECT! NO POINTS GIVEN")
        return 0


def getscore(correct_answers, guesses):
    cls()
    print("")
    print("-------YOUR RESULTS ARE-------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_answers/len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


def reset_game():
    resp = input("Play again? y/n")
    resp = resp.lower()

    if resp == "y" or "Y":
        return True
    else:
        return False


questions = {
    "What Nintendo franchise is the popular character Link a part of?": "C",
    "In the Resident Evil franchise, what virus causes the zombie outbreak in Raccoon City?": "B",
    "In Super Mario Brothers, the main character Mario has the PRIMARY profession of what?": "A",
    "In the Metroid seris, what is the protagonist\'s actual name?": "B",
    "In the game Elden Ring, what is the player character called by NPCs?": "C",
    "Grand Theft Auto III is set in what fictional city?": "A",
    "The original Super Mario Brothers game for the NES featured what other Nintendo character as Mario's nemesis?": "B",
    "In the Warcraft universe, the Lich King was originally a Paladin named what?": "A",
    "The primary character in the original Half-Life series is a scientist named Dr. Gordon what?": "C",
    "Solid Snake is the hero of what franchise?": "B"
}

answerbank = [["A. Donkey Kong", "B. Metroid", "C. Legend of Zelda", "D. Super Smash Brothers"],
              ["A. G Virus", "B. T Virus", "C. D Virus", "D. Zombie Virus"],
              ["A. Plumber", "B. Carpenter", "C. Doctor", "D. Luigis Brother"],
              ["A. Metroid", "B. Samus", "C. Sam", "D. Ellie"],
              ["A. Chosen Undead", "B. Steve", "C. Tarnished", "D. Sekiro"],
              ["A. Liberty City", "B. Vice City",
                  "C. San Andreas", "D. Los Santos"],
              ["A. Link", "B. Donkey Kong", "C. Bowser", "D. The Hammer Bros"],
              ["A. Arthas", "B. Ner'zhul", "C. Uther", "D. Varian"],
              ["A. Smith", "B. Johnson", "C. Freeman", "D. Gonzalez"],
              ["A. Hitman", "B. Metal Gear Solid",
                  "C. Call of Duty", "D. Backyard Baseball"]
              ]

result = pyfiglet.figlet_format("WELCOME TO GAME TRIVIA")
print(result)
input("Press Enter to Continue")


def console():
    print("\nWelcome to GAME TRIVIA\n" +
          "The goal of GAME TRIVIA is to correctly answer as many trivia questions as possible\n" + "\nAll trivia questions will reference popular video games\n" +
          "You only have 3 lives, and an incorrect answer will remove one! After 3 incorrect guesses your game will end. Choose wisely, and good luck!\n")


console()

input("PRESS ANY KEY TO BEGIN GAME")
quiz()


while reset_game():
    quiz()
