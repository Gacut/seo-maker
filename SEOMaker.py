from gui import GUI
from clients.claude_client import ClaudeClient
from processors.text_processor import TextProcessor
from processors.paraphraser import Paraphraser



if __name__ == "__main__":
    # Create GUI first without linking components
    gui = GUI(text_processor=None, paraphraser=None, claude_client=None)

 
    text_processor = TextProcessor(gui)    # Initialize components
    gui.textProcessor = text_processor     # Link components to GUI
    paraphraser = Paraphraser(gui)
    gui.paraphraser = paraphraser
    claude_client = ClaudeClient(gui)
    gui.ClaudeClient = claude_client

    # Start the GUI application
    gui.run()
