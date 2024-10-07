

__all__ = ('SezimalLocalePL',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale, EuroCurrency
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocalePL(EuroCurrency, SezimalLocale):
    LANG = 'pl'
    LANGUAGE = 'polski'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = 'zł'
    CURRENCY_SUBUNIT_SYMBOL = 'gr'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

    CASE_NOMINATIVE = 'N'
    CASE_GENITIVE = 'G'
    CASE_DATIVE = 'D'
    CASE_ACCUSATIVE = 'A'
    CASE_INSTRUMENTAL = 'I'
    CASE_LOCATIVE = 'L'
    CASE_VOCATIVE = 'V'

    CASE_ROMAN = 'R'

    CASES = [
        CASE_NOMINATIVE,
        CASE_GENITIVE,
        CASE_DATIVE,
        CASE_ACCUSATIVE,
        CASE_INSTRUMENTAL,
        CASE_LOCATIVE,
        CASE_VOCATIVE,
    ]

    WEEKDAY_NAME = [
        'poniedziałek', # masculine
        'wtorek',       # masculine
        'środa',        # feminine
        'czwartek',     # masculine
        'piątek',       # feminine
        'sobota',       # feminine
        'niedziela',    # feminine
    ]

    WEEKDAY_NAME_GENITIVE = [
        'poniedziałku',
        'wtorku',
        'środy',
        'czwartku',
        'piątku',
        'soboty',
        'niedzieli',
    ]

    WEEKDAY_NAME_DATIVE = [
        'poniedziałkowi',
        'wtorkowi',
        'środzie',
        'czwartkowi',
        'piątkowi',
        'sobocie',
        'niedzieli',
    ]

    WEEKDAY_NAME_ACCUSATIVE = [
        'poniedziałek',
        'wtorek',
        'środę',
        'czwartek',
        'piątek',
        'sobotę',
        'niedzielę',
    ]

    WEEKDAY_NAME_INSTRUMENTAL = [
        'poniedziałkiem',
        'wtorkiem',
        'środą',
        'czwartkiem',
        'piątkiem',
        'sobotą',
        'niedzielą',
    ]

    WEEKDAY_NAME_LOCATIVE = [
        'poniedziałku',
        'wtorku',
        'środzie',
        'czwartku',
        'piątku',
        'sobocie',
        'niedzieli',
    ]

    WEEKDAY_NAME_VOCATIVE = [
        'poniedziałku',
        'wtorku',
        'środo',
        'czwartku',
        'piątku',
        'soboto',
        'niedzielo'
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'pon',
        'wto',
        'śro',
        'czw',
        'pią',
        'sob',
        'nie',
    ]

    MONTH_NAME = [
        'styczeń',
        'luty',
        'marzec',
        'kwiecień',
        'maj',
        'czerwiec',
        'lipiec',
        'sierpień',
        'wrzesień',
        'październik',
        'listopad',
        'grudzień',
    ]

    MONTH_NAME_GENITIVE = [
        'stycznia',
        'lutego',
        'marca',
        'kwietnia',
        'maja',
        'czerwca',
        'lipca',
        'sierpnia',
        'września',
        'października',
        'listopada',
        'grudnia',
    ]

    MONTH_NAME_DATIVE = [
        'styczniowi',
        'lutemu',
        'marcowi',
        'kwietniowi',
        'majowi',
        'czerwcowi',
        'lipcowi',
        'sierpniowi',
        'wrześniowi',
        'październikowi',
        'listopadowi',
        'grudniowi',
    ]

    MONTH_NAME_ACCUSATIVE = [
        'styczeń',
        'luty',
        'marzec',
        'kwiecień',
        'maj',
        'czerwiec',
        'lipiec',
        'sierpień',
        'wrzesień',
        'październik',
        'listopad',
        'grudzień',
    ]

    MONTH_NAME_INSTRUMENTAL = [
        'styczniem',
        'lutym',
        'marcem',
        'kwietniem',
        'majem',
        'czerwcem',
        'lipcem',
        'sierpniem',
        'wrześniem',
        'październikiem',
        'listopadem',
        'grudniem',
    ]

    MONTH_NAME_LOCATIVE = [
        'styczniu',
        'lutym',
        'marcu',
        'kwietniu',
        'maju',
        'czerwcu',
        'lipcu',
        'sierpniu',
        'wrześniu',
        'październiku',
        'listopadzie',
        'grudniu',
    ]

    MONTH_NAME_VOCATIVE = [
        'styczniu',
        'luty',
        'marcu',
        'kwietniu',
        'maju',
        'czerwcu',
        'lipcu',
        'sierpniu',
        'wrześniu',
        'październiku',
        'listopadzie',
        'grudniu',
    ]

    MONTH_NAME_ROMAN = [
        'I',
        'II',
        'III',
        'IV',
        'V',
        'VI',
        'VII',
        'VIII',
        'IX',
        'X',
        'XI',
        'XII',
    ]

    MONTH_ABBREVIATED_NAME = [
        'sty',
        'lut',
        'mar',
        'kwi',
        'maj',
        'cze',
        'lip',
        'sie',
        'wrz',
        'paź',
        'lis',
        'gru',
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

    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#-d. #M #Y r.'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d.#m.#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d. #M #Y r., #u:#p:#a'
    DST_NAME = 'Czas Letni'
    DST_SHORT_NAME = 'CzL'
    DEFAULT_TIME_ZONE = 'Europe/Warsaw'

    SEASON_NAME = {
        'spring_cross_quarter': 'Przejście Zima – Wiosna',
        'spring_equinox': 'Wiosna',
        'summer_cross_quarter': 'Przejście Wiosna – Lato',
        'summer_solstice': 'Lato',
        'autumn_cross_quarter': 'Przejście Lato – Jesień',
        'autumn_equinox': 'Jesień',
        'winter_cross_quarter': 'Przejście Jesień – Zima',
        'winter_solstice': 'Zima',
    }

    #
    # TODO: revise, these are translations from a table on the Russian Wikipedia
    #
    MOON_PHASE = {
        'new': 'Nów',
        'waxing_crescent': 'Młody',
        'first_quarter': 'Kwadra Pierwsza',
        'waxing_gibbous': 'Przybywający',
        'full': 'Pełnia',
        'waning_gibbous': 'Ubywający',
        'third_quarter': 'Ostatnia Kwadra',
        'waning_crescent': 'Stary',
    }

    #
    # Error messages
    #
    ERROR = 'Błąd'
    WEEKDAY_ERROR = 'Nieprawidłowy dzień tygodnia {weekday}'
    MONTH_ERROR = 'Nieprawidłowy miesiąc {month}'
    WEEK_NUMBER_SYMBOL = 'tydz'

    def weekday_name(self, weekday: SezimalInteger, case: str = CASE_ACCUSATIVE) -> str:
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
            elif case == self.CASE_INSTRUMENTAL:
                return self.WEEKDAY_NAME_INSTRUMENTAL[int(weekday.decimal)]
            elif case == self.CASE_LOCATIVE:
                return self.WEEKDAY_NAME_LOCATIVE[int(weekday.decimal)]
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
            elif case == self.CASE_INSTRUMENTAL:
                return self.MONTH_NAME_INSTRUMENTAL[int(month.decimal)]
            elif case == self.CASE_LOCATIVE:
                return self.MONTH_NAME_LOCATIVE[int(month.decimal)]
            elif case == self.CASE_VOCATIVE:
                return self.MONTH_NAME_VOCATIVE[int(month.decimal)]
            elif case == self.CASE_ROMAN:
                return self.MONTH_NAME_ROMAN[int(month.decimal)]

        return self.MONTH_NAME[int(month.decimal)]

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        return '.'

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for case in self.CASES:
            if f'#${case}W' in fmt:
                fmt = fmt.replace(f'#${case}W', self.weekday_name(date.weekday, case))

            if f'#${case}M' in fmt:
                fmt = fmt.replace(f'#${case}M', self.month_name(date.month, case))

        #
        # Dealing with:
        # w → we
        # z → ze
        #
        if f'#$WW' in fmt:
            if date.weekday in (2, 4):
                fmt = fmt.replace(f'#$WW', 'we')
            else:
                fmt = fmt.replace(f'#$WW', 'w')

        if f'#$ZW' in fmt:
            if date.weekday in (3, 10):
                fmt = fmt.replace(f'#$ZW', 'ze')
            else:
                fmt = fmt.replace(f'#$ZW', 'z')

        if f'#$WM' in fmt:
            if date.month in 13:
                fmt = fmt.replace(f'#$WM', 'we')
            else:
                fmt = fmt.replace(f'#$WM', 'w')

        if f'#$ZM' in fmt:
            if date.month in (1, 12):
                fmt = fmt.replace(f'#$ZM', 'ze')
            else:
                fmt = fmt.replace(f'#$ZM', 'z')

        #
        # Special case for months using Roman numerals
        #
        if f'#$RM' in fmt:
            fmt = fmt.replace(f'#$RM', self.month_name(date.month, 'R'))

        return fmt
