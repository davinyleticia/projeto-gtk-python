import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AppView(Gtk.Window):
    def __init__(self):
        super().__init__(title="MVC com Pastas - Python e GTK")
        self.set_border_width(15)
        self.set_default_size(300, 150)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        instruction_label = Gtk.Label(label="Digite algo abaixo:")
        box.pack_start(instruction_label, False, False, 0)

        self.input_entry = Gtk.Entry()
        box.pack_start(self.input_entry, False, False, 0)

        self.submit_button = Gtk.Button(label="Enviar")
        box.pack_start(self.submit_button, False, False, 0)

        self.result_label = Gtk.Label(label="")
        box.pack_start(self.result_label, False, False, 0)
