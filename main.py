from hangman_states import lives, game_name
from country_dict import guess_list
import random


def play_game():
    variable_for_user = ""
    counter = 0
    counter_letter = 6
    random_choice_by_computer = random.choice(guess_list)
    print("Welcome to HangMan!!")
    print("Guess the European Country")
    print("You get 6 tries to identify the word. Let's start the game!!")
    print("The country has " + str(len(random_choice_by_computer)) + " letters.")
    while True:
        take_input_letter = input("Guess the letter: ")
        if counter == 0:
            variable_for_user = "_" * len(random_choice_by_computer)
        list_var = list(variable_for_user)
        for j, letter in enumerate(random_choice_by_computer):
            if letter == take_input_letter:
                list_var[j] = take_input_letter
                variable_for_user = "".join(list_var)
            elif letter.swapcase() == take_input_letter:
                list_var[j] = take_input_letter.swapcase()
                variable_for_user = "".join(list_var)
        if take_input_letter not in random_choice_by_computer and take_input_letter.swapcase() not in random_choice_by_computer:
            if counter_letter == 0:
                print(lives[counter_letter])
                print("You have no more tries left")
                print("You have failed")
                print("The item is {}".format(random_choice_by_computer))
                break
            print(lives[counter_letter])
            print("You have {} more tries left".format(counter_letter))
            counter_letter -= 1
        if variable_for_user == random_choice_by_computer:
            print(variable_for_user)
            print(game_name)
            print("Congratulations!! You found the country")
            break
        print(variable_for_user)
        counter += 1


if __name__ == '__main__':
    play_game()
