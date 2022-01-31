from jinja2 import Template

# Default configuration
text = """
<div>
    {% if True %}
        some text
    {% endif %}
</div>

<div>
    {%- if True %}
        some text
    {%- endif %}
</div>
"""

template = Template(text)
response = template.render()
print(response)


# Removed Whitespace
text = """
<div>
    {% if True %} With White space {% endif %}
</div>

<div>
    {%- if True %} Removed White space {% endif -%}
</div>
"""

template = Template(text)
response = template.render()
print(response)

