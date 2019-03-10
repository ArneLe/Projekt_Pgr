import tkinter as tki
from PIL import Image, ImageDraw, ImageFont
import numpy as np  # abkürzung
import matplotlib.pyplot as plt

from sys import platform  # um zu checken ob auf Windows oder aufm Raspi, aufm raspi wird die LED`S ausgegeben aufm Windoof ein Fenster.
import time
import hardware
import muster1
import muster2

if platform == "linux" or platform == "linux2":
    import board
    import neopixel
    import LED_Test
#else:
    #import windows

if platform == "linux" or platform == "linux2":
    pixels = neopixel.NeoPixel(board.D18, 34, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

LED_COUNT = 34  # Anzahl LEDS
width = 100
height = 34



def ArrayErstellen():
    column = [0 for x in range(width)]  # erstellen vom Array
    for x in range(width):
        column[x] = bytearray(height * 3 + 1)
    return column


def los(event):
    column = spalte
    print('c', column)
    zeitzwspalten = int(entry_time.get()) / width

    if platform == "linux" or platform == "linux2":
        hardware.LEDAnzeigen(column, width, height, pixels, int(zeitzwspalten))

    elif platform == "win32":

        muster_anzeigen(column, width, height)



def muster_anzeigen(column, width, height):

    root1 = tki.Tk()

    c = tki.Canvas(root1, width=width*10, height=height*10)
    c.pack()

    for x in range(width):
        for y in range(height):  # height ist fest und gegeben durch die leds
            y3 = y * 3
            c.create_rectangle(x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill=_from_rgb((column[x][y3], column[x][y3 + 1], column[x][y3 + 2])))

    root1.mainloop()

def drop(event):
    tki.entry_sv.set(event.data)


def Text(event):
    print("Texteingabe")
    if (e1.get() == ""):
        tki.messagebox.showinfo(message='Bitte geben sie einen Text ein', title='Achtung')
    else:
        b = e1.get()
        img = Image.new('RGBA', (14 * len(b), 36),
                        color='black')  # (mode, Größe, Farbe(geht auch mit RGB Werten) Hier müsste man dann die Anzahl der LEDs wählen???
        fnt = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 25)  # Schriftart wählen, Dateipfad angeben
        d = ImageDraw.Draw(img)

        if (entry_R.get() == "" or entry_G.get() == "" or entry_B.get() == ""):
            d.text((5, 5), b, font=fnt, fill=(Scale_TextfarbeR.get(), Scale_TextfarbeG.get(), Scale_TextfarbeB.get(),
                                              255))  # Position, Text, Schriftart, Farbe
            img.save('images/text.png')
        else:
            d.text((5, 5), b, font=fnt, fill=(
            int(entry_R.get()), int(entry_G.get()), int(entry_B.get()), 255))  # Position, Text, Schriftart, Farbe
            img.save('images/text.png')

        # plt.imshow(img)       Warum auch immer es nicht funktioniert, wenn sie im Text sind
        # plt.show()
        ti = Image.open('images/text.png').convert('RGB')  # textImage
        column = np.asarray(ti)  # textimage Array
        print(column)  # ausgabe array Bildtext
        print(column.shape)  # gibt die höhe und breite des Arrays aus

        # Bild wird neu skaliert, eigentlich nicht notwendig, nur eine Vorsichtsmaßnahme
        newWidth = float(ti.size[0]) / float(ti.size[1]) * LED_COUNT
        ti = ti.resize((int(newWidth), LED_COUNT))
        column = np.asarray(ti)
        print(column)  # zur Überprüfung
        plt.imshow(column)
        plt.show()




def Muster(event):

    global spalte

    print('Muster')
    m = var1.get() + int(var2.get()) + int(var3.get()) + int(var4.get()) + int(var5.get())
    print(m)
    column = ArrayErstellen()

    if (m != 1):
        tki.messagebox.showinfo(message='Bitte nur ein Muster auswählen', title='Achtung')
    elif (var1.get() == 1):  # waagerecht

        print("Muster 1")
    elif (var2.get() == 1):  # senkrecht

        print("Muster 2")
    elif (var3.get() == 1):  # schräge
        column = muster1.saw(width, height, column)
        print("Muster 3")
    elif (var4.get() == 1):  # kleines Karo
        column = muster2.karo(width, height, column)
        print("Muster 4")
    elif (var5.get() == 1):  # großes Karo
        print("Muster 5")

    spalte = column







