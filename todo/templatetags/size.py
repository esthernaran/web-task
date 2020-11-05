from django import template
from django.utils.safestring import mark_safe

register = template.Library()

SIZES = {
    1: ('XS', 'xtrasmall'),
    2: ('S', 'small'),
    3: ('M', 'medium'),
    4: ('L', 'large'),
    5: ('XL', 'xtralarge'),
}

@register.filter()
def as_task_size(size_level, format="short"):
    if size_level < 0 or size_level >5:
        return size_level
    t = SIZES.get(size_level)
    if format == 'long':
        index = 1
    else:
        index = 0
    return t[index]
