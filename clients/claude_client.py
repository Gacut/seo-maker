import anthropic
import json
import os
import tkinter as tk
from utils.prompt_loader import load_prompt
from utils.get_base_path import get_base_path 

import time
    
class ClaudeClient:
    def __init__(self, gui): 
        self.gui = gui 
        base_path = get_base_path()        
        config_path = os.path.join(base_path, 'config.json')
        
        try:
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
                self.api_key = config.get("ANTHROPIC_API_KEY")
                if not self.api_key:
                    raise ValueError("Brak ANTHROPIC_API_KEY w config.json")
        except FileNotFoundError:
            raise FileNotFoundError(f"Plik config.json nie został znaleziony w {config_path}")
        except json.JSONDecodeError:
            raise ValueError("Plik config.json zawiera nieprawidłowy format JSON")
        
        
        self.client = anthropic.Anthropic(
            api_key=self.api_key
        )
        
        self.paraphrase_prompt = load_prompt('paraphraser')
    
        
        self.MAX_RETRIES = 3
        self.DELAY = 5
        
    
    
    def createMessage(self, button_type):
         
        self.button_config = {
            "text_from_spec_generator":{
                "input": self.gui.paraphraser.extractContent(self.gui.HTMLWindowTab3),
                "output_window": self.gui.textWindowTab1,
                "prompt": load_prompt('text_gen')
            },
            "paraphraser":{
                "input": self.gui.paraphraser.extractContent(self.gui.HTMLWindowTab3),
                "output_window": self.gui.textWindowTab3,
                "prompt": load_prompt('paraphraser')
            }
        } 
        config = self.button_config[button_type]
        
        for attempt in range(self.MAX_RETRIES):
            try:
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1000,
                    temperature=0,
                    system= config["prompt"],
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": config["input"]
                                }
                            ]
                        }
                    ]
                )
                
                message = response.content[0].text
                config["output_window"].delete("1.0", tk.END)
                config["output_window"].insert("end", message)
                return
            except Exception as e:
                if attempt < self.MAX_RETRIES -1:
                    print(f"Połączenie {attempt + 1} zawiodło. Ponowna próba za {self.DELAY} sekund...")
                    time.sleep(self.DELAY)
                else:
                    print(f"Przekroczono ilość prób. Spróbuj ponownie później. Error: {e}")
                    config["output_window"].insert("end", f"Przekroczono ilość prób. Spróbuj ponownie później. Error: {e}\n\nSprawdź status dostępności API na https://status.anthropic.com/")
                    
