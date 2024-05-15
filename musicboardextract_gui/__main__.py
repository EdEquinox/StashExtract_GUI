import musicboardextract_gui

# Set up the main app and loading screen
app = musicboardextract_gui.setup_app()
#loading_screen = musicboardextract_gui.setup_loading_screen(app)

# Configure the rows and columns to expand
buttons = musicboardextract_gui.setup_buttons(app)


# Run the app
app.mainloop()