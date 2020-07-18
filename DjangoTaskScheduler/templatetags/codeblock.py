from django import template


def code(value):
    return "\n".join([f"<code>{l}</code>" for l in value.splitlines()])


register = template.Library()

register.filter('code', code)
