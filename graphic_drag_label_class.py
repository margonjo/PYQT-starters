from PyQt4.QtGui import *
from PyQt4.QtCore import *
import field_resources

class QDragLabel(QLabel):
    """This class provides an image label that can be dragged and dropped"""

    def __init__ (self, picture):
        super().__init__()
        self.setPixmap(picture.scaledToWidth(35,1))
        self.mimetext = None

    def mouseMoveEvent(self,event):
        if event.buttons() == Qt.LeftButton:
            data = QByteArray()
            mime_data = QMimeData()
            mime_data.setData(self.mimetext,data)
            drag = QDrag(self)
            drag.setMimeData(mime_data)
            drag.setHotSpot(self.rect().topLeft())
            drop_action = drag.start(Qt.MoveAction)


class WheatDragLabel(QDragLabel):
    """This class provides a Wheat label that can be dragged and dropped"""
    def __init__(self):
        super().__init__(QPixmap(":/wheat_seed.png"))
        self.mimetext = "application/x-wheat"

class PotatoDragLabel(QDragLabel):
    """This class provides a potato label that can be dragged and dropped"""
    def __init__(self):
        super().__init__(QPixmap(":/potato_seed.png"))
        self.mimetext = "application/x-potato"

class CowDragLabel(QDragLabel):
    """This class provides a cow label that can be dragged and dropped"""
    def __init__(self):
        super().__init__(QPixmap(":/cow_baby.png"))
        self.mimetext = "application/x-cow"

class SheepDragLabel(QDragLabel):
    """This class provides a sheep label that can be dragged and dropped"""
    def __init__(self):
        super().__init__(QPixmap(":/sheep_baby.png"))
        self.mimetext = "application/x-sheep"
