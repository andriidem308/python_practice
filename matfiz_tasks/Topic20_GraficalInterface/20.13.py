from random import randint
from tkinter.filedialog import *
from tkinter import messagebox as mb

BGCOLOR = "#FFCF00"
COLOR_1 = "#407DFF"
COLOR_2 = "#0052FF"


# ________________________________________________________________________________

def OpenFile(ev=None):
    try:
        name = askopenfilename()
        f = open(name, 'r')
        for line in f:
            linelist = line.rstrip().split()
            string_match = "{0} {1}:{2} {3}".format(linelist[0], int(linelist[2]), int(linelist[3]),
                                                    linelist[1]).title()
            matches_list.insert(END, string_match)
        filelabel.configure(text=name)
    except FileNotFoundError:
        mb.showinfo("Внимание", "Файл не загружен")
    except IndexError:
        mb.showinfo("Внимание", "Формат содержимого файла неккоректный\n" +
                    "Измените содержимое согласно инструкции:\n" +
                    "Help -> How to use?")

    except TypeError:
        mb.showinfo("Внимание", "Формат содержимого файла неккоректный\n" +
                    "Измените содержимое согласно инструкции:\n" +
                    "Help -> How to use?")

    except ValueError:
        mb.showinfo("Внимание", "Формат содержимого файла неккоректный\n" +
                    "Измените содержимое согласно инструкции:\n" +
                    "Help -> How to use?")


def Help():
    filewin = Toplevel(root)
    f = open("Readme2013.txt", 'r')
    strfile = f.read()
    label = Label(filewin, text=strfile, justify="left")
    label.pack()


def About():
    filewin = Toplevel(root)
    f = open("About2013.txt", 'r')
    strfile = f.read()
    label = Label(filewin, text=strfile, justify="left")
    label.pack()


def SaveFileAs(ev=None):
    try:
        assert filelabel['text'] is not ""
        name = asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(label["text"])
        name.write(text2save)
        name.close

    except AssertionError:
        mb.showinfo("Внимание", "Файл не загружен\nСписок матчей пустой!")


# ________________________________________________________________________________
def get_teams(filename):
    file = open(filename, 'r')
    _teams = dict()
    for match in file:
        _team_1 = match.split()[0]
        _team_2 = match.split()[1]
        _goals_1 = int(match.split()[2])
        _goals_2 = int(match.split()[3])

        _points_1 = 0
        _points_2 = 0

        if _goals_1 > _goals_2:
            _points_1 += 3
        elif _goals_2 > _goals_1:
            _points_2 += 3
        else:
            _points_1 += 1
            _points_2 += 1

        win1 = 1 if _points_1 > _points_2 else 0
        win2 = 1 if _points_1 < _points_2 else 0
        if _goals_1 == _goals_2:
            draw1, draw2 = 1, 1
        else:
            draw1, draw2 = 0, 0
        lose1 = 1 if win2 else 0
        lose2 = 1 if win1 else 0

        if _team_1 not in _teams:
            _teams[_team_1] = {"place": 0, "team": _team_1, "games": 1, "wins": win1, "draws": draw1,
                               "loses": lose1, "goals": _goals_1, "missed": _goals_2, "points": _points_1}
        else:
            _teams[_team_1]["games"] += 1
            _teams[_team_1]["goals"] += _goals_1
            _teams[_team_1]["missed"] += _goals_2
            _teams[_team_1]["wins"] += win1
            _teams[_team_1]["draws"] += draw1
            _teams[_team_1]["loses"] += lose1
            _teams[_team_1]["points"] += _points_1

        if _team_2 not in _teams:
            _teams[_team_2] = {"place": 0, "team": _team_2, "games": 1, "wins": win2, "draws": draw2,
                               "loses": lose2, "goals": _goals_2, "missed": _goals_1, "points": _points_2}
        else:
            _teams[_team_2]["games"] += 1
            _teams[_team_2]["goals"] += _goals_2
            _teams[_team_2]["missed"] += _goals_1
            _teams[_team_2]["wins"] += win2
            _teams[_team_2]["draws"] += draw2
            _teams[_team_2]["loses"] += lose2
            _teams[_team_2]["points"] += _points_2

    return _teams


def get_winner(teams):
    result_teams = dict(teams)
    max_points = 0
    max_teams = []

    for _team in result_teams.values():
        if _team["points"] > max_points:
            max_points = _team["points"]
            best_team = _team["team"]
    for _team in teams.values():
        if _team["points"] == max_points: max_teams.append(_team)

    if len(max_teams) == 1: return best_team

    max_difference = 0

    result_teams, max_teams = max_teams, []

    for _team in result_teams:
        if _team["goals"] - _team["missed"] > max_difference:
            max_difference = _team["goals"] - _team["missed"]
            best_team = _team["team"]

    for _team in result_teams:
        if _team["goals"] - _team["missed"] == max_difference:
            max_teams.append(_team)

    if len(max_teams) == 1: return best_team

    result_teams, max_teams = max_teams, []
    max_goals = 0
    for _team in result_teams:
        if _team["goals"] > max_goals:
            max_goals = _team["goals"]
            best_team = _team["team"]
    for _team in result_teams:
        if _team["goals"] == max_goals:
            max_teams.append(_team)

    if len(max_teams) == 1: return best_team

    k = randint(0, len(max_teams) - 1)
    return max_teams[k]


def get_league_table(filename):
    res = []
    global_teams = get_teams(filename)
    teams = get_teams(filename)
    keys = list(teams.keys())
    values = list(teams.values())

    while len(global_teams) != len(res):
        res.append(get_winner(teams))
        teams = dict()
        for i in range(len(keys)):
            if keys[i] not in res:
                teams[keys[i]] = values[i]

    return res


