"""
Template tags and helper functions for email templates
"""


from django import template
from django.conf import settings

register = template.Library()  # pylint: disable=invalid-name


@register.simple_tag(name="imsimbi_registration_url")
def imsimbi_registration_url():
    """
    Django template tag that outputs the URL of the registration page
    {% imsimbi_registration_url %}
    """
    return settings.IMSIMBI_REGISTRATION_URL

@register.filter(name="imsimbi_registration_url_email")
def imsimbi_registration_url_email(email):
    """
    Django template filter to retur a registration rul with an email query parameter.
    {{ email|imsimbi_registration_url_email }}
    """
    return settings.IMSIMBI_REGISTRATION_URL+"?email="+email
