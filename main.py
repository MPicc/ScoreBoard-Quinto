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

if not os.path.exists("./data"):
    os.makedirs("./data")
if not os.path.exists("./data/score"):
    os.makedirs("./data/score")
if not os.path.exists("./data/out"):
    os.makedirs("./data/out")
for i in range (0,34):
    with open("./data/out/" + str(i) + ".txt", 'a+', encoding="utf-8") as f:
        f.close()
with open("./data/score/period.txt", 'a+', encoding="utf-8") as f:
    f.close()
with open("./data/score/scq.txt", 'a+', encoding="utf-8") as f:
    if (os.path.getsize("./data/score/scq.txt") == 0):
        f.write(str(0))
    f.close()
with open("./data/score/ospiti.txt", 'a+', encoding="utf-8") as f:
    if (os.path.getsize("./data/score/ospiti.txt") == 0):
        f.write(str(0))
    f.close()

def this():
    '''do stuff and return next menu'''
    print("5")
    return [{'desc': 'do that', 'f': that}]


def update_last_scorer(scorer_path):
    original = scorer_path
    target = "./data/score/scorer.txt"

    shutil.copyfile(original, target)

def write_scorer_GUI(scorer):
    scorer = "".join(scorer)
    scorer = scorer.strip("[']")
    with open("./data/score/scorer.txt", 'w+', encoding="utf-8") as f:
        f.write(str(scorer))


def create_player_list(offset):
    players: List = []
    for i in range(0, 16):
        if (i == 0):
            with open("./data/out/" + str(i + offset) + ".txt", 'r', encoding="utf-8") as f:
                players.append(f.read())
        else:
            with open("./data/out/" + str(i + offset) + ".txt", 'r', encoding="utf-8") as f:
                players.append(str(i) + ". " + f.read())
    return players

def create_teams_textfile15():

    player_list = create_player_list(0)
    player_list_osp = create_player_list(16)

    with open("./data/out/32.txt", 'r', encoding="utf-8") as f:
        allSCQ = f.read()
    with open("./data/out/33.txt", 'r', encoding="utf-8") as f:
        allOSP = f.read()

    with open("./data/score/" + "PlayerListSCQ" + ".txt", 'w+', encoding="utf-8") as f:
        for i in range(1, 16):
            f.write("\n" + "".join(player_list[i]))
        f.write("\n\nAll. "+ allSCQ)

    with open("./data/score/" + "PlayerListOSP" + ".txt", 'w+', encoding="utf-8") as f:
        for i in range(1, 16):
            f.write("\n" + "".join(player_list_osp[i]))
        f.write("\n\nAll. "+ allOSP)

def create_teams_textfile13():

    player_list = create_player_list(0)
    player_list_osp = create_player_list(16)

    with open("./data/out/32.txt", 'r', encoding="utf-8") as f:
        allSCQ = f.read()
    with open("./data/out/33.txt", 'r', encoding="utf-8") as f:
        allOSP = f.read()

    with open("./data/score/" + "PlayerListSCQ" + ".txt", 'w+', encoding="utf-8") as f:
        for i in range(1, 14):
            f.write("\n" + "".join(player_list[i]))
        f.write("\n\nAll. "+ allSCQ)

    with open("./data/score/" + "PlayerListOSP" + ".txt", 'w+', encoding="utf-8") as f:
        for i in range(1, 14):
            f.write("\n" + "".join(player_list_osp[i]))
        f.write("\n\nAll. "+ allOSP)


def check_status():
    with open("./data/out/16.txt", 'r', encoding="utf-8") as f:
        out = f.read()
    with open("./data/out/0.txt", 'r', encoding="utf-8") as f:
        home = f.read()
    with open("./data/score/period.txt", 'r', encoding="utf-8") as f:
        period = f.read()
    with open("./data/score/scq.txt", 'r', encoding="utf-8") as f:
        scq = f.read()
    with open("./data/score/ospiti.txt", 'r', encoding="utf-8") as f:
        ospiti = f.read()

    output = "\n" + home + " - " + out + "\n" + scq + " - " + ospiti + "\n" + period + "\n"

    return output


def change_period(period):
    with open("./data/score/period.txt", 'w+', encoding="utf-8") as f:
        f.write(str(period))


def do_operation(file_path, op):
    with open("./data/score/" + file_path, 'r', encoding="utf-8") as f:
        value = f.read()

        if ((int(value) + (op)) >= 0):
            num = int(value) + (op)
        else:
            num = int(value)

        with open("./data/score/" + file_path, 'w+', encoding="utf-8") as fx:
            fx.write(str(num))


