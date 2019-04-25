import tkinter as tki
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import numpy as np  # abkürzung
import matplotlib.pyplot as plt

from sys import platform  # um zu checken ob auf Windows oder aufm Raspi, aufm raspi wird die LED`S ausgegeben aufm Windoof ein Fenster.
import time
import hardware
import muster1


if platform == "linux" or platform == "linux2":
    import board
    import neopixel
    import LED_Test


if platform == "linux" or platform == "linux2":
    pixels = neopixel.NeoPixel(board.D18, 34, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

LED_COUNT = 34  # Anzahl LEDS
width = 100
height = 34



def ArrayErstellen():
    global column
    colum = None            # löscht alle Daten die noch in derm Array seien könnten
    column = [0 for x in range(width)]  # erstellen vom Array
    for x in range(width):
        column[x] = bytearray(height * 3 + 1)

ArrayErstellen()

def los(event): #sorgt dafür, dass die LEDs gestartet werden
    print('c', column)
    zeitzwspalten = int(entry_time.get()) / width
    print(zeitzwspalten)

    if platform == "linux" or platform == "linux2":
        hardware.LEDAnzeigen(column, width, height, pixels, float(zeitzwspalten))

    elif platform == "win32":

        muster_anzeigen(column, width, height)



def muster_anzeigen(column, width, height): #Funktion zum Überprüfen der Grafiken am PC

    root1 = tki.Tk()

    c = tki.Canvas(root1, width=width*10, height=height*10)
    c.pack()

    for x in range(width):
        for y in range(height):  # height ist fest und gegeben durch die leds
            y3 = y * 3
            c.create_rectangle(x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill=_from_rgb((column[x][y3], column[x][y3 + 1], column[x][y3 + 2])))

    root1.mainloop()



def Text(event):    #erstellen des Textes
    global column
    print("Texteingabe")
    if (e1.get() == ""):    #Warnung
        tki.messagebox.showinfo(message='Bitte geben sie einen Text ein', title='Achtung')
    else:
        b = e1.get()
        img = Image.new('RGBA', (14 * len(b), height),
                        color='black')      #schwarzes Bld erstellen

        if platform == "linux" or platform == "linux2":
            fnt = ImageFont.truetype('/usr/share/fonts/truetype/crosextra/Caladea-Regular.ttf', 25)  # Calibir ist auf raspi nicht vorhanfen
        else:
            fnt = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 25)  # Schriftart wählen, Dateipfad angeben
        d = ImageDraw.Draw(img)

        if (entry_R.get() == "" or entry_G.get() == "" or entry_B.get() == ""): # wenn keine Werte eingegeben sind, dann nehme die Ferte von den Schiebebalken
            d.text((5, 5), b, font=fnt, fill=(Scale_TextfarbeR.get(), Scale_TextfarbeG.get(), Scale_TextfarbeB.get(),255))  # Position, Text, Schriftart, Farbe
            img.save('images/text.png')
        else: # sonst nehme die eingegebenen Werte
            d.text((5, 5), b, font=fnt, fill=(
            int(entry_R.get()), int(entry_G.get()), int(entry_B.get()), 255))  # Position, Text, Schriftart, Farbe
            img.save('images/text.png')


        ti = Image.open('images/text.png').convert('RGB')  # textImage

        coulumnbild = np.asarray(ti)
        global width

        print(coulumnbild)
        width = int(14 * len(b))
        ArrayErstellen()

        for x in range(0, width, +1):
            for y in range(0, height, +1):
                y3 = y * 3
                column[x][y3] = coulumnbild[y][x][0]
                column[x][y3 + 1] = coulumnbild[y][x][1]
                column[x][y3 + 2] = coulumnbild[y][x][2]

        #plt.imshow(column)
       # plt.show()




