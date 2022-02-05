import tkinter as tk

# window management
root = tk.Tk()
root.title("Tic-Tac-Toe in Tic-Tac_Toe")
root.geometry("810x792")  # perfectly fits 81 buttons

player = "X"  # variable for players X/O

winners = ["", "", "", "", "", "", "", "", ""]  # set of strings for checking Big Win


def change_player():
    """Changes player from X to O and form O to X"""
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def disable_everything():
    """Disables ALL buttons"""
    global listOfPlaces
    for i in listOfPlaces:
        for j in i:
            list_of_buttons[j]["state"] = tk.DISABLED


def enable_everything():
    """Enables ALL EMPTY buttons"""
    global listOfPlaces
    for i in listOfPlaces:
        for j in i:
            if list_of_buttons[j]["text"] == "":
                list_of_buttons[j]["state"] = tk.NORMAL


def check_small_win(clicked_button):
    """Checks small win in the medium square of clicked button"""
    global listOfSqr
    for sqr in listOfSqr:
        if clicked_button in sqr:
            """Rules for the small win"""
            if (list_of_buttons[sqr[0]]["text"] == list_of_buttons[sqr[1]]["text"] and list_of_buttons[sqr[0]][
                "text"] == list_of_buttons[sqr[2]]["text"] and list_of_buttons[sqr[0]]["text"] != "") or (
                    list_of_buttons[sqr[3]]["text"] == list_of_buttons[sqr[4]]["text"] and list_of_buttons[sqr[3]][
                "text"] == list_of_buttons[sqr[5]]["text"] and list_of_buttons[sqr[3]]["text"] != "") or (
                    list_of_buttons[sqr[6]]["text"] == list_of_buttons[sqr[7]]["text"] and list_of_buttons[sqr[7]][
                "text"] == list_of_buttons[sqr[8]]["text"] and list_of_buttons[sqr[6]]["text"] != "") or (
                    list_of_buttons[sqr[0]]["text"] == list_of_buttons[sqr[3]]["text"] and list_of_buttons[sqr[0]][
                "text"] == list_of_buttons[sqr[6]]["text"] and list_of_buttons[sqr[0]]["text"] != "") or (
                    list_of_buttons[sqr[1]]["text"] == list_of_buttons[sqr[4]]["text"] and list_of_buttons[sqr[1]][
                "text"] == list_of_buttons[sqr[7]]["text"] and list_of_buttons[sqr[1]]["text"] != "") or (
                    list_of_buttons[sqr[2]]["text"] == list_of_buttons[sqr[5]]["text"] and list_of_buttons[sqr[5]][
                "text"] == list_of_buttons[sqr[8]]["text"] and list_of_buttons[sqr[2]]["text"] != "") or (
                    list_of_buttons[sqr[0]]["text"] == list_of_buttons[sqr[4]]["text"] and list_of_buttons[sqr[0]][
                "text"] == list_of_buttons[sqr[8]]["text"] and list_of_buttons[sqr[0]]["text"] != "") or (
                    list_of_buttons[sqr[2]]["text"] == list_of_buttons[sqr[4]]["text"] and list_of_buttons[sqr[2]][
                "text"] == list_of_buttons[sqr[6]]["text"] and list_of_buttons[sqr[2]]["text"] != ""):
                for z in sqr:
                    """If someone wins in medium square all empty small squares get . so they're not empty anymore 
                    could be changed if we find some better symbol"""
                    if list_of_buttons[z]["text"] == "":
                        list_of_buttons[z]["text"] = "."
                for i in range(9):
                    """Adds players win to winners"""
                    if listOfSqr[i] == sqr:
                        winners[i] = player


def check_big_win():
    """checks the big win"""
    if winners[0] == winners[1] and winners[1] == winners[2] and winners[1] != "" or winners[0] == winners[3] and \
            winners[3] == winners[6] and winners[3] != "" or winners[0] == winners[4] and winners[4] == winners[8] and \
            winners[4] != "":
        print(f"Winner is {winners[0]}!")
        root.destroy()
        quit()
    elif winners[1] == winners[4] and winners[4] == winners[7] and winners[4] != "" or winners[3] == winners[4] and \
            winners[4] == winners[5] and winners[4] != "":
        print(f"Winner is {winners[4]}!")
        root.destroy()
        quit()
    elif winners[6] == winners[7] and winners[7] == winners[8] and winners[7] != "":
        print(f"Winner is {winners[7]}!")
        root.destroy()
        quit()
    elif winners[2] == winners[5] and winners[5] == winners[8] and winners[5] != "":
        print(f"Winner is {winners[2]}!")
        root.destroy()
        quit()


def enable_sqr(clicked_button):
    """Enables medium square depending on position of the last clicked button"""
    global listOfSqr
    global listOfPlaces

    for i in range(len(listOfPlaces)):
        if clicked_button in listOfPlaces[i]:
            print("powinno dzialac")
            if winners[i] == "":
                for j in listOfSqr[i]:
                    if list_of_buttons[j]["text"] == "":
                        list_of_buttons[j]["state"] = tk.NORMAL
            else:
                """If position indicated already won medium square it sends it to enable_everything"""
                enable_everything()


