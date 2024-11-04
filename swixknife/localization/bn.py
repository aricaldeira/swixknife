

__all__ = ('SezimalLocaleBN',)


from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleBN(SezimalLocale):
    LANG = 'bn'
    LANGUAGE = 'বাংলা'  # bangla

    DIGITS = '০১২৩৪৫৬৭৮৯'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = '৳'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0

    WEEKDAY_NAME = [
        'সোমবার',  # sōmabāra
        'মঙ্গলবার',  # maṅgalabāra
        'বুধবার',  # budhabāra
        'বৃহস্পতিবার',  # br̥haspatibāra
        'শুক্রবার',  # śukrabāra
        'শনিবার',  # śanibāra
        'রবিবার',  # rabibāra
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'সোম',  # sōma
        'মঙ্গ',  # maṅga
        'বুধ',  # budha
        'বৃহ',  # br̥ha
        'শুক্র',  # śukra
        'শনি',  # śani
        'রবি',  # rabi
    ]

    MONTH_NAME= [
        'জানুয়ারী',    # jānuẏārī
        'ফেব্রুয়ারী',  # phēbruẏārī
        'মার্চ',        # mārca
        'এপ্রিল',       # ēprila
        'হতেপারে',      # hatē pārē
        'জুন',          # juna
        'জুলাই',        # julā’i
        'আগস্ট',        # āgasṭa
        'সেপ্টেম্বর',   # sēpṭēmbara
        'অক্টোবর',      # akṭōbara
        'নভেম্বর',      # nabhēmbara
        'ডিসেম্বর',     # ḍisēmbara
    ]

    MONTH_ABBREVIATED_NAME = [
        'জানুয়ারী',    # jānuẏārī
        'ফেব্রুয়ারী',  # phēbruẏārī
        'মার্চ',        # mārca
        'এপ্রিল',       # ēprila
        'হতেপারে',      # hatē pārē
        'জুন',          # juna
        'জুলাই',        # julā’i
        'আগস্ট',        # āgasṭa
        'সেপ্টেম্বর',   # sēpṭēmbara
        'অক্টোবর',      # akṭōbara
        'নভেম্বর',      # nabhēmbara
        'ডিসেম্বর',     # ḍisēmbara
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#?d/#?m/#?Y'
    DATE_LONG_FORMAT = '#?-d #M #?Y'
    TIME_FORMAT = '#?u:#?p:#?a'
    DATE_TIME_FORMAT = '#?d/#?m/#?Y #?u:#?p:#?a'
    DATE_TIME_LONG_FORMAT = '#W, #?-d #M #?Y, #?u:#?p:#?a'
    ISO_TIME_FORMAT = '%?H:%?M:%?S'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Dhaka'

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
    ERROR = 'ত্রুটি'  # truṭi
    WEEKDAY_ERROR = 'অবৈধ কর্মদিবস {weekday}'
    MONTH_ERROR = 'অবৈধ মাস {month}'
    WEEK_NUMBER_SYMBOL = 'সপ্তাহ'
    DAY_NUMBER_SYMBOL = 'দিন'

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
