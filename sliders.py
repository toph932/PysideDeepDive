from PySide6.QtWidgets import QMainWindow, QSlider
from PySide6.QtCore import Qt

class SliderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Slider Basics')
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 700)

        slider = QSlider(Qt.Orientation.Horizontal)

        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(25)

        slider.valueChanged.connect(self.slider_response)
        self.setCentralWidget(slider)

    def slider_response(self, data):
        print(f'slider moved to {data}')
