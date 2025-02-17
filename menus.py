from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MenusWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 700)

        self.setWindowTitle("Menus Basics")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")

        toolbar = QToolBar("Main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"), "Some Other Action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click Here"))

        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

        button1 = QPushButton("BUTTON")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        print("Action Triggered")
        self.statusBar().showMessage("Message from my app", 3000)

    def button1_clicked(self):
        self.statusBar().showMessage("Button 1 pressed", 2000)