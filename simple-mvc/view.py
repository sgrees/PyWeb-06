from model import widget
from template import Template

class View(object):

    @classmethod
    def dispatch(cls.request):
        path = request.path
        name = path.strip('/').split('/')[0]

        widget = widget.get_widget(name)

        method = {
            'GET': cls.get,
            'POST': cls.post,
        }.get(request.method)

        return method(request, widget)

    @classmethod
    def get(cls, request, widget):
        return cls.render_widget(widget)

    @classmethod
    def post(cls, request, widget):
        new_value = request.fields.getvalue('value')

        widget.set_value(new_value)

        return cls.render_widget(widget)

    @classmethod
    def render_widget(cls, widget):
        return Template.render({'value': widget.get_value()})
