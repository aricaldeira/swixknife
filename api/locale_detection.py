
from flask import request


def browser_preferred_locale():
    try:
        al = request.headers.get('Accept-Language', 'en')
    except:
        return 'en-us'

    if ',' in al:
        al = al.split(',')[0]

    if al == 'en':
        return 'iso'

    return al
