from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class WidgetsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 700)

        self.setWindowTitle('Widget Basics')

        # button_layout = QHBoxLayout()
        button_layout = QVBoxLayout()

        button1 = QPushButton("BUTTON1")
        button_layout.addWidget(button1)
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton("BUTTON2")
        button_layout.addWidget(button2)
        button2.clicked.connect(self.button2_clicked)

        self.setLayout(button_layout)

    def button1_clicked(self):
        print("button one clicked")

    def button2_clicked(self):
        print("button two clicked")
