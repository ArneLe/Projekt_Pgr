from tkinter import *
import sys
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *
from TkinterDnD2 import *

from PIL import Image, ImageDraw, ImageFont
import numpy as np          #abkürzung
import matplotlib.pyplot as plt

LED_COUNT=36    #Anzahl LEDS

def drop(event):
    entry_sv.set(event.data)
    
def Text(event):
    print("Texteingabe")
    b= e1.get()
    img = Image.new('RGBA',(14*len(b), 36), color = 'black') #(mode, Größe, Farbe(geht auch mit RGB Werten) Hier müsste man dann die Anzahl der LEDs wählen???
    fnt= ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf',25) #Schriftart wählen, Dateipfad angeben
    d = ImageDraw.Draw(img)

    d.text((5,5), b, font=fnt, fill=(255,255,255,255)) #Position, Text, Schriftart, Farbe

    img.save('images/text.png')
    #plt.imshow(img)       Warum auch immer es nicht funktioniert, wenn sie im Text sind 
    #plt.show()
    ti = Image.open('images/text.png').convert('RGB')   #textImage
    tiar = np.asarray(ti)                   #textimage Array
    print(tiar)                             #ausgabe array Bildtext
    print(tiar.shape)# gibt die höhe und breite des Arrays aus

    # Bild wird neu skaliert, eigentlich nicht notwendig, nur eine Vorsichtsmaßnahme
    newWidth=float(ti.size[0])/float(ti.size[1])*LED_COUNT
    ti=ti.resize((int(newWidth),LED_COUNT))
    tiar=np.asarray(ti)
    print (tiar)# zur Überprüfung
    plt.imshow(tiar)
    plt.show()

def Muster(event):
    print('Muster')

def Bild(event):
    print('Bild')
    a=str(entry.get())
    i = Image.open(a[1:-1]).convert('RGB')        #Hier muss der Dateipfad des Bildes angegeben werden oder via Drag and Drop
    iar = np.asarray(i)         #Image Array
    print(iar)                  #gibt das Array aus

    #plt.imshow(iar)
    #plt.show()
    
        # Bild wird neu skaliert
    newWidth=float(i.size[0])/float(i.size[1])*LED_COUNT
    i=i.resize((int(newWidth),LED_COUNT))
    iar=np.asarray(i)
    print ('2:',iar)# zur Überprüfung
    plt.imshow(iar)
    plt.show()




root = TkinterDnD.Tk()

button_Text = Button(root, text="Text")
button_Text.bind("<Button-1>",Text)
button_Text.pack()

Label_Text=Label(root, text='Texteingabe')
Label_Text.pack()
e1=Entry(root)
e1.pack()


button_Muster = Button(root, text="Muster")
button_Muster.bind("<Button-1>",Muster)
button_Muster.pack()

button_Bild = Button(root, text="Bild")
button_Bild.bind("<Button-1>",Bild)
button_Bild.pack()

#Drag and Drop für Bildfunktion
entry_sv = StringVar()      
entry_sv.set('Drop Here...')
entry = Entry(root, textvar=entry_sv, width=80)
entry.pack(fill=X, padx=10, pady=10)
entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)





root.mainloop
