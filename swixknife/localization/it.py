

__all__ = ('SezimalLocaleIT',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleIT(SezimalLocale):
    LANG = 'it'
    LANGUAGE = 'italiano'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'lunedì',
        'martedì',
        'mercoledì',
        'giovedì',
        'venerdì',
        'sabato',
        'domenica',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'lun',
        'mar',
        'mer',
        'gio',
        'ven',
        'sab',
        'dom',
    ]

    MONTH_NAME= [
        'gennaio',
        'febbraio',
        'marzo',
        'aprile',
        'maggio',
        'giugno',
        'luglio',
        'agosto',
        'settembre',
        'ottobre',
        'novembre',
        'dicembre',
    ]

    MONTH_ABBREVIATED_NAME = [
        'gen',
        'feb',
        'mar',
        'apr',
        'mag',
        'giu',
        'lug',
        'ago',
        'set',
        'ott',
        'nov',
        'dic',
    ]

    ERA_NAME = [
        #
        # Era Umana Sesimale
        #
        'EUS',
        #
        # Avanti l’Era Umana Sesimale
        #
        'aEUS',
    ]

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'º'

        return ''

    def _change_word_weekday(self, word: str, weekday: SezimalInteger) -> str:
        if weekday != 11:
            word += ' '
        elif word == 'il':
            word = 'la '
        elif word == 'un':
            word = 'una '
        else:
            word += 'la '

        return word

    def _change_word_month(self, word: str, month: SezimalInteger) -> str:
        if month not in (4, 12, 14):
            word += ' '
        elif word == 'il':
            word = 'l’'
        elif word == 'un':
            word = 'un '
        elif word == 'col':
            word = 'con l’'
        else:
            word += 'l’'

        return word

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for word in ['IL', 'UN', 'AL', 'DEL', 'NEL', 'DAL', 'SUL', 'COL']:
            if f'#${word}W' in fmt:
                parola = self._change_word_weekday(word.lower(), date.weekday)
                fmt = fmt.replace(f'#${word}W', parola)

            if f'#${word}M' in fmt:
                parola = self._change_word_month(word.lower(), date.month)
                fmt = fmt.replace(f'#${word}M', parola)

        return fmt
