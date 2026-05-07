import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Conectando os eventos
        self.view.submit_button.connect("clicked", self.on_submit_clicked)
        self.view.connect("destroy", self.on_window_destroy)

    def on_submit_clicked(self, widget):
        user_input = self.view.input_entry.get_text()
        self.model.set_text(user_input)
        
        texto_salvo = self.model.get_text()
        
        if texto_salvo.strip():
            self.view.result_label.set_markup(f"<b>Você digitou:</b> {texto_salvo}")
        else:
            self.view.result_label.set_text("Por favor, digite algo no campo.")
            
        self.view.input_entry.set_text("")

    def on_window_destroy(self, widget):
        Gtk.main_quit()