def Bild1(event):

    print('Bild')
    a = str(tki.entry.get())
    i = Image.open(a[1:-1]).convert('RGB')  # Drag and Drop element

    # i = Image.open(c[:]).convert('RGB') #Hier muss der Dateipfad des Bildes angegeben werden oder via Drag and Drop
    iar = np.asarray(i)  # Image Array
    print(iar)  # gibt das Array aus

    # plt.imshow(iar)
    # plt.show()

    # Bild wird neu skaliert
    newWidth = float(i.size[0]) / float(i.size[1]) * LED_COUNT
    columni = i.resize((int(newWidth), LED_COUNT))
    column = np.asarray(i)
    print('2:', column)  # zur Überprüfung
    plt.imshow(column)
    plt.show()


def Bild2(event):
    print('Bild')
    # a=str(entry.get())
    # i = Image.open(a[1:-1]).convert('RGB')  # Drag and Drop element

    i = Image.open(c[:]).convert('RGB')  # Hier muss der Dateipfad des Bildes angegeben werden oder via Drag and Drop
    iar = np.asarray(i)  # Image Array
    print(iar)  # gibt das Array aus

    # plt.imshow(iar)
    # plt.show()

    # Bild wird neu skaliert
    newWidth = float(i.size[0]) / float(i.size[1]) * LED_COUNT
    i = i.resize((int(newWidth), LED_COUNT))
    column = np.asarray(i)
    print('2:', column)  # zur Überprüfung
    plt.imshow(column)
    plt.show()


def ShowColour(event):
    if (entry_R.get() == "" or entry_G.get() == "" or entry_B.get() == ""):
        label_farbvorschau.config(
            background=_from_rgb((Scale_TextfarbeR.get(), Scale_TextfarbeG.get(), Scale_TextfarbeB.get())))
    else:
        label_farbvorschau.config(background=_from_rgb((int(entry_R.get()), int(entry_G.get()), int(entry_B.get()))))


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def fileoeffnen(event):
    root.filename = tki.filedialog.askopenfilename(initialdir="/", title="selectfile",
                                               filetypes=(("jpeg files"), ("all files", "*.*")))
    label_ausgewaehlteDatei = tki.Label(bildframe, text=root.filename)
    label_ausgewaehlteDatei.grid(row=5, column=0)
    global c
    c = str(root.filename)

    return c
    print(root.filename)



if platform == "linux" or platform == "linux2":

    LED_Test.LEDTest(1, pixels)


root = tki.Tk()

topframe = tki.Frame(root)
topframe.pack(fill="both", expand=True)
# topframe.grid_columnconfigure(1, weight=1)
# topframe.grid_columnconfigure(2, weight=1)
# topframe.grid_columnconfigure(3, weight=1)
topframe.configure(bg="white smoke")

textframe = tki.Frame(root)
textframe.pack(fill="both", expand=True)

textframe.configure(background='snow')

# textframe.grid_columnconfigure(0,weight=1)
textframe.grid_columnconfigure(1, weight=1)
textframe.grid_columnconfigure(2, weight=1)
textframe.grid_columnconfigure(3, weight=1)

musterframe = tki.Frame(root)
musterframe.pack(fill="both", expand=True)
musterframe.configure(background="white smoke")
# musterframe.grid_columnconfigure(0, weight=1)
musterframe.grid_columnconfigure(1, weight=1)
musterframe.grid_columnconfigure(2, weight=1)
musterframe.grid_columnconfigure(3, weight=1)
musterframe.grid_columnconfigure(4, weight=1)
musterframe.grid_columnconfigure(5, weight=1)

bildframe = tki.Frame(root)
bildframe.pack(fill="both", expand=True)
bildframe.configure(background="snow")
# bildframe.grid_columnconfigure(0, weight=1)
bildframe.grid_columnconfigure(1, weight=1)
bildframe.grid_columnconfigure(2, weight=1)
bildframe.grid_columnconfigure(3, weight=1)

# topframe
label_p9 = tki.Label(topframe, width=9, bg="white smoke")
label_p9.grid()
label_p10 = tki.Label(topframe, width=3, bg="white smoke")
label_p10.grid(column=3, row=3)
label_p11 = tki.Label(topframe, width=9, bg="white smoke")
label_p11.grid(row=4)

label_time = tki.Label(topframe, text="Belichtungszeit", bg="white smoke", padx=5, anchor=tki.E)
label_time.grid(row=3, column=1)
entry_time = tki.Entry(topframe, width=7)
entry_time.grid(row=3, column=2)
entry_time.insert(0, 15)
button_los = tki.Button(topframe, text="Los")
button_los.bind("<Button-1>", los)
button_los.grid(row=3, column=4)

# Textframe
label_p = tki.Label(textframe, width=9, bg="snow")
label_p.grid()
label_p4 = tki.Label(textframe, width=9, bg="snow")
label_p4.grid(column=4)
label_p6 = tki.Label(textframe, width=9, bg="snow")
label_p6.grid(row=10)

