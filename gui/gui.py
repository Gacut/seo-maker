import tkinter as tk
from tkinter import Toplevel, ttk
from processors.scraper import Scraper
from utils.prompt_loader import load_prompt
from utils.get_base_path import get_base_path
from utils.insert_text import insert_text
import os
from .tabs import create_tab1, create_tab2, create_tab3



class GUI:
    def __init__(self, text_processor, paraphraser, claude_client):
        self.window = tk.Tk()
        self.window.title("SEOMaker v2.2.2")
                          
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
        self.last_product_spec = None
        self.programmatic_edit = False
        
        self.createWidgets()
        self.setupLayout()

    def on_text_modified(self, event):
        if self.programmatic_edit: 
            return
        if self.textWindowTab1.edit_modified():
            self.textProcessor.filename_source = 'name'
            self.textWindowTab1.edit_modified(False)
            
    def insert_claude_response(self, text, output_widget):
        self.programmatic_edit = True
        try:
            output_widget.delete("1.0", tk.END)
            output_widget.insert(tk.END, text)
        finally:
            self.programmatic_edit = False
            output_widget.edit_modified(False)  # reset of the modification flag
    
    
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
    
    
    def get_scraped_product_data(self):
        if not self.linkEntryTab1.get():
            return
            
        scraper = Scraper(self.linkEntryTab1.get(), self.textProcessor)
        input_template = scraper.generate_input()
        
        if input_template:
            self.last_product_spec = input_template
        else:
            self.last_product_spec = "Nie udało się pobrać danych"

        
    def open_product_spec_window(self, product_spec=None):
        product_spec_window = Toplevel(self.window)
        product_spec_window.title("Specyfikacja produktu")
        
        product_spec_box = tk.Text(product_spec_window, height=50, width=70)
        product_spec_box.pack(padx=5, pady=5)
        
        spec_content = self.last_product_spec if self.last_product_spec else "Brak dostępnej specyfikacji"
        insert_text(product_spec_box, spec_content)
    
    #EXTRACT TO UTILS
    def radioSelectionSend(self):
        self.textProcessor.selectedType = self.radio_var.get()
        
    def linkCheckBoxSend(self):
        self.textProcessor.linkSelection = self.link_var.get()