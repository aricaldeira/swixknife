
from flask import request


def browser_preferred_locale():
    al = request.headers.get('Accept-Language', 'en')

    if ',' in al:
        al = al.split(',')[0]

    if al == 'en':
        return 'iso'

    return al
