

__all__ = ('SezimalLocaleJA_LATN',)



from .ja import SezimalLocaleJA



class SezimalLocaleJA(SezimalLocaleJA):
    LANG = 'ja'
    LANGUAGE = 'nihôn̄ḡo'  # nihongo

    IDEOGRAPHIC = False

    WEEKDAY_NAME = [
        'getsuyōbi',
        'kayōbi',
        'suiyōbi',
        'mokuyōbi',
        'kin’yōbi',
        'doyōbi',
        'nichiyōbi',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'getsu',
        'ka',
        'sui',
        'moku',
        'kin',
        'do',
        'nichi',
    ]

    WEEKDAY_SYMBOL = [
        'g',
        'k',
        's',
        'm',
        'k',
        'd',
        'n',
    ]

    MONTH_NAME= [
        'ichigatsu',
        'nigatsu',
        'sangatsu',
        'shigatsu',
        'gogatsu',
        'rokugatsu',
        'muichigatsu',
        'munigatsu',
        'musangatsu',
        'mushigatsu',
        'mugogatsu',
        'nimugatsu',
    ]

    ISO_MONTH_NAME = [
        'ichigatsu',
        'nigatsu',
        'sangatsu',
        'shigatsu',
        'gogatsu',
        'rokugatsu',
        'nanagatsu',
        'hachigatsu',
        'kugatsu',
        'jūgatsu',
        'jūichigatsu',
        'jūnigatsu',
    ]

    MONTH_ABBREVIATED_NAME = [
        '1G',
        '2G',
        '3G',
        '4G',
        '5G',
        '10G',
        '11G',
        '12G',
        '13G',
        '14G',
        '15G',
        '20G',
    ]

    ISO_MONTH_ABBREVIATED_NAME = [
        '1G',
        '2G',
        '3G',
        '4G',
        '5G',
        '6G',
        '7G',
        '8G',
        '9G',
        '10G',
        '11G',
        '12G',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#Y/#m/#d'
    DATE_LONG_FORMAT = '#Y年#m月#d日'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#Y/#m/#d #@W #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#Y年#-m月#-d日#W #u:#p:#a'
    DEFAULT_TIME_ZONE = 'Asia/Tokyo'
    DST_NAME = '夏時間'  # natsu jikan
    DST_SHORT_NAME = 'DST'

    SEASON_NAME = {
        'spring_cross_quarter': 'fuyu kara haru e no nakaba',
        'spring_equinox': 'haru',
        'summer_cross_quarter': 'haru kara natsu e no nakaba',
        'summer_solstice': 'natsu',
        'autumn_cross_quarter': 'natsu kara aki e no nakaba',
        'autumn_equinox': 'aki',
        'winter_cross_quarter': '秋から冬への半ば',  # aki kara fuyu e no nakaba
        'winter_solstice': '冬',                   # fuyu
    }

    MOON_PHASE = {
        'new': '新月',                        # shingetsu
        'waxing_crescent': '上弦の三日月',     # jōgen no mikadzuki
        'first_quarter': '上弦の月',           # jōgen no tsuki
        'waxing_gibbous': '上弦の巨大な月',     # jōgen no kyodaina tsuki
        'full': '満月',                        # man getsu
        'waning_gibbous': '欠けていく巨大な月',  # kakete iku kyodaina tsuki
        'third_quarter': '上弦の月',            # jōgen no tsuki
        'waning_crescent': '欠けていく三日月',   # kakete iku mikadzuki
    }

    #
    # Error messages
    #
    ERROR = 'エラー'
    WEEKDAY_ERROR = '{weekday}は曜日が無効です'
    MONTH_ERROR = '{month}は月が無効です'
    WEEK_NUMBER_SYMBOL = '週'
    DAY_NUMBER_SYMBOL = '日'

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
        lakh_crore_grouping: bool = False,
        #
        # 萬/万: Chinese wàn/ㄨㄢˋ, Japanese まん man, Korean 만 man, Vietnamese vạn
        # https://en.wikipedia.org/wiki/Japanese_numerals#Powers_of_10
        #
        wan_man_van_grouping: bool = True,
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
