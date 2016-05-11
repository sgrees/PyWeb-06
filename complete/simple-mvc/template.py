page = """

<html>
<body>
    <p>The value of this widget is {value}</p>
    <form method="POST" target=".">
        Value: <input type="text" name="value">
        <input type="submit" name="submit" value="submit">
    </form>
</body>
</html>

"""


class Template(object):

    @staticmethod
    def render(context):
        return page.format(**context)
