from tkinter import *
from tkinter import messagebox, filedialog
import sys
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *
from TkinterDnD2 import *

from PIL import Image, ImageDraw, ImageFont, ImageTk
import numpy as np          #abkürzung
import matplotlib.pyplot as plt

from sys import platform  # um zu checken ob auf Windows oder aufm Raspi, aufm raspi wird die LED`S ausgegeben aufm Windoof ein Fenster.
import time
import hardware
import muster1
import muster2#import board
import neopixel
import LED_Test
import board


#pixels = neopixel.NeoPixel(board.D18, 34, brightness=0.2, auto_write=False,pixel_order = neopixel.GRB)
LED_COUNT=34    #Anzahl LEDS
width = 100
height = 34
pixels = neopixel.NeoPixel(board.D18, 34, brightness=0.2, auto_write=False,pixel_order = neopixel.GRB)


def los(event):
    print ('c',column)
    hardware.LEDAnzeigen(column, width, height,pixels)


def drop(event):
    entry_sv.set(event.data)
    
def Text(event):
    global column
    print("Texteingabe")
    if (e1.get()==""):
        messagebox.showinfo(message='Bitte geben sie einen Text ein', title='Achtung')
    else: 
        b= e1.get()
        img = Image.new('RGBA',(14*len(b), 36), color = 'black') #(mode, Größe, Farbe(geht auch mit RGB Werten) Hier müsste man dann die Anzahl der LEDs wählen???
        fnt= ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf',25) #Schriftart wählen, Dateipfad angeben
        d = ImageDraw.Draw(img)

        if (entry_R.get()=="" or entry_G.get()=="" or entry_B.get()=="" ):
            d.text((5,5), b, font=fnt, fill=(Scale_TextfarbeR.get(),Scale_TextfarbeG.get(),Scale_TextfarbeB.get(),255)) #Position, Text, Schriftart, Farbe
            img.save('images/text.png')
        else:
            d.text((5,5), b, font=fnt, fill=(int(entry_R.get()),int(entry_G.get()),int(entry_B.get()),255)) #Position, Text, Schriftart, Farbe    
            img.save('images/text.png')
   
    #plt.imshow(img)       Warum auch immer es nicht funktioniert, wenn sie im Text sind 
    #plt.show()
        ti = Image.open('images/text.png').convert('RGB')   #textImage
        column = np.asarray(ti)                   #textimage Array
        print(column)                             #ausgabe array Bildtext
        print(column.shape)# gibt die höhe und breite des Arrays aus
        

    # Bild wird neu skaliert, eigentlich nicht notwendig, nur eine Vorsichtsmaßnahme
        newWidth=float(ti.size[0])/float(ti.size[1])*LED_COUNT
        ti=ti.resize((int(newWidth),LED_COUNT))
        column=np.asarray(ti)
        print (column)# zur Überprüfung
        plt.imshow(column)
        plt.show()

def Muster(event):
    print('Muster')
    global column
    column = [0 for x in range(width)] 
    m= var1.get()+var2.get()+var3.get()+var4.get()+var5.get()
    if (m!=1):
        messagebox.showinfo(message='Bitte nur ein Muster auswählen', title='Achtung')
    elif(var1.get()==1):  #waagerecht
        print("Muster 1")  #Hier die entsprechenden Muster eintragen
    elif(var2.get()==1):  #senkrecht
        print("Muster 2")
    elif(var3.get()==1):  #schräge
        print("Muster 3")
    elif(var4.get()==1):  #kleines Karo
        print("Muster 4")
        for x in range(width):
            column[x] = bytearray(height * 3 + 1)
    # wenn der Knopf dann Bild Umwandeln und speichern
    #column = muster1.saw(width, height, column)
        column = muster2.karo(width, height, column)
        #column=np.asarray(column)
        print('clll',column)
        #print('column',column)
        return column
        
    elif(var5.get()==1):  #großes Karo
        print("Muster 5")

def Bild1(event):
    global column
    print('Bild')
    a=str(entry.get())
    i = Image.open(a[1:-1]).convert('RGB')  # Drag and Drop element
    
    #i = Image.open(c[:]).convert('RGB') #Hier muss der Dateipfad des Bildes angegeben werden oder via Drag and Drop
    iar = np.asarray(i)         #Image Array
    print(iar)                  #gibt das Array aus

    #plt.imshow(iar)
    #plt.show()
    
        # Bild wird neu skaliert
    newWidth=float(i.size[0])/float(i.size[1])*LED_COUNT
    columni=i.resize((int(newWidth),LED_COUNT))
    column=np.asarray(i)
    print ('2:',column)# zur Überprüfung
    plt.imshow(column)
    plt.show()

