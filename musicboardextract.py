
from musicboardextract_gui import setup_app, setup_buttons
import traceback
import time

try:
    app = setup_app()
    buttons = setup_buttons(app)
    app.mainloop()
except Exception:
    traceback.print_exc()
    input("Press Enter to continue...")

   
