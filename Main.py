from Controllers.StateController import *
from Controllers.InsertStateController import *
from Views.MainWindow import *

insertController = InsertStateController(Graph(), None)
mainWindow = MainWindow(insertController)
mainWindow.run()