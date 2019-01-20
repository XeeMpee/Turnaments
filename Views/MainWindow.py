import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow():
    
    def __init__(self):
        pass
    
    def run(self):
        win = Gtk.Window()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
        pass