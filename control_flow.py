from jinja2 import Template

text_content = """

{%- if data.name %}
    Hi {{data.name}}
{%- endif %}

{%- if not data.nothing %}
    Nothing
{%- endif %}

{%- if data.something %}
    Something
{%- endif %}

{%- if data.age < 18 %}
    You are under age
{%- elif data.age == 18 %}
    You are 18
{%- elif data.age > 18 %}
    You are 18+
{%- endif %}

"""

data = {
    "name": "HMTMCSE",
    "age": 17,
}

template = Template(text_content)
response = template.render(data=data)

print(response)

text_content = """
{% for user in data.users %}
    {{- user.name}} - {{- user.age}}
{% else %}
    No data Available
{% endfor %}
"""

data = {
    "users": [
        {"name": "User 1", "age": 10},
        {"name": "User 2", "age": 12},
        {"name": "User 3", "age": 13},
        {"name": "User 4", "age": 14},
    ]
}

template = Template(text_content)
response = template.render(data=data)

print(response)