def Bild2(event):
    print('Bild')
    global column
    #a=str(entry.get())
    #i = Image.open(a[1:-1]).convert('RGB')  # Drag and Drop element
    
    i = Image.open(c[:]).convert('RGB') #Hier muss der Dateipfad des Bildes angegeben werden oder via Drag and Drop
    iar = np.asarray(i)         #Image Array
    print(iar)                  #gibt das Array aus

    #plt.imshow(iar)
    #plt.show()
    
        # Bild wird neu skaliert
    newWidth=float(i.size[0])/float(i.size[1])*LED_COUNT
    i=i.resize((int(newWidth),LED_COUNT))
    column=np.asarray(i)
    print ('2:',column)# zur Überprüfung
    plt.imshow(column)
    plt.show()

def ShowColour(event):
    if (entry_R.get()=="" or entry_G.get()=="" or entry_B.get()=="" ):
        label_farbvorschau.config(background=_from_rgb((Scale_TextfarbeR.get(),Scale_TextfarbeG.get(),Scale_TextfarbeB.get())))
    else:
        label_farbvorschau.config(background=_from_rgb((int(entry_R.get()),int(entry_G.get()),int(entry_B.get()))))
        
    
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def fileoeffnen(event):
    root.filename = filedialog.askopenfilename(initialdir = "/", title= "selectfile", filetypes=(("jpeg files"),("all files","*.*")))
    label_ausgewaehlteDatei=Label(bildframe,text=root.filename)
    label_ausgewaehlteDatei.grid(row=5, column=0)
    global c
    c=str(root.filename)
   
    return c
    print(root.filename)

root = TkinterDnD.Tk()

topframe=Frame(root)
topframe.pack(fill="both", expand=True)
#topframe.grid_columnconfigure(1, weight=1)
#topframe.grid_columnconfigure(2, weight=1)
#topframe.grid_columnconfigure(3, weight=1)
topframe.configure(bg="white smoke")

textframe=Frame(root)
textframe.pack(fill="both", expand=True)

textframe.configure(background='snow')


 


#textframe.grid_columnconfigure(0,weight=1)
textframe.grid_columnconfigure(1,weight=1)
textframe.grid_columnconfigure(2,weight=1)
textframe.grid_columnconfigure(3,weight=1)

musterframe=Frame(root)
musterframe.pack(fill="both", expand=True)
musterframe.configure(background="white smoke")
#musterframe.grid_columnconfigure(0, weight=1)
musterframe.grid_columnconfigure(1, weight=1)
musterframe.grid_columnconfigure(2, weight=1)
musterframe.grid_columnconfigure(3, weight=1)
musterframe.grid_columnconfigure(4, weight=1)
musterframe.grid_columnconfigure(5, weight=1)

bildframe=Frame(root)
bildframe.pack(fill="both", expand=True)
bildframe.configure(background="snow")
#bildframe.grid_columnconfigure(0, weight=1)
bildframe.grid_columnconfigure(1, weight=1)
bildframe.grid_columnconfigure(2, weight=1)
bildframe.grid_columnconfigure(3, weight=1)

#topframe
label_p9=Label(topframe, width=9, bg="white smoke")
label_p9.grid()
label_p10=Label(topframe, width=3, bg="white smoke")
label_p10.grid(column=3,row=3)
label_p11=Label(topframe, width=9, bg="white smoke")
label_p11.grid(row=4)

label_time=Label(topframe, text="Belichtungszeit", bg="white smoke",padx=5,anchor=E)
label_time.grid(row=3, column=1)
entry_time=Entry(topframe, width=7)
entry_time.grid(row=3, column=2)
button_los=Button(topframe, text="Los")
button_los.bind("<Button-1>",los)
button_los.grid(row=3, column=4)

#Textframe
label_p=Label(textframe,width=9, bg="snow")
label_p.grid()
label_p4=Label(textframe,width=9, bg="snow")
label_p4.grid(column=4)
label_p6=Label(textframe,width=9, bg="snow")
label_p6.grid(row=10)

Text_label=Label(textframe, text="Text",font=("Calibri 15 bold"),bg="snow")
Text_label.grid(row=1, column= 1)

