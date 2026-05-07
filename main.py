
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Importando das respectivas pastas (módulos)
from models.text_model import TextModel
from views.app_view import AppView
from controllers.app_controller import AppController

if __name__ == "__main__":
    model = TextModel()
    view = AppView()
    controller = AppController(model, view)

    view.show_all()
    Gtk.main()
