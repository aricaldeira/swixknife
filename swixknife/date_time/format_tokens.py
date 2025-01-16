
from itertools import product
import re


DATE_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'#{base}{zero}{value[0]}'),
        f'#{base}{zero}{value[0]}'.replace('\\', ''), base.replace('\\', ''), zero.replace('\\', ''), *value
    )
    for base, zero, value in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '\\?', '9\\?', '↋\\?', 'Z\\?'),
        ('\\*\\-', '\\-', '\\*\\>', '\\>', '\\*', ''),
        (
            ('tdM', 'total_days_in_month', 2, 2, 2),      # 44/55 (28_dec/35_dec)
            ('tdQ', 'total_days_in_quarter', 3, 2, 2),    # 231/242 (91_dec/98_dec)
            ('tdY', 'total_days_in_year', 4, 2, 3),       # 1404/1415 (364_dec/371_dec)

            ('twM', 'total_weeks_in_month', 1, 1, 1),     # 4/5
            ('twQ', 'total_weeks_in_quarter', 2, 1, 2),   # 21/22 (13_dec/14_dec)
            ('twY', 'total_weeks_in_year', 3, 2, 2),      # 124/125 (52_dec/53_dec)

            ('tmQ', 'total_months_in_quarter', 1, 1, 1),  # 3
            ('tmY', 'total_months_in_year', 2, 2, 2),     # 20

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
            ('gy', 'gregorian_year', 5, 2, 4),
            ('ghy', 'gregorian_holocene_year', 10, 3, 5),
            ('sy', 'symmetric_year', 5, 2, 4),
            ('shy', 'symmetric_holocene_year', 10, 3, 5),
        ),
    )
)


YEAR_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'#{base}{separator}{value[0]}'),
        f'#{base}{separator}{value[0]}'.replace('\\', ''), base.replace('\\', ''), separator, *value
    )
    for base, separator, value, in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '\\?', '9\\?', '↋\\?', 'Z\\?'),
        (
            '', '_', '\\.', ',', '˙', 'ʼ',
            '’', "'", '•', '◦', '\u0020', '\u00a0',
            '\u2000', '\u2001', '\u2002', '\u2003', '\u2004', '\u2005',
            '\u2006', '\u2007', '\u2008', '\u2009', '\u200a', '\u202f',
            '\u205f', '\U000f1e6c', '\U000f1e6d', '\U000f1e6e', '\U000f1e6f',
        ),
        (
            ('Y', 'year'),
            ('X', 'year'),
            ('gY', 'gregorian_year'),
            ('ghY', 'gregorian_holocene_year'),
            ('sY', 'symmetric_year'),
            ('shY', 'symmetric_holocene_year'),
            ('>Y', 'year'),
            ('>X', 'year'),
        )
    )
)


DATE_TEXT_FORMAT_TOKEN = re.compile(
    r'#(?P<base>Z|9|↋)?(?P<size>@|1|2|3)?(?P<case>\!|\?|\>)?(?P<month_week>M|W)(?P<calendar>&)?'
)


TIME_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'#{base}{zero}{value[0]}'),
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
            ('x', 'shaditiboda', 12, 4, 7),
        ),
    )
)


TIME_ZONE_OFFSET_FORMAT_TOKENS = tuple(
    (
        re.compile(f'#{base}{colon}t'),
        f'#{base}{colon}t'.replace('\\', ''), base.replace('\\', ''), colon.replace('\\', '')
    )
    for base, colon in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '99', '↋↋', '\\?', '9\\?', '↋\\?', 'Z\\?', '99\\?', '↋↋\\?'),
        ('', '\\:'),
    )
)


DAY_FRACTION_FORMAT_TOKEN = re.compile(
    r'#(?P<base>@|!|@!|Z|9|↋|\?|Z\?|9\?|↋\?)?(?P<integer>[0-9A-Z↊↋]{1,2})\.(?P<fraction>[0-9A-Z↊↋]{1,2})fD'
)


SEASON_MOON_TEXT_FORMAT_TOKENS = tuple(
    (
        re.compile(f'#{base}{hemisphere}{number}{case}{season_moon}'),
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
        re.compile(f'#T{base}{number}{season_moon}'),
        base.replace('\\', ''), number, season_moon
    )
    for base, number, season_moon in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '\\?', '9\\?', '↋\\?', 'Z\\?', '99', '↋↋', '99\\?', '↋↋\\?', '%'),
        ('4', ''),  # number
        ('L', 'S'),  # season or moon phase
    )
)


