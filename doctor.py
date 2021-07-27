# %%
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

# %%
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    file_idx = 0
    message = "Hi, don't worry, you are fine!"
    def do_GET(self):
        self.send_response(200)
        # self.send_header('hh', 'awf')
        self.end_headers()
        response = BytesIO()
        response.write(SimpleHTTPRequestHandler.message)
        self.wfile.write(response.getvalue())
        print("Incomming address", self.client_address)
        content = self.rfile.read()

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
        print(len(body))
        print(type(body))
        print(body)

        with open('image/' + str(self.file_idx), 'wb') as file:
            SimpleHTTPRequestHandler.file_idx += 1
            file.write(body)

# %%
httpd = HTTPServer(('', 2095), SimpleHTTPRequestHandler)
httpd.serve_forever()
