import musicboardextract_gui
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
    
    label_later = musicboardextract_gui.input_module_label(app, "Link of your listen later list:")
    label_later.place(x=50, y=170)
    
    text_input_later, button_later = musicboardextract_gui.input_module_form(app)
    text_input_later.configure(font=("Arial", 15), width=300, height=1)
    text_input_later.place(x=50, y=200)
    button_later.configure(font=("Arial", 15), width=300, height=50)
    button_later.place(x=50, y=250)

    label_album = musicboardextract_gui.input_module_label(app, "Link of your album list:")
    label_album.place(x=50, y=370)

    text_input_album, button_album = musicboardextract_gui.input_module_form(app)
    text_input_album.configure(font=("Arial", 15), width=300, height=1)
    text_input_album.place(x=50, y=400)
    button_album.configure(font=("Arial", 15), width=300, height=50)
    button_album.place(x=50, y=450)

    label_review = musicboardextract_gui.input_module_label(app, "Link of your reviews list:")
    label_review.place(x=450, y=170)

    text_input_review, button_review = musicboardextract_gui.input_module_form(app)
    text_input_review.configure(font=("Arial", 15), width=300, height=1)
    text_input_review.place(x=450, y=200)
    button_review.configure(font=("Arial", 15), width=300, height=50)
    button_review.place(x=450, y=250)
    
    label_list = musicboardextract_gui.input_module_label(app, "Link of your list:")
    label_list.place(x=450, y=370)
    
    text_input_list, button_list = musicboardextract_gui.input_module_form(app)
    text_input_list.configure(font=("Arial", 15), width=300, height=1)
    text_input_list.place(x=450, y=400)
    button_list.configure(font=("Arial", 15), width=300, height=50)
    button_list.place(x=450, y=450)
    
    buttons = [button_later, button_album, button_review, button_list]
    texts = [text_input_later, text_input_album, text_input_review, text_input_list]
    
    musicboardextract_gui.configure_button(button_later, text_input_later, musicboardextract_gui.extract_list_later, musicboardextract_gui.process_and_update, app, buttons, texts)
    musicboardextract_gui.configure_button(button_album, text_input_album, musicboardextract_gui.extract_list_album, musicboardextract_gui.process_and_update, app, buttons, texts)
    musicboardextract_gui.configure_button(button_review, text_input_review, musicboardextract_gui.extract_list_reviews, musicboardextract_gui.process_and_update, app, buttons, texts)
    musicboardextract_gui.configure_button(button_list, text_input_list, musicboardextract_gui.extract_list, musicboardextract_gui.process_and_update, app, buttons, texts)
    
    return button_later, button_album, button_review, button_list