def uncolor_last_button():
    """Changes color of the last-last clicked button to default - white or green"""
    global last_b
    if last_b in sqrUL or last_b in sqrUR or last_b in sqrM or last_b in sqrDL or last_b in sqrDR:
        list_of_buttons[last_b]["bg"] = '#e6ffe6'
    else:
        list_of_buttons[last_b]["bg"] = 'SystemButtonFace'


def button_click(clicked_button):
    """Pretty much new version of main()
    When you click a button you come here
    Firstly de-colors the last-last button clicked
    Changes text on button to player - X/O
    Changes clicked button color to yellow so everyone knows where are enabled buttons
    Disables all the buttons
    Checks for small win - medium square
    Checks for big win - whole tic-tac-toe
    Changes player
    Enables squares for the next player
    Changes last_b to now clicked to de-color it in next move
    """
    global last_b
    uncolor_last_button()
    print(list_of_buttons[clicked_button])
    list_of_buttons[clicked_button]["text"] = player
    list_of_buttons[clicked_button]["bg"] = '#ffff00'
    disable_everything()
    check_small_win(list_of_buttons[clicked_button])
    check_big_win()
    change_player()
    enable_sqr(list_of_buttons[clicked_button])
    last_b = clicked_button


"""Buttons. A lot of them. 
they are colored checkered way...? idk how to say it I'm tired
G G G W W W G G G
G G G W W W G G G
G G G W W W G G G
W W W G G G W W W 
W W W G G G W W W       < - LIKE THAT G - green, W - white
W W W G G G W W W
G G G W W W G G G
G G G W W W G G G
G G G W W W G G G
"""

"""OTHER WAY"""

list_of_buttons = []


def start():
    column = 0
    row = 0

    for i in range(81):
        if i in [1, 2, 0, 10, 11, 9, 19, 20, 18, 7, 8, 6, 16, 17, 15, 25, 26, 24, 31, 32, 30, 40, 41, 39, 49, 50, 48,
                 55, 56, 54, 64, 65, 63, 73, 74, 72, 61, 62, 60, 70, 71, 69, 79, 80, 78]:
            b = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                          command=lambda a=i: button_click(a))
        else:
            b = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                          command=lambda a=i: button_click(a))
        b.grid(row=row, column=column)
        list_of_buttons.append(b)

        column += 1
        if column == 9:
            column = 0
            row += 1


start()

"""
Useful lists of buttons
"""
# Little squares in medium squares
sqr1 = [0, 1, 2, 9, 10, 11, 18, 19, 20]  # top left
sqr2 = [3, 4, 5, 12, 13, 14, 21, 22, 23]  # top middle
sqr3 = [6, 7, 8, 15, 16, 17, 24, 25, 26]  # top right
sqr4 = [27, 28, 29, 36, 37, 38, 45, 46, 47]  # middle left
sqr5 = [30, 31, 32, 39, 40, 41, 48, 49, 50]  # center
sqr6 = [33, 34, 35, 42, 43, 44, 51, 52, 53]  # middle right
sqr7 = [54, 55, 56, 63, 64, 65, 72, 73, 74]  # down left
sqr8 = [57, 58, 59, 66, 67, 68, 75, 76, 77]  # down middle
sqr9 = [60, 61, 62, 69, 70, 71, 78, 79, 80]  # down right

listOfSqr = [sqr1, sqr2, sqr3, sqr4, sqr5, sqr6, sqr7, sqr8, sqr9]  # List of all medium squares in order

# Lists of squares depending on their position
sqrUL = [0, 3, 6, 27, 30, 33, 54, 57, 60]  # List of upper lefts
sqrU = [1, 4, 7, 28, 31, 34, 55, 58, 61]  # List of upper middles
sqrUR = [2, 5, 8, 29, 32, 35, 56, 59, 62]  # List of upper rights
sqrL = [9, 12, 15, 36, 39, 42, 63, 66, 69]  # List of middle lefts
sqrM = [10, 13, 16, 37, 40, 43, 64, 67, 70]  # List of centers
sqrR = [11, 14, 17, 38, 41, 44, 65, 68, 71]  # List of middle rights
sqrDL = [18, 21, 24, 45, 48, 51, 72, 75, 78]  # List of down lefts
sqrD = [19, 22, 25, 46, 49, 52, 74, 76, 79]  # List of down middles
sqrDR = [20, 23, 26, 47, 50, 53, 74, 77, 80]  # List of down rights

# List of all the buttons to "easily" put them into window


# List of all lists of squares depending on position
listOfPlaces = [sqrUL, sqrU, sqrUR, sqrL, sqrM, sqrR, sqrDL, sqrD, sqrDR]

last_b = 0  # setting up a last_b for coloring buttons

"""Small function to put buttons on their places"""

"""Main loop"""
root.mainloop()
