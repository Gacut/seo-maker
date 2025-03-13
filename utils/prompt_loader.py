from .get_base_path import get_base_path
import os

def load_prompt(prompt_type="paraphraser"):
  
    base_path = get_base_path()
    prompt_files = {
        "paraphraser": "paraphraser_prompt.txt",
        "text_gen": "text_gen_prompt.txt",
    }
    
    if prompt_type not in prompt_files:
        raise ValueError(f"Unknown prompt type: {prompt_type}")
    
    filename = prompt_files.get(prompt_type)
    prompt_path = os.path.join(base_path, 'resources', filename)


    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file '{filename}' not found in resources directory.")