Text_label = tki.Label(textframe, text="Text", font=("Calibri 15 bold"), bg="snow")
Text_label.grid(row=1, column=1)

button_Text = tki.Button(textframe, text="Text generieren", pady=2)
button_Text.bind("<Button-1>", Text)
button_Text.grid(row=9, column=2)

Label_Text = tki.Label(textframe, text='Texteingabe', bg="snow")
Label_Text.grid(row=2, column=2)
e1 = tki.Entry(textframe)
e1.grid(row=3, column=2)

Label_Farbe = tki.Label(textframe, text="Wähle eine Farbe", bg="snow")
Label_Farbe.grid(row=4, column=2)

# Regler zum Einstellen der Farbe des TExtes
Label_R = tki.Label(textframe, text='R', bg="snow", width=6)
Label_R.grid(row=5, column=1)
Scale_TextfarbeR = tki.Scale(textframe, from_=0, to=255, orient=tki.HORIZONTAL, command=ShowColour, length=500)
Scale_TextfarbeR.grid(row=5, column=2)
entry_R = tki.Entry(textframe, width=6)
entry_R.grid(row=5, column=3)
Label_G = tki.Label(textframe, text='G', bg="snow")
Label_G.grid(row=6, column=1)
Scale_TextfarbeG = tki.Scale(textframe, from_=0, to=255, orient=tki.HORIZONTAL, command=ShowColour, length=500)
Scale_TextfarbeG.grid(row=6, column=2)
entry_G = tki.Entry(textframe, width=6)
entry_G.grid(row=6, column=3)
Label_B = tki.Label(textframe, text='B', bg="snow")
Label_B.grid(row=7, column=1)
Scale_TextfarbeB = tki.Scale(textframe, from_=0, to=255, orient=tki.HORIZONTAL, command=ShowColour, length=500)
Scale_TextfarbeB.grid(row=7, column=2)
entry_B = tki.Entry(textframe, width=6)
entry_B.grid(row=7, column=3)

# image_colour = Image.new('RGB',(14, 14), color = (Scale_TextfarbeR.get(),Scale_TextfarbeG.get(),Scale_TextfarbeB.get()))
# image_colour.save('images/textcolour.png')
# load = Image.open('images/textcolour.png')
# render=Imagetki.PhotoImage(load)
# image_textcolour = tki.Label(textframe, image=render)
# image_textcolour.image = render
# image_textcolour.grid(row=7, column=1)
# image1= PhotoImage(file='images/Jill.JPG')

# label zur Farbvorschau
label_farbvorschau = tki.Label(textframe, background='black', width=5, height=2, pady=2)
label_farbvorschau.grid(row=8, column=2)

button_RGB = tki.Button(textframe, text='Eingabe')
button_RGB.bind("<Button-1>", ShowColour)
button_RGB.grid(row=8, column=3)
# separator = Frame(height=2, bd=1, relief=SUNKEN)
# separator.pack(fill=X, padx=5, pady=5)

# Muster
label_p5 = tki.Label(musterframe, width=9, bg="white smoke")  # platzhalter
label_p5.grid(column=7)
label_p7 = tki.Label(musterframe, width=9, bg="white smoke")  # platzhalter
label_p7.grid(row=2)
label_p8 = tki.Label(musterframe, width=9, bg="white smoke")  # platzhalter
label_p8.grid(row=6)
label_p9 = tki.Label(musterframe, width=9, bg="white smoke")  # platzhalter
label_p9.grid(row=8)

Muster_label = tki.Label(musterframe, text="Muster", font=("Calibri 15 bold"), bg="white smoke")
Muster_label.grid(row=1, column=1)

button_Muster = tki.Button(musterframe, text="Muster generieren")  # Button der die Muster generiert
button_Muster.bind("<Button-1>", Muster)
button_Muster.grid(row=7, column=3)

