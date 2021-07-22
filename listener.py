# %%
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

# %%
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        with open('model_example', 'rb') as model:
            response.write(model.read())
        self.wfile.write(response.getvalue())
        print("Incomming address", self.client_address)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

# %%
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
