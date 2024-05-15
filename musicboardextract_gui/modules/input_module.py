import customtkinter
import threading

def input_module_label(app, text):
    label = customtkinter.CTkLabel(app, text=text, width=300, height=30, font=("Arial", 15), corner_radius=0)
    return label
    
    
def input_module_form(app):
    text_input = customtkinter.CTkEntry(app, corner_radius=0)
    button = customtkinter.CTkButton(app, text="Extract!", fg_color='blue', corner_radius=0)
    
    return text_input, button

def configure_button(button, text_input, target, function, app, buttons, texts):
    button._command = lambda: threading.Thread(
        target= function, args=(target, text_input.get(), app, buttons, texts)).start()