button_Text = Button(textframe, text="Text generieren", pady=2)
button_Text.bind("<Button-1>",Text)
button_Text.grid(row=9,column=2)

Label_Text=Label(textframe, text='Texteingabe', bg="snow")
Label_Text.grid(row=2, column=2)
e1=Entry(textframe)
e1.grid(row=3, column=2)

Label_Farbe = Label(textframe, text="Wähle eine Farbe", bg="snow")
Label_Farbe.grid(row=4, column=2)


# Regler zum Einstellen der Farbe des TExtes
Label_R=Label(textframe, text='R', bg="snow", width=6)
Label_R.grid(row=5,column=1)
Scale_TextfarbeR= Scale(textframe, from_=0, to=255, orient=HORIZONTAL, command=ShowColour,length=500)
Scale_TextfarbeR.grid(row=5, column=2)
entry_R= Entry(textframe, width=6)
entry_R.grid(row=5, column=3)
Label_G=Label(textframe, text='G', bg="snow")
Label_G.grid(row=6, column=1)
Scale_TextfarbeG= Scale(textframe, from_=0, to=255, orient=HORIZONTAL,command=ShowColour,length=500)
Scale_TextfarbeG.grid(row=6, column=2)
entry_G= Entry(textframe, width=6)
entry_G.grid(row=6, column=3)
Label_B=Label(textframe, text='B', bg="snow")
Label_B.grid(row=7, column=1)
Scale_TextfarbeB= Scale(textframe, from_=0, to=255, orient=HORIZONTAL,command=ShowColour,length=500)
Scale_TextfarbeB.grid(row=7, column=2)
entry_B= Entry(textframe, width=6)
entry_B.grid(row=7, column=3)

    #image_colour = Image.new('RGB',(14, 14), color = (Scale_TextfarbeR.get(),Scale_TextfarbeG.get(),Scale_TextfarbeB.get()))
    #image_colour.save('images/textcolour.png')
    #load = Image.open('images/textcolour.png')
    #render=ImageTk.PhotoImage(load)
    #image_textcolour = Label(textframe, image=render)
    #image_textcolour.image = render
    #image_textcolour.grid(row=7, column=1)
#image1= PhotoImage(file='images/Jill.JPG')

#label zur Farbvorschau
label_farbvorschau=Label(textframe, background='black', width=5,height=2,pady=2)
label_farbvorschau.grid(row=8, column=2)

button_RGB = Button(textframe, text='Eingabe')
button_RGB.bind("<Button-1>", ShowColour)
button_RGB.grid(row=8, column=3)
#separator = Frame(height=2, bd=1, relief=SUNKEN)
#separator.pack(fill=X, padx=5, pady=5)

#Muster
label_p5=Label(musterframe,width=9, bg="white smoke")  #platzhalter
label_p5.grid(column=7)
label_p7=Label(musterframe,width=9, bg="white smoke")  #platzhalter
label_p7.grid(row=2)
label_p8=Label(musterframe,width=9, bg="white smoke")  #platzhalter
label_p8.grid(row=6)
label_p9=Label(musterframe,width=9, bg="white smoke")  #platzhalter
label_p9.grid(row=8)

Muster_label=Label(musterframe, text="Muster",font=("Calibri 15 bold"),bg="white smoke")
Muster_label.grid(row=1, column= 1)

button_Muster = Button(musterframe, text="Muster generieren")   #Button der die Muster generiert
button_Muster.bind("<Button-1>",Muster)
button_Muster.grid(row=7, column=3)

