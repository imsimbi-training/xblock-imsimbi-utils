"""
Template tags and helper functions for email templates
"""


from django import template
from django.conf import settings
from urllib.parse import quote


register = template.Library()  # pylint: disable=invalid-name


@register.simple_tag(name="imsimbi_registration_url")
def imsimbi_registration_url():
    """
    Django template tag that outputs the URL of the registration page
    {% imsimbi_registration_url %}
    """
    print('imsimbi_registration_url: ' + settings.IMSIMBI_REGISTRATION_URL)
    return settings.IMSIMBI_REGISTRATION_URL

@register.filter(name="imsimbi_registration_url_email")
def imsimbi_registration_url_email(email):
    """
    Django template filter to retur a registration rul with an email query parameter.
    {{ email|imsimbi_registration_url_email }}
    """
    print('imsimbi_registration_url: ' + settings.IMSIMBI_REGISTRATION_URL + "?email=" + email)
    return settings.IMSIMBI_REGISTRATION_URL + "?email=" + email


@register.simple_tag(name="imsimbi_profile_url")
def imsimbi_profile_url():
    """
    Django template tag that outputs the URL of the registration page
    {% imsimbi_registration_url %}
    """
    print('imsimbi_profile_url: ' + settings.IMSIMBI_PROFILE_URL)
    return settings.IMSIMBI_PROFILE_URL

@register.filter(name="imsimbi_account_activation_url")
def imsimbi_account_activation_url(openedx_url):
    """
    Django template filter to return an activation url that is handled by the Imsimbi app rather than the openedx LMS.
    {{ openedx_url|imsimbi_account_activation_url }}
    """
    url = settings.IMSIMBI_ACTIVATION_URL+"?activation_url="+quote(openedx_url)
    print('imsimbi_account_activation_url: ' + url)
    return url


