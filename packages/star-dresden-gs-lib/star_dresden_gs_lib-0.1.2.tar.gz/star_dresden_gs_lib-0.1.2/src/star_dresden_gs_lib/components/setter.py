from typing import Callable

from PyQt6 import QtWidgets


class SetterWidget(QtWidgets.QWidget):

    def __init__(self, name: str, endpoint: Callable, button: QtWidgets.QPushButton = QtWidgets.QPushButton('None'),
                 text: QtWidgets.QLabel = QtWidgets.QLabel('None'), execute_func: Callable = None, *args, **kwargs):
        """

        :param name: the name of the Widget
        :param endpoint: a Callable function for either the Endpoint
        :param button_pos: (optional)
        :param text_pos: (optional)
        :param execute_func: (optional) a custom function for the button press
        :param args: (optional)
        :param kwargs: (optional)
        """
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.name = name
        self._endpoint = endpoint

        self.button = button
        self.button.setObjectName(name)
        # self.input_field = QtWidgets.QLineEdit
        self.text = text

        # noinspection PyUnresolvedReferences
        # self.textbox.textChanged.connect(self.textbox_text_changed)
        self.button.clicked.connect(self.__execute if execute_func is None else execute_func)

        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.text, 0, 0)
        self.layout.addWidget(self.text, 0, 2)


    def __change_text(self, value):
        self.text.setText(f"{self.name}: {value}")

    def __execute(self):
        value = self._endpoint()


