# sorry for python 2.7
import os
import sys
import csv
import shutil
import re

from collections import Counter
from typing import List, Any

from pip._vendor.distlib.compat import raw_input
import PySimpleGUI as sg



def this():
    '''do stuff and return next menu'''
    print("5")
    return [{'desc': 'do that', 'f': that}]


def update_last_scorer(scorer_path):
    original = scorer_path
    target = "./data/score/scorer.txt"

    shutil.copyfile(original, target)


def create_player_list(offset):
    players: List = []
    for i in range(0, 14):
        with open("./data/out/" + str(i + offset) + ".txt", 'r', encoding="utf-8") as f:
            players.append(str(i) + ". " + f.read())
    return players

player_list = create_player_list(0)


def check_status():
    with open("./data/out/14.txt", 'r', encoding="utf-8") as f:
        out = f.read()
    with open("./data/out/0.txt", 'r', encoding="utf-8") as f:
        home = f.read()
    with open("./data/score/period.txt", 'r', encoding="utf-8") as f:
        period = f.read()
    with open("./data/score/scq.txt", 'r', encoding="utf-8") as f:
        scq = f.read()
    with open("./data/score/ospiti.txt", 'r', encoding="utf-8") as f:
        ospiti = f.read()

    output = "                       " + home + " - " + out + "\nRisultato attuale:       " + scq + " - " + ospiti + "\nTempo: " + period

    return output


def change_period(period):
    with open("./data/score/period.txt", 'w', encoding="utf-8") as f:
        f.write(str(period))


def do_operation(file_path, op):
    with open("./data/score/" + file_path, 'r', encoding="utf-8") as f:
        value = f.read()
        num = int(value) + (op)
        with open("./data/score/" + file_path, 'w', encoding="utf-8") as fx:
            fx.write(str(num))


def write_to_file(word):
    with open("/Dictionaries/eng.txt", "a+") as f:
        f.write(word + "\n")


def read_teams():
    with open('./data/teams.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                for i in range(0, 1):
                    filename = "./data/out/" + str(line_count) + ".txt"
                    with open(filename, 'w+') as f:
                        f.write(row[i])
                line_count += 1
            else:
                for i in range(0, 1):
                    filename = "./data/out/" + str(line_count) + ".txt"
                    with open(filename, 'w+') as f:
                        f.write(row[i])
                line_count += 1


def that():
    '''do stuff and return next menu'''
    print("7")
    return [{'desc': 'do this', 'f': this}]


def no_op():
    pass


def quit():
    sys.exit()


def serve_menu():
    # it would be nice to clear the screen here too
    print(check_status() +
          "\n\n"
          "S - Premi S se ha segnato il Quinto!!\n"
          "D - Premi D per togliere un punto al Quinto :'(\n"
          "O - Premi O se ha segnato la squadra ospite \n"
          "P - Premi P per togliere un punto alla squadra ospite :-) \n"
          "# - Scrivi il numero del periodo di gioco e premi invio!\n"
          "\n"
          "T - Premi T per caricare i dati delle squadre\n"
          "R - Premi R per resettare tutto!\n"
          "G - Premi G per avviare la GUI!\n"
          "X - Premi X per uscire!")

    options = 'abcdefghijk'

    choice = raw_input('>>>').lower()  # just input in python 3
    os.system('cls||clear')

    if choice == 'x':
        return sys.exit()

    elif choice == 's':
        print("Ho aggiunto un punto allo Sporting \n\n")
        do_operation("scq.txt", 1)
        scq_scorer_menu()
        return serve_menu(),

    elif choice == 'd':
        print("Ho tolto un punto allo Sporting \n\n")
        do_operation("scq.txt", -1)
        return serve_menu(),

    elif choice == 'o':
        print("Ho aggiunto un punto agli altri \n\n")
        do_operation("ospiti.txt", 1)
        out_scorer_menu()
        return serve_menu(),

    elif choice == 'p':
        print("Ho tolto un punto agli altri \n\n")
        do_operation("ospiti.txt", -1)
        return serve_menu(),

    elif choice == 't':
        read_teams()
        print("Ho caricato i dati dei giocatori \n\n")
        return serve_menu(),

    elif choice == 'r':
        print("Ho resettato tutto \n\n")
        return serve_menu(),

    elif choice == '1':
        print("Comincia il primo tempo! \n\n")
        change_period(1)
        return serve_menu(),

    elif choice == '2':
        print("Comincia il secondo tempo! \n\n")
        change_period(2)
        return serve_menu(),

    elif choice == '3':
        print("Comincia il terzo tempo! \n\n")
        change_period(3)
        return serve_menu(),

    elif choice == '4':
        print("Comincia il quarto tempo! \n\n")
        change_period(4)
        return serve_menu(),

    elif choice == 'g':
        print("GUI avviata! \n\n")
        
        # Choose a Theme for the Layout
        sg.theme('DarkRed1')

       
        layout = [[sg.Text('List of InBuilt Themes')],
                [sg.Text(check_status(), key ='-RES-')],
                [sg.Button('Quinto'), sg.Button('Ospiti'))    # set options for item in listbox
],
                [sg.Listbox(values = player_list,
                            size =(20, 12),
                            key ='-LIST-',
                            enable_events = True),
                sg.Listbox(values = player_list,
                            size =(20, 12),
                            key ='-LIST-',
                            enable_events = True)],
                [sg.Button('Exit')]]
        
        window = sg.Window('SCQuinto Scoreboard Manager', layout)

        # This is an Event Loop
        while True:  
            event, values = window.read()
            
            if event in (None, 'Exit'):
                break

            if event in (None, 'Quinto'):
                do_operation("scq.txt", 1)
                window['-RES-'].Update(check_status())


            if event in (None, 'Ospiti'):
                do_operation("ospiti.txt", 1)
                window['-RES-'].Update(check_status())
                            
        # Close
        window.close()

        return serve_menu(),


    else:
        return serve_menu()


def scq_scorer_menu():
    # it would be nice to clear the screen here too
    print("\nChi ha segnato?")
    player_list = create_player_list(0)
    for value in player_list:
        print(value + "")

    choice = raw_input('>>>').lower()  # just input in python 3
    choice = int(choice)

    if int(choice)  in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
        target_file = "./data/out/" + str(int(choice)) + ".txt"
        update_last_scorer(target_file)
    else:
        print("ERRORE!! INPUT NON VALIDO!")
        return

    os.system('cls||clear')

    if choice == 'x':
        return sys.exit()


def out_scorer_menu():
    # it would be nice to clear the screen here too
    print("\nChi ha segnato?")
    player_list = create_player_list(0 + 14)
    for value in player_list:
        print(value + "")

    choice = raw_input('>>>').lower()  # just input in python 3

    if int(choice)  in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
        target_file = "./data/out/" + str(int(choice)+14) + ".txt"
        update_last_scorer(target_file)
    else:
        print("ERRORE!! INPUT NON VALIDO!")
        return


    os.system('cls||clear')

    if choice == 'x':
        return sys.exit()


while True:
    func = serve_menu()
    func()