def Muster(event):

    global column
    #Welche Farbe wurde ausgewählt? Setze RGB-Werte
    if (Farbe1_Muster1.get()=="rot"):
        print('Farbe rot')
        a=0
        b=255
        c=0
    if (Farbe1_Muster1.get()=="pink"):
        a=0
        b=255
        c=255
    if (Farbe1_Muster1.get()=="weiß"):
        a=255
        b=255
        c=255
    if (Farbe1_Muster1.get()=="grün"):
        a=255
        b=0
        c=0
    if (Farbe1_Muster1.get()=="hellblau"):
        a=255
        b=0
        c=255
    if (Farbe1_Muster1.get()=="schwarz"):
        a=0
        b=0
        c=0
    if (Farbe1_Muster1.get()=="dunkelblau"):
        a=0
        b=0
        c=255
    if (Farbe1_Muster1.get()=="gelb"):
        a=255
        b=255
        c=0
    if (Farbe1_Muster1.get()=="orange"):
        a=125
        b=255
        c=0

    if (Farbe2_Muster1.get()=="rot"):
        d=0
        e=255
        f=0
    if (Farbe2_Muster1.get()=="pink"):
        d=0
        e=255
        f=255
    if (Farbe2_Muster1.get()=="weiß"):
        d=255
        e=255
        f=255
    if (Farbe2_Muster1.get()=="grün"):
        d=255
        e=0
        f=0
    if (Farbe2_Muster1.get()=="hellblau"):
        d=255
        e=0
        f=255
    if (Farbe2_Muster1.get()=="schwarz"):
        d=0
        e=0
        f=0
    if (Farbe2_Muster1.get()=="dunkelblau"):
        d=0
        e=0
        f=255
    if (Farbe2_Muster1.get()=="gelb"):
        d=255
        e=255
        f=0
    if (Farbe2_Muster1.get()=="orange"):
        d=125
        e=255
        f=0
        
    Farbe2_Muster1.get()
    print('Muster')
    m = var1.get() + int(var2.get()) + int(var3.get()) + int(var4.get()) + int(var5.get())
    print(m)
    x=int(var6.get()) # Farbverlauf Hacken
    global width
    width = int(entry_pixel.get())+1
    ArrayErstellen()
    if (m != 1):
        tki.messagebox.showinfo(message='Bitte nur ein Muster auswählen', title='Achtung')  #Warnung, wenn zu viele oder kein Muster ausgewählt wurde
    elif (var1.get() == 1):  # waagerecht
        column = muster1.waagerecht(int(entry_pixel.get()), height, column, a, b, c, d, e, f,x)
        print("Muster 1")
    elif (var2.get() == 1):  # senkrecht
        column = muster1.senkrecht(int(entry_pixel.get()), height, column, a, b, c, d, e, f,x)
        print("Muster 2")
    elif (var3.get() == 1):  # schräge
        column = muster1.saw(int(entry_pixel.get()), height, column, a, b, c, d, e, f,x)
        print("Muster 3")
    elif (var4.get() == 1):  # kleines Karo
        column = muster1.karo(int(entry_pixel.get()), height, column, a, b, c, d, e, f,x) #rgb werte der beiden Farben
        print("Muster 4")
    elif (var5.get() == 1): # REGENBOGEN
        column = muster1.regenbogen(width, height, column)
        print("Muster 5")

def Bild2(event):
    print('Bild')

    i = Image.open(c[:]).convert('RGB')  # Hier muss der Dateipfad des Bildes angegeben werden
    iar = np.asarray(i)  # Image Array
    print(iar)  # gibt das Array aus


    # Bild wird neu skaliert
    newWidth = float(i.size[0]) / float(i.size[1]) * LED_COUNT
    i = i.resize((int(newWidth), LED_COUNT))

    # np.asarray(i) muss umgerechnet werden
    coulumnbild = np.asarray(i)

    global width
    print(coulumnbild)
    width = int(newWidth)
    ArrayErstellen()

    for x in range(0, width, +1):
        for y in range(0, height, +1):
            y3 = y * 3
            column[x][y3] = coulumnbild[y][x][0]
            column[x][y3 + 1] = coulumnbild[y][x][1]
            column[x][y3 + 2] = coulumnbild[y][x][2]


    print('2:', column)  # zur Überprüfung
    #plt.imshow(column)
    #plt.show()


def ShowColour(event):      #Farbvorschau
    if (entry_R.get() == "" or entry_G.get() == "" or entry_B.get() == ""):
        label_farbvorschau.config(
            background=_from_rgb((Scale_TextfarbeR.get(), Scale_TextfarbeG.get(), Scale_TextfarbeB.get()))) #Farbe von Schiebebalken
    else:
        label_farbvorschau.config(background=_from_rgb((int(entry_R.get()), int(entry_G.get()), int(entry_B.get())))) #eingegebene Werte


def _from_rgb(rgb): #rgb in Hexa
    return "#%02x%02x%02x" % rgb


def fileoeffnen(event):     #öffnen von Dateien
    if platform == "linux" or platform == "linux2":
        root.filename = tki.filedialog.askopenfilename(initialdir="/media/pi", title="selectfile",filetypes=(("jpeg files", "*.jpg;*.jpeg;*.png"), ("all files", "*.*")))
    else:
        root.filename = tki.filedialog.askopenfilename(initialdir="/", title="selectfile",filetypes=(("jpeg files", "*.jpg;*.jpeg;*.png"), ("all files", "*.*")))

    label_ausgewaehlteDatei = tki.Label(bildframe, text=root.filename)
    label_ausgewaehlteDatei.grid(row=5, column=0)
    global c    #c wird in der Bild-Funktion benötigt
    c = str(root.filename)

    return c
    print(root.filename)



