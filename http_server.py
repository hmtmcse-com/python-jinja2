from http.server import BaseHTTPRequestHandler, HTTPServer


class Content:
    html = "Web Server"


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(Content.html, "utf8"))


web_server = HTTPServer(('', 1212), RequestHandler)

