# __init__.py

# Import any necessary modules or packages here

from .modules.app_setup import setup_app
from .modules.loading_screen_setup import setup_loading_screen
from .modules.button_setup import setup_buttons
from .modules.input_module import input_module_label, input_module_form
from .utils.process_loading import process_and_update
from .modules.input_module import configure_button
from .modules.extract_data import extract_list
from .modules.extract_data import extract_list_album
from .modules.extract_data import extract_list_later
from .modules.extract_data import extract_list_reviews
import os

# Define any global variables or constants here

APP_GEOMETRY = "800x600"
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_IMG = os.path.join(CURRENT_DIR, "assets", "Sprinkle.png")
ICON_PATH = os.path.join(CURRENT_DIR, "assets", "logo_musicboard.ico")

# Define any functions or classes here

# Optionally, include any initialization code here
