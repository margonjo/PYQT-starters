import sys
import random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *
from manual_grow_dialog_class import *
from crop_view import *

from wheat_class import *
from potato_class import *

class CropWindow(QMainWindow):
    """this class creates a main window to observe the growth of a singal crop"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop simulatot")
        self.create_select_crop_layout()

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.select_crop_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def create_select_crop_layout(self):
        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop", ("wheat","potato"))
        self.instantiate_button = QPushButton("Create Crop")

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)



        self.instantiate_button.clicked.connect(self.instantiate_crop)

    def create_view_crop_layout(self,crop_type):
        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days growing")
        self.status_label = QLabel("Crop status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        if crop_type ==1:
            self.crop_view = WheatView()
        elif crop_type ==2:
            self.crop_view = PotatoView()
        self.crop_view.setHorizontalScrollBarPolicy(1)
        self.crop_view.setVerticalScrollBarPolicy(1)
        self.crop_view.setFixedHeight(182)
        self.crop_view.setFixedWidth(242)
        self.manual_grow_button = QPushButton("Manually grow")
        self.automatic_grow_button = QPushButton("automatically grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        self.grow_grid.addWidget(self.crop_view,0,0)
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)

        self.automatic_grow_button.clicked.connect(self.automatically_grow_crop)
        self.manual_grow_button.clicked.connect(self.manually_grow_crop)

    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button()
        if crop_type ==1:
            self.simulated_crop = Wheat()

        elif crop_type ==2:
            self.simulated_crop  = Potato()
        self.create_view_crop_layout(crop_type)
        self.stacked_layout.addWidget(self.view_crop_widget)
        self.stacked_layout.setCurrentIndex(1)

    def automatically_grow_crop(self):
        for days in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            self.simulated_crop.grow(light,water)
        self.update_crop_view_status()

    def manually_grow_crop(self):
        manual_values_dialog = ManualGrowDialog()
        manual_values_dialog.exec_()
        light, water = manual_values_dialog.values()
        self.simulated_crop.grow(light,water)
        self.update_crop_view_status()
    
    def update_crop_view_status(self):
        crop_status_report = self.simulated_crop.report()
        if crop_status_report["status"] == "Seed":
            self.crop_view.switch_scene(0)
        elif crop_status_report["status"] == "Seedling":
            self.crop_view.switch_scene(1)
        elif crop_status_report["status"] == "Young":
            self.crop_view.switch_scene(2)
        elif crop_status_report["status"] == "Mature":
            self.crop_view.switch_scene(3)
        elif crop_status_report["status"] == "Old":
            self.crop_view.switch_scene(4)
            
            

        self.growth_line_edit.setText(str(crop_status_report["growth"]))
        self.days_line_edit.setText(str(crop_status_report["days growing"]))
        self.status_line_edit.setText(str(crop_status_report["status"]))
def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()
    
if __name__ == "__main__":
    main()
