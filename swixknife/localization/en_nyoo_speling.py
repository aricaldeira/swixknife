

__all__ = ('SezimalLocaleEN_NYOO_SPELING',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger

from .en import SezimalLocaleEN

class SezimalLocaleEN_NYOO_SPELING(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Inglish - Nyoo Speling'

    WEEKDAY_NAME = [
        'Múndey',
        'Choozdey',
        'Wenzdey',
        'Thúrzdey',
        'Fraydey',
        'Saturdey',
        'Súndey',
    ]
    WEEKDAY_ABBREVIATED_NAME = [
        'Mún',
        'Cho',
        'Wen',
        'Thú',
        'Fra',
        'Sat',
        'Sún',
    ]

    MONTH_NAME = [
        'Janyooeri',
        'Febyooeri',
        'March',
        'Eyprul',
        'Mey',
        'Joon',
        'Julay',
        'Ogust',
        'Septémbur',
        'Októwbur',
        'Nowvémbur',
        'Disémbur',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Jan',
        'Feb',
        'Mar',
        'Eyp',
        'Mey',
        'Joo',
        'Jul',
        'Ogu',
        'Sep',
        'Okt',
        'Now',
        'Dis',
    ]

    DATE_TIME_LONG_FORMAT = '#W, dhu #-d#O #M #Y, #u:#p:#a'
    DST_NAME = 'Deylayt Seyving Taym'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_HOUR_MINUTE_FORMAT = '%I:%M %P'

    SEASON_NAME = {
        'spring_cross_quarter': 'Spring Kros‐Kwartur',
        'spring_equinox': 'Spring',
        'summer_cross_quarter': 'Sumur Kros‐Kwartur',
        'summer_solstice': 'Sumur',
        'autumn_cross_quarter': 'Otum Kros‐Kwartur',
        'autumn_equinox': 'Otum',
        'winter_cross_quarter': 'Wintur Kros‐Kwartur',
        'winter_solstice': 'Wintur',
    }

    MOON_PHASE = {
        'new': 'Nyoo',
        'waxing_crescent': 'Waksing Kresunt',
        'first_quarter': 'Furst Kwartur',
        'waxing_gibbous': 'Waksing Jibus',
        'full': 'Fool',
        'waning_gibbous': 'Weyning Jibus',
        'third_quarter': 'Thurd Kwartur',
        'waning_crescent': 'Weyning Kresunt',
    }
