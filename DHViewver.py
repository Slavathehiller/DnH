from tkinter import*
from PIL import Image, ImageTk
from Options import*

class DHViewer:
    options = None
    Map = []
    BackgroundRaw = []
    BackgroundPhoto = []
    outviget = None
    model = None
    BigSlotPhoto = None
    SmallSlotPhoto = None
    HeadTemplatePhoto = None
    TorsoTemplatePhoto = None
    RHtemplatePhoto = None
    LHtemplatePhoto = None
    HeroPanelPhoto = None
    MessagePanelPhoto = None
    Timer = None
    HeroesInterfaces = []
    currentHero = None

    def __init__(self, outviget, model, options):
        self.outviget = outviget
        self.model = model
        self.options = options
        BigSlotImage = Image.open('BigSlot.png')
        self.BigSlotPhoto = ImageTk.PhotoImage(BigSlotImage)
        SmallSlotImage = Image.open('SmallSlot.png')
        self.SmallSlotPhoto = ImageTk.PhotoImage(SmallSlotImage)
        HeadTemplate = Image.open('HeadTemplate.png')
        self.HeadTemplatePhoto = ImageTk.PhotoImage(HeadTemplate)
        TorsoTemplate = Image.open('TorsoTemplate.png')
        self.TorsoTemplatePhoto = ImageTk.PhotoImage(TorsoTemplate)
        RHtemplate = Image.open('RHandTemplate.png')
        self.RHtemplatePhoto = ImageTk.PhotoImage(RHtemplate)
        LHtemplate = Image.open('LHandTemplate.png')
        self.LHtemplatePhoto = ImageTk.PhotoImage(LHtemplate)

    def RefreshHeroInterface(self):
        #print("CurrentHeroIndex", self.model.CurrentHeroIndex)
        if self.model.CurrentHeroIndex is None:
            return
        HeroIndex = self.model.CurrentHeroIndex
        #print("HeroIndex", HeroIndex)
        if self.model.Heroes[HeroIndex].Weapon is not None:
            print("Weapon.BaseImage", self.model.Heroes[HeroIndex].Weapon.BaseImage)
            self.HeroesInterfaces[HeroIndex][RHAND].config(image=self.model.Heroes[HeroIndex].Weapon.PhotoImage)
        else:
            self.HeroesInterfaces[HeroIndex][RHAND].config(image=self.RHtemplatePhoto)



    def InitInterface(self):
        HeroesFrame = Frame(self.outviget)
        HeroesFrame.pack(fill=BOTH, side=LEFT)
        HeroPalenBackground = Label(HeroesFrame)
        image = Image.open("HeroPanelImage.png")
        self.HeroPanelPhoto = ImageTk.PhotoImage(image)
        HeroPalenBackground.config(image=self.HeroPanelPhoto, bd=0)
        HeroPalenBackground.pack()

        FieldFrame = Frame(self.outviget)
        FieldFrame.pack(fill=BOTH, side=LEFT)
        self.BackgroundRaw = []
        self.BackgroundPhoto = []
        mapImage = Image.open('map_stone.png').convert('RGBA')
        splitterImage = Image.open('VerticalSplitter.png').convert('RGBA')
        mapImage.paste(splitterImage, (-20, 0,), splitterImage)
        mapImage.paste(splitterImage, (740, 0,), splitterImage)

        MessageFrame = Frame(self.outviget)
        MessageFrame.pack(fill=BOTH, side=LEFT)
        MessageBackground = Label(MessageFrame)
        image = Image.open("MessagePanelImage.png").convert('RGBA')
        self.MessagePanelPhoto = ImageTk.PhotoImage(image)
        MessageBackground.config(image=self.MessagePanelPhoto)
        MessageBackground.pack()


        for y in range(self.options.sizeY):  # Разрезаем карту на квадратики и сохраняем квадратики в списке
            ImageLine = list()  # Создаем игровое поле в виде набора меток, содержащих фрагменты карты
            PhotoImageLine = list()
            LineFrame = Frame(FieldFrame)
            LineFrame.pack(side=TOP)
            VisualLine = list()
            for x in range(self.options.sizeX):
                SquareImage = mapImage.crop((x * 50, y * 50, x * 50 + 50, y * 50 + 50))
                ImageLine.append(SquareImage)
                SquarePhotoImage = ImageTk.PhotoImage(SquareImage)
                PhotoImageLine.append(SquarePhotoImage)
                SquareLabel = Label(LineFrame, bd=0)
                SquareLabel.config(image=SquarePhotoImage)
                SquareLabel.pack(side=LEFT)
                VisualLine.append(SquareLabel)
            self.BackgroundRaw.append(ImageLine)
            self.BackgroundPhoto.append(PhotoImageLine)
            self.Map.append(VisualLine)

        for Hero in self.model.Heroes:

            HeroInterface = []

            HeroIndex = self.model.Heroes.index(Hero)
            CoordMultiplier = 170

            InventoryFrame = Frame(HeroesFrame)
            InventoryFrame.place(x=5, y=HeroIndex * CoordMultiplier + 50)
            BigSlotLabel = Label(InventoryFrame)
            BigSlotLabel.config(image=self.BigSlotPhoto, bd=0)
            BigSlotLabel.pack(side=TOP)
            HeroInterface.append(BigSlotLabel)

            SmallSlotLabel = Label(InventoryFrame)
            SmallSlotLabel.config(image=self.SmallSlotPhoto, bd=0)
            SmallSlotLabel.pack(side=TOP)
            HeroInterface.append(SmallSlotLabel)

            SmallSlotLabel = Label(InventoryFrame)
            SmallSlotLabel.config(image=self.SmallSlotPhoto, bd=0)
            SmallSlotLabel.pack(side=TOP)
            HeroInterface.append(SmallSlotLabel)

            HeroLabel = Label(HeroesFrame)
            HeroLabel.place(x=87, y=HeroIndex * CoordMultiplier + 50)
            HeroLabel.config(image=Hero.PresenterImage)

            HeadLabel = Label(HeroesFrame)
            HeadLabel.config(image=self.HeadTemplatePhoto, bd=0)
            HeadLabel.place(x=105, y=HeroIndex * CoordMultiplier)
            HeroInterface.append(HeadLabel)

            TorsoLabel = Label(HeroesFrame)
            TorsoLabel.config(image=self.TorsoTemplatePhoto, bd=0)
            TorsoLabel.place(x=36, y=HeroIndex * CoordMultiplier + 50)
            HeroInterface.append(TorsoLabel)

            HandsFrame = Frame(HeroesFrame)
            HandsFrame.place(x=170, y=HeroIndex * CoordMultiplier + 50)

            RightHandLabel = Label(HandsFrame)
            RightHandLabel.config(image=self.RHtemplatePhoto, bd=0)
            RightHandLabel.pack(side=TOP)
            HeroInterface.append(RightHandLabel)

            LeftHandLabel = Label(HandsFrame)
            LeftHandLabel.config(image=self.LHtemplatePhoto, bd=0)
            LeftHandLabel.pack(side=TOP)
            HeroInterface.append(LeftHandLabel)

            self.HeroesInterfaces.append(HeroInterface)

    def PlaceObjects(self, x, y, objects):
        image = self.BackgroundRaw[y][x].copy()
        for currentObject in objects:
            pasteImage = currentObject.GetCurrentImage()
            image.paste(pasteImage, (0, 0, 50, 50), pasteImage)
        self.BackgroundPhoto[y][x] = ImageTk.PhotoImage(image)
        self.Map[y][x].config(image=self.BackgroundPhoto[y][x])
        self.Map[y][x].update()

    def drawmap(self):
        for y in range(self.options.sizeY):
            for x in range(self.options.sizeX):
                objects = self.model.GetObjectsAt(x, y)
                self.PlaceObjects(x, y, objects)
        self.RefreshHeroInterface()
