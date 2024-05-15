# __init__.py

# This is the initialization file for the extract_list package.
# It imports the extract_list module and the extracted_list module.
# It also defines the __all__ variable which is used to specify which modules are imported when the package is imported.

from .app_setup import setup_app
from .loading_screen_setup import setup_loading_screen
from .button_setup import setup_buttons
from .input_module import input_module_label, input_module_form
from .extract_data import extract_list
from .extract_data import extract_list_album
from .extract_data import extract_list_later
from .extract_data import extract_list_reviews