#Drop Down Menues
Farbe1_Muster1 = StringVar(root)
Farbe1_Muster1.set("Farbe 1") # default value
Dropdown_Farbe1_Muster1 = OptionMenu(musterframe,Farbe1_Muster1, "rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe1_Muster1.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster1.grid(row=4,column=1)

Farbe2_Muster1 = StringVar(root)
Farbe2_Muster1.set("Farbe 2") # default value
Dropdown_Farbe2_Muster1 = OptionMenu(musterframe,Farbe2_Muster1,"rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe2_Muster1.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster1.grid(row=5,column=1)

Farbe1_Muster2 = StringVar(root)
Farbe1_Muster2.set("Farbe 1") # default value
Dropdown_Farbe1_Muster2 = OptionMenu(musterframe, Farbe1_Muster2, "rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe1_Muster2.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster2.grid(row=4,column=2)

Farbe2_Muster2 = StringVar(root)
Farbe2_Muster2.set("Farbe 2") # default value
Dropdown_Farbe2_Muster2 = OptionMenu(musterframe,Farbe2_Muster2, "rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe2_Muster2.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster2.grid(row=5,column=2)

Farbe1_Muster3 = StringVar(root)
Farbe1_Muster3.set("Farbe 1") # default value
Dropdown_Farbe1_Muster3 = OptionMenu(musterframe,Farbe1_Muster3, "rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe1_Muster3.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster3.grid(row=4,column=3)

Farbe2_Muster3 = StringVar(root)
Farbe2_Muster3.set("Farbe 2") # default value
Dropdown_Farbe2_Muster3 = OptionMenu(musterframe,Farbe2_Muster3, "rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe2_Muster3.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster3.grid(row=5,column=3)

Farbe1_Muster4 = StringVar(root)
Farbe1_Muster4.set("Farbe 1") # default value
Dropdown_Farbe1_Muster4 = OptionMenu(musterframe,Farbe1_Muster4, "rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe1_Muster4.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster4.grid(row=4,column=4)

Farbe2_Muster4 = StringVar(root)
Farbe2_Muster4.set("Farbe 2") # default value
Dropdown_Farbe2_Muster4 = OptionMenu(musterframe,Farbe2_Muster4,"rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe2_Muster4.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster4.grid(row=5,column=4)

Farbe1_Muster5 = StringVar(root)
Farbe1_Muster5.set("Farbe 1") # default value
Dropdown_Farbe1_Muster5 = OptionMenu(musterframe,Farbe1_Muster5,"rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe1_Muster5.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe1_Muster5.grid(row=4,column=5)

Farbe2_Muster5 = StringVar(root)
Farbe2_Muster5.set("Farbe 2") # default value
Dropdown_Farbe2_Muster5 = OptionMenu(musterframe,Farbe2_Muster5,"rot","pink","weiß","grün","hellblau","schwarz","dunkelblau","gelb","orange")
Dropdown_Farbe2_Muster5.config(width=8) #legt die breite fest, damit diese nicht mit der Länge des Wortes variiert
Dropdown_Farbe2_Muster5.grid(row=5,column=5)

#Checkboxen
var1 = IntVar()
Checkbutton(musterframe, text="waagerechte Streifen", variable=var1).grid(row=3, column=1, pady=3)
var2 = IntVar()
Checkbutton(musterframe, text="senkrechte Streifen", variable=var2).grid(row=3, column=2)
var3 = IntVar()
Checkbutton(musterframe, text="Schräge", variable=var3).grid(row=3, column=3)
var4 = IntVar()
Checkbutton(musterframe, text="kleines Karo", variable=var4).grid(row=3, column=4)
var5 = IntVar()
Checkbutton(musterframe, text="großes Karo", variable=var5).grid(row=3, column=5)


#Platzhalter
label_p2=Label(bildframe,width=9, bg="snow")
label_p2.grid(row=0, column=0)
label_p3=Label(bildframe,width=12, bg="snow")
label_p3.grid(row=3, column=1)
label_p4=Label(bildframe,width=9, bg="snow")
label_p4.grid(row=6,column=4)

label_Bild = Label(bildframe, text="Bild",font=("Calibri 15 bold"),bg="snow")
label_Bild.grid(column=1, row=1)

#Drag and Drop für Bildfunktion
label_dragndrop=Label(bildframe, text="Drag'n Drop",bg="snow")
label_dragndrop.grid(row=2, column=2)

entry_sv = StringVar()      
entry_sv.set('Drop Here...')
entry = Entry(bildframe, textvar=entry_sv, width=80)
entry.grid(row=3, column=2, padx=10, pady=10)
entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)
button_Los1=Button(bildframe, text= "Bild generieren",width=18)
button_Los1.bind("<Button-1>",Bild1)
button_Los1.grid(row=3, column=3)

# Auswählen einer Datei für Bildfunkton ohne Drag and Drop
label_datei= Label(bildframe, text="Datei auswählen",bg="snow")
label_datei.grid(row=4, column=2)
button_Bildoeffnen = Button(bildframe, text="öffnen")
button_Bildoeffnen.bind("<Button-1>",fileoeffnen)
button_Bildoeffnen.grid(row=5, column=2)
button_Los2=Button(bildframe, text= "Bild generieren", width=18)
button_Los2.bind("<Button-1>",Bild2)
button_Los2.grid(row=5, column=3)





root.mainloop
