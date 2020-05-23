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
hero1 = Knight(1, 0, None)
hero2 = Barbarian(0, 0, None)
goathorn = Goathorn(5, 0, None)
model = DHModeller([hero1, hero2], [goathorn], options)
hero1.model = model
hero2.model = model
goathorn.model = model

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
TopButton.bind("<Button-1>", lambda event: RunCommand([control.currentHero, Up]))
TopButton.place(x=100, y=30)

BottomButton = Button(ActionFrame, text="⇩", justify=CENTER, height=29, width=32, image=imageButtonDown, border=0)
BottomButton.bind("<Button-1>", lambda event: RunCommand([control.currentHero, Down]))
BottomButton.place(x=100, y=100)

LeftButton = Button(ActionFrame, text="⇦", justify=CENTER, height=29, width=32, image=imageButtonLeft, border=0)
LeftButton.bind("<Button-1>", lambda event: RunCommand([control.currentHero, Left]))
LeftButton.place(x=50, y=65)

RightButton = Button(ActionFrame, text="⇨", justify=CENTER, height=29, width=32, image=imageButtonRight, border=0)
RightButton.bind("<Button-1>", lambda event: RunCommand([control.currentHero, Right]))
RightButton.place(x=150, y=65)

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
    CommandFrame.place(x=200, y=65)
    for i in range(len(control.currentHero.Commands)):
        imageUp = control.currentHero.Commands[i].ButtonImage
        imageDown = control.currentHero.Commands[i].ButtonPressedImage
        rbCommand = Radiobutton(CommandFrame, selectcolor='#ca935a', bg='#ca935a', justify=CENTER, variable=CommandVar, value=i, image=imageUp, selectimage=imageDown, indicatoron=False, anchor=CENTER, bd=0)
        rbCommand.pack(side=LEFT)
    pass

def CurrentCommand():
    return CommandVar.get()

def CheckGameState(state):
    pass

def RunCommand(params):
    print(control.currentHero)
    if control.currentHero is not None:
        control.RunCommand(CurrentCommand(), params)
        view.drawmap()
    if control.currentHero is None:

        while model.tic() != ENDOFCYCLE:
            window.after(500)
            view.drawmap()
        control.currentHero = model.Heroes[0]
        RecreateCommandPanel()

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
        RunCommand([control.currentHero, direction])

window.bind("<Key>", KeyPress)


RecreateCommandPanel()

window.mainloop()
