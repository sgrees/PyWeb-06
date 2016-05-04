class Request(object):

    def __init__(self, method, path, fields):
        self.method = method
        self.path = path
        self.fields = fields
