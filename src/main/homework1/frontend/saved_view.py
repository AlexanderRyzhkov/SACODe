from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget

from src.main.homework1 import config
from src.main.homework1.frontend.utils import center


class SavedView(QMainWindow):
    def __init__(self, previous_view):
        super().__init__()
        self.setWindowTitle("Filters")
        center(self)
        self.setCentralWidget(self.configure_main_widget(previous_view))

    def configure_main_widget(self, previous_view):
        main_widget = QWidget()
        main_widget.setLayout(self.configure_main_layout(previous_view))

        return main_widget

    def configure_main_layout(self, previous_view):
        def ok_button_click():
            previous_view.show()
            self.hide()

        description = QLabel()
        description.setText(f"Successfully saved to {config.directory_to_save}")

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(ok_button_click)

        main_layout = QVBoxLayout()
        main_layout.addWidget(description)
        main_layout.addWidget(ok_button)

        return main_layout