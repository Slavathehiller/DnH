from tkinter import*
from PIL import Image, ImageTk
from Options import*
from Goathorn import*
from Knight import*
from Barbarian import*
from DHViewver import*
from DHModeller import*
from DHController import*
from Command import*

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

def NewGameMenu():
    NewGameMenuwindow = Toplevel()
    NewGameMenuwindow.geometry('540x700')
    NewGameMenuwindow.title('Подземелья и герои')

    NewGame = Button(NewGameMenuwindow, text="Новая игра", justify=CENTER, height=3, width=35)
    NewGame.bind("<Button-1>")
    NewGame.grid(padx=140, pady=60)
    NewGame.configure(state=DISABLED)

    ContinueGame = Button(NewGameMenuwindow, text="Продолжить игру", justify=CENTER, height=3, width=35)
    ContinueGame.bind("<Button-1>")
    ContinueGame.grid(padx=140, pady=20)
    ContinueGame.configure(state=DISABLED)

    Settings = Button(NewGameMenuwindow, text="Настройки", justify=CENTER, height=3, width=35)
    Settings.bind("<Button-1>")
    Settings.grid(padx=140, pady=20)

    TechnoDemo = Button(NewGameMenuwindow, text="Технодемо", justify=CENTER, height=3, width=35)
    TechnoDemo.bind("<Button-1>", lambda event: NewGameMenuwindow.destroy())
    TechnoDemo.grid(padx=140, pady=20)

    Exit = Button(NewGameMenuwindow, text="Выход", justify=CENTER, height=3, width=35)
    Exit.bind("<Button-1>", lambda event: exit(0))
    Exit.grid(padx=140, pady=20)

menuFile = Menu(mainmenu, tearoff=0)
menuFile.add_command(label="Выход", command=lambda: exit(0))
mainmenu.add_cascade(label="Файл", menu=menuFile)

menuGame = Menu(mainmenu, tearoff=0)
menuGame.add_command(label="Начать игру", command=Newgame)
menuGame.add_command(label="Настройки", command=SetOptions)
mainmenu.add_cascade(label="Игра", menu=menuGame)
mainmenu.add_cascade(label="Новая игра", command=NewGameMenu)

menuHelp = Menu(mainmenu, tearoff=0)
menuHelp.add_command(label="О программе", command=menuAbout)
menuHelp.add_command(label="Инструкция", command=menuInstruction)
mainmenu.add_cascade(label="Помощь", menu=menuHelp)

options = SimpleOptions()
hero1 = Knight(1, 0, None)
hero1.Weapon = Spear(-1, -1)
hero2 = Barbarian(0, 0, None)
hero2.Weapon = Axe(-2, -2)
#hero3 = Barbarian(0, 0, None)
goathorn = Goathorn(5, 0, None)
model = DHModeller([hero1, hero2], [goathorn], options)
model.CurrentHeroIndex = 0

ActionFrame = Frame(window)
image = Image.open("ActionPanelImage.png").convert('RGBA')
APImage = ImageTk.PhotoImage(image)

ActionPanelBackground = Label(ActionFrame)
ActionPanelBackground.config(image=APImage, bd=0)
ActionPanelBackground.pack()
ActionFrame.pack(side=BOTTOM, fill=BOTH)

ViewFrame = Frame(window)
ViewFrame.pack(side=TOP, fill=BOTH)


image = Image.open("ArrowButton.png").convert('RGBA')
imageButtonLeft = ImageTk.PhotoImage(image)
image = image.transpose(Image.FLIP_LEFT_RIGHT)
imageButtonRight = ImageTk.PhotoImage(image)
image = image.transpose(Image.ROTATE_90)
imageButtonUp = ImageTk.PhotoImage(image)
image = image.transpose(Image.ROTATE_180)
imageButtonDown = ImageTk.PhotoImage(image)


TopButton = Button(ActionFrame, text="⇧", justify=CENTER, height=29, width=32, image=imageButtonUp, border=0)
TopButton.bind("<Button-1>", lambda event: RunCommand([Up]))
TopButton.place(x=100, y=30)

BottomButton = Button(ActionFrame, text="⇩", justify=CENTER, height=29, width=32, image=imageButtonDown, border=0)
BottomButton.bind("<Button-1>", lambda event: RunCommand([Down]))
BottomButton.place(x=100, y=100)

LeftButton = Button(ActionFrame, text="⇦", justify=CENTER, height=29, width=32, image=imageButtonLeft, border=0)
LeftButton.bind("<Button-1>", lambda event: RunCommand([Left]))
LeftButton.place(x=50, y=65)

RightButton = Button(ActionFrame, text="⇨", justify=CENTER, height=29, width=32, image=imageButtonRight, border=0)
RightButton.bind("<Button-1>", lambda event: RunCommand([Right]))
RightButton.place(x=150, y=65)

view = DHViewer(window, model, options)
view.InitInterface()
view.drawmap()
control = DHController(model, options)

CommandFrame = Frame(ActionFrame)

CommandVar = IntVar()
Cycling = False

def RecreateCommandPanel():
    global CommandFrame, CommandVar
    CommandFrame.destroy()
    CommandFrame = Frame(ActionFrame)
    CommandFrame.place(x=200, y=65)
    if control.CurrentHero is None:
        return
    for i in range(len(control.CurrentHero.Commands)):
        imageUp = control.CurrentHero.Commands[i].ButtonImage
        imageDown = control.CurrentHero.Commands[i].ButtonPressedImage
        rbCommand = Radiobutton(CommandFrame, selectcolor='#ca935a', bg='#ca935a', justify=CENTER, variable=CommandVar, value=i, image=imageUp, selectimage=imageDown, indicatoron=False, anchor=CENTER, bd=0)
        rbCommand.pack(side=LEFT)
    pass

def CurrentCommand():
    return CommandVar.get()

def CheckGameState(state):
    pass

def RunCommand(params):
    global Cycling
    if Cycling:
        return
    if control.CurrentHero is not None:
        control.RunCommand(CurrentCommand(), params)
        view.drawmap()
    if control.CurrentHero is None:
        Cycling = True
        while model.tic() != ENDOFCYCLE:
            window.after(500)
            view.drawmap()
        Cycling = False
        control.CurrentHero = model.Heroes[0]
    RecreateCommandPanel()

def KeyPress(event):
    if gameEnded or Cycling:
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
