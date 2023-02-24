import os
from os import listdir
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
from src.main.homework1 import config
from src.main.homework1.frontend.saved_view import SavedView
from src.main.homework1.frontend.utils import center


class TwoPicturesView(QMainWindow):
    def __init__(self, previous_view, pixmap_without_filters, pixmap_with_filters):
        super().__init__()
        self.setWindowTitle("Filters")
        center(self)
        self.setCentralWidget(
            self.configure_main_widget(previous_view, pixmap_with_filters, pixmap_without_filters))


    def configure_main_widget(self, previous_view, pixmap_with_filters, pixmap_without_filters):
        main_widget = QWidget()
        main_widget.setLayout(
            self.configure_main_layout(previous_view, pixmap_with_filters, pixmap_without_filters))

        return main_widget

    def configure_main_layout(self, previous_view, pixmap_with_filters, pixmap_without_filters):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.configure_pictures_layout(pixmap_without_filters, pixmap_with_filters))
        main_layout.addLayout(self.configure_menu_layout(previous_view, pixmap_with_filters))

        return main_layout

    def configure_menu_layout(self, previous_view, pixmap_with_filters):
        def save_button_click():
            path = config.directory_to_save
            if not os.path.exists(path):
                os.mkdir(path)

            pixmap_with_filters.save(f"{path}/file{len(listdir(path))}.png")

            SavedView(self).show()
            self.hide()

        def back_button_click():
            previous_view.show()
            self.hide()

        save_button = QPushButton("Save result")
        save_button.clicked.connect(save_button_click)

        back_button = QPushButton("Back")
        back_button.clicked.connect(back_button_click)

        menu_layout = QHBoxLayout()
        menu_layout.addWidget(save_button)
        menu_layout.addWidget(back_button)

        return menu_layout

    def configure_pictures_layout(self, pixmap_without_filters, pixmap_with_filters):
        pictures_layout = QHBoxLayout()
        pictures_layout \
            .addLayout(self.configure_picture_layout("Picture without filters", pixmap_without_filters))
        pictures_layout \
            .addLayout(self.configure_picture_layout("Picture with filters", pixmap_with_filters))

        return pictures_layout

    def configure_picture_layout(self, description, pixmap):
        description_label = QLabel()
        description_label.setText(description)

        picture_label = QLabel()
        picture_label.setPixmap(pixmap)

        picture_layout = QVBoxLayout()
        picture_layout.addWidget(description_label)
        picture_layout.addWidget(picture_label)

        return picture_layout


