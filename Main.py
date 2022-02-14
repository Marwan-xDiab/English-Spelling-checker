from tkinter import *  # import module
from googletrans import Translator

gui = Tk()  # creat GUI
gui.geometry("500x500")  # size of window
gui.resizable(0, 0)
gui.title("Translation")  # write any of tkinter title
gui.configure(background="#ddd")
# GUI InterFace

txtbox1 = StringVar(gui)
indexbox = IntVar(gui)


def translate():
    translator = Translator()
    translation = translator.translate(txtbox1.get(), dest=lan2.get())
    Lbox1.insert(0, translation.text)


def selectData():
    print("Language From: " + lan1.get() + " To: " + lan2.get())


def insertData():
    Lbox.insert(0, txtbox1.get())


def oneselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    indexbox.set(index)


def deleteData():
    Lbox.delete(indexbox.get())


def clearData():
    txtbox1.set("")
    indexbox.set("")


Lbl1 = Label(gui, text="Text", font="Calibri", bg="#ddd").place(x=90, y=60)
Lbox = Listbox(gui, font="Calibri", width=20)
Lbox.place(x=50, y=80)
Lbl2 = Label(gui, text="Translation", font="Calibri", bg="#ddd").place(x=310, y=60)
Lbox1 = Listbox(gui, font="Calibri", width=20)
Lbox1.place(x=280, y=80)

Lbl4 = Label(gui, text="Enter Text", font="Calibri", bg="#ddd").place(x=70, y=290)
Txtbox1 = Entry(gui, width=20, font="Calibri", textvariable=txtbox1).place(x=50, y=310)

Lbl5 = Label(gui, text="Item Index", font="Calibri", bg="#ddd").place(x=350, y=290)
Txtbox2 = Entry(gui, width=15, font="Calibri", textvariable=indexbox).place(x=330, y=310)

# Button function
B1 = Button(gui, text="Insert", width=20, font="Calibri", command=insertData)
B1.place(x=150, y=340)
B2 = Button(gui, text="Translate", width=20, font="Calibri", command=translate)
B2.place(x=150, y=370)
B3 = Button(gui, text="Delete", width=20, font="Calibri", command=deleteData)
B3.place(x=150, y=400)
B4 = Button(gui, text="Clear", width=20, font="Calibri", command=clearData)
B4.place(x=150, y=430)
B5 = Button(gui, text="Select", width=20, font="Calibri", command=selectData)
B5.place(x=150, y=460)

# Variable for dropdown list
lan1 = StringVar(gui)
lan2 = StringVar(gui)

#  list  for dropdownlists
lan1.set(' From')
lan2.set(' To')

lan1menu = OptionMenu(gui, lan1, 'En', 'Ar').place(x=150, y=5)
Label(gui, text="Select a language", font="Calibri", bg="#ddd").place(x=20, y=5)
lan2menu = OptionMenu(gui, lan2, 'En', 'Ar').place(x=410, y=5)
Label(gui, text="Select a language", font="Calibri", bg="#ddd").place(x=280, y=5)

Lbox.bind('<<ListboxSelect>>', oneselect)
gui.mainloop()  # creat loop