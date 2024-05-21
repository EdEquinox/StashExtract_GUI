# loading_screen_setup.py

import customtkinter
from PIL import Image, ImageTk
import stashextract_gui

def setup_loading_screen(app: customtkinter.CTk) -> customtkinter.CTkFrame:
    loading_screen = customtkinter.CTkFrame(app)
    
    loading_screen.place(x=0, y=0, relwidth=1, relheight=1)
    
    label = customtkinter.CTkLabel(loading_screen, text="Loading...")

    label.configure(justify='center')
    label.pack()
  
    
    loading_screen.lift()

    return loading_screen