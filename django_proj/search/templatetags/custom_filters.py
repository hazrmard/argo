from django import template
register = template.Library()

@register.filter
def get_range(num):
    return range(1, num+1)

@register.filter
def concat_page_query(val, arg):
    return str(val) + '&page=' + str(arg)

@register.filter
def process_date(val):
    return '\t'.join(val.split('T'))