from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout

class ButtonWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 700)

        self.setWindowTitle('Button Basics')

        button = QPushButton('Press')
        button.clicked.connect(self.greeting)

        self.setCentralWidget(button)

    def greeting(self):
        print("Hello!")

class ButtonWidget(QWidget):
    def __init__(self):
        super().__init__()
        #signals
        self.setWindowTitle("Custom MAinWindow")

        button = QPushButton("Click")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def button_clicked(self):
        print("clicked")
    def button_pressed(self):
        print("pressed")
    def button_released(self):
        print("released")
