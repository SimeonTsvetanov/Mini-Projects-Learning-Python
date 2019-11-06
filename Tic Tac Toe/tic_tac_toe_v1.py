tic_tac_toe = [
    ["| |", "| |", "| |"],
    ["| |", "| |", "| |"],
    ["| |", "| |", "| |"],
]

current_move = 0
player = ""
current_position = ""


def print_chess():
    global player
    next_player = 2
    next_sign = "0"
    if player == "X":
        next_player = 2
        next_sign = "0"
    elif player == "O":
        next_player = 1
        next_sign = "X"
    line_number = 1
    print(90*"-")
    print(f"Current Game State:")
    print("   A   B   C ")
    for line in tic_tac_toe:
        print(line_number, end=" ")
        print(*line)
        line_number += 1
    print(90 * "-")
    print(f"It's time for Player-{next_player} to place their sign: '{next_sign}'.")


def start():
    print(90*"-"+"\n"+90*"-")
    print("Hello :) You are about to play a game of Tic Tac Toe")
    print("You will need a second player for this game as I can't do AI for now:D.")
    print("The first player will be: 'X' and the second 'O'")
    print("Rules are pretty simple Just enter the Column A, B ot C followed by the row 1, 2 or 3:")
    print("Example : A1 or 2B or C2")
    print("And hit Enter!")
    print("------------------------EXAMPLE-----------------------")
    print(f"   A   B   C                               A   B   C ")
    print(f"1 | | | | | |   --> IF YOU ENTER: -->   1 | | | | | |")
    print(f"2 | | | | | |   -->      B2       -->   2 | | |X| | |")
    print(f"3 | | | | | |   --> YOU WILL GET  -->   3 | | | | | |")
    print(54 * "-")
    print("OR ENTER 'game' to check your game, 'help' to see this menu again or 'end' to exit.")
    get_input()


def clean_screen():
    print(25*"\n")


def get_input():
    global current_position, player
    if current_move % 2 == 0:
        player = "X"
    else:
        player = "O"
    sort_input(input("Enter Position:  "), player)


def sort_input(text, current_player):
    global tic_tac_toe, current_move
    text = text.upper()
    if text == "HELP":
        start()
    elif text == "END":
        print("It was a nice game but you lost before even finishing... lame as F***!")
        exit(0)
    elif text == "GAME":
        print_chess()
        get_input()
    else:
        valid_inputs = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3",
                        "1A", "2A", "3A", "1B", "2B", "3B", "1C", "2C", "3C"]
        if text in valid_inputs and len(text) == 2:
            if text[0].isdigit():
                text = text[::-1]
            column = text[0]
            row = int(text[1]) - 1
            if column == "A":
                column = 0
            elif column == "B":
                column = 1
            elif column == "C":
                column = 2
            if tic_tac_toe[row][column] == "| |":
                tic_tac_toe[row][column] = f"|{current_player}|"
                check_for_win()
                current_move += 1
                print_chess()
                get_input()
            else:
                print(f"!!!This position is taken !!! Try Again: !!!")
                get_input()
        else:
            print("!!! Invalid input !!! Try Again !!!")
            get_input()


def check_for_win():
    winner = None
    # Check the horizontal lines:
    for horizontal_line in tic_tac_toe:
        if "| |" not in horizontal_line:
            if len(set(horizontal_line)) == 1:
                winner = horizontal_line[0]
    # check the vertical lines:
    if (tic_tac_toe[0][0] == tic_tac_toe[1][0] == tic_tac_toe[2][0]) and tic_tac_toe[0][0] != "| |":
        winner = tic_tac_toe[0][0]
    elif (tic_tac_toe[0][1] == tic_tac_toe[1][1] == tic_tac_toe[2][1]) and tic_tac_toe[0][1] != "| |":
        winner = tic_tac_toe[0][1]
    elif (tic_tac_toe[0][2] == tic_tac_toe[1][2] == tic_tac_toe[2][2]) and tic_tac_toe[0][2] != "| |":
        winner = tic_tac_toe[0][2]
    # Check the diagonal lines:
    elif (tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2]) and tic_tac_toe[0][0] != "| |":
        winner = tic_tac_toe[0][0]
    elif (tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0]) and tic_tac_toe[0][2] != "| |":
        winner = tic_tac_toe[0][2]
    # Check for tie
    if ("| |" not in tic_tac_toe[0]) and ("| |" not in tic_tac_toe[1]) and ("| |" not in tic_tac_toe[2]):
        tie()
    if winner:
        win(winner)


def win(x_or_o):
    clean_screen()
    winner_num = 0
    if x_or_o == "|X|":
        winner_num = 1
    else:
        winner_num = 2

    line_number = 1
    print(f"Final Game State:")
    print("   A   B   C ")
    for line in tic_tac_toe:
        print(line_number, end=" ")
        print(*line)
        line_number += 1

    print(90 * "*"+"\n"+90 * "*")
    print(90 * "*"+"\n"+f"THE WINNER SI PLAYER - {winner_num}"+"\n"+90 * "*")
    print(90 * "*" + "\n" + 90 * "*")
    print("\n\n\nCreated by Simeon Tsvetanov :)")
    exit(0)


def tie():
    clean_screen()
    print(90 * "-" + "\n" + 90 * "-")
    print("Unfortunately, You are equally big suckers")
    line_number = 1
    print(f"Final Game State:")
    print("   A   B   C ")
    for line in tic_tac_toe:
        print(line_number, end=" ")
        print(*line)
        line_number += 1
    print(f"And its a ----TIE----")
    print("\n\n\nCreated by Simeon Tsvetanov :)")
    print(90 * "-" + "\n" + 90 * "-")
    exit(0)


if __name__ == '__main__':
    start()
