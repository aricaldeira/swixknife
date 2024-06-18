

__all__ = ('SezimalLocaleHI',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleHI(SezimalLocale):
    LANG = 'hi'
    LANGUAGE = 'हिन्दी'  # hindi

    DIGITS = '०१२३४५६७८९'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'सोमवार',  # somvār
        'मंगलवार',  # maṅgalvār
        'बुधवार',  # budhvār
        'गुरुवार',  # guruvār
        'शुक्रवार',  # śukravār
        'शनिवार',  # śanivār
        'रविवार',  # ravivār
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'सोम',  # som
        'मंग',  # maṅ
        'बुध',  # budh
        'गुरु',  # gur
        'शुक्र',  # śuk
        'शनि',  # śani
        'रवि',  # ravi
    ]

    MONTH_NAME= [
        'जनवरी',  # janvarī
        'फ़रवरी',  # farvarī
        'मार्च',  # mārc
        'अप्रैल',  # aprel
        'मई',  # maī
        'जून',  # jūn
        'जुलाई',  # julāī
        'अगस्त',  # agast
        'सितंबर',  # sitambar
        'अक्तूबर',  # akṭūbar
        'नवंबर',  # navambar
        'दिसंबर',  # disambar
    ]

    MONTH_ABBREVIATED_NAME = [
        'जन॰',  # jan
        'फ़र॰',  # far
        'मार्च',  # mārc
        'अप्रैल',   # aprail,
        'मई',  # maī
        'जून',  # jūn
        'जुल॰',  # jul
        'अग॰',  # agast
        'सित॰',  # sit
        'अक्तू॰',  # akṭū
        'नव॰',  # nav
        'दिस॰',  # dis
    ]

    DATE_FORMAT = '#?d/#?m/#?Y'
    DATE_LONG_FORMAT = '#?d/#?m/#?Y #@W'
    TIME_FORMAT = '#?u:#?p:#?a'
    DATE_TIME_FORMAT = '#?d/#?m/#?Y #?u:#?p:#?a'
    DATE_TIME_LONG_FORMAT = '#?d/#?m/#?Y #@W #?u:#?p:#?a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Kolkata'

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
    ERROR = 'त्रुटि'
    WEEKDAY_ERROR = 'अमान्य कार्यदिवस {weekday}'
    MONTH_ERROR = 'अमान्य महीना {month}'

