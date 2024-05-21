import customtkinter
import stashextract_gui
from PIL import Image, ImageTk
from tkinter import PhotoImage, Label
import traceback

def setup_app():
    
    customtkinter.set_appearance_mode("System")

    app = customtkinter.CTk()

    app.title("StachExtractor")
    #app.iconbitmap(musicboardextract_gui.ICON_PATH)
    app.geometry(stashextract_gui.APP_GEOMETRY)
    app.resizable(False,False)

    img = Image.open(stashextract_gui.BACKGROUND_IMG)
    background = ImageTk.PhotoImage(img)
    background_label = Label(app, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)   

    newspace = customtkinter.CTkLabel(app, text="")
    newspace.pack()
    newspace.configure(font=("Courier", 12))
    title = customtkinter.CTkLabel(app, text="StashExtract")
    title.pack()
    title.configure(font=("Courier", 44))
    space = customtkinter.CTkLabel(app, text="")
    space.pack()
    space.configure(font=("Courier", 8))
    subtitle = Label(app, text="Own your data.")
    subtitle.pack()
    subtitle.configure(font=("Courier", 22))

    img = Image.open(stashextract_gui.ICON_PATH)
    img = img.resize((50, 50), Image.LANCZOS)  # Resize the image
    logo = ImageTk.PhotoImage(img)
    logo_label = Label(app, image=logo)
    logo_label.image = logo
    logo_label.place(x=275, y=300)

    return app
    