from tkinter import*
from PIL import Image, ImageTk
from Options import*
from Goathorn import*
from Swinemar import*
from Knight import*
from Barbarian import*
from DHViewver import*
from DHModeller import*
from DHController import*
from Command import*
from Armor import*
from Shield import*

window = Tk()
window.geometry('1200x640')
window.title('Подземелья и герои')
window.resizable(width=False, height=False)
window.iconbitmap('DnH.ico')
window.config(bg='#ca935a')

gameEnded = False

image = Image.open("Opening.jpg")
opening = ImageTk.PhotoImage(image)

image = Image.open("ArrowButton.png").convert('RGBA')
imageButtonLeft = ImageTk.PhotoImage(image)
image = image.transpose(Image.FLIP_LEFT_RIGHT)
imageButtonRight = ImageTk.PhotoImage(image)
image = image.transpose(Image.ROTATE_90)
imageButtonUp = ImageTk.PhotoImage(image)
image = image.transpose(Image.ROTATE_180)
imageButtonDown = ImageTk.PhotoImage(image)

image = Image.open("ActionPanelImage.png").convert('RGBA')
APImage = ImageTk.PhotoImage(image)

MainMenuWindowShowed = False

def MainMenu(roomBattle):
    global MainMenuWindowShowed
    MainMenuWindow = Toplevel()
    MainMenuWindow.geometry('604x386+350+100')
    MainMenuWindow.title('Главное меню')
    MainMenuWindow.iconbitmap('DnH.ico')
    MainMenuWindow.resizable(width=False, height=False)
    BackgroundLabel = Label(MainMenuWindow)
    BackgroundLabel.config(image=opening)
    BackgroundLabel.pack()
    MainMenuWindowShowed = True

    NewGame = Button(MainMenuWindow, text="Новая игра", justify=CENTER, height=1, width=35)
    NewGame.bind("<Button-1>")
    NewGame.place(x=190, y=60)
    NewGame.configure(state=DISABLED)

    ContinueGame = Button(MainMenuWindow, text="Продолжить игру", justify=CENTER, height=1, width=35)
    ContinueGame.bind("<Button-1>")
    ContinueGame.place(x=190, y=90)
    ContinueGame.configure(state=DISABLED)

    Settings = Button(MainMenuWindow, text="Настройки", justify=CENTER, height=1, width=35)
    Settings.bind("<Button-1>")
    Settings.place(x=190, y=120)

    TechnoDemo = Button(MainMenuWindow, text="Технодемо", justify=CENTER, height=1, width=35)
    TechnoDemo.bind("<Button-1>", lambda event: RunTechnoDemo())
    TechnoDemo.place(x=190, y=150)

    Exit = Button(MainMenuWindow, text="Выход", justify=CENTER, height=1, width=35)
    Exit.bind("<Button-1>", lambda event: exit(0))
    Exit.place(x=190, y=180)
    MainMenuWindow.lift()
    MainMenuWindow.focus_force()
    MainMenuWindow.attributes("-topmost", True)

    def RunTechnoDemo():
        global MainMenuWindowShowed
        roomBattle()
        MainMenuWindowShowed = False
        MainMenuWindow.destroy()
        window.lift()
        window.attributes("-topmost", True)
        window.focus_force()
        window.mainloop()

    def KeyPress(event):
        global MainMenuWindowShowed
        if event.keysym == "Escape":
            MainMenuWindowShowed = False
            MainMenuWindow.destroy()
            window.lift()
            window.attributes("-topmost", True)
            window.focus_force()
            window.mainloop()

    MainMenuWindow.bind("<Key>", KeyPress)


ViewFrame = Frame(window)
MainBackgroundLabel = Label(ViewFrame)
ViewFrame.pack(side=TOP, fill=BOTH)

Cycling = False
def RoomBattle():
    options = SimpleOptions()
    hero1 = Knight(1, 0, None)
    hero1.Weapon = Sword(-1, -1)
    hero1.Helm = HeavyHelm(0, 0)
    hero1.Torso = HeavyArmor(-1, 0)
    hero1.Shield = Shield(-2, 0)
    hero2 = Barbarian(0, 0, None)
    hero2.Helm = LightHelm(-2, 0)
    hero2.Weapon = Mace(-2, -2)
    #hero3 = Knight(2, 0, None)
    goathorn = Goathorn(5, 0, None)
    swinemar = Swinemar(3, 0, None)
    model = DHModeller([hero1, hero2], [goathorn, swinemar], options)
    model.CurrentHeroIndex = 0
    view = DHViewer(window, model, options)
    view.InitInterface()
    view.drawmap()
    control = DHController(model, options)

    def CurrentCommand():
        return CommandVar.get()

    CommandVar = IntVar()

    def RecreateCommandPanel(commandVar):
        global CommandFrame
        CommandFrame.destroy()
        CommandFrame = Frame(ActionFrame)
        CommandFrame.place(x=200, y=65)
        if control.CurrentHero is None:
            return
        for i in range(len(control.CurrentHero.Commands)):
            imageUp = control.CurrentHero.Commands[i].ButtonImage
            imageDown = control.CurrentHero.Commands[i].ButtonPressedImage
            rbCommand = Radiobutton(CommandFrame, selectcolor='#ca935a', bg='#ca935a', justify=CENTER, variable=commandVar, value=i, image=imageUp, selectimage=imageDown, indicatoron=False, anchor=CENTER, bd=0)
            rbCommand.pack(side=LEFT)

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
            view.drawmap()
        RecreateCommandPanel(CommandVar)

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
        elif event.keysym == "Escape":
            print(MainMenuWindowShowed)
            if not MainMenuWindowShowed:
                MainMenu(RoomBattle)
            return
        if not gameEnded:
            RunCommand([direction])

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

    RecreateCommandPanel(CommandVar)
    window.bind("<Key>", KeyPress)

ActionFrame = Frame(window)

ActionPanelBackground = Label(ActionFrame)
ActionPanelBackground.config(image=APImage, bd=0)
ActionPanelBackground.pack()
ActionFrame.pack(side=BOTTOM, fill=BOTH)

CommandFrame = Frame(ActionFrame)

MainMenu(RoomBattle)

window.mainloop()
