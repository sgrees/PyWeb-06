
class Widget(object):
    """
    The Widget class shall present the class method:

        get_widget(name)

    which retrieves the widget of the given name.

    Each widget instance shall present the methods:

        get_value()
        set_value(value)

    which are self-explanatory.
    """
    
    name_widget_dict = {}

    def __init__(self, name):
        self.name = name
        self.value = '5'

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    @classmethod
    def get_widget(cls, name):
        try:
            widget = cls.name_widget_dict[name]
        except KeyError:
            widget = cls(name)

            cls.name_widget_dict[name] = widget

        return widget