# Drop Down Menues
Farbe1_Muster1 = tki.StringVar(root)
Farbe1_Muster1.set("Farbe 1")  # default value
Dropdown_Farbe1_Muster1 = tki.OptionMenu(musterframe, Farbe1_Muster1, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe1_Muster1.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster1.grid(row=4, column=1)

Farbe2_Muster1 = tki.StringVar(root)
Farbe2_Muster1.set("Farbe 2")  # default value
Dropdown_Farbe2_Muster1 = tki.OptionMenu(musterframe, Farbe2_Muster1, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe2_Muster1.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster1.grid(row=5, column=1)

Farbe1_Muster2 = tki.StringVar(root)
Farbe1_Muster2.set("Farbe 1")  # default value
Dropdown_Farbe1_Muster2 = tki.OptionMenu(musterframe, Farbe1_Muster2, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe1_Muster2.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster2.grid(row=4, column=2)

Farbe2_Muster2 = tki.StringVar(root)
Farbe2_Muster2.set("Farbe 2")  # default value
Dropdown_Farbe2_Muster2 = tki.OptionMenu(musterframe, Farbe2_Muster2, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe2_Muster2.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster2.grid(row=5, column=2)

Farbe1_Muster3 = tki.StringVar(root)
Farbe1_Muster3.set("Farbe 1")  # default value
Dropdown_Farbe1_Muster3 = tki.OptionMenu(musterframe, Farbe1_Muster3, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe1_Muster3.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster3.grid(row=4, column=3)

Farbe2_Muster3 = tki.StringVar(root)
Farbe2_Muster3.set("Farbe 2")  # default value
Dropdown_Farbe2_Muster3 = tki.OptionMenu(musterframe, Farbe2_Muster3, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe2_Muster3.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster3.grid(row=5, column=3)

Farbe1_Muster4 = tki.StringVar(root)
Farbe1_Muster4.set("Farbe 1")  # default value
Dropdown_Farbe1_Muster4 = tki.OptionMenu(musterframe, Farbe1_Muster4, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe1_Muster4.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster4.grid(row=4, column=4)

Farbe2_Muster4 = tki.StringVar(root)
Farbe2_Muster4.set("Farbe 2")  # default value
Dropdown_Farbe2_Muster4 = tki.OptionMenu(musterframe, Farbe2_Muster4, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe2_Muster4.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster4.grid(row=5, column=4)

Farbe1_Muster5 = tki.StringVar(root)
Farbe1_Muster5.set("Farbe 1")  # default value
Dropdown_Farbe1_Muster5 = tki.OptionMenu(musterframe, Farbe1_Muster5, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe1_Muster5.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster5.grid(row=4, column=5)

Farbe2_Muster5 = tki.StringVar(root)
Farbe2_Muster5.set("Farbe 2")  # default value
Dropdown_Farbe2_Muster5 = tki.OptionMenu(musterframe, Farbe2_Muster5, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe2_Muster5.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster5.grid(row=5, column=5)

# Checkboxen
var1 = tki.IntVar()
chb1 = tki.Checkbutton(musterframe, text="waagerechte Streifen", variable=var1).grid(row=3, column=1, pady=3)
var2 = tki.IntVar()
chb2 = tki.Checkbutton(musterframe, text="senkrechte Streifen", variable=var2).grid(row=3, column=2)
var3 = tki.IntVar()
chb3 = tki.Checkbutton(musterframe, text="Schräge", variable=var3).grid(row=3, column=3)
var4 = tki.IntVar()
chb4 = tki.Checkbutton(musterframe, text="kleines Karo", variable=var4).grid(row=3, column=4)
var5 = tki.IntVar()
chb5 = tki.Checkbutton(musterframe, text="großes Karo", variable=var5).grid(row=3, column=5)

# Platzhalter
label_p2 = tki.Label(bildframe, width=9, bg="snow")
label_p2.grid(row=0, column=0)
label_p3 = tki.Label(bildframe, width=12, bg="snow")
label_p3.grid(row=3, column=1)
label_p4 = tki.Label(bildframe, width=9, bg="snow")
label_p4.grid(row=6, column=4)

label_Bild = tki.Label(bildframe, text="Bild", font=("Calibri 15 bold"), bg="snow")
label_Bild.grid(column=1, row=1)

# Drag and Drop für Bildfunktion
# label_dragndrop=Label(bildframe, text="Drag'n Drop",bg="snow")
# label_dragndrop.grid(row=2, column=2)

# entry_sv = tki.StringVar()
# entry_sv.set('Drop Here...')
# entry = tki.Entry(bildframe, textvar=entry_sv, width=80)
# entry.grid(row=3, column=2, padx=10, pady=10)
# entry.drop_target_register(DND_FILES)
# entry.dnd_bind('<<Drop>>', drop)
# button_Los1=Button(bildframe, text= "Bild generieren",width=18)
# button_Los1.bind("<Button-1>",Bild1)
# button_Los1.grid(row=3, column=3)

# Auswählen einer Datei für Bildfunkton ohne Drag and Drop
label_datei = tki.Label(bildframe, text="Datei auswählen", bg="snow")
label_datei.grid(row=3, column=2)
button_Bildoeffnen = tki.Button(bildframe, text="öffnen")
button_Bildoeffnen.bind("<Button-1>", fileoeffnen)
button_Bildoeffnen.grid(row=4, column=2)
button_Los2 = tki.Button(bildframe, text="Bild generieren", width=18)
button_Los2.bind("<Button-1>", Bild2)
button_Los2.grid(row=4, column=3)

tki.mainloop()