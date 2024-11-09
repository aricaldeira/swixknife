

__all__ = ('SezimalLocaleEN_IE',)


from typing import TypeVar

Sezimal = TypeVar('Sezimal', bound='Sezimal')
SezimalInteger = TypeVar('SezimalInteger', bound='SezimalInteger')
SezimalFraction = TypeVar('SezimalFraction', bound='SezimalFraction')
Decimal = TypeVar('Decimal', bound='Decimal')

from .en import SezimalLocaleEN


class SezimalLocaleEN_IN(SezimalLocaleEN):
    LANG = 'en'
    LANGUAGE = 'Indian English'

    DEFAULT_TIME_ZONE = 'Asia/Kolkata'
    ISO_TIME_FORMAT = '%I:%M:%S %P'
    ISO_SHORT_TIME_FORMAT = '%I:%M %P'

    CURRENCY_UNIT_SYMBOL = '₹'
    CURRENCY_SUBUNIT_SYMBOL = 'प'

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

    HOLIDAYS = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('213010-01-41', '🇮\ufe0f🇳\ufe0f Republic Day (#i) #Sym454'),
        ('213003-12-31', '🇮\ufe0f🇳\ufe0f Independence Day (#i) #Sym454'),
        ('212353-13-43', '🇮\ufe0f🇳\ufe0f👳🏽‍♂️ Gandhi Jayanti (#i) #Sym454'),
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # National Holidays
        # that occur on a specific date
        #
        ('ISO-1950-01-26', '🇮\ufe0f🇳\ufe0f Republic Day (%i)'),
        ('ISO-1947-08-15', '🇮\ufe0f🇳\ufe0f Independence Day (%i)'),
        ('ISO-1869-10-02', '🇮\ufe0f🇳\ufe0f👳🏽‍♂️ Gandhi Jayanti (%i)'),
    ]
