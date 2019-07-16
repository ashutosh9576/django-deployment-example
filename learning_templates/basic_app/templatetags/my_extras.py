from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """This cuts all values of "arg" from the string i.e. value"""
    return value.replace(arg,'')

# register.filter('cut',cut)