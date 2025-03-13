import os
import sys

def get_base_path():
  
    #Returns the base path for the application, considering both local and PyInstaller builds.
    
    if getattr(sys, 'frozen', False):  # If running as a PyInstaller bundle
        return sys._MEIPASS  # Folder where PyInstaller extracts resources
    
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(
        os.path.join(current_dir, '..')
    )
    
    if not os.path.exists(base_path):
        raise FileNotFoundError(f"Base path not found: {base_path}")
    
    return base_path    
