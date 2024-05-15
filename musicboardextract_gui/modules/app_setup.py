import customtkinter
import musicboardextract_gui
from PIL import Image, ImageTk
from tkinter import PhotoImage, Label

def setup_app():
    
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    
    app.title("MusicboardExtractor")
    #app.iconbitmap(musicboardextract_gui.ICON_PATH)
    app.geometry(musicboardextract_gui.APP_GEOMETRY)
    app.resizable(False,False)
    
    img = Image.open(musicboardextract_gui.BACKGROUND_IMG)
    background = ImageTk.PhotoImage(img)
    background_label = Label(app, image=background)
    background_label.image = background
    background_label.place(x=0, y=0, relwidth=1, relheight=1)   
    
    newspace = customtkinter.CTkLabel(app, text="")
    newspace.pack()
    newspace.configure(font=("Courier", 12))
    title = customtkinter.CTkLabel(app, text="MusicboardExtract")
    title.pack()
    title.configure(font=("Courier", 44))
    space = customtkinter.CTkLabel(app, text="")
    space.pack()
    space.configure(font=("Courier", 8))
    subtitle = Label(app, text="Own your data.")
    subtitle.pack()
    subtitle.configure(font=("Courier", 22))
    
    img = Image.open(musicboardextract_gui.ICON_PATH)
    img = img.resize((50, 50), Image.LANCZOS)  # Resize the image
    logo = ImageTk.PhotoImage(img)
    logo_label = Label(app, image=logo)
    logo_label.image = logo
    logo_label.place(x=375, y=300)

    return app