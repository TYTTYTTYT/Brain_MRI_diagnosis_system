# %%
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

# %%
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        # self.send_header('hh', 'awf')
        self.end_headers()
        response = BytesIO()
        with open('model_example', 'rb') as model:
            response.write(model.read())
        self.wfile.write(response.getvalue())
        print(self.headers)
        print(self.path)
        print("Incomming address", self.client_address)
        content = self.rfile.read()
        print(content)

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
httpd = HTTPServer(('', 8880), SimpleHTTPRequestHandler)
httpd.serve_forever()
