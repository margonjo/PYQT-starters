from PyQt4.QtGui import *

class FieldItemGraphicPixmapItem(QGraphicsPixmapItem):
    """This class provides a pixmap item with a preset image for the item"""

    def __init__(self, graphics_list):
        super().__init__()
        self.available_graphics = graphics_list
        self.current_graphic = QPixmap(self.available_graphics[0])
        self.setPixmap(self.current_graphic.scaledToWidth(25,1))
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def update_status(self):
        pass
