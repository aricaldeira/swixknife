
import os

import swixknife
from ..localization import SezimalLocale


def user_preferences(locale: SezimalLocale = None) -> dict:
    if not os.path.isfile(os.path.expanduser('~/.swixknife.py')):
        return {}

    arq = open(os.path.expanduser('~/.swixknife.py'), 'r').read()
    code = compile(arq, '', 'exec')
    localdict = {}
    globaldict = swixknife.__dict__
    globaldict['locale'] = locale
    eval(code, globaldict, localdict)

    return localdict
