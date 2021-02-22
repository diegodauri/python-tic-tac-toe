import time
print("Welcome to tic tac toe!")

values = [' ' for x in range(9)]

win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

is_on = True


def print_board():
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


def choosex():
    positionx = input("Player X chose one cell 1-9: ")

    if values[int(positionx) - 1] == " ":

        values[int(positionx) - 1] = "X"
    else:
        print("Cell is occupied, try again!")
        choosex()


def choosey():
    positiony = input("Player O chose one cell 1-9: ")

    if values[int(positiony) - 1] == " ":

        values[int(positiony) - 1] = "O"
    else:
        print("Cell is occupied, try again!")
        choosey()


def check_win():
    for combination in win_combinations:
        if values[combination[0] - 1] == "X" and values[combination[1] - 1] == "X" and values[combination[2] - 1] == "X" or values[combination[0] - 1] == "O" and values[combination[1] - 1] == "O" and values[combination[2] - 1] == "O":
            global is_on
            is_on = False
            sign = values[combination[0] - 1]
            print(f"Player {sign} win!")
            time.sleep(1)
            print_board()


time.sleep(1)

while is_on:
    print_board()

    choosex()

    check_win()

    print_board()

    choosey()

    check_win()


