from jinja2 import Template

text_content = """
Hi {{name}},
Your registration ID is {{register_id}}.
Your Age is : {{age}}
"""

template = Template(text_content)
response = template.render(name="HMTMCSE", register_id=12, age=30)

print(response)
