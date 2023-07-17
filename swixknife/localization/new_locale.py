#/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Shows the sezimal calendar')
parser.add_argument('-l', '--locale', dest='locale', help='Locale')

from swixknife import sezimal_locale


LOCALE_TEMPLATE = '''

__all__ = ('SezimalLocale{locale_class}',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocale{locale_class}(SezimalLocale):
    LANG = '{locale.LANG}'
    LANGUAGE = '{locale.LANGUAGE}'

    SEZIMAL_SEPARATOR = {sezimal_separator}

    GROUP_SEPARATOR = {group_separator}
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        '{locale.WEEKDAY_NAME[0]}',
        '{locale.WEEKDAY_NAME[1]}',
        '{locale.WEEKDAY_NAME[2]}',
        '{locale.WEEKDAY_NAME[3]}',
        '{locale.WEEKDAY_NAME[4]}',
        '{locale.WEEKDAY_NAME[5]}',
        '{locale.WEEKDAY_NAME[6]}',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        '{locale.WEEKDAY_ABBREVIATED_NAME[0]}',
        '{locale.WEEKDAY_ABBREVIATED_NAME[1]}',
        '{locale.WEEKDAY_ABBREVIATED_NAME[2]}',
        '{locale.WEEKDAY_ABBREVIATED_NAME[3]}',
        '{locale.WEEKDAY_ABBREVIATED_NAME[4]}',
        '{locale.WEEKDAY_ABBREVIATED_NAME[5]}',
        '{locale.WEEKDAY_ABBREVIATED_NAME[6]}',
    ]

    MONTH_NAME= [
        '{locale.MONTH_NAME[0]}',
        '{locale.MONTH_NAME[1]}',
        '{locale.MONTH_NAME[2]}',
        '{locale.MONTH_NAME[3]}',
        '{locale.MONTH_NAME[4]}',
        '{locale.MONTH_NAME[5]}',
        '{locale.MONTH_NAME[6]}',
        '{locale.MONTH_NAME[7]}',
        '{locale.MONTH_NAME[8]}',
        '{locale.MONTH_NAME[9]}',
        '{locale.MONTH_NAME[10]}',
        '{locale.MONTH_NAME[11]}',
    ]

    MONTH_ABBREVIATED_NAME = [
        '{locale.MONTH_ABBREVIATED_NAME[0]}',
        '{locale.MONTH_ABBREVIATED_NAME[1]}',
        '{locale.MONTH_ABBREVIATED_NAME[2]}',
        '{locale.MONTH_ABBREVIATED_NAME[3]}',
        '{locale.MONTH_ABBREVIATED_NAME[4]}',
        '{locale.MONTH_ABBREVIATED_NAME[5]}',
        '{locale.MONTH_ABBREVIATED_NAME[6]}',
        '{locale.MONTH_ABBREVIATED_NAME[7]}',
        '{locale.MONTH_ABBREVIATED_NAME[8]}',
        '{locale.MONTH_ABBREVIATED_NAME[9]}',
        '{locale.MONTH_ABBREVIATED_NAME[10]}',
        '{locale.MONTH_ABBREVIATED_NAME[11]}',
    ]

    DATE_FORMAT = '{locale.DATE_FORMAT}'
    DATE_LONG_FORMAT = '{locale.DATE_LONG_FORMAT}'
    TIME_FORMAT = '{locale.TIME_FORMAT}'
    DATE_TIME_FORMAT = '{locale.DATE_TIME_FORMAT}'
    DATE_TIME_LONG_FORMAT = '{locale.DATE_TIME_LONG_FORMAT}'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'UTC'

    SEASON_NAME = {{
        'spring_cross_quarter': 'Spring Cross-Quarter',
        'spring_equinox': 'Spring',
        'summer_cross_quarter': 'Summer Cross-Quarter',
        'summer_solstice': 'Summer',
        'autumn_cross_quarter': 'Autumn Cross-Quarter',
        'autumn_equinox': 'Autumn',
        'winter_cross_quarter': 'Winter Cross-Quarter',
        'winter_solstice': 'Winter',
    }}

    MOON_PHASE = {{
        'new': 'New',
        'waxing_crescent': 'Waxing Crescent',
        'first_quarter': 'First Quarter',
        'waxing_gibbous': 'Waxing Gibbous',
        'full': 'Full',
        'waning_gibbous': 'Waning Gibbous',
        'third_quarter': 'Third Quarter',
        'waning_crescent': 'Waning Crescent',
    }}

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDAR = []
    WEEKDAY_ERROR = 'Invalid weekday {{weekday}}'
    MONTH_ERROR = 'Invalid month {{month}}'
'''


if __name__ == '__main__':
    arguments = parser.parse_args()

    locale = sezimal_locale(arguments.locale, force_icu=True)

    locale_class = arguments.locale.upper().replace('-', '_')

    if locale.SEZIMAL_SEPARATOR == '.':
        sezimal_separator = 'SEPARATOR_DOT'
    elif locale.SEZIMAL_SEPARATOR == ',':
        sezimal_separator = 'SEPARATOR_COMMA'
    elif locale.SEZIMAL_SEPARATOR == '\u0020\u00a0':
        sezimal_separator = 'SEPARATOR_NARROW_NOBREAK_SPACE'
    else:
        sezimal_separator = f"'{locale.SEZIMAL_SEPARATOR}'"

    if locale.GROUP_SEPARATOR == '.':
        group_separator = 'SEPARATOR_DOT'
    elif locale.GROUP_SEPARATOR == ',':
        group_separator = 'SEPARATOR_COMMA'
    elif locale.GROUP_SEPARATOR in '\u0020\u00a0':
        group_separator = 'SEPARATOR_NARROW_NOBREAK_SPACE'
    else:
        group_separator = f"'{locale.GROUP_SEPARATOR}'"

    text = LOCALE_TEMPLATE.format(
        locale_class=locale_class,
        locale=locale,
        sezimal_separator=sezimal_separator,
        group_separator=group_separator,
    )

    print(text)
