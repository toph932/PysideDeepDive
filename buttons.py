from PySide6.QtWidgets import QMainWindow, QPushButton

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
