

__all__ = ('SezimalLocaleHI',)


from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

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

    CURRENCY_UNIT_SYMBOL = '₹'
    CURRENCY_SUBUNIT_SYMBOL = 'प'

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
    WEEK_NUMBER_SYMBOL = 'सप्त'

    def format_decimal_number(self,
        number: str | int | float | Decimal | Sezimal | SezimalInteger | SezimalFraction,
        decimal_places: str | int | Decimal | SezimalInteger = 2,
        use_group_separator: bool = True,
        use_fraction_group_separator: bool = False,
        typographical_negative: bool = True,
        minimum_size: str | int | Decimal | Sezimal | SezimalInteger = 0,
        prefix: str = '',
        suffix: str = '',
        positive_format: str = '{prefix}{value}{suffix}',
        negative_format: str = '-{prefix}{value}{suffix}',
        recurring_digits_notation: bool | str | int | Decimal | Sezimal | SezimalInteger = False,
        keep_original_aspect: bool = False,
        #
        # Lakhs and crores are Indian names for powers of ten
        # https://en.wikipedia.org/wiki/Indian_numbering_system
        #
        lakh_crore_grouping: bool = True,
        #
        # 萬/万: Chinese wàn/ㄨㄢˋ, Japanese まん man, Korean 만 man, Vietnamese vạn
        # https://en.wikipedia.org/wiki/Japanese_numerals#Powers_of_10
        #
        wan_man_van_grouping: bool = False,
        native_digits: bool = True,
    ) -> str:
        return super().format_decimal_number(
            number,
            decimal_places,
            use_group_separator,
            use_fraction_group_separator,
            typographical_negative,
            minimum_size,
            prefix,
            suffix,
            positive_format,
            negative_format,
            recurring_digits_notation,
            keep_original_aspect,
            lakh_crore_grouping,
            wan_man_van_grouping,
            native_digits,
        )