ISO_DATE_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'%{base}{zero}{value[0]}'),
        f'%{base}{zero}{value[0]}'.replace('\\', ''), base.replace('\\', ''), zero.replace('\\', ''), *value
    )
    for base, zero, value in product(
        ('', '5', '5\\!', '@', '\\!', '@\\!', 'Z', '↋', '\\?', '↋\\?', 'Z\\?', '9'),
        ('\\*\\-', '\\-', '\\*\\>', '\\>', '\\*', ''),
        (
            ('W', 'iso_week', 2, 2, 3),
            ('yW', 'iso_year', 4, 3, 5),
            ('dW', 'iso_weekday', 1, 1, 2),

            ('d', 'gregorian_day', 2, 1, 2),
            ('m', 'gregorian_month', 2, 1, 2),
            ('Y', 'gregorian_year', 4, 3, 5),
            ('y', 'gregorian_year', 4, 3, 5),
            ('e', 'gregorian_day', 2, 1, 2),
            ('j', 'gregorian_day_in_year', 3, 2, 4),
            ('w', 'weekday', 1, 1, 2),
        ),
    )
)


ISO_TIME_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'%{base}{zero}{value[0]}'),
        f'%{base}{zero}{value[0]}'.replace('\\', ''), base.replace('\\', ''), zero.replace('\\', ''), *value
    )
    for base, zero, value in product(
        ('', '5', '5\\!', '@', '\\!', '@\\!', 'Z', '↋', '\\?', 'Z\\?', '5\\?', '↋\\?'),
        ('\\*\\-', '\\-', '\\*', ''),
        (
            ('d', 'gregorian_day', 2, 1, 2),
            ('H', 'iso_hour', 2, 1, 2),
            ('M', 'iso_minute', 2, 1, 3),
            ('S', 'iso_second', 2, 1, 3),
            ('f', 'iso_microsecond', 10, 1, 2),
        ),
    )
)


DCC_DATE_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'&{base}{zero}{value[0]}'),
        f'&{base}{zero}{value[0]}'.replace('\\', ''), base.replace('\\', ''), zero.replace('\\', ''), *value
    )
    for base, zero, value in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '\\?', '9\\?', '↋\\?', 'Z\\?', 'c', 'c\\!', 'c9', 'c↋'),
        ('\\*\\-', '\\-', '\\*\\>', '\\>', '\\*', ''),
        (
            ('dY', 'dcc_day_in_year', 4, 2, 3),
            ('dT', 'dcc_day_in_term', 1, 1, 1),
            ('dM', 'dcc_day', 2, 1, 2),
            ('dW', 'dcc_weekday', 1, 1, 1),

            ('wY', 'dcc_week_in_year', 3, 2, 2),
            ('wT', 'dcc_week_in_term', 1, 1, 1),
            ('wM', 'dcc_week', 1, 1, 1),

            ('mY', 'dcc_month', 3, 2, 2),
            ('mT', 'dcc_month_in_term', 1, 1, 1),

            ('tdY', 'dcc_total_days_in_year', 4, 2, 3),
            ('tdT', 'dcc_total_days_in_term', 3, 2, 2),
            ('tdM', 'dcc_total_days_in_month', 2, 1, 2),
            ('tdW', 'dcc_total_days_in_week', 1, 1, 1),

            ('twY', 'dcc_total_weeks_in_year', 3, 2, 2),
            ('twT', 'dcc_total_weeks_in_term', 2, 1, 2),
            ('twM', 'dcc_total_weeks_in_month', 1, 1, 1),

            ('tmY', 'dcc_total_months_in_year', 2, 1, 2),
            ('tmT', 'dcc_total_months_in_term', 1, 1, 1),

            ('ttY', 'dcc_total_terms_in_year', 1, 1, 1),

            ('tY', 'dcc_term', 3, 2, 2),

            ('w', 'dcc_weekday', 1, 1, 1),
            ('d', 'dcc_day', 2, 1, 2),
            ('m', 'dcc_month', 2, 1, 2),

            ('t', 'dcc_term', 1, 1, 1),

            ('y', 'dcc_year', 10, 3, 4),
        ),
    )
)


DCC_YEAR_NUMBER_FORMAT_TOKENS = tuple(
    (
        re.compile(f'&{base}{separator}{value[0]}'),
        f'&{base}{separator}{value[0]}'.replace('\\', ''), base.replace('\\', ''), separator, *value
    )
    for base, separator, value, in product(
        ('', '@', '\\!', '@\\!', 'Z', '9', '↋', '\\?', '9\\?', '↋\\?', 'Z\\?', 'c', 'c\\!', 'c9', 'c↋',),
        (
            '', '_', '\\.', ',', '˙', 'ʼ',
            '’', "'", '•', '◦', '\u0020', '\u00a0',
            '\u2000', '\u2001', '\u2002', '\u2003', '\u2004', '\u2005',
            '\u2006', '\u2007', '\u2008', '\u2009', '\u200a', '\u202f',
            '\u205f', '\U000f1e6c', '\U000f1e6d', '\U000f1e6e', '\U000f1e6f',
        ),
        (
            ('Y', 'dcc_year'),
            ('X', 'dcc_year'),
            ('>Y', 'dcc_year'),
            ('>X', 'dcc_year'),
        )
    )
)


DCC_DATE_TEXT_FORMAT_TOKEN = re.compile(
    r'&(?P<base>Z|9|↋|c|c9|c↋)?(?P<size>@|1|2|3)?(?P<case>\!|\?|\>)?(?P<month_week_term>M|W|T)'
)
