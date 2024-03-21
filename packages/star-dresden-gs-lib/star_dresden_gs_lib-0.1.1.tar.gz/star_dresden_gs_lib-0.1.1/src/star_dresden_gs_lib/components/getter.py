import random
import sys
from typing import Callable, Tuple

from PyQt6 import QtWidgets

from star_dresden_gs_lib.tools.async_tools import run_async


# TODO: No Param
#       Single Param:       GetterWithParamWidget, AsyncGetterWithParamWidget
#       Multiple Params:    GetterWithParamsWidget, AsyncGetterWithParamsWidget

class GetterWidget(QtWidgets.QWidget):

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
        self.button.setText(name)
        # self.input_field = QtWidgets.QLineEdit
        self.text = text
        self.text.setText(name)

        self.last_data = {}

        # noinspection PyUnresolvedReferences
        # self.textbox.textChanged.connect(self.textbox_text_changed)
        self.button.clicked.connect(self.__execute if execute_func is None else execute_func)

        self.layout.addWidget(self.button, 0, 0)
        self.layout.addWidget(self.text, 0, 1)


    def __change_text(self, value):
        self.text.setText(f"{self.name}: {value}")

    def __execute(self):
        value = self._endpoint()
        self.last_data = value


class GetterWidgetAsync(QtWidgets.QWidget):

    def __init__(self, name: str, endpoint: Callable, button: QtWidgets.QPushButton = QtWidgets.QPushButton('None'),
                 text: QtWidgets.QLabel = QtWidgets.QLabel('None'), execute_func: Callable = None, *args, **kwargs):
        """

        :param name: the name of the Widget
        :param endpoint: a Async Callable function for either the Endpoint
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
        self.button.setText(name)
        # self.input_field = QtWidgets.QLineEdit
        self.text = text
        self.text.setText(name)

        self.last_data = {}
        #self.last_sent = {}

        # noinspection PyUnresolvedReferences
        # self.textbox.textChanged.connect(self.textbox_text_changed)
        self.button.clicked.connect(self.__execute if execute_func is None else execute_func)

        self.layout.addWidget(self.button, 0, 0)
        self.layout.addWidget(self.text, 0, 1)



    def __change_text(self, value):
        self.text.setText(f"{self.name}: {value}")

    def __resolve_data_callback(self, data):
        self.last_data = data

    @run_async(__resolve_data_callback)
    def __execute(self):
        return self._endpoint()


class GetterWithParamWidget(QtWidgets.QWidget):

    def __init__(self, name: str, endpoint: Callable, input_field: QtWidgets.QLineEdit=QtWidgets.QLineEdit("input"),  button: QtWidgets.QPushButton = QtWidgets.QPushButton('None'),
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
        self.button.setText(name)
        # self.input_field = QtWidgets.QLineEdit
        self.text = text
        self.text.setText(name)

        self.input_field = input_field

        self.last_data = {}
        self.last_sent = {}

        # noinspection PyUnresolvedReferences
        # self.textbox.textChanged.connect(self.textbox_text_changed)
        self.button.clicked.connect(self.__execute if execute_func is None else execute_func)

        self.layout.addWidget(self.input_field,0,0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.text, 0, 2)

    def __change_text(self, value):
        self.text.setText(f"{self.name}: {value}")

    def __execute(self):
        self.last_sent = self.input_field.text()
        value = self._endpoint()
        self.last_data = value


class GetterWithParamWidgetAsync(QtWidgets.QWidget):

    def __init__(self, name: str, endpoint: Callable, input_field: QtWidgets.QLineEdit=QtWidgets.QLineEdit("input"), button: QtWidgets.QPushButton = QtWidgets.QPushButton('None'),
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
        self.button.setText(name)
        # self.input_field = QtWidgets.QLineEdit
        self.text = text
        self.text.setText(name)

        self.input_field = input_field

        self.last_data = {}
        self.last_sent = {}

        # noinspection PyUnresolvedReferences
        # self.textbox.textChanged.connect(self.textbox_text_changed)
        self.button.clicked.connect(self.__execute if execute_func is None else execute_func)

        self.layout.addWidget(self.input_field, 0, 0)
        self.layout.addWidget(self.button, 0, 1)
        self.layout.addWidget(self.text, 0, 2)


    def set_button_pos(self, x,y):
        self.layout.removeWidget(self.button)
        self.layout.addWidget(self.button, x, y)

    def set_text_pos(self, x,y):
        self.layout.removeWidget(self.button)
        self.layout.addWidget(self.button, x, y)

    def set_input_pos(self, x,y):
        self.layout.removeWidget(self.button)
        self.layout.addWidget(self.button, x, y)

    def __change_text(self, value):
        self.text.setText(f"{self.name}: {value}")


    def __resolve_data_callback(self, data):
        self.last_data = data

    @run_async(__resolve_data_callback)
    def __execute(self):
        self.last_sent=self.input_field.text()
        return self._endpoint(self.last_sent)