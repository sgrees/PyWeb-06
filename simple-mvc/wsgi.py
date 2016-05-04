"""
Widget Storage: a Simple MVC Application With Persistence

Each widget shall be addressed as follows:
    http://localhost:8080/example/
    http://localhost:8080/blarg/
    http://localhost:8080/4/

or any other alphanumeric "root" "directory". There
exists a widget at each possible widget address,
irrespective of whether or not that widget address
has yet been visited.

Each widget has a "name". The "names" of the widgets
in the examples above are "example", "blarg", and "4"

All widgets contain a "value". By default, that value
is "5" for every widget. However, it is possible to
set a widget's value.

All widget addresses shall accept POST requests and
GET requests.

A POST request shall include a form-encoded variable
named "value". This value shall be treated as a string,
and becomes the value of the widget at that address.

A GET request shall yield a well formatted html page
including some text declaring the value stored in that
widget, and a form allowing the visitor to change the
value of that variable.

"""

import cgi

from request import Request
from view import View


def main(request):
    """
    Returns a UNICODE STRING VALUED response body, given
    a request object.
    """

    return View.dispatch(request)

def makeFieldValueMap(environ):
    """
    Given a wsgi environ map, return a convenient
    field value map, ala cgi.FieldStorage.


    Suppose the user submits a form field such as:
    <input type="text" name="my-field">

    Then the value of that field will be available via:
    makeFieldValueMap(environ).getvalue("my-field", "default")
    """

    return cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)

def application(environ, start_response):
    headers = [('Content-type', 'text/html')]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        fields = makeFieldValueMap(environ)
        method = environ.get('REQUEST_METHOD')
        request = Request(method, path, fields)
        
        body = main(request)

        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1> Internal Server Error</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
