

__all__ = ('SezimalLocaleLAT',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleLAT(SezimalLocale):
    LANG = 'lat'
    LANGUAGE = 'lingua latīna'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

    CASE_NOMINATIVE = 'N'
    CASE_GENITIVE = 'G'
    CASE_DATIVE = 'D'
    CASE_ACCUSATIVE = 'A'
    CASE_ABLATIVE = 'B'
    CASE_VOCATIVE = 'V'

    CASES = [
        CASE_NOMINATIVE,
        CASE_GENITIVE,
        CASE_DATIVE,
        CASE_ACCUSATIVE,
        CASE_ABLATIVE,
        CASE_VOCATIVE,
    ]

    WEEKDAY_NAME = [
        'diēs Lūnae ',
        'diēs Mārtis',
        'diēs Mercuriī ',
        'diēs Iovis',
        'diēs Veneris',
        'diēs Sāturnī',
        'diēs Sōlis',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Lūn',
        'Mār',
        'Mer',
        'Iov',
        'Ven',
        'Sat',
        'Sōl',
    ]

    WEEKDAY_SYMBOL = [
        'L',
        'M',
        'M',
        'I',
        'V',
        'S',
        'S',
    ]

    WEEKDAY_NAME_GENITIVE = [
        'diēī Lūnae',
        'diēī Mārtis',
        'diēs Mercuriī',
        'diēs Iovis',
        'diēs Veneris',
        'diēs Sāturnī',
        'diēs Sōlis',
    ]

    WEEKDAY_NAME_DATIVE = [
        'diēī Lūnae',
        'diēī Mārtis',
        'diēī Mercuriī',
        'diēī Iovis',
        'diēī Veneris',
        'diēī Sāturnī',
        'diēī Sōlis',
    ]

    WEEKDAY_NAME_ACCUSATIVE = [
        'diēm Lūnae',
        'diem Mārtis',
        'diem Mercuriī',
        'diem Iovis',
        'diem Veneris',
        'diem Sāturnī',
        'diem Sōlis',
    ]

    WEEKDAY_NAME_ABLATIVE = [
        'diē Lūnae',
        'diē Mārtis',
        'diē Mercuriī',
        'diē Iovis',
        'diē Veneris',
        'diē Sāturnī',
        'diē Sōlis',
    ]

    WEEKDAY_NAME_VOCATIVE = [
        'diēs Lūnae',
        'diēs Mārtis',
        'diēs Mercuriī',
        'diēs Iovis',
        'diēs Veneris',
        'diēs Sāturnī',
        'diēs Sōlis',
    ]

    # WEEKDAY_NAME = [
    #     'diēs Lūnae ',
    #     'diēs Mārtis',
    #     'diēs Mercuriī ',
    #     'diēs Iovis',
    #     'diēs Veneris',
    #     'diēs Sabbatī',
    #     'diēs Dominicus',
    # ]
    #
    # WEEKDAY_ABBREVIATED_NAME = [
    #     'Lūn',
    #     'Mār',
    #     'Mer',
    #     'Iov',
    #     'Ven',
    #     'Sab',
    #     'Dom',
    # ]
    #
    # WEEKDAY_SYMBOL = [
    #     'L',
    #     'M',
    #     'M',
    #     'I',
    #     'V',
    #     'S',
    #     'D',
    # ]
    #
    # WEEKDAY_NAME_GENITIVE = [
    #     'diēī Lūnae',
    #     'diēī Mārtis',
    #     'diēī Mercuriī',
    #     'diēī Iovis',
    #     'diēī Veneris',
    #     'diēī Sabbatī',
    #     'diēī Dominicī',
    # ]
    #
    # WEEKDAY_NAME_DATIVE = [
    #     'diēī Lūnae',
    #     'diēī Mārtis',
    #     'diēī Mercuriī',
    #     'diēī Iovis',
    #     'diēī Veneris',
    #     'diēī Sabbatī',
    #     'diēī Dominicō',
    # ]
    #
    # WEEKDAY_NAME_ACCUSATIVE = [
    #     'diēm Lūnae',
    #     'diem Mārtis',
    #     'diem Mercuriī',
    #     'diem Iovis',
    #     'diem Veneris',
    #     'diem Sabbatī',
    #     'diem Dominicum',
    # ]
    #
    # WEEKDAY_NAME_ABLATIVE = [
    #     'diē Lūnae',
    #     'diē Mārtis',
    #     'diē Mercuriī',
    #     'diē Iovis',
    #     'diē Veneris',
    #     'diē Sabbatī',
    #     'diē Dominicō',
    # ]
    #
    # WEEKDAY_NAME_VOCATIVE = [
    #     'diēs Lūnae',
    #     'diēs Mārtis',
    #     'diēs Mercuriī',
    #     'diēs Iovis',
    #     'diēs Veneris',
    #     'diēs Sabbatī',
    #     'diēs Dominice',
    # ]

    MONTH_NAME = [
        'Iānuārius',
        'Februārius',
        'Mārtius',
        'Aprīlis',
        'Maius',
        'Iūnius',
        'Iūlius',
        'Augustus',
        'September',
        'Octōber',
        'November',
        'December',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Iān',
        'Feb',
        'Mār',
        'Apr',
        'Mai',
        'Iūn',
        'Iūl',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec',
    ]

    MONTH_NAME_GENITIVE = [
        'Iānuāriī',
        'Februāriī',
        'Mārtiī',
        'Aprīlis',
        'Maiī',
        'Iūniī',
        'Iūliī',
        'Augustī',
        'Septembris',
        'Octōbris',
        'Novembris',
        'Decembris',
    ]

    MONTH_NAME_DATIVE = [
        'Iānuāriō',
        'Februāriō',
        'Mārtiō',
        'Aprīlī',
        'Maiō',
        'Iūniō',
        'Iūliō',
        'Augustō',
        'Septembrī',
        'Octōbrī',
        'Novembrī',
        'Decembrī',
    ]

    MONTH_NAME_ACCUSATIVE = [
        'Iānuārium',
        'Februārium',
        'Mārtium',
        'Aprīlem',
        'Maium',
        'Iūnium',
        'Iūlium',
        'Augustum',
        'Septembrem',
        'Octōbrem',
        'Novembrem',
        'Decembrem',
    ]

    MONTH_NAME_ABLATIVE = [
        'Iānuāriō',
        'Februāriō',
        'Mārtiō',
        'Aprīlī',
        'Maiō',
        'Iūniō',
        'Iūliō',
        'Augustō',
        'Septembrī',
        'Octōbrī',
        'Novembrī',
        'Decembrī',
    ]

    MONTH_NAME_VOCATIVE = [
        'Iānuārie',
        'Februārie',
        'Mārtie',
        'Aprīlis',
        'Maie',
        'Iūnie',
        'Iūlie',
        'Auguste',
        'September',
        'Octōber',
        'November',
        'December',
    ]

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#$ND #$GM #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #$ND #$GM #Y, #u:#p:#a'
    DST_NAME = 'Ora Legale'
    DST_SHORT_NAME = 'OL'
    DEFAULT_TIME_ZONE = 'Europe/Rome'
    WEEK_NUMBER_SYMBOL = 'heb'
    DAY_NUMBER_SYMBOL = 'diēs'
    ISO_DATE_LONG_FORMAT = '%-d %b. %Y'
    DATE_TEXT_SHORT_MONTH_FORMAT = '#$GM'
    TEXT_MONTH_DAY_FORMAT = '#-d #$GM'
    YEAR_TEXT_MONTH_FORMAT = '#$NM #Y'

    SEASON_NAME = {
        'spring_cross_quarter': 'Hieme vēr',
        'spring_equinox': 'Vēr',
        'summer_cross_quarter': 'Vēre aestātem',
        'summer_solstice': 'Aestās',
        'autumn_cross_quarter': 'Aestāte autumnum',
        'autumn_equinox': 'Autumnus',
        'winter_cross_quarter': 'Autumnō hiemem',
        'winter_solstice': 'Hiems',
    }

    MOON_PHASE = {
        'new': 'Lūna nova',
        'waxing_crescent': 'Lūna accrēscēns corniculātā',
        'first_quarter': 'Lūna accrēscēns dīmidiātā',
        'waxing_gibbous': 'Lūna accrēscēns in orbem īnsinuāta',
        'full': 'Lūna plēna',
        'waning_gibbous': 'Lūna dēcrēscēns in orbem īnsinuāta',
        'third_quarter': 'Lūna dēcrēscēns dīmidiātā',
        'waning_crescent': 'Lūna dēcrēscēns corniculātā',
    }

    #
    # Error messages
    #
    ERROR = 'Error'
    WEEKDAY_ERROR = 'Non acceptābilis diēs hebdomadis {weekday}'
    MONTH_ERROR = 'Non acceptābilis mēnsis {month}'

    def weekday_name(self, weekday: SezimalInteger, case: str = CASE_NOMINATIVE) -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        if case:
            case = case.upper()

            if case == self.CASE_GENITIVE:
                return self.WEEKDAY_NAME_GENITIVE[int(weekday.decimal)]
            elif case == self.CASE_DATIVE:
                return self.WEEKDAY_NAME_DATIVE[int(weekday.decimal)]
            elif case == self.CASE_ACCUSATIVE:
                return self.WEEKDAY_NAME_ACCUSATIVE[int(weekday.decimal)]
            elif case == self.CASE_ABLATIVE:
                return self.WEEKDAY_NAME_ABLATIVE[int(weekday.decimal)]
            elif case == self.CASE_VOCATIVE:
                return self.WEEKDAY_NAME_VOCATIVE[int(weekday.decimal)]

        return self.WEEKDAY_NAME[int(weekday.decimal)]

    def month_name(self, month: SezimalInteger, case: str = CASE_GENITIVE) -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month -= 1

        if case:
            case = case.upper()

            if case == self.CASE_GENITIVE:
                return self.MONTH_NAME_GENITIVE[int(month.decimal)]
            elif case == self.CASE_DATIVE:
                return self.MONTH_NAME_DATIVE[int(month.decimal)]
            elif case == self.CASE_ACCUSATIVE:
                return self.MONTH_NAME_ACCUSATIVE[int(month.decimal)]
            elif case == self.CASE_ABLATIVE:
                return self.MONTH_NAME_ABLATIVE[int(month.decimal)]
            elif case == self.CASE_VOCATIVE:
                return self.MONTH_NAME_VOCATIVE[int(month.decimal)]

        return self.MONTH_NAME[int(month.decimal)]

    CALENDAE = 0
    NONAE = 1
    IDUS = 2

    DAY_NAME = [
        'Calendae',
        'Nōnae',
        'Īdūs',
    ]

    DAY_NAME_GENITIVE = [
        'Calendārum',
        'Īduum',
        'Nōnārum',
    ]

    DAY_NAME_DATIVE = [
        'Calendīs',
        'Īdibus',
        'Nōnīs',
    ]

    DAY_NAME_ACCUSATIVE = [
        'Calendās',
        'Īdūs',
        'Nōnās',
    ]

    DAY_NAME_ABLATIVE = [
        'Calendīs',
        'Īdibus',
        'Nōnīs',
    ]

    DAY_NAME_VOCATIVE = [
        'Calendae',
        'Īdūs',
        'Nōnae',
    ]

    def day_name(self, date: SezimalDate, case: str = CASE_NOMINATIVE) -> str:
        if date.day == 1:
            day = self.CALENDAE
        elif (date.is_long_month and date.day == 13) \
            or ((not date.is_long_month) and date.day == 5):
            day = self.NONAE
        elif (date.is_long_month and date.day == 25) \
            or ((not date.is_long_month) and date.day == 21):
            day = self.IDUS
        else:
            return date.format('#-d')

        if case:
            case = case.upper()

            if case == self.CASE_GENITIVE:
                return self.DAY_NAME_GENITIVE[day]
            elif case == self.CASE_DATIVE:
                return self.DAY_NAME_DATIVE[day]
            elif case == self.CASE_ACCUSATIVE:
                return self.DAY_NAME_ACCUSATIVE[day]
            elif case == self.CASE_ABLATIVE:
                return self.DAY_NAME_ABLATIVE[day]
            elif case == self.CASE_VOCATIVE:
                return self.DAY_NAME_VOCATIVE[day]

        return self.DAY_NAME[day]

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for case in self.CASES:
            if f'#${case}W' in fmt:
                fmt = fmt.replace(f'#${case}W', self.weekday_name(date.weekday, case))

            if f'#${case}M' in fmt:
                fmt = fmt.replace(f'#${case}M', self.month_name(date.month, case))

            if f'#${case}D' in fmt:
                fmt = fmt.replace(f'#${case}D', self.day_name(date, case))

        return fmt
