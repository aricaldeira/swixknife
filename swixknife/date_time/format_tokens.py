
from itertools import product
import re


DATE_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\#{base}{zero}{value[0]}'),
        f'#{base}{zero}{value[0]}'.replace('\\', ''), base.replace('\\', ''), zero.replace('\\', ''), *value
    )
    for base, zero, value in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '\\?', '9\\?', '↋\\?', 'Z\\?'),
        ('\\*\\-', '\\-', '\\*\\>', '\\>', '\\*', ''),
        (
            ('dQ', 'day_in_quarter', 3, 2, 2),    # 001 – 231/242 (01_dec – 91_dec/98_dec)
            ('dY', 'day_in_year', 4, 2, 3),       # 0001 – 1404/1415 (001_dec – 364_dec/371_dec)

            ('wM', 'week_in_month', 1, 1, 1),     # 1 – 4/5
            ('wQ', 'week_in_quarter', 2, 1, 2),   # 01 – 21/22 (01_dec – 13_dec/14_dec)
            ('wY', 'week_in_year', 3, 2, 2),      # 001 – 124/125 (01_dec – 52_dec/53_dec)

            ('mQ', 'month_in_quarter', 1, 1, 1),  # 1 – 3

            ('d', 'day', 2, 1, 2),                # 01 – 44/55 (01_dec – 28_dec/35_dec)
            ('w', 'weekday', 2, 1, 1),            # 01 - 11 (01_dec – 7_dec)
            ('m', 'month', 2, 1, 2),              # 01 – 20 (01_dec – 12_dec)
            ('q', 'quarter', 1, 1, 1),            # 1 – 4
            ('y', 'year', 10, 3, 5),              # 000_000 – 555_555 (−10_000_dec – 36_655_dec)
        ),
    )
)


YEAR_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\#{base}{separator}Y'),
        f'#{base}{separator}Y'.replace('\\', ''), base.replace('\\', ''), separator
    )
    for base, separator, in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '\\?', '9\\?', '↋\\?', 'Z\\?'),
        (
            '', '\\_', '\\.', '\\,', '\\˙', '\\ʼ',
            '\\’', "'", '\\•', '\\◦', '\\\u0020', '\\\u00a0',
            '\\\u2000', '\\\u2001', '\\\u2002', '\\\u2003', '\\\u2004', '\\\u2005',
            '\\\u2006', '\\\u2007', '\\\u2008', '\\\u2009', '\\\u200a', '\\\u202f',
            '\\\u205f'
        )
    )
)

DATE_TEXT_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\#{base}{case}{month_week}'),
        f'#{base}{case}{month_week}'.replace('\\', ''), base.replace('\\', ''), case.replace('\\', ''), month_week
    )
    for base, case, month_week in product(
        ('', '@', '1', '2', '3'),
        ('', '\\!', '\\?', '\\>'),
        ('M', 'W'),
    )
)


TIME_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\#{base}{zero}{value[0]}'),
        f'#{base}{zero}{value[0]}'.replace('\\', ''), base.replace('\\', ''), zero.replace('\\', ''), *value
    )
    for base, zero, value in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '99', '↋↋', '\\?', 'Z\\?', '9\\?', '↋\\?', '99\\?', '↋↋\\?'),
        ('\\*\\-', '\\-', '\\*', ''),
        (
            ('d', 'day', 2, 1, 2),
            ('u', 'uta', 2, 1, 2),
            ('p', 'posha', 2, 1, 2),
            ('a', 'agrima', 2, 1, 2),
            ('n', 'anuga', 2, 1, 2),
            ('b', 'boda', 2, 1, 2),
            ('e', 'ekaditiboda', 12, 4, 7),
            ('h', 'uta', 2, 1, 2),
            ('t', 'posha', 2, 1, 2),
            ('s', 'agrima', 2, 1, 2),
        ),
    )
)


TIME_ZONE_OFFSET_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\#{base}{colon}t'),
        f'#{base}{colon}t'.replace('\\', ''), base.replace('\\', ''), colon.replace('\\', '')
    )
    for base, colon in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '99', '↋↋', '\\?', '9\\?', '↋\\?', 'Z\\?', '99\\?', '↋↋\\?'),
        ('', '\\:'),
    )
)


SEASON_MOON_TEXT_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\#{base}{hemisphere}{number}{case}{season_moon}'),
        base, hemisphere, number, case.replace('\\', ''), season_moon
    )
    for base, hemisphere, number, case, season_moon in product(
        ('@', '~', '@~', ''),  # base
        ('S', 'N', ''),  # hemisphere; it’s important that the '' is last
        ('4', ''),  # number
        ('\\!', '\\?', '\\>', ''),  # case
        ('L', 'S'),  # season or moon phase; it’s important that 'S' is last
    )
)

SEASON_MOON_TIME_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\#T{base}{number}{season_moon}'),
        base.replace('\\', ''), number, season_moon
    )
    for base, number, season_moon in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '\\?', '9\\?', '↋\\?', 'Z\\?', '99', '↋↋', '99\\?', '↋↋\\?'),
        ('4', ''),  # number
        ('L', 'S'),  # season or moon phase
    )
)


ISO_DATE_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\%{base}{zero}{value[0]}'),
        f'%{base}{zero}{value[0]}'.replace('\\', ''), base.replace('\\', ''), zero.replace('\\', ''), *value
    )
    for base, zero, value in product(
        ('', '5', '5\\!', '@', '\\!', '@\\!', 'Z', '↋', '\\?', '↋\\?', 'Z\\?'),
        ('\\*\\-', '\\-', '\\*\\>', '\\>', '\\*', ''),
        (
            ('d', 'gregorian_day', 2, 1, 2),
            ('m', 'gregorian_month', 2, 1, 2),
            ('Y', 'gregorian_year', 4, 3, 5),
            ('y', 'gregorian_year', 4, 3, 5),
            ('e', 'gregorian_day', 2, 1, 2),
            ('w', 'weekday', 1, 1, 2),
            ('W', 'weekday', 1, 1, 2),
        ),
    )
)


ISO_TIME_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'\%{base}{zero}{value[0]}'),
        f'%{base}{zero}{value[0]}'.replace('\\', ''), base.replace('\\', ''), zero.replace('\\', ''), *value
    )
    for base, zero, value in product(
        ('', '5', '5\\!', '@', '\\!', '@\\!', 'Z', '↋', '\\?', 'Z\\?', '5\\?', '↋\\?'),
        ('\\*\\-', '\\-', '\\*', ''),
        (
            ('d', 'gregorian_day', 2, 1, 2),
            ('H', 'iso_hour', 2, 1, 2),
            ('M', 'iso_minute', 2, 1, 2),
            ('S', 'iso_second', 2, 1, 2),
            ('f', 'iso_microsecond', 10, 1, 2),
        ),
    )
)

