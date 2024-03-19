# STAR Dresden Rover Groundstation Lib

## Description
A Library for creating a Groundstation using PyQt6.
It contains multiple Components, which can be used as Framework for creating A Groundstation.



## Installation
`pip install star-dresden-gs-lib`

## Usage

Note that the Widgets are using CamelCase instead of snake_case because of PyQts Guidelines.

### Components
#### Getter
`from components.getter import GetterWidget`
``` python
# widget with required args name and a callable to execute
self.getter_widget = GetterWidget("rand", self.randnum)
# add the widget to your layout (preferable grid)
self.layout.addWidget(self.getter_widget, 0, 0)

# the callable function used in this case
def rand_num(self):
    return random.randint(0, 200)
```
Parameters:
- `name`: the name of the Widget that will be displayed on the button
- `endpoint`: a Callable function used as endpoint by the button presses execute function
- `button_pos`: (optional) a tuple containing x and y int values for the button position in its internal grid
- `text_pos`: (optional) a tuple containing x and y int values for the label position in its internal grid
- `execute_func`: (optional) a custom function for the button press, note that the endpoint operator is obsolete and the label won't change when using this. Consider just using a Button instead

## Authors and acknowledgment
Members of STAR Dresden:
- Lars Lukas Reiche