def writenumber(file_path, op):
    with open("./data/score/" + file_path, 'r', encoding="utf-8") as f:
        value = f.read()
        num = (op)
        with open("./data/score/" + file_path, 'w+', encoding="utf-8") as fx:
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

        player_list = create_player_list(0)
        player_list_osp = create_player_list(16)

        print("GUI avviata! \n\n")
        
        # Choose a Theme for the Layout
        sg.theme('SystemDefault')
       
        layout = [[sg.Text('Scoreboard per dirette by Marco',font=("Arial",18))],
                [sg.Text(check_status(), key ='-RES-', justification='c', font = ("Arial", 14))],
                [sg.Button('!Quinto', size=(5,2)), sg.Button('Quinto', size=(15,2)), sg.Button('Ospiti', size=(15,2)), sg.Button('!Ospiti', size=(5,2))], #sg.Button('Load Data')],  # set options for item in listbox
                [sg.Listbox(values = player_list,
                            size =(24, 16),
                            key ='-LISTscq-',
                            enable_events = True),
                sg.Listbox(values = player_list_osp,
                            size =(24, 16),
                            key ='-LISTosp-',
                            enable_events = True)],
                # [sg.Text ('Allenatori: ')],
                # [sg.InputText(key ='allSCQ', size = (21,20)),sg.InputText(key ='allOSP', size = (21,20))],
                [sg.Text ('\n', font=("Arial",2))],                
                [sg.Text ('Tempo: ')],
                [sg.Combo (['1° Tempo', '2° Tempo','3° Tempo', '4° Tempo','1° T. Supp', '2° T. Supp', 'Tiri Rigore'], key='timesSlider', enable_events= True, size=(40,20))],
                [sg.Text ('\n', font=("Arial",5))],
                [sg.Button('Reset'), sg.Button ('Inserisci Giocatori'), sg.Button('Exit')]],
        
        window = sg.Window('SCQuinto Scoreboard Manager', layout, element_justification='c')

        # This is an Event Loop
        while True:  
            event, values = window.read()

            if (event == sg.WIN_CLOSED):
                break

            if event in (None,'timesSlider'):
                k = (values['timesSlider'])
                change_period(k)
                window['-RES-'].Update(check_status())

            if event in (None,'-LISTscq-'):
                k = (values['-LISTscq-'])
                write_scorer_GUI(k)
                window['-RES-'].Update(check_status())

            if event in (None,'-LISTosp-'):
                k = (values['-LISTosp-'])
                write_scorer_GUI(k)
                window['-RES-'].Update(check_status())

            if event in (None, 'Exit'):
                quit()
                break

            if event in (None, 'Quinto'):
                do_operation("scq.txt", 1)
                window['-RES-'].Update(check_status())

            if event in (None, 'Ospiti'):
                do_operation("ospiti.txt", 1)
                window['-RES-'].Update(check_status())

            if event in (None, '!Quinto'):
                do_operation("scq.txt", -1)
                window['-RES-'].Update(check_status())

            if event in (None, '!Ospiti'):
                do_operation("ospiti.txt", -1)
                window['-RES-'].Update(check_status())
            
            if event in (None, 'Reset'):
                writenumber("ospiti.txt", 0)
                writenumber("scq.txt", 0)
                window['-RES-'].Update(check_status())

            if event in (None, 'Inserisci Giocatori'):
                inserisci_giocatori()
                player_list = create_player_list(0)
                player_list_osp = create_player_list(16)
                window['-LISTscq-'].Update(player_list)
                window['-LISTosp-'].Update(player_list_osp)
                window['-RES-'].Update(check_status())   

            if event in (None, 'Load Data'):
                read_teams()
                player_list = create_player_list(0)
                player_list_osp = create_player_list(16)
                window['-LISTscq-'].Update(player_list)
                window['-LISTosp-'].Update(player_list_osp)
                window['-RES-'].Update(check_status())           
                            
