

__all__ = ('SezimalLocaleAR_LATN',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

#
# Romanization according to Egyptian pronunciation:
#
# ‹m› /m/ | ‹n› /n/
# ‹p› /p/ | ‹t› /t/   |         | ‹k›  /k/ |          | ‹q› /ʔ/
# ‹b› /b/ | ‹d› /d/   |         | ‹g›  /g/
# ‹f› /f/ | ‹s› /s/   | ‹x› /ʃ/ | ‹kh› /x/ | ‹ħ›  /ħ/ | ‹h› /h/
# ‹v› /v/ | ‹z› /z/   | ‹j› /ʒ/ | ‹gh› /ɣ/ | ‹għ› /ʕ/
#         | ‹r› /ɾ~r/
#         | ‹l›       | ‹y› /j/ | ‹w›  /w/
#
# Emphatic:                 Classic:
#    ‹m’› /mˤ/ ‹b’› /bˤ/    ‹q’› /q/
#    ‹t’› /tˤ/ ‹d’› /dˤ/    ‹th’› /θ/ ‹dh’› /ð/
#    ‹s’› /sˤ/ ‹z’› /zˤ/
#    ‹r’› /rˤ/ ‹l’› /lˤ/
#
# Gemminated and consonant clusters:
#    kh + kh = kkh  | k + kh = k’kh | kh + h = kh’h | k + h = k’h
#    gh + gh = ggh  | g + gh = g’gh | gh + h = gh’h | g + h = g’h
#    għ + għ = ggħ  | g + għ = g’għ | għ + ħ = għ’ħ | g + ħ = g’ħ
#
# Vowels:
# https://en.wikivoyage.org/wiki/Egyptian_Arabic_phrasebook
#
#  a /æ/  á /æː/ | à /ɑ/  â /ɑː/
#  i /i/  í /iː/ | e /e/  é /eː/
#  u /u/  ú /uː/ | o /o/  ó /oː/
#


class SezimalLocaleAR_LATN(SezimalLocale):
    LANG = 'ar'
    LANGUAGE = 'el-għàràbí'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '£'
    CURRENCY_SUBUNIT_SYMBOL = 'PT'

    FIRST_WEEKDAY = 'SUN'
    DAY_OF_REST = 'SAT'
    OPTIONAL_DAY_OF_REST = 'FRI'

    WEEKDAY_NAME = [
        'el etnín',
        'et talát',
        'el àrbàgħ',
        'el khamís',
        'el gomgħà',
        'es sabt',
        'el ħad',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'etn',
        'tal',
        'àrb',
        'kha',
        'gom',
        'sab',
        'ħad',
    ]

    WEEKDAY_SYMBOL = [
        'e',
        't',
        'à',
        'k',
        'g',
        's',
        'ħ',
    ]

    MONTH_NAME= [
        'yanáyer',
        'febrâyer',
        'máres',
        'ebríl',
        'máyu',
        'yonyo',
        'yolyu',
        'àghóstos',
        'sebtámber',
        'októbàr',
        'novamber',
        'desamber',
    ]


    MONTH_ABBREVIATED_NAME = [
        'yan',
        'feb',
        'már',
        'ebr',
        'máy',
        'yon',
        'yol',
        'agħ',
        'seb',
        'okt',
        'nov',
        'des',
    ]

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#d/#m/#Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d/#m/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#d/#m/#Y #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Africa/Cairo'

    SEASON_NAME = {
        'spring_cross_quarter': 'Spring Cross-Quarter',
        'spring_equinox': 'Fàslu er ràbígħi',
        'summer_cross_quarter': 'Summer Cross-Quarter',
        'summer_solstice': 'Fàslu es sàyfi',
        'autumn_cross_quarter': 'Autumn Cross-Quarter',
        'autumn_equinox': 'Fàslu el kharífi',
        'winter_cross_quarter': 'Winter Cross-Quarter',
        'winter_solstice': 'Fàslu ex xetáqi',
    }

    MOON_PHASE = {
        'new': 'New',
        'waxing_crescent': 'Waxing Crescent',
        'first_quarter': 'First Quarter',
        'waxing_gibbous': 'Waxing Gibbous',
        'full': 'Full',
        'waning_gibbous': 'Waning Gibbous',
        'third_quarter': 'Third Quarter',
        'waning_crescent': 'Waning Crescent',
    }

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDAR = []

    #
    # Error messages
    #
    ERROR = 'Khat’áq'
    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'
    WEEK_NUMBER_SYMBOL = 'asb'
    DAY_NUMBER_SYMBOL = 'yom'
