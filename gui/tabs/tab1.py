import tkinter as tk
from tkinter import ttk
from utils.insert_text import insert_text
from utils.copy_to_clipboard import copy_to_clipboard

def create_tab1(parent, self):
    self.radio_var = tk.IntVar()
    self.link_var = tk.IntVar()
    
    self.tab1 = ttk.Frame(self.notebook)

    self.textLabelTab1 = tk.Label(self.tab1, text="Tekst")
    self.htmlLabelTab1 = tk.Label(self.tab1, text="HTML")

    self.textWindowTab1 = tk.Text(self.tab1, height=20, width=30)
    self.HTMLWindowTab1 = tk.Text(self.tab1, height=20, width=30)

    self.transferToHTMLButtonTab1 = tk.Button(
        self.tab1,
        text="--->",
        command=lambda: self.textProcessor.generateSEO(),
        bg="#008CBA",
        width="15"
    )

    self.copyHTMLButtonTab1 = tk.Button(
        self.tab1,
        text="Kopiuj HTML",
        command=lambda: self.copy_to_clipboard(
            window=self.window, 
            widget=self.HTMLWindowTab1, 
            add_prompt=False, 
            prompt_state=None, 
            prompt_text_widget=None
        ),
        bg="#008CBA",
        width="30"
    )

    self.linkButtonTab1 = tk.Button(
        self.tab1,
        text="Stwórz tekst produktu",
        # command = lambda: #wyslij message i wstaw to message w lewy window
        
    )
    
    self.imageNameTab1 = tk.Label(self.tab1, text="Nazwy grafik")
    self.imageNameEntryTab1 = tk.Entry(self.tab1, width=20)
    self.copyNameButtonTab1 = tk.Button(
        self.tab1,
        text="Kopiuj nazwę",
        command=lambda: self.copyToClipboard(self.imageNameEntryTab1),
        bg="#008CBA"
    )

    self.linkEntryTab1 = tk.Entry(self.tab1, width=20 )

    
    self.centerRadioTab1 = tk.Radiobutton(
        self.tab1,
        text="CENTER",
        variable=self.radio_var,
        value=1,
        command=self.radioSelectionSend
    )
    self.leftRadioTab1 = tk.Radiobutton(
        self.tab1,
        text="LEWO",
        variable=self.radio_var,
        value=2,
        command=self.radioSelectionSend
    )
    self.miniRadioTab1 = tk.Radiobutton(
        self.tab1,
        text="MINI",
        variable=self.radio_var,
        value=3,
        command=self.radioSelectionSend
    )
    self.useLinkCheckboxTab1 = tk.Checkbutton(
        self.tab1,
        text="POBIERZ Z LINKA",
        variable=self.link_var,
        onvalue=1,
        offvalue=0,
        command=()
    ) 
   
   
    # Layout for Tab 1
    self.centerRadioTab1.grid(row=0, column=0, padx=(50, 25), pady=(20, 0))
    self.leftRadioTab1.grid(row=0, column=1, padx=(25, 25), pady=(20, 0))
    self.miniRadioTab1.grid(row=0, column=2, padx=(25, 50), pady=(20, 0))

    self.useLinkCheckboxTab1.grid(row=1, column=0, padx=(25, 25), pady=(20, 0))
    self.linkEntryTab1.grid(row=1, column=1, padx=(25, 25), pady=(20, 0))
    self.linkButtonTab1.grid(row=1, column=2, padx=(25, 25), pady=(20, 0))
    
    self.textLabelTab1.grid(row=2, column=0, padx=(50, 25), pady=(20, 0))
    self.htmlLabelTab1.grid(row=2, column=2, padx=(25, 50), pady=(20, 0))

    self.textWindowTab1.grid(row=3, column=0, padx=(50, 25), pady=(5, 10))
    self.transferToHTMLButtonTab1.grid(row=3, column=1, padx=(25, 25), pady=10)
    self.HTMLWindowTab1.grid(row=3, column=2, padx=(25, 50), pady=(5, 10))

    self.copyHTMLButtonTab1.grid(row=4, column=2, padx=(25, 50), pady=10)

    self.imageNameTab1.grid(row=5, column=0, pady=30)
    self.imageNameEntryTab1.grid(row=5, column=1, pady=30)
    self.copyNameButtonTab1.grid(row=5, column=2, pady=30)

    return self.tab1
