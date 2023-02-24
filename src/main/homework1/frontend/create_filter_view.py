from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QWidget, QLabel

from src.main.homework1.frontend.utils import center


class CreateFilterView(QMainWindow):
    def __init__(self, previous_view, filters_matrices_list, filters_list_layout):
        def configure_main_widget():
            self.filter_matrix_layout = QVBoxLayout()
            main_widget = QWidget()
            main_widget.setLayout(self.configure_main_layout(previous_view, filters_matrices_list, filters_list_layout))

            return main_widget

        super().__init__()
        self.setWindowTitle("Filters")
        #center(self)
        self.setCentralWidget(configure_main_widget())

    def configure_main_layout(self, previous_view, filters_matrices_list, filters_list_layout):
        main_layout = QHBoxLayout()
        main_layout.addLayout(self.configure_filter_matrix_info_layout())
        main_layout.addLayout(
            self.configure_menu_layout(previous_view, filters_matrices_list, filters_list_layout))

        return main_layout

    def configure_menu_layout(self, previous_view, filters_matrices_list, filters_list_layout):
        admit_button = QPushButton("Admit")
        admit_button.clicked.connect(lambda:
            self.admit_button_click(previous_view, filters_matrices_list, filters_list_layout))

        back_button = QPushButton("Back")
        back_button.clicked.connect(lambda: self.back_button_click((previous_view)))

        menu_layout = QVBoxLayout()
        menu_layout.addLayout(self.configure_change_dimensions_layout())
        menu_layout.addWidget(admit_button)
        menu_layout.addWidget(back_button)

        return menu_layout

    def configure_dimensions_parameters_layout(self, width, height):
        def configure_layout(label_text, widget):
            label = QLabel()
            label.setText(label_text)

            layout = QVBoxLayout()
            layout.addWidget(label)
            layout.addWidget(widget)

            return layout

        def configure_width_layout():
            return configure_layout("Width (Only positive, odd numbers):", width)

        def configure_height_layout():
            return configure_layout("Width (Only positive, odd numbers):", height)

        dimensions_parameters_layout = QHBoxLayout()
        dimensions_parameters_layout.addLayout(configure_width_layout())
        dimensions_parameters_layout.addLayout(configure_height_layout())

        return dimensions_parameters_layout

    def init_filter_matrix(self, n, m):
        for i in range(self.filter_matrix_layout.count()):
            cur_line = self.filter_matrix_layout.itemAt(i)

            for j in range(cur_line.count()):
                cur_line.itemAt(j).widget().deleteLater()

            cur_line.layout().deleteLater()

        for i in range(n):
            horizontal_layout = QHBoxLayout()

            for j in range(m):
                element = QLineEdit()
                element.setText("0")

                horizontal_layout.addWidget(element)

            self.filter_matrix_layout.addLayout(horizontal_layout)

        return self.filter_matrix_layout

    def configure_filter_matrix_info_layout(self):
        label = QLabel()
        label.setText("Filter matrix")

        filter_matrix_info_layout = QVBoxLayout()
        filter_matrix_info_layout.addWidget(label)
        filter_matrix_info_layout.addLayout(self.init_filter_matrix(3, 3))

        return filter_matrix_info_layout

    def admit_button_click(self, previous_view, filters_matrices_list, filters_list_layout):
        result = []
        correct = True
        for i in range(self.filter_matrix_layout.count()):
            horizontal = self.filter_matrix_layout.itemAt(i)
            line = []
            for j in range(horizontal.count()):
                try:
                    line.append(int(horizontal.itemAt(j).widget().text()))
                except ValueError:
                    correct = False
                    horizontal.itemAt(j).widget().setText("0")

            result.append(line)

        if not correct:
            return

        filters_matrices_list.append(result)

        label = QLabel()
        label.setText("Custom filter")
        filters_list_layout.addWidget(label)

        previous_view.show()
        self.hide()

    def change_dimensions_button_click(self, height, width):
        correct = True
        try:
            h = int(height.text())
            w = int(width.text())

            if h <= 0 or h % 2 == 0 or w <= 0 or w % 2 == 0:
                correct = False
            else:
                self.init_filter_matrix(h, w)
        except ValueError:
            correct = False

        if not correct:
            width.setText(f"{self.filter_matrix_layout.itemAt(0).count()}")
            height.setText(f"{self.filter_matrix_layout.count()}")

    def configure_change_dimensions_layout(self):
        width = QLineEdit()
        width.setText("3")

        height = QLineEdit()
        height.setText("3")

        description = QLabel()
        description.setText("Change matrix dimensions")

        change_dimensions_button = QPushButton("Change dimensions")
        change_dimensions_button.clicked.connect(lambda: self.change_dimensions_button_click(height, width))

        change_dimensions_layout = QVBoxLayout()
        change_dimensions_layout.addWidget(description)
        change_dimensions_layout.addLayout(self.configure_dimensions_parameters_layout(width, height))
        change_dimensions_layout.addWidget(change_dimensions_button)

        return change_dimensions_layout

    def back_button_click(self, previous_view):
        previous_view.show()
        self.hide()