def calc(ev=None):
    try:
        FILENAME = filelabel['text']
        TEAMS = get_teams(FILENAME)
        league_table = get_league_table(FILENAME)

        league_table_window = Tk()
        # league_table_window.configure(background=BGCOLOR)
        frame = Frame(league_table_window, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        place = Label(frame, text='Place', background=BGCOLOR, width=6, borderwidth=2, relief="groove")
        place.grid(column=0, row=0, ipady=5, ipadx=4)
        team = Label(frame, text='Team', background=BGCOLOR, width=20, borderwidth=2, relief="groove")
        team.grid(column=1, row=0, ipady=5, ipadx=4)
        games = Label(frame, text='Games', background=BGCOLOR, width=9, borderwidth=2, relief="groove")
        games.grid(column=2, row=0, ipady=5, ipadx=4)
        wins = Label(frame, text='Wins', background=BGCOLOR, width=9, borderwidth=2, relief="groove")
        wins.grid(column=3, row=0, ipady=5, ipadx=4)
        draws = Label(frame, text='Draws', background=BGCOLOR, width=9, borderwidth=2, relief="groove")
        draws.grid(column=4, row=0, ipady=5, ipadx=4)
        lose = Label(frame, text='Lose', background=BGCOLOR, width=9, borderwidth=2, relief="groove")
        lose.grid(column=5, row=0, ipady=5, ipadx=4)
        goals = Label(frame, text='Goals', background=BGCOLOR, width=9, borderwidth=2, relief="groove")
        goals.grid(column=6, row=0, ipady=5, ipadx=4)
        missed = Label(frame, text='Missed', background=BGCOLOR, width=9, borderwidth=2, relief="groove")
        missed.grid(column=7, row=0, ipady=5, ipadx=4)
        score = Label(frame, text='Score', background=BGCOLOR, width=9, borderwidth=2, relief="groove")
        score.grid(column=8, row=0, ipady=5, ipadx=4)
        frame.pack(padx=7, pady=7)

        for i in range(len(league_table)):
            if i % 2 == 0:
                color = COLOR_1
            else:
                color = COLOR_2
            place = Label(frame, text=i + 1, background=color, width=6, borderwidth=2, relief="groove", fg="white")
            place.grid(column=0, row=i + 1, ipady=1, ipadx=4)
            team = Label(frame, text=TEAMS[league_table[i]]["team"].title(), background=color, width=20, borderwidth=2,
                         relief="groove", fg="white")
            team.grid(column=1, row=i + 1, ipady=1, ipadx=4)
            games = Label(frame, text=TEAMS[league_table[i]]["games"], background=color, width=9, borderwidth=2,
                          relief="groove", fg="white")
            games.grid(column=2, row=i + 1, ipady=1, ipadx=4)
            wins = Label(frame, text=TEAMS[league_table[i]]["wins"], background=color, width=9, borderwidth=2,
                         relief="groove", fg="white")
            wins.grid(column=3, row=i + 1, ipady=1, ipadx=4)
            draws = Label(frame, text=TEAMS[league_table[i]]["draws"], background=color, width=9, borderwidth=2,
                          relief="groove", fg="white")
            draws.grid(column=4, row=i + 1, ipady=1, ipadx=4)
            lose = Label(frame, text=TEAMS[league_table[i]]["loses"], background=color, width=9, borderwidth=2,
                         relief="groove", fg="white")
            lose.grid(column=5, row=i + 1, ipady=1, ipadx=4)
            goals = Label(frame, text=TEAMS[league_table[i]]["goals"], background=color, width=9, borderwidth=2,
                          relief="groove", fg="white")
            goals.grid(column=6, row=i + 1, ipady=1, ipadx=4)
            missed = Label(frame, text=TEAMS[league_table[i]]["missed"], background=color, width=9, borderwidth=2,
                           relief="groove", fg="white")
            missed.grid(column=7, row=i + 1, ipady=1, ipadx=4)
            score = Label(frame, text=TEAMS[league_table[i]]["points"], background=color, width=9, borderwidth=2,
                          relief="groove", fg="white")
            score.grid(column=8, row=i + 1, ipady=1, ipadx=4)

        label.configure(text=get_winner(get_teams(FILENAME)))
    except FileNotFoundError:
        mb.showinfo("Внимание", "Файл не загружен\nСписок матчей пустой!")
    except TypeError or IndexError:
        mb.showinfo("Внимание", "Формат содержимого файла неккоректный\n" +
                    "Измените содержимое согласно инструкции:\n" +
                    "Help -> How to use?")


# _____________________________________________________________________________


root = Tk()
root.configure()
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_command(label="Save", command=SaveFileAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to use?", command=Help)
helpmenu.add_command(label="About...", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

label = Label(root, text="________________", width=15, height=2)
label.pack(side=TOP)

matchesframe = Frame(root)
matches_list = Listbox(matchesframe, borderwidth=3, relief="sunken", width=30, height=6, font=("timesnewroman", 12),
                       justify="center")
matches_list.pack(side=LEFT, pady=15, padx=15)
scrollbar = Scrollbar(matchesframe)
scrollbar.pack(side=LEFT, fill=Y)
matchesframe.pack(side=TOP)
button = Button(root, text="Визначити переможця", command=calc, bg="grey")
button.pack(side=TOP, pady=15, padx=15)

scrollbar.config(command=matches_list.yview)
matches_list['yscrollcommand'] = scrollbar.set
filelabel = Label(root)
file2save = Label(root)
root.bind("<Control-Key-o>", OpenFile)
root.bind("<Escape>", quit)
root.bind("<Control-Key-s>", SaveFileAs)
root.config(menu=menubar)
root.mainloop()
