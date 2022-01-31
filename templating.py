from jinja2 import Environment, FileSystemLoader
from http_server import Content, web_server

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

data = {
    "name": "HMTMCSE",
    "age": 30,
    "register_id": 12,
}

template = env.get_template('page.html')
output = template.render(data=data)

# Custom Web server for see the output into browser
Content.html = output
web_server.serve_forever()
# Browse from the browser http://localhost:1212/
