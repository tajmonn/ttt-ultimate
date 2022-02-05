import tkinter as tk

# stupid window management
root = tk.Tk()
root.title("Tic-Tac-Toe in Tic-Tac_Toe")
root.geometry("810x792")    # perfectly fits 81 buttons

player = "X"    # variable for players X/O


winners = ["", "", "", "", "", "", "", "", ""]      # set of strings for checking Big Win


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
            j["state"] = tk.DISABLED


def enable_everything():
    """Enables ALL EMPTY buttons"""
    global listOfPlaces
    for i in listOfPlaces:
        for j in i:
            if j["text"] == "":
                j["state"] = tk.NORMAL


def check_small_win(clicked_button):
    """Checks small win in the medium square of clicked button"""
    global listOfSqr
    for sqr in listOfSqr:
        if clicked_button in sqr:
            """Don't we love to write all of those stupid rules by finger?"""
            if (sqr[0]["text"] == sqr[1]["text"] and sqr[0]["text"] == sqr[2]["text"] and sqr[0]["text"] != "") or (
                    sqr[3]["text"] == sqr[4]["text"] and sqr[3]["text"] == sqr[5]["text"] and sqr[3]["text"] != "") or (
                    sqr[6]["text"] == sqr[7]["text"] and sqr[7]["text"] == sqr[8]["text"] and sqr[6]["text"] != "") or (
                    sqr[0]["text"] == sqr[3]["text"] and sqr[0]["text"] == sqr[6]["text"] and sqr[0]["text"] != "") or (
                    sqr[1]["text"] == sqr[4]["text"] and sqr[1]["text"] == sqr[7]["text"] and sqr[1]["text"] != "") or (
                    sqr[2]["text"] == sqr[5]["text"] and sqr[5]["text"] == sqr[8]["text"] and sqr[2]["text"] != "") or (
                    sqr[0]["text"] == sqr[4]["text"] and sqr[0]["text"] == sqr[8]["text"] and sqr[0]["text"] != "") or (
                    sqr[2]["text"] == sqr[4]["text"] and sqr[2]["text"] == sqr[6]["text"] and sqr[2]["text"] != ""):
                for z in sqr:
                    """If someone wins in medium square all empty small squares get . so they're not empty anymore 
                    could be changed if we find some better symbol"""
                    if z["text"] == "":
                        z["text"] = "."
                for i in range(9):
                    """Adds players win to winners"""
                    if listOfSqr[i] == sqr:
                        winners[i] = player


def check_big_win():
    """OH, YES! Some more stupid rules for stupid tic-tac-toe. JK I love them. We all love them.
    Just like we love Shrek"""
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
            if winners[i] == "":
                for j in listOfSqr[i]:
                    if j["text"] == "":
                        j["state"] = tk.NORMAL
            else:
                "If position is indicating already won medium square it sends it to enable_everything"
                enable_everything()


def uncolor_last_button():
    """Changes color of the last last clicked button to default - white or green"""
    global last_b
    if last_b in sqrUL or last_b in sqrUR or last_b in sqrM or last_b in sqrDL or last_b in sqrDR:
        last_b["bg"] = '#e6ffe6'
    else:
        last_b["bg"] = 'SystemButtonFace'


def button_click(clicked_button):
    """Pretty much new version of main()
    When you click a button you come here
    Firstly de-colors the last last button clicked
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
    clicked_button["text"] = player
    clicked_button["bg"] = '#ffff00'
    disable_everything()
    check_small_win(clicked_button)
    check_big_win()
    change_player()
    enable_sqr(clicked_button)
    last_b = clicked_button


"""Buttons. A lot of them. SO FUCKING MANY
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
b1 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6', command=lambda: button_click(b1))
b2 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6', command=lambda: button_click(b2))
b3 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6', command=lambda: button_click(b3))
b4 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
               command=lambda: button_click(b4))
b5 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
               command=lambda: button_click(b5))
b6 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
               command=lambda: button_click(b6))
