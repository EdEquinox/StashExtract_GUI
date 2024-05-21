
from tkinter import filedialog
from typing import Any
import customtkinter
from plyer import notification

def process_and_update(function: Any, url, app: customtkinter.CTk, buttons: customtkinter.CTkButton, texts) -> None:
    """
    Executes the provided function with the given url and updates the loading screen.

    Args:
        function (callable): The function to be executed. It should accept two arguments: url and filepath.
        url (str): The url to be processed.
        loading_screen (Tkinter Toplevel): The loading screen to be updated.

    Returns:
        None
    """
    filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if filepath:
        
        for button in buttons:
            button.configure(state='disabled', text='Loading...', fg_color='gray')

        for text in texts:
            text.configure(state='disabled')
        
       
        result = function(url,filepath)
        
        notification._name = "MusicboardExtract"
        
        if result == 1:
            notification.notify("MusicboardExtract", "Data extraction completed successfully!", timeout=1)
        else:
            
            notification.notify("MusicboardExtract", "There was an error on the extraction, try again!", timeout=1)
        
        for button in buttons:
            button.configure(state='normal', text='Extract', fg_color='black')
        for text in texts:
            text.configure(state='normal')
            text.delete(0, 'end')
            
        return
        
            
            
            