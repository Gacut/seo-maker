import tkinter as tk
from tkinter import ttk
from utils.prompt_loader import load_prompt
from utils.get_base_path import get_base_path
import os
from .tabs import create_tab1, create_tab2, create_tab3



class GUI:
    def __init__(self, text_processor, paraphraser, claude_client):
        self.window = tk.Tk()
        self.window.title("SEOMaker v2.2.1")
                          
        # set the icon by dynamically constructing the path to the file                          
        base_path = get_base_path()
        icon_path = os.path.join(base_path, 'resources', 'icon.ico')                  
        self.window.iconbitmap(icon_path)
        
        
        self.window.geometry("900x650")
        self.window.configure(background='white')
        self.window.resizable(False, False)

        self.textProcessor = text_processor
        self.paraphraser = paraphraser
        self.ClaudeClient = claude_client
        self.defaultPrompt = load_prompt()

        self.createWidgets()
        self.setupLayout()

    def createWidgets(self):
        self.notebook = ttk.Notebook(self.window)
        self.tab1 = create_tab1(self.notebook, self)
        self.tab2 = create_tab2(self.notebook, self)
        self.tab3 = create_tab3(self.notebook, self)
        self.notebook.add(self.tab1, text="Nowy opis")
        self.notebook.add(self.tab2, text="Parafrazy Manual")
        self.notebook.add(self.tab3, text="Parafrazy API")
        
    

    def setupLayout(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background='lightblue')
        style.map('TNotebook.Tab', background=[('selected', '#008CBA')])

       
        self.notebook.pack(expand=True, fill='both')


    def run(self):
        self.window.mainloop() 
    
    #EXTRACT TO UTILS
    def radioSelectionSend(self):
        self.textProcessor.selectedType = self.radio_var.get()
        
    def linkCheckBoxSend(self):
        self.textProcessor.linkSelection = self.link_var.get()