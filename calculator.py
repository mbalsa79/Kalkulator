

from tkinter import *
from turtle import width


root = Tk()
root.title("Kalkulator")
root.resizable(False, False)


e = Entry(root, width=25, font=("Helvetica",28))
e.grid(row=0, column=0, columnspan=4)

def stisni_dugme(broj):
    trenutni=e.get()
    e.delete(0,END)
    e.insert(0, str(trenutni)+ str(broj))

def ocisti():
    e.delete(0,END)

def makni_jedno():
    greska=str(e.get())
    ispravljeno= greska[:-1]
    e.delete(0,END)
    e.insert(0, ispravljeno)
    




def jednako():
    izraz=str((e.get()))
    try:
     a=eval(izraz)
     e.delete(0,END)
     e.insert(0,a)
    except:
        e.delete(0,END)
        e.insert(0,"Error")


    

dugme_1 = Button(root, text="1",font=("Helvetica", 15),padx=55,pady=20, command= lambda: stisni_dugme("1"))
dugme_2 = Button(root, text="2", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("2"))
dugme_3 = Button(root, text="3", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("3"))
dugme_4 = Button(root, text="4", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("4"))
dugme_5 = Button(root, text="5", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("5"))
dugme_6 = Button(root, text="6", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("6"))
dugme_7 = Button(root, text="7", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("7"))
dugme_8 = Button(root, text="8", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("8"))
dugme_9 = Button(root, text="9", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("9"))
dugme_0 = Button(root, text="0", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("0"))
dugme_jednako= Button(root, text="=  ", font=("Helvetica", 15), padx=55, pady=20,command= jednako)
dugme_mnozenje= Button(root, text="*", font=("Helvetica", 15), padx=57, pady=20, command= lambda: stisni_dugme("*"))
dugme_dijeljenje= Button(root, text="/ ", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("/"))
dugme_oduzimanje= Button(root, text="- ", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("-"))
dugme_sabiranje= Button(root, text="+", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("+"))
dugme_ocisti= Button(root, text="C", font=("Helvetica", 15), padx=55, pady=20, command= ocisti)
dugme_tacka= Button(root, text=".", font=("Helvetica", 15), padx=57, pady=20, command= lambda: stisni_dugme("."))
dugme_otovrena= Button(root, text="(   ", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme("("))
dugme_zatvorena= Button(root, text=")   ", font=("Helvetica", 15), padx=55, pady=20, command= lambda: stisni_dugme(")"))
dugme_izbrisi= Button(root, text="<--", font=("Helvetica", 15), padx=55, pady=20, command=makni_jedno)


dugme_9.grid(row=1, column=2)
dugme_8.grid(row=1, column=1)
dugme_7.grid(row=1, column=0)
dugme_6.grid(row=2, column=2)
dugme_5.grid(row=2, column=1)
dugme_4.grid(row=2, column=0)
dugme_3.grid(row=3, column=2)
dugme_2.grid(row=3, column=1)
dugme_1.grid(row=3, column=0)
dugme_0.grid(row=4, column=0)
dugme_ocisti.grid(row=1, column=3)
dugme_sabiranje.grid(row=2, column=3)
dugme_oduzimanje.grid(row=3, column=3)
dugme_jednako.grid(row=4, column=4)
dugme_mnozenje.grid(row=4, column=2)
dugme_dijeljenje.grid(row=4, column=3)
dugme_tacka.grid(row=4, column=1)
dugme_otovrena.grid(row=2, column=4)
dugme_zatvorena.grid(row=3, column=4)
dugme_izbrisi.grid(row=1, column=4)




root.mainloop()