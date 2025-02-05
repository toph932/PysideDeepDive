from PySide6.QtWidgets import QMainWindow

class MenusWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 700)

        self.setWindowTitle("Menus Basics")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")