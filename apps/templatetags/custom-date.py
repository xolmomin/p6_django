from django import template

register = template.Library()


@register.filter
def posted_time(value):
    return '4 minutes ago'


'''
0-59 (sec) now
1-59 (min) minutes ago
1-23 (hour) hours ago
1-30 (day) days ago
31-360 (month) months ago
366- (years) years ago

'''