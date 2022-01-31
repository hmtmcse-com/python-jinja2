from http_server import web_server, Content

Content.html = "Render something"
web_server.serve_forever()