b7 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6', command=lambda: button_click(b7))
b8 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6', command=lambda: button_click(b8))
b9 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6', command=lambda: button_click(b9))
b10 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b10))
b11 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b11))
b12 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b12))
b13 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b13))
b14 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b14))
b15 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b15))
b16 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b16))
b17 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b17))
b18 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b18))
b19 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b19))
b20 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b20))
b21 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b21))
b22 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b22))
b23 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b23))
b24 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b24))
b25 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b25))
b26 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b26))
b27 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b27))
b28 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b28))
b29 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b29))
b30 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b30))
b31 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b31))
b32 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b32))
b33 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b33))
b34 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b34))
b35 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b35))
b36 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b36))
b37 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b37))
b38 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b38))
b39 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b39))
b40 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b40))
b41 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b41))
b42 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b42))
b43 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b43))
b44 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b44))
b45 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b45))
b46 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b46))
b47 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b47))
b48 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b48))
b49 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b49))
b50 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b50))
b51 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b51))
b52 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b52))
b53 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b53))
b54 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b54))
b55 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b55))
b56 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b56))
b57 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b57))
b58 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b58))
b59 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b59))
b60 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b60))
b61 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b61))
b62 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b62))
b63 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b63))
b64 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b64))
b65 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b65))
b66 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b66))
b67 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b67))
b68 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b68))
b69 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b69))
b70 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b70))
b71 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b71))
b72 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b72))
b73 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b73))
b74 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b74))
b75 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b75))
b76 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b76))
b77 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b77))
b78 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='SystemButtonFace',
                command=lambda: button_click(b78))
b79 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b79))
b80 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b80))
b81 = tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5, bg='#e6ffe6',
                command=lambda: button_click(b81))

"""
This is just pain...
if anyone asks why... Tell them I don't know
it was just pain...
"""
# Little squares in medium squares
sqr1 = [b1, b2, b3, b10, b11, b12, b19, b20, b21]  # top left
sqr2 = [b4, b5, b6, b13, b14, b15, b22, b23, b24]  # top middle
sqr3 = [b7, b8, b9, b16, b17, b18, b25, b26, b27]  # top right
sqr4 = [b28, b29, b30, b37, b38, b39, b46, b47, b48]  # middle left
sqr5 = [b31, b32, b33, b40, b41, b42, b49, b50, b51]  # center
sqr6 = [b34, b35, b36, b43, b44, b45, b52, b53, b54]  # middle right
sqr7 = [b55, b56, b57, b64, b65, b66, b73, b74, b75]  # down left
sqr8 = [b58, b59, b60, b67, b68, b69, b76, b77, b78]  # down middle
sqr9 = [b61, b62, b63, b70, b71, b72, b79, b80, b81]  # down right

listOfSqr = [sqr1, sqr2, sqr3, sqr4, sqr5, sqr6, sqr7, sqr8, sqr9]  # List of all medium squares in order

# Lists of squares depending on their position
sqrUL = [b1, b4, b7, b28, b31, b34, b55, b58, b61]  # List of upper lefts
sqrU = [b2, b5, b8, b29, b32, b35, b56, b59, b62]  # List of upper middles
sqrUR = [b3, b6, b9, b30, b33, b36, b57, b60, b63]  # List of upper rights
sqrL = [b10, b13, b16, b37, b40, b43, b64, b67, b70]  # List of middle lefts
sqrM = [b11, b14, b17, b38, b41, b44, b65, b68, b71]  # List of centers
sqrR = [b12, b15, b18, b39, b42, b45, b66, b69, b72]  # List of middle rights
sqrDL = [b19, b22, b25, b46, b49, b52, b73, b76, b79]  # List of down lefts
sqrD = [b20, b23, b26, b47, b50, b53, b74, b77, b80]  # List of down middles
sqrDR = [b21, b24, b27, b48, b51, b54, b75, b78, b81]  # List of down rights

# List of all the buttons to "easily" put them into window
listOfButtons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22,
                 b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42,
                 b43, b44, b45, b46, b47, b48, b49, b50, b51, b52, b53, b54, b55, b56, b57, b58, b59, b60, b61, b62,
                 b63, b64, b65, b66, b67, b68, b69, b70, b71, b72, b73, b74, b75, b76, b77, b78, b79, b80, b81]

# List of all lists of squares depending on position
listOfPlaces = [sqrUL, sqrU, sqrUR, sqrL, sqrM, sqrR, sqrDL, sqrD, sqrDR]

last_b = b1     # setting up a last_b for coloring buttons

"""This shit is just for putting buttons into their places"""
column = 0
row = 0

for button in listOfButtons:
    button.grid(row=row, column=column)
    column += 1
    if column == 9:
        column = 0
        row += 1

"""LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP"""
root.mainloop()
