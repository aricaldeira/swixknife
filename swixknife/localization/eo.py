

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
        'januaro',
        'februaro',
        'marto',
        'aprilo',
        'majo',
        'junio',
        'julio',
        'aŭgusto',
        'septembro',
        'oktobro',
        'novembro',
        'decembro',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan',
        'feb',
        'mar',
        'apr',
        'maj',
        'jun',
        'jul',
        'aŭg',
        'sep',
        'okt',
        'nov',
        'dec',
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

