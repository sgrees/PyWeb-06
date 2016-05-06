page = """
<html>
<body>
    <p>The value of this widget is {value}</p>
    <form method="POST" target=".">
        value: <input type="text" name="value">
        <input type="submit" name="submit" value="submit">
    </form>
</body>
</html>
"""

class Template(object):
    @staticmethod
    def render(context):
        # Hopefully, context looks like:
        # {'value': '5'}

        return page.format(**context)
