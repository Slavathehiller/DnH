from tkinter import*
from tkinter import Frame
from PIL import Image, ImageTk
from Options import*
from Goathorn import*
from Knight import*
from Barbarian import*
from DHViewver import*
from DHModeller import*
from DHController import*

window = Tk()
window.geometry('1200x660')
window.title('Подземелья и герои')
mainmenu = Menu(window)
window.config(menu=mainmenu)

gameEnded = False

def Newgame():
    pass

def SetOptions():
    pass

def menuAbout():
    pass

def menuInstruction():
    pass

menuFile = Menu(mainmenu, tearoff=0)
menuFile.add_command(label="Выход", command=lambda: exit(0))
mainmenu.add_cascade(label="Файл", menu=menuFile)

menuGame = Menu(mainmenu, tearoff=0)
menuGame.add_command(label="Начать игру", command=Newgame)
menuGame.add_command(label="Настройки", command=SetOptions)
mainmenu.add_cascade(label="Игра", menu=menuGame)

menuHelp = Menu(mainmenu, tearoff=0)
menuHelp.add_command(label="О программе", command=menuAbout)
menuHelp.add_command(label="Инструкция", command=menuInstruction)
mainmenu.add_cascade(label="Помощь", menu=menuHelp)

options = SimpleOptions()
hero1 = Knight(0, 0, None)
hero2 = Barbarian(1, 0, None)
goathorn = Goathorn(10, 0, None)
model = DHModeller([hero1, hero2], [goathorn], options)
hero1.model = model
hero2.model = model
goathorn.model = model

ActionFrame = Frame(window)
ActionFrame.pack(side=BOTTOM, fill=BOTH)

ViewFrame = Frame(window)
ViewFrame.pack(side=TOP, fill=BOTH)

TopButton = Button(ActionFrame, text="⇧", justify=CENTER, height=1, width=3)
TopButton.bind("<Button-1>", lambda event: RunCommand([Up]))
TopButton.grid(column=1, row=0)

BottomButton = Button(ActionFrame, text="⇩", justify=CENTER, height=1, width=3)
BottomButton.bind("<Button-1>", lambda event: RunCommand([Down]))
BottomButton.grid(column=1, row=2)

LeftButton = Button(ActionFrame, text="⇦", justify=CENTER, height=1, width=3)
LeftButton.bind("<Button-1>", lambda event: RunCommand([Left]))
LeftButton.grid(column=0, row=1)

RightButton = Button(ActionFrame, text="⇨", justify=CENTER, height=1, width=3)
RightButton.bind("<Button-1>", lambda event: RunCommand([Right]))
RightButton.grid(column=3, row=1)


view = DHViewer(window, model, options)
view.InitInterface()
view.drawmap()
control = DHController(model, options)

CommandFrame = Frame(ActionFrame)

CommandVar = IntVar()

def RecreateCommandPanel():
    global CommandFrame, CommandVar
    CommandFrame.destroy()
    CommandFrame = Frame(ActionFrame)
    CommandFrame.grid(column=4, row=1)
    for i in range(len(control.currentHero.Commands)):
        rbCommand = Radiobutton(CommandFrame, text=control.currentHero.CommandsNames[i], variable=CommandVar, value=i)
        rbCommand.pack(side=LEFT)


def CurrentCommand():
    return CommandVar.get()

def CheckGameState(state):
    pass

def RunCommand(params):
    control.RunCommand(CurrentCommand(), params)
    RecreateCommandPanel()
    view.drawmap()

def KeyPress(event):
    if gameEnded:
        return
    direction = None
    if event.keycode == 38:
        direction = Up
    elif event.keycode == 37:
        direction = Left
    elif event.keycode == 40:
        direction = Down
    elif event.keycode == 39:
        direction = Right
    if not gameEnded:
        RunCommand([direction])

window.bind("<Key>", KeyPress)


RecreateCommandPanel()

window.mainloop()
