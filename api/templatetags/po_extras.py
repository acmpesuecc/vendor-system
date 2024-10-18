# templatetags/po_extras.py

from django import template

register = template.Library()

@register.filter
def sum_price(items):
    total_price = 0
    for item in items:
        total_price += item['price'] * item['quantity']
    return total_price
