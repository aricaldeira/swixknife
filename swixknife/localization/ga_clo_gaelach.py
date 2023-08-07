

__all__ = ('SezimalLocaleGA_CLO_GAELACH',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE
from .ga_traditional import SezimalLocaleGA_TRADITIONAL

#
# Information about lenition, eclipsis etc. from Wikitionary;
#
# Using mí/mhí:
#    https://blogs.transparent.com/irish/nios-mo-faoi-na-mionna-more-about-the-months-in-irish/
#    https://blogs.transparent.com/irish/to-%E2%80%9Cmi%E2%80%9D-or-not-to-%E2%80%9Cmi%E2%80%9D-using-the-word-%E2%80%9Cmonth%E2%80%9D-in-irish/
#
# Ordinal suffix:
#    https://en.wikipedia.org/wiki/Date_and_time_notation_in_Ireland
#
# Date format:
#    https://forum.wordreference.com/threads/irish-gaelic-dates.1477128/
#


def _clo_gaelach(text: str) -> str:
    CLO_ROMHANACH = [
        'A', 'a', 'Á', 'á', 'Á', 'á',
        'D', 'd', 'Ḋ', 'ḋ', 'Ḋ', 'ḋ',
        'F', 'f', 'Ḟ', 'ḟ', 'Ḟ', 'ḟ',
        'G', 'g', 'Ġ', 'ġ', 'Ġ', 'ġ',
        'i',
        'R', 'r',
        'S', 's', 'Ṡ', 'ṡ', 'Ṡ', 'ṡ',
        'T', 't', 'Ṫ', 'ṫ', 'Ṫ', 'ṫ',
    ]
    CLO_GAELACH = [
        'Ɑ', 'ɑ', 'Ɑ́', 'ɑ́', 'Ɑ́', 'ɑ́',
        'Ꝺ', 'ꝺ', 'Ꝺ̇', 'ꝺ̇', 'Ꝺ̇', 'ꝺ̇',
        'Ꝼ', 'ꝼ', 'Ꝼ̇', 'ꝼ̇', 'Ꝼ̇', 'ꝼ̇',
        'Ᵹ', 'ᵹ', 'Ᵹ̇', 'ᵹ̇', 'Ᵹ̇', 'ᵹ̇',
        'ı',
        'Ꞃ', 'ꞃ',
        'Ꞅ', 'ꞅ', 'Ꞅ̇', 'ꞅ̇', 'Ꞅ̇', 'ꞅ̇',
        'Ꞇ', 'ꞇ', 'Ꞇ̇', 'ꞇ̇', 'Ꞇ̇', 'ꞇ̇',
    ]

    for i in range(len(CLO_ROMHANACH)):
        text = text.replace(CLO_ROMHANACH[i], CLO_GAELACH[i])

    return text


class SezimalLocaleGA_CLO_GAELACH(SezimalLocaleGA_TRADITIONAL):
    LANG = 'ga'
    LANGUAGE = 'Ᵹɑeılᵹe'

    WEEKDAY_NAME = [
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_NAME[0]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_NAME[1]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_NAME[2]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_NAME[3]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_NAME[4]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_NAME[5]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_NAME[6]),
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_ABBREVIATED_NAME[0]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_ABBREVIATED_NAME[1]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_ABBREVIATED_NAME[2]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_ABBREVIATED_NAME[3]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_ABBREVIATED_NAME[4]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_ABBREVIATED_NAME[5]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.WEEKDAY_ABBREVIATED_NAME[6]),
    ]

    MONTH_NAME = [
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[0]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[1]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[2]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[3]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[4]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[5]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[6]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[7]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[8]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[9]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[10]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_NAME[11]),
    ]

    MONTH_ABBREVIATED_NAME = [
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[0]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[1]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[2]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[3]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[4]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[5]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[6]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[7]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[8]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[9]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[10]),
        _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MONTH_ABBREVIATED_NAME[11]),
    ]

    DATE_TIME_LONG_FORMAT = '#W, ɑn #-d#O lɑ́ ꝺe #$MHÍM #Y, #u:#p:#a'

    SEASON_NAME = {
        'spring_cross_quarter': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.SEASON_NAME['spring_cross_quarter']),
        'spring_equinox': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.SEASON_NAME['spring_equinox']),
        'summer_cross_quarter': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.SEASON_NAME['summer_cross_quarter']),
        'summer_solstice': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.SEASON_NAME['summer_solstice']),
        'autumn_cross_quarter': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.SEASON_NAME['autumn_cross_quarter']),
        'autumn_equinox': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.SEASON_NAME['autumn_equinox']),
        'winter_cross_quarter': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.SEASON_NAME['winter_cross_quarter']),
        'winter_solstice': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.SEASON_NAME['winter_solstice']),
    }

    MOON_PHASE = {
        'new': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MOON_PHASE['new']),
        'waxing_crescent': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MOON_PHASE['waxing_crescent']),
        'first_quarter': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MOON_PHASE['first_quarter']),
        'waxing_gibbous': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MOON_PHASE['waxing_gibbous']),
        'full': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MOON_PHASE['full']),
        'waning_gibbous': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MOON_PHASE['waning_gibbous']),
        'third_quarter': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MOON_PHASE['third_quarter']),
        'waning_crescent': _clo_gaelach(SezimalLocaleGA_TRADITIONAL.MOON_PHASE['waning_crescent']),
    }

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'ꝺ'
        elif day == 2:
            return 'ɑ'

        return 'ú'

    def weekday_name(self, weekday: SezimalInteger, mutation: str = ', ', case: str = ', ') -> str:
        return _clo_gaelach(super().weekday_name(weekday, mutation, case))

    def weekday_abbreviated_name(self, weekday: SezimalInteger, mutation: str = ', ', case: str = ', ') -> str:
        return _clo_gaelach(super().weekday_abbreviated_name(weekday, mutation, case))

    def month_name(self, month: SezimalInteger, mutation: str = ', ', case: str = ', ') -> str:
        return _clo_gaelach(super().month_name(month, mutation, case))

    def month_abbreviated_name(self, month: SezimalInteger, mutation: str = ', ', case: str = ', ') -> str:
        return _clo_gaelach(super().month_abbreviated_name(month, mutation, case))
