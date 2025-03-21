from tkinter import *

root = Tk()

def otworz_okienko():
    # Tworzenie nowego okna
    okienko = Toplevel(root)
    okienko.title("Moje okienko")
    
    # Dodawanie zawartości
    label = Label(okienko, text="To jest moja wiadomość!")
    label.pack(padx=20, pady=20)

przycisk = Button(root, text="Otwórz okienko", command=otworz_okienko)
przycisk.pack()

root.mainloop()