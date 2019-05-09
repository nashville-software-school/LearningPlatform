from django import template
from django.contrib.auth.models import Group

register = template.Library()

# Uses groups from admin to verify user is an instructor. Only instructors can create student notes
# Note that this custom Library is registered in settings.py, under TEMPLATES
@register.filter(name='has_group')
def has_group(user, group_name):
    try:
      group = Group.objects.get(name='instructors')
      return True if group in user.groups.all() else False
    except Group.DoesNotExist:
      return
