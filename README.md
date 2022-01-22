# Imsimbi Utils XBlock

## Introduction

This XBlock applies various utilities for use with email templates, for example, constructing URLs to the imsimbi web app.

I am not sure if this needs to be an XBlock or not. As an XBlock it does not get picked up, so I currently need to do this in settings, through the `imsimbiutils.yml` plugin:

```
INSTALLED_APPS.append('xblock_imsimbi_utils')
```

as well as add it to the `private.txt` to be built into the image.


## `imsimbi_utils` template tags

```
{% load imsimbi_utils %}
```


`{% imsimbi_registration_url %}` the URL for registration on the Imsimbi app

`{{ email_address|imsimbi_registration_url_email }}` the URL for registration on the Imsimbi app with a query param `?email={email_address}` appended