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

LED_COUNT=36    #Anzahl LEDS

def drop(event):
    entry_sv.set(event.data)
    
def Text(event):
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
    iar=np.asarray(i)
    print ('2:',iar)# zur Überprüfung
    plt.imshow(iar)
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
    label_ausgewaehlteDatei.pack()
    global c
    c=str(root.filename)
   
    return c
    print(root.filename)

root = TkinterDnD.Tk()
topframe=Frame(root)
topframe.pack()
textframe=Frame(root)
textframe.pack()
musterframe=Frame(root)
musterframe.pack()
bildframe=Frame(root)
bildframe.pack()

button_Text = Button(textframe, text="Text")
button_Text.bind("<Button-1>",Text)
button_Text.grid(row=0,column=1)

Label_Text=Label(textframe, text='Texteingabe')
Label_Text.grid(row=1, column=1)
e1=Entry(textframe)
e1.grid(row=2, column=1)

Label_Farbe = Label(textframe, text="Wähle eine Farbe")
Label_Farbe.grid(row=3, column=1)

# Regler zum Einstellen der Farbe des TExtes
Label_R=Label(textframe, text='R')
Label_R.grid(row=4)
Scale_TextfarbeR= Scale(textframe, from_=0, to=255, orient=HORIZONTAL, command=ShowColour)
Scale_TextfarbeR.grid(row=4, column=1)
entry_R= Entry(textframe, width=6)
entry_R.grid(row=4, column=2)
Label_G=Label(textframe, text='G')
Label_G.grid(row=5, column=0)
Scale_TextfarbeG= Scale(textframe, from_=0, to=255, orient=HORIZONTAL,command=ShowColour)
Scale_TextfarbeG.grid(row=5, column=1)
entry_G= Entry(textframe, width=6)
entry_G.grid(row=5, column=2)
Label_B=Label(textframe, text='B')
Label_B.grid(row=6, column=0)
Scale_TextfarbeB= Scale(textframe, from_=0, to=255, orient=HORIZONTAL,command=ShowColour)
Scale_TextfarbeB.grid(row=6, column=1)
entry_B= Entry(textframe, width=6)
entry_B.grid(row=6, column=2)

    #image_colour = Image.new('RGB',(14, 14), color = (Scale_TextfarbeR.get(),Scale_TextfarbeG.get(),Scale_TextfarbeB.get()))
    #image_colour.save('images/textcolour.png')
    #load = Image.open('images/textcolour.png')
    #render=ImageTk.PhotoImage(load)
    #image_textcolour = Label(textframe, image=render)
    #image_textcolour.image = render
    #image_textcolour.grid(row=7, column=1)
#image1= PhotoImage(file='images/Jill.JPG')
label_farbvorschau=Label(textframe, background='black', height=5, width=5)
label_farbvorschau.grid(row=7, column=1)
button_RGB = Button(textframe, text='Eingabe')
button_RGB.bind("<Button-1>", ShowColour)
button_RGB.grid(row=7, column=2)

button_Muster = Button(musterframe, text="Muster")
button_Muster.bind("<Button-1>",Muster)
button_Muster.pack()

variable =StringVar(root)
variable.set('Farbe1')
Dropdown_Farbe_Muster = OptionMenu(musterframe, variable,"black","blue","green")
Dropdown_Farbe_Muster.pack()

button_Bild = Button(bildframe, text="Bild")
button_Bild.bind("<Button-1>",Bild)
button_Bild.grid(column=0, row=0)

#Drag and Drop für Bildfunktion
label_dragndrop=Label(bildframe, text="Drag'n Drop")
label_dragndrop.grid(row=1, column=0)

entry_sv = StringVar()      
entry_sv.set('Drop Here...')
entry = Entry(bildframe, textvar=entry_sv, width=80)
entry.grid(row=2, column=0,fill=X, padx=10, pady=10)
entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)

# Auswählen einer Datei für Bildfunkton ohne Drag and Drop
label_datei= Label(bildframe, text="Datei auswählen")
label_datei.grid(row=3, column=0)
button_Bildoeffnen = Button(bildframe, text="öffnen")
button_Bildoeffnen.bind("<Button-1>",fileoeffnen)
button_Bildoeffnen.grid(row=4, column=0)
button_Los=Button(bildframe, text= "Bild generieren")
button_Los.grid(row=4, column=1)





root.mainloop
