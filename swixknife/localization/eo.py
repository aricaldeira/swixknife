

__all__ = ('SezimalLocaleEO',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleEO(SezimalLocale):
    LANG = 'eo'
    LANGUAGE = 'Esperanto'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = 'Sm'
    CURRENCY_SUBUNIT_SYMBOL = 'S'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 3

    WEEKDAY_NAME = [
        'lundo',
        'mardo',
        'merkredo',
        'ĵaŭdo',
        'vendredo',
        'sabato',
        'dimanĉo',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'lun',
        'mar',
        'mer',
        'ĵaŭ',
        'ven',
        'sab',
        'dim',
    ]

    MONTH_NAME= [
        'Januaro',
        'Februaro',
        'Marto',
        'Aprilo',
        'Majo',
        'Junio',
        'Julio',
        'Aŭgusto',
        'Septembro',
        'Oktobro',
        'Novembro',
        'Decembro',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'Maj',
        'Jun',
        'Jul',
        'Aŭg',
        'Sep',
        'Okt',
        'Nov',
        'Dec',
    ]

    ERA_NAME = [
        #
        # Sesuma Homara Erao
        #
        'SHE',
        #
        # Antaŭ Sesuma Homara Erao
        #
        'aSHE',
    ]

    DATE_SEPARATOR = '-'
    DATE_FORMAT = '#d-#m-#Y'
    DATE_LONG_FORMAT = 'la #-d-an de #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d-#m-#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, la #-d-an de #M #Y, #u:#p:#a'
    DST_NAME = 'Somera Tempo'
    DST_SHORT_NAME = 'ST'
    WEEK_NUMBER_SYMBOL = 'sem'
    DAY_NUMBER_SYMBOL = 'tago'

    SEASON_NAME = {
        'spring_cross_quarter': 'Transiĝo Vintro – Primtempo',
        'spring_equinox': 'Primtempo',
        'summer_cross_quarter': 'Transiĝo Primtempo – Somero',
        'summer_solstice': 'Somero',
        'autumn_cross_quarter': 'Transiĝo Somero – Aŭtuno',
        'autumn_equinox': 'Aŭtuno',
        'winter_cross_quarter': 'Transiĝo Aŭtuno – Vintro',
        'winter_solstice': 'Vintro',
    }

    MOON_PHASE = {
        'new': 'Nova',
        'waxing_crescent': 'Kreskanta',
        'first_quarter': 'Kreskanta Kvarono',
        'waxing_gibbous': 'Kreskanta Kvarono al Plena',
        'full': 'Plena',
        'waning_gibbous': 'Plena al Malkreskanta Kvarono',
        'third_quarter': 'Malkreskanta Kvarono',
        'waning_crescent': 'Malkreskanta',
    }

    HOLIDAYS = [
        ('130_523-20-15', '💚\ufe0f👼🏼\ufe0f Naskiĝo de Zamenhof (#i)'),  # Ĵaŭdo, 130_523-20-15 ~ 1859-12-15_dec
        ('131_011-11-35', '💚\ufe0f📗\ufe0f Unua Libro (#i)'),     # Mardo, 131_011-11-35 ~ 1887-07-26_dec
        ('212_513-04-24', '💚\ufe0f🪦\ufe0f Memortago de Zamenhof (#i)'),  # Mardo, 212_513-04-24 ~ 1917-04-17_dec
        ('212_453-12-10', '💚\ufe0f🌐\ufe0f Unua Universala Kongreso (#i)'),  # Sabato, 212_453-12-10

        # ('130_523-20-23', '💚\ufe0f Zamenhof-Tago (#i) #𝑠𝑖𝑚'),  # Lundo,    20-23 ~ 12-15_dec
        # ('131_011-11-42', '📗\ufe0f Unua Libro (#i) #𝑠𝑖𝑚'),     # Vendredo, 11-42 ~ 07-26_dec
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        ('ISO+1859-12-15', '💚\ufe0f👼🏼\ufe0f Naskiĝo de Zamenhof (%i)'),
        ('ISO+1887-07-26', '💚\ufe0f📗\ufe0f Unua Libro (%i)'),
        ('ISO+1917-04-17', '💚\ufe0f🪦\ufe0f Memortago de Zamenhof (%i)'),
        ('ISO+1905-08-05', '💚\ufe0f🌐\ufe0f Unua Universala Kongreso (%i)'),
    ]

    #
    # Error messages
    #
    ERROR = 'Eraro'
    WEEKDAY_ERROR = 'Nevalida semajntago {weekday}'
    MONTH_ERROR = 'Nevalida monato {month}'

    COLLATION_RULES = '''
[caseFirst upper]
&A<<Â<<<Ầ<<<Ấ<<<Ậ<<<Ẩ<<<Ẫ<<À<<Á<<Ã<<Ä<<<Ǟ<<Ă<<<Ằ<<<Ắ<<<Ặ<<<Ẳ<<<Ẵ<<Ā<<Ǎ<<Å<<<Ǻ<<Ȧ<<<Ǡ<<Ą<<Ả<<Ạ<<Ȁ<<Ȃ<<Ḁ<<Ⱥ<<Ɐ<<Ɑ<<Ɒ <<< ª<<ᵃ̱<<a<<â<<<ầ<<<ấ<<<ậ<<<ẩ<<<ẫ<<à<<á<<ã<<ä<<<ǟ<<ă<<<ằ<<<ắ<<<ặ<<<ẳ<<<ẵ<<ā<<ǎ<<å<<<ǻ<<ȧ<<<ǡ<<ą<<ả<<ạ<<ȁ<<ȃ<<ḁ<<ⱥ<<ɐ<<ɑ<<ɒ
&AE<<Æ
&ae<<æ
&ÁE<<Ǽ
&áe<<ǽ

&B<<Ḃ<<Ḅ<<Ƀ <<< b<<ḃ<<ḅ<<ƀ

&C<<Ç<<Ć<<Ḉ<<Ĉ<<Č<<Ċ<<Ȼ <<< c<<ç<<ć<<ḉ<<ĉ<<č<<ċ<<ȼ
&c<Ĉ<<<ĉ

&D<<Ď<<Ḋ<<Ḑ<<Ḍ<<Đ <<< d<<ď<<ḋ<<ḑ<<ḍ<<đ
&DH<<Ð
&dh<<ð

&E<<Ê<<<Ề<<<Ế<<<Ệ<<<Ể<<<Ễ<<È<<É<<Ẽ<<Ë<<Ĕ<<Ē<<Ě<<Ė<<Ȩ<<Ę<<Ẻ<<Ẹ<<Ɇ<<Ǝ<<Ə<<Ɛ <<< '\u0026'<<ᵉ̱<<e<<ê<<<ề<<<ế<<<ệ<<<ể<<<ễ<<è<<é<<ẽ<<ë<<ĕ<<ē<<ě<<ė<<ȩ<<ę<<ẻ<<ẹ<<ɇ<<ǝ<<ə<<ɛ

&F<<Ḟ <<< f<<ḟ

&G<<Ǵ<<Ğ<<Ǧ<<Ġ<<Ģ<<Ǥ <<< g<<ǵ<<ğ<<ǧ<<ġ<<ģ<<ǥ
&g<Ĝ<<ĝ

&H<<Ḧ<<Ȟ<<Ḣ<<Ḥ<<Ħ <<< h<<ḧ<<ȟ<<ḣ<<ḥ<<ħ
&h<Ĥ<<ĥ

&I<<Î<<Ì<<Í<<Ĩ<<Ï<<Ĭ<<Ī<<Ǐ<<İ<<<𝚤<<Į<<Ỉ<<Ị<<Ɨ <<< ⁱ̱<<i<<î<<ì<<í<<ĩ<<ï<<ĭ<<ī<<ǐ<<ı<<<𝚤<<į<<ỉ<<ị<<ɨ

&J<<Ɉ<<Ʒ <<< j<<ǰ<<ɉ<<ʒ
&j<Ĵ<<ĵ

&K<<Ḱ<<Ǩ<<Ķ<<Ḳ <<< k<<ḱ<<ǩ<<ķ<<ḳ

&L<<Ĺ<<Ľ<<Ŀ<<Ļ<<Ḷ<<Ł <<< l<<ĺ<<ľ<<ŀ<<ļ<<ḷ<<ł

&M<<M̀<<Ḿ<<Ṁ<<Ṃ <<< m<<m̀<<ḿ<<ṁ<<ṃ

&N<<Ǹ<<Ń<<Ñ<<Ň<<Ņ<<Ṅ<<Ṇ <<< n<<ǹ<<ń<<ñ<<ň<<ņ<<ṅ<<ṇ
&NG<<Ŋ
&ng<<ŋ

&O<<Ô<<<Ồ<<<Ố<<<Ổ<<<Ỗ<<Ò<<Ó<<Õ<<<Ṍ<<<Ṏ<<<Ȭ<<Ö<<<Ȫ<<Ő<<Ŏ<<Ō<<<Ṑ<<<Ṓ<<Ǒ<<Ȯ<<<Ȱ<<Ǫ<<<Ǭ<<Ỏ<<Ơ<<<Ờ<<<Ớ<<<Ợ<<<Ở<<<Ỡ<<Ọ<<Ø<<<Ǿ<<Ɔ <<< º<<ᵒ̱<<o<<ô<<<ồ<<<ố<<<ộ<<<ổ<<<ỗ<<ò<<ó<<õ<<<ṍ<<<ṏ<<<ȭ<<ö<<<ȫ<<ő<<ŏ<<ō<<<ṑ<<<ṓ<<ǒ<<ȯ<<<ȱ<<ǫ<<<ǭ<<ỏ<<ơ<<<ờ<<<ớ<<<ợ<<<ở<<<ỡ<<ọ<<ø<<<ǿ<<ɔ
&OE<<Œ<<Ø
&oe<<œ<<ø

&P<<Ṕ<<Ṗ<<Ᵽ <<< p<<ṕ<<ṗ<<ᵽ

&Q <<< q

&R<<Ŕ<<Ř<<Ṙ<<Ŗ<<Ṛ<<Ɍ <<< r<<ŕ<<ř<<ṙ<<ŗ<<ṛ<<ɍ

&S<<Ś<<Š<<Ṡ<<Ș<<Ş<<Ṣ <<< s<<ś<<š<<ṡ<<ș<<ş<<ṣ
&SS<<ẞ
&ss<<ß
&s<Ŝ<<ŝ

&T<<Ť<<Ṫ<<Ț<<Ţ<<Ṭ<<Ŧ <<< t<<ẗ<<ť<<ṫ<<ț<<ţ<<ṭ<<ŧ
&TH<<Þ
&th<<þ

&U<<Û<<Ù<<Ú<<Ũ<<<Ṹ<<Ü<<<Ǖ<<<Ǘ<<<Ǜ<<<Ǚ<<Ű<<Ū<<<Ṻ<<Ǔ<<Ů<<Ų<<Ủ<<Ư<<<Ừ<<<Ứ<<<Ự<<<Ử<<<Ữ<<Ụ<<Ʉ<<Ʊ <<< ᵘ̱<<u<<û<<ù<<ú<<ũ<<<ṹ<<ü<<<ǖ<<<ǘ<<<ǜ<<<ǚ<<ű<<ū<<<ṻ<<ǔ<<ů<<ų<<ủ<<ư<<<ừ<<<ứ<<<ự<<<ử<<<ữ<<ụ<<ʉ<<ʊ
&u<Ŭ<<ŭ

&V<<Ṽ<<Ṿ <<< v<<ṽ<<ṿ

&W<<Ŵ<<Ẁ<<Ẃ<<W̃<<Ẅ<<Ẇ<<Ẉ<<Ƿ <<< w<<ŵ<<ẁ<<ẃ<<w̃<<ẅ<<ẇ<<ẉ<<ƿ

&X<<Ẍ<<Ẋ <<< x<<ẍ<<ẋ

&Y<<Ŷ<<Ỳ<<Ý<<Ỹ<<Ÿ<<Ȳ<<Ẏ<<Ỷ<<Ỵ<<Ɏ <<< y<<ŷ<<ỳ<<ý<<ỹ<<ÿ<<ȳ<<ẏ<<ỷ<<ỵ<<ɏ

&Z<<Ẑ<<Z̀<<Ź<<Ž<<Ż<<Ẓ<<Ƶ <<< z<<ẑ<<z̀<<ź<<ž<<ż<<ẓ<<ƶ
'''

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None):
        if case:
            return 'a' + case

        return 'a'

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        if f'#$M' in fmt:
            fmt = fmt.replace(f'#$M', self.month_name(date.month)[:-1])

        if f'#$W' in fmt:
            fmt = fmt.replace(f'#$W', self.weekday_name(date.weekday)[:-1])

        return fmt

    DCC_TERM_NAME = [
        'dumonato‐nul',
        'dumonato‐unu',
        'dumonato‐du',
        'dumonato‐tri',
        'dumonato‐kvar',
    ]

    DCC_TERM_ABBREVIATED_NAME = [
        'DM0',
        'DM1',
        'DM2',
        'DM3',
        'DM4',
    ]

    DCC_MONTH_NAME = [
        'Monato‐Nul',
        'Monato‐Unu',
        'Monato‐Du',
        'Monato‐Tri',
        'Monato‐Kvar',
        'Monato‐Kvin',
        'Monato‐Ses',
        'Monato‐Ses‐Unu',
        'Monato‐Ses‐Du',
        'Monato‐Ses‐Tri',
        'Monato‐Ses‐Kvar',
    ]

    DCC_WEEKDAY_NAME = [
        'Semajntago‐Nul',
        'Semajntago‐Unu',
        'Semajntago‐Du',
        'Semajntago‐Tri',
        'Semajntago‐Kvar',
        'Semajntago‐Kvin',
    ]

    DCC_WEEKDAY_ABBREVIATED_NAME = [
        'ST0',
        'ST1',
        'ST2',
        'ST3',
        'ST4',
        'ST5',
    ]

    DCC_NUMBER = [
        'nul',
        'unu',
        'du',
        'tri',
        'kvar',
        'kvin',
        'ses',
        'ses‐unu',
        'ses‐du',
        'ses‐tri',
        'ses‐kvar',
    ]

    DCC_YEAR_COUNT = {
        None: '&>Y jaroj',
        SezimalInteger('1'): '&>Y jaro',
    }

    DCC_TERM_COUNT = {
        None: '&-t dumonatoj',
        SezimalInteger('1'): '&-t dumonato',
    }

    DCC_MONTH_COUNT = {
        None: '&-m monatoj',
        SezimalInteger('1'): '&-m monato',
    }

    DCC_WEEK_COUNT = {
        None: '&-wM semajnoj',
        SezimalInteger('1'): '&-wM semajno',
    }

    DCC_WEEK_IN_YEAR_COUNT = {
        None: '&-wY semajnoj',
        SezimalInteger('1'): '&-wY semajno',
    }

    DCC_DAY_COUNT = {
        None: '&-d tagoj',
        SezimalInteger('1'): '&-d tago',
    }

    DCC_DAY_IN_YEAR_COUNT = {
        None: '&-dY tagoj',
        SezimalInteger('1'): '&-dY tago',
    }

    DCC_DAY_IN_WEEK_COUNT = {
        None: '&-dW tagoj',
        SezimalInteger('1'): '&-dW tago',
    }

    DCC_DATE_MONTH_DAY_SEPARATOR = ' kaj '

    ADC_MONTH_NAME = [
        'Fiŝoj',
        'Baleno',
        'Rivero',
        'Unukornulo',
        'Hidro',
        'Leono',
        'Virgo',
        'Serpento',
        'Aglo',
        'Amforo',
        # 'Pesilo',
        # 'Oriono',
        'Sekstanto',
    ]

    ADC_MONTH_ABBREVIATED_NAME = [
        'Fiŝ',
        'Bal',
        'Riv',
        'Unu',
        'Hid',
        'Leo',
        'Vir',
        'Ser',
        'Agl',
        'Amf',
        # 'Pes',
        # 'Ori',
        'Sek',
    ]

    ADC_MONTH_SYMBOL = [
        'F',
        'B',
        'R',
        'U',
        'H',
        'L',
        'V',
        'Sr',
        'Ag',
        'Am',
        # 'P',
        # 'O',
        'Sk',
    ]

    ADC_WEEKDAY_NAME = [
        'Suno',
        # 'Merkuro',
        'Venuso',
        'Marsu',
        'Jupiteru',
        'Saturno',
        'Luno',
    ]

    ADC_WEEKDAY_ABBREVIATED_NAME = [
        'Sun',
        # 'Mer',
        'Ven',
        'Mar',
        'Jup',
        'Sat',
        'Lun',
    ]

    ADC_WEEKDAY_SYMBOL = [
        'S', # ☉
        # 'M', # ☿
        'V', # ♀
        'M', # ♂
        'J', # ♃
        'S', # ♄
        'L', # ○ ☉
    ]

    DCC_DATE_LONG_FORMAT_ON_DATE = '&󱹭>Y, monato &-m, tago &-d'
    DCC_DATE_LONG_FORMAT_ON_DATE_DAYS = '&󱹭>Y, tago &-dY'
    DCC_DATE_LONG_FORMAT_ON_DATE_WEEKS = '&󱹭>Y, semajno &-wY, tago &-dW'
    DCC_DATE_LONG_FORMAT_ON_DATE_MONTHS_WEEKS = '&󱹭>Y, monato &-m, semajno &-wM, tago &-dW'

    ADC_DATE_LONG_FORMAT_ON_DATE = '&󱹭>Y, monato de &cM, tago &-d'
    ADC_DATE_LONG_FORMAT_ON_DATE_WEEKDAY = '&󱹭>Y, monato de &cM, semajno &wM, tago de &cW'

    HIJRI_CALENDAR_MONTH_NAME = [
        'Muharramo',
        'Safaro',
        'Rabiaŭo Unua',
        'Rabiaŭo Dua',
        'Ĝumado Unua',
        'Ĝumado Dua',
        'Raĝabo',
        'Ŝabano',
        'Ramadano',
        'Ŝavalo',
        'Dulkado',
        'Dulĥiĝo',
    ]

    HIJRI_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'Muh',
        'Saf',
        'Rb1',
        'Rb2',
        'Ĝm2',
        'Ĝm2',
        'Raĝ',
        'Ŝab',
        'Ram',
        'Ŝav',
        'Dlk',
        'Dlĥ',
    ]

    CALENDAR_TYPE = {
        #
        # Civil calendars
        #
        'SEZ': 'Simetria',
        'SYM': 'Simetria',
        'ISO': 'Gregoria',
        'DCC': 'Kiom-da-Tagoj',
        'ADC': 'Astronomia Kiom-da-Tagoj',
        'ISR': 'Israela',
        'IND': 'Indiana',

        #
        # Religious calendars
        #
        'JUL': 'Ortodoxo/Juliano',
        'JEW': 'Juda',
        'HIJ': 'Islama',
        'IRN': 'Islâmico Solar',

        #
        # Páscoa referencial
        #
        'SEZ+EASTER': 'Páscoa Sezimal - 11 de abril',
        'SYM+EASTER': 'Páscoa Simétrica - 7 de abril',
        'ISO+EASTER': 'Páscoa (Gregoriano)',
        'JUL+EASTER': 'Páscoa Ortodoxa (Juliano)',
        'JEW+EASTER': 'Páscoa Judaica (Pêssach)',
    }

    CALENDAR_TYPE_ABBREVIATION = {
        #
        # Civil calendars
        #
        'SEZ': 'Sim.',
        'SYM': 'Sim.',
        'ISO': 'Gre.',
        'DCC': 'KdT',
        'ADC': 'AKdT',
        'ISR': 'Isr.',
        'IND': 'Ind.',
        #
        # Religious calendars
        #
        'JUL': 'Jul.',
        'JEW': 'Jud.',
        'HIJ': 'Isl.',
        'IRN': 'Irn.',
    }
