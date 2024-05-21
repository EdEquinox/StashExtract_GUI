import stashextract_gui
import customtkinter
from customtkinter import CTkButton

def animate_button(button: CTkButton):
    button.configure(state="disabled")
    button.configure(text="Loading...")
    

def setup_buttons(app):
    
    buttons = []
    texts = []
    
    footer = customtkinter.CTkLabel(app, text="© 2022 edquinox. All rights reserved.                Contact: jmarquesnox@gmail.com", justify="center")
    footer.pack(side = "bottom", fill = "both")
    
    

    label = stashextract_gui.input_module_label(app, "Link of your list:")
    label.place(x=150, y=170)

    text_input, button = stashextract_gui.input_module_form(app)
    text_input.configure(font=("Arial", 15), width=300, height=1)
    text_input.place(x=150, y=200)
    button.configure(font=("Arial", 15), width=300, height=50)
    button.place(x=150, y=230)

    
    
    buttons = [ button]
    texts = [text_input]
    
    stashextract_gui.configure_button(button, text_input, stashextract_gui.extract_list, stashextract_gui.process_and_update, app, buttons, texts)
    
    return button