if platform == "linux" or platform == "linux2":

    LED_Test.LEDTest(1, pixels)


root = tki.Tk()
root.title('Lichtpinsel')


topframe = tki.Frame(root)
topframe.pack(fill="both", expand=True)
topframe.configure(bg="white smoke")

textframe = tki.Frame(root)
textframe.pack(fill="both", expand=True)
textframe.configure(background='snow')

#Gewichtung der Spalten festlegen
textframe.grid_columnconfigure(1, weight=1)
textframe.grid_columnconfigure(2, weight=1)
textframe.grid_columnconfigure(3, weight=1)

musterframe = tki.Frame(root)
musterframe.pack(fill="both", expand=True)
musterframe.configure(background="white smoke")
musterframe.grid_columnconfigure(1, weight=1)
musterframe.grid_columnconfigure(2, weight=1)
musterframe.grid_columnconfigure(3, weight=1)
musterframe.grid_columnconfigure(4, weight=1)
musterframe.grid_columnconfigure(5, weight=1)

bildframe = tki.Frame(root)
bildframe.pack(fill="both", expand=True)
bildframe.configure(background="snow")
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
#Platzhalter
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
Scale_TextfarbeR = tki.Scale(textframe, from_=0, to=255, orient=tki.HORIZONTAL, command=ShowColour, length=500)#
Scale_TextfarbeR.set(255)
Scale_TextfarbeR.grid(row=5, column=2)
entry_R = tki.Entry(textframe, width=6)
entry_R.grid(row=5, column=3)
Label_G = tki.Label(textframe, text='G', bg="snow")
Label_G.grid(row=6, column=1)
Scale_TextfarbeG = tki.Scale(textframe, from_=0, to=255, orient=tki.HORIZONTAL, command=ShowColour, length=500)
Scale_TextfarbeG.set(255)
Scale_TextfarbeG.grid(row=6, column=2)
entry_G = tki.Entry(textframe, width=6)
entry_G.grid(row=6, column=3)
Label_B = tki.Label(textframe, text='B', bg="snow")
Label_B.grid(row=7, column=1)
Scale_TextfarbeB = tki.Scale(textframe, from_=0, to=255, orient=tki.HORIZONTAL, command=ShowColour, length=500)
Scale_TextfarbeB.set(255)
Scale_TextfarbeB.grid(row=7, column=2)
entry_B = tki.Entry(textframe, width=6)
entry_B.grid(row=7, column=3)



# label zur Farbvorschau
label_farbvorschau = tki.Label(textframe, background='black', width=5, height=2, pady=2)
label_farbvorschau.grid(row=8, column=2)

#Button zur Vorschau der eingegebenen RGB Werte
button_RGB = tki.Button(textframe, text='Eingabe')
button_RGB.bind("<Button-1>", ShowColour)
button_RGB.grid(row=8, column=3)


# Muster
#Platzhalter
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
Farbe1_Muster1.set("rot")  # default value
Dropdown_Farbe1_Muster1 = tki.OptionMenu(musterframe, Farbe1_Muster1, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe1_Muster1.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster1.grid(row=4, column=1)

Farbe2_Muster1 = tki.StringVar(root)
Farbe2_Muster1.set("weiß")  # default value
Dropdown_Farbe2_Muster1 = tki.OptionMenu(musterframe, Farbe2_Muster1, "rot", "pink", "weiß", "grün", "hellblau", "schwarz",
                                     "dunkelblau", "gelb", "orange")
Dropdown_Farbe2_Muster1.config(width=8)  # legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster1.grid(row=5, column=1)



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
chb5 = tki.Checkbutton(musterframe, text="Regenbogen", variable=var5).grid(row=3, column=5)

#Checkbox Farbverlauf
var6 = tki.IntVar()
chb6 = tki.Checkbutton(musterframe, text="Farbverlauf", variable=var6).grid(row=5, column=2)

#Auswahl der Größe
label_pixel=tki.Label(musterframe, text="Breite in Pixeln")
label_pixel.grid(row=4, column=3)
entry_pixel = tki.Entry(musterframe)
entry_pixel.grid(row=5, column=3)
entry_pixel.insert(0, 100)

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
