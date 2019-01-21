import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Controllers.InsertStateController import *
from Participant import *
from enum import Enum

class ActionMode(Enum):
            NONE=0,
            ADD=1,
            MODIFY=2,
            DELETE=3


class MainWindow():
    """
    Main Window of program

    Attributes:
    # _window : GtkWindow
    # insertController : InsertController
    # _handlers : GtkWindow
    - __mode : ActionMode(Enum)
         
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

        # MODE:
        self.__mode = ActionMode.NONE

        # Disactive AcceptButton:
        self.__enteringAreaSetSensitive(False)


    def run(self):

        self._window.show_all()
        Gtk.main()


    def __accept_button_clicked(self, button):
        print("Accept button clicked")
        
        if(self.__mode==ActionMode.ADD):
            entry = self._builder.get_object("entry")
            text = entry.get_text()
            print("Value:|{}|" .format(text))

            if(text != ""):
                listboxRow = Gtk.ListBoxRow()
                listboxRow.add(Gtk.Label(text))
                listboxRow.set_size_request(60,60)
                if(self._insertController.isParticipant(text)):
                    print("Participant already exists!")
                else:
                    self.__listBox.add(listboxRow)
                    self._insertController.addParticipant(Participant(text))
                    self._window.show_all()
            elif(self.__mode==ActionMode.MODIFY):
                pass
            elif(self.__mode==ActionMode.DELETE):
                pass
        
        
        self.__addButtonSetSensitive(True)
        self.__deleteButtonSetSensitive(True)
        self.__modifyButtonSetSensitive(True)
        self.__enteringAreaSetSensitive(False)
        self.__clearEntry()

    
    def __add_button_clicked(self,button):
        print("Add button clicked")

        self.__enteringAreaSetSensitive(True)
        self.__deleteButtonSetSensitive(False)
        self.__modifyButtonSetSensitive(False)
        self.__mode=ActionMode.ADD

    
    def __modify_button_clicked(self, button):
        print("Modify button clicked")
        self.__addButtonSetSensitive(False)
        self.__deleteButtonSetSensitive(False)
        self.__enteringAreaSetSensitive(True)
        self.__mode=ActionMode.MODIFY

    def __delete_button_clicked(self, button):
        print("Delete button clicked")
        self.__addButtonSetSensitive(False)
        self.__modifyButtonSetSensitive(False)
        self.__enteringAreaSetSensitive(True)
        self.__mode=ActionMode.DELETE


    def __enteringAreaSetSensitive(self, boolean=True):
        acceptButton=self._builder.get_object("accept_button")
        enteringArea=self._builder.get_object("entry")
        acceptButton.set_sensitive(boolean)
        enteringArea.set_sensitive(boolean)


    def __addButtonSetSensitive(self, boolean=True):
        addButton=self._builder.get_object("add_button")
        addButton.set_sensitive(boolean)

    
    def __deleteButtonSetSensitive(self, boolean=True):
        deleteButton=self._builder.get_object("delete_button")
        deleteButton.set_sensitive(boolean)


    def __modifyButtonSetSensitive(self, boolean=True):
        modifyButton=self._builder.get_object("modify_button")
        modifyButton.set_sensitive(boolean)

    def __clearEntry(self):
        entry = self._builder.get_object("entry")
        entry.set_text("")

    def __start_turnament_button_clicked(self, button):
        print("Start turnament button clicked")





