import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers.InsertStateController import *
from Participant import *

class MainWindow():
    """
    Main Window of program

    Attributes:
    # _window : GtkWindow
    # insertController : InsertController
    # _handlers : GtkWindow
         
    Methods:
    + run() : void
    - __add_button_clicked(button)
    - __modify_button_clicked(button)
    - __delete_button_clicked(button)
    - __start_turnament_button_clicked(button)
    """
    
    def __init__(self, controller):
        
        # Gtk init and builde staffs:
        self._insertController = controller
        self._builder = Gtk.Builder()
        
        self._builder.add_from_file("Views/MainWindow.glade")
        
        self._window = self._builder.get_object("main_window")
        self._window.connect("destroy", Gtk.main_quit)
 
        handlers = {
        "onDestroy": Gtk.main_quit,
        "add_button_clicked": self.__add_button_clicked,
        "modify_button_clicked": self.__modify_button_clicked,
        "delete_button_clicked": self.__delete_button_clicked,
        "start_turnament_button_clicked": self.__start_turnament_button_clicked,
        "accept_button_clicked" : self.__accept_button_clicked
        }
        self._builder.connect_signals(handlers)

        # Gtk displaying added participants:
        self._participantsvViewPort = self._builder.get_object("participants_view_port")
        self.__listBox = Gtk.ListBox()
        self.__listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        self._participantsvViewPort.add(self.__listBox)


    def run(self):

        self._window.show_all()
        Gtk.main()


    def __accept_button_clicked(self, button):
        print("Accept button clicked")

    
    def __add_button_clicked(self,button):
        print("Add button clicked")
        entry = self._builder.get_object("entry")
        text = entry.get_text()
        print("Value:|{}|" .format(text))

        if(text != ""):
            listboxRow = Gtk.ListBoxRow()
            listboxRow.add(Gtk.Label(text))
            self.__listBox.add(listboxRow)
            self._insertController.addParticipant(Participant(text))
            self._window.show_all()


    def __modify_button_clicked(self, button):
        print("Modify button clicked")


    def __delete_button_clicked(self, button):
        print("Delete button clicked")


    def __start_turnament_button_clicked(self, button):
        print("Start turnament button clicked")





