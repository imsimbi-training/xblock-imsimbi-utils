"""
Template tags and helper functions for email templates
"""


from django import template
from django.conf import settings

register = template.Library()  # pylint: disable=invalid-name

print('Registering imsimbi_utils tags')

@register.simple_tag(name="registration_url")
def registration_url():
    """
    Django template tag that outputs the URL of the registration page
    {% registration_url %}
    """
    return settings.IMSIMBI_REGISTRATION_URL