def inserisci_giocatori():

    print("GUI inserimento giocatori avviata! \n\n")
    
    # Choose a Theme for the Layout
    sg.theme('SystemDefault')

    loaded = []
    for i in range (0,34):
        with open("./data/out/" + str(i) + ".txt", 'r', encoding="utf-8") as f:
            loaded.insert(i, f.read())
        
    
    layout = [
            [ sg.Text('Squadre'),       sg.InputText(key ='HomeTeam', size =        (21,20),  default_text= loaded[0]) ,            sg.InputText(key ='OSPTeam',         size = (21,20),  default_text= loaded[16] )],
            [ sg.Text('1'),             sg.InputText(key ='SCQPlayer1', size =      (21,20),  default_text= loaded[1]),             sg.InputText(key ='OSPPlayer1',      size = (21,20),  default_text= loaded[17] )],
            [ sg.Text('2'),             sg.InputText(key ='SCQPlayer2', size =      (21,20),  default_text= loaded[2]),             sg.InputText(key ='OSPPlayer2',      size = (21,20),  default_text= loaded[18] )],
            [ sg.Text('3'),             sg.InputText(key ='SCQPlayer3', size =      (21,20),  default_text= loaded[3]),             sg.InputText(key ='OSPPlayer3',      size = (21,20),  default_text= loaded[19] )],
            [ sg.Text('4'),             sg.InputText(key ='SCQPlayer4', size =      (21,20),  default_text= loaded[4]),             sg.InputText(key ='OSPPlayer4',      size = (21,20),  default_text= loaded[20] )],
            [ sg.Text('5'),             sg.InputText(key ='SCQPlayer5', size =      (21,20),  default_text= loaded[5]),             sg.InputText(key ='OSPPlayer5',      size = (21,20),  default_text= loaded[21] )],
            [ sg.Text('6'),             sg.InputText(key ='SCQPlayer6', size =      (21,20),  default_text= loaded[6]),             sg.InputText(key ='OSPPlayer6',      size = (21,20),  default_text= loaded[22] )],
            [ sg.Text('7'),             sg.InputText(key ='SCQPlayer7', size =      (21,20),  default_text= loaded[7]),             sg.InputText(key ='OSPPlayer7',      size = (21,20),  default_text= loaded[23] )],
            [ sg.Text('8'),             sg.InputText(key ='SCQPlayer8', size =      (21,20),  default_text= loaded[8]),             sg.InputText(key ='OSPPlayer8',      size = (21,20),  default_text= loaded[24] )],
            [ sg.Text('9'),             sg.InputText(key ='SCQPlayer9', size =      (21,20),  default_text= loaded[9]),             sg.InputText(key ='OSPPlayer9',      size = (21,20),  default_text= loaded[25] )],
            [ sg.Text('10'),            sg.InputText(key ='SCQPlayer10', size =     (21,20),  default_text= loaded[10]),             sg.InputText(key ='OSPPlayer10',     size = (21,20),  default_text= loaded[26] )],
            [ sg.Text('11'),            sg.InputText(key ='SCQPlayer11', size =     (21,20),  default_text= loaded[11]),             sg.InputText(key ='OSPPlayer11',     size = (21,20),  default_text= loaded[27] )],
            [ sg.Text('12'),            sg.InputText(key ='SCQPlayer12', size =     (21,20),  default_text= loaded[12]),             sg.InputText(key ='OSPPlayer12',     size = (21,20),  default_text= loaded[28] )],
            [ sg.Text('13'),            sg.InputText(key ='SCQPlayer13', size =     (21,20),  default_text= loaded[13]),             sg.InputText(key ='OSPPlayer13',     size = (21,20),  default_text= loaded[29] )],
            [ sg.Text('14'),            sg.InputText(key ='SCQPlayer14', size =     (21,20),  default_text= loaded[14]),             sg.InputText(key ='OSPPlayer14',     size = (21,20),  default_text= loaded[30] )],
            [ sg.Text('15'),            sg.InputText(key ='SCQPlayer15', size =     (21,20),  default_text= loaded[15]),             sg.InputText(key ='OSPPlayer15',     size = (21,20),  default_text= loaded[31] )],
            [ sg.Text('Allenatori'),    sg.InputText(key ='SCQ Allenatore', size =  (21,20),  default_text= loaded[32]),             sg.InputText(key ='OSP Allenatore',  size = (21,20),  default_text= loaded[33] )],
            [ sg.Button('Annulla'), sg.Button('Carica e Crea Lista')]
    ]
    
    window2 = sg.Window('Inserimento Formazioni', layout, element_justification='r')

    # This is an Event Loop
    while True:  
        event, values = window2.read()

        if (event == sg.WIN_CLOSED):
            window2.close()
            break


        if (event in (None, 'Annulla')):
            window2.close()
            break

        if (event in (None, 'Carica e Crea Lista')):

            with open("./data/out/" + "0.txt", 'w+', encoding="utf-8") as f:
                        f.write(values['HomeTeam'])
            with open("./data/out/" + "16.txt", 'w+', encoding="utf-8") as f:
                        f.write(values['OSPTeam'])

            for i in range(1, 16):
                    with open("./data/out/" + str(i) + ".txt", 'w+', encoding="utf-8") as f:
                        f.write(values['SCQPlayer' + str(i)])
            for i in range(1, 16):
                    with open("./data/out/" + str(i+16) + ".txt", 'w+', encoding="utf-8") as f:
                        f.write(values['OSPPlayer' + str(i)])
                
            with open("./data/out/" + "32.txt", 'w+', encoding="utf-8") as f:
                        f.write(values['SCQ Allenatore'])
            with open("./data/out/" + "33.txt", 'w+', encoding="utf-8") as f:
                        f.write(values['OSP Allenatore'])

            create_teams_textfile13()

            if (values['SCQPlayer14'].strip() != "" or values['SCQPlayer15'].strip() != "" or values['OSPPlayer14'].strip() != "" or values['OSPPlayer15'].strip() != ""):
                create_teams_textfile15()

            
            window2.close()
            break




while True:
    serve_menu()
    break


