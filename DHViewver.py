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
            HeroFrame = Frame(HeroesFrame)
            HeroFrame.place(x=0, y=self.model.Heroes.index(Hero) * 160)


            InventoryFrame = Frame(HeroFrame)
            InventoryFrame.grid(column=0, row=1)
            BigSlotLabel = Label(InventoryFrame)
            BigSlotLabel.config(image=self.BigSlotPhoto)
            BigSlotLabel.pack(side=TOP)

            SmallSlotLabel = Label(InventoryFrame)
            SmallSlotLabel.config(image=self.SmallSlotPhoto)
            SmallSlotLabel.pack(side=TOP)

            SmallSlotLabel = Label(InventoryFrame)
            SmallSlotLabel.config(image=self.SmallSlotPhoto)
            SmallSlotLabel.pack(side=TOP)

            HeroLabel = Label(HeroFrame)
            HeroLabel.grid(column=2, row=1)
            HeroLabel.config(image=Hero.PresenterImage)

            HeadLabel = Label(HeroFrame)
            HeadLabel.config(image=self.HeadTemplatePhoto)
            HeadLabel.grid(column=2, row=0)

            TorsoLabel = Label(HeroFrame)
            TorsoLabel.config(image=self.TorsoTemplatePhoto)
            TorsoLabel.grid(column=1, row=1)

            HandsFrame = Frame(HeroFrame)
            HandsFrame.grid(column=4, row=1)

            RightHandLabel = Label(HandsFrame)
            RightHandLabel.config(image=self.RHtemplatePhoto)
            RightHandLabel.pack(side=TOP)

            LeftHandLabel = Label(HandsFrame)
            LeftHandLabel.config(image=self.LHtemplatePhoto)
            LeftHandLabel.pack(side=TOP)

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
