

__all__ = ('SezimalLocaleFA_LATN',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

#
# Romanization and date/time notation
# following the Nowdabire system:
# http://nowdabire.blogfa.com/
#
# The thing most inovative about it is the
# way it deals with the glotal stop (mul/ist),
# use ë/diacritics instead of ’ (apostrophe)
#
class SezimalLocaleFA_LATN(SezimalLocale):
    LANG = 'fa'
    LANGUAGE = 'fârsi'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FIRST_WEEKDAY = 'SAT'
    DAY_OF_REST = 'FRI'
    OPTIONAL_DAY_OF_REST = ''

    WEEKDAY_NAME = [
        'doŝanbe',     # došanbe
        'seŝanbe',     # sešanbe
        'câhârŝanbe',  # čahâršanbe
        'panjŝanbe',   # panjšanbe
        'jomé',        # âdine/jom’e  / ëâdine
        'ŝanbe',       # šanbe
        'yekŝanbe',    # yekšanbe
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        '2ŝn',  # 2šn
        '3ŝn',  # 3šn
        '4ŝn',  # 4šn
        '5ŝn',  # 5šn
        'jmë',  # jm’ / âdn  / ëdn
        'ŝnb',  # šnb
        '1ŝn',  # 1šn
    ]

    MONTH_NAME= [
        'ĵânviye',   # žânviye
        'fevriye',
        'mârs',
        'âvril',
        'me',
        'ĵuan',      # žu’an
        'ĵuiye',     # žu’iye
        'ut',
        'septâmbr',
        'oktobr',
        'novâmbr',
        'desâmbr',
    ]

    MONTH_ABBREVIATED_NAME = [
        'ĵân',  # žan
        'fev',
        'mâr',
        'âvr',
        'me',
        'ĵëa',  # ž’a
        'ĵëy',  # ž’y
        'ut',
        'sep',
        'okt',
        'nov',
        'des',
    ]

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O e #M e #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d/#m/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #d#O e #M e #Y, #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Tehran'

    SEASON_NAME = {
        'spring_cross_quarter': 'Spring Cross-Quarter',
        'spring_equinox': 'Spring',
        'summer_cross_quarter': 'Summer Cross-Quarter',
        'summer_solstice': 'Summer',
        'autumn_cross_quarter': 'Autumn Cross-Quarter',
        'autumn_equinox': 'Autumn',
        'winter_cross_quarter': 'Winter Cross-Quarter',
        'winter_solstice': 'Winter',
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
    ERROR = 'Khatá'
    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        return 'ᵒᵐ'
