

__all__ = ('SezimalLocaleIT',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleIT(SezimalLocale):
    LANG = 'it'
    LANGUAGE = 'italiano'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '€'
    CURRENCY_SUBUNIT_SYMBOL = 'c'
    CURRENCY_UNIT_SYMBOL_POSITION = 'R'

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

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #M #Y, #u:#p:#a'
    DST_NAME = 'Ora Legale'
    DST_SHORT_NAME = 'OL'
    DEFAULT_TIME_ZONE = 'Europe/Rome'
    WEEK_NUMBER_SYMBOL = 'set'
    DAY_NUMBER_SYMBOL = 'giorno'

    SEASON_NAME = {
        'spring_cross_quarter': 'Transizione Inverno – Primavera',
        'spring_equinox': 'Primavera',
        'summer_cross_quarter': 'Transizione Primavera – Estate',
        'summer_solstice': 'Estate',
        'autumn_cross_quarter': 'Transizione Estate – Autunno',
        'autumn_equinox': 'Autunno',
        'winter_cross_quarter': 'Transizione Autunno – Inverno',
        'winter_solstice': 'Inverno',
    }

    MOON_PHASE = {
        'new': 'Nuova',
        'waxing_crescent': 'Crescente',
        'first_quarter': 'Primo Quarto',
        'waxing_gibbous': 'Dal Primo Quarto alla Piena',
        'full': 'Piena',
        'waning_gibbous': 'Dalla Piena all’Ultimo Quarto',
        'third_quarter': 'Ultimo Quarto',
        'waning_crescent': 'Calante',
    }

    #
    # Error messages
    #
    ERROR = 'Errore'
    WEEKDAY_ERROR = 'Giorno della settimana non valido {weekday}'
    MONTH_ERROR = 'Mese non valido {month}'

    HOLIDAYS = [
        ('01-01', '🕊\ufe0f️  Capodanno'),
        ('01-10', '🍬\ufe0f Epifania'),
        # ('EASTER', 'Pasqua'),
        ('04-12', '🧺\ufe0f Pasquetta'),
        ('04-41', '🇮🇹\ufe0f Festa della Liberazione'),
        ('05-01', '🐝\ufe0f Festa del Lavoro'),
        ('10-02', '🇮🇹\ufe0f Festa della Repubblica Italiana'),
        ('12-21', '🏖\ufe0f️ Ferragosto'),
        ('15-01', '🪦\ufe0f Ognissanti'),
        ('20-12', '⛪\ufe0f Immacolata Concezione'),
        ('20-41', '👼🏼\ufe0f Natale'),
        ('20-42', '⛪\ufe0f Santo Stefano'),
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

    DCC_TERM_NAME = [
        'bimestre‐zero',
        'bimestre‐uno',
        'bimestre‐due',
        'bimestre‐tre',
        'bimestre‐quattro',
    ]

    DCC_TERM_ABBREVIATED_NAME = [
        'B0',
        'B1',
        'B2',
        'B3',
        'B4',
    ]

    DCC_MONTH_NAME = [
        'mese‐zero',
        'mese‐unoi',
        'mese‐due',
        'mese‐tre',
        'mese‐quattro',
        'mese‐cinque',
        'mese‐sei',
        'mese‐seiuno',
        'mese‐seidue',
        'mese‐seitré',
        'mese‐seiquattro',
    ]

    DCC_WEEKDAY_NAME = [
        'giorno‐della‐setimana‐zero',
        'giorno‐della‐setimana‐uno',
        'giorno‐della‐setimana‐due',
        'giorno‐della‐setimana‐tre',
        'giorno‐della‐setimana‐quattro',
        'giorno‐della‐setimana‐cinque',
    ]

    DCC_WEEKDAY_ABBREVIATED_NAME = [
        'GS0',
        'GS1',
        'GS2',
        'GS3',
        'GS4',
        'GS5',
    ]

    DCC_NUMBER = [
        'zero',
        'unoi',
        'due',
        'tre',
        'quattro',
        'cinque',
        'sei',
        'seiuno',
        'seidue',
        'seitré',
        'seiquattro',
    ]

    DCC_YEAR_COUNT = {
        None: '&>Y anni',
        SezimalInteger('1'): '&>Y anno',
    }

    DCC_TERM_COUNT = {
        None: '&-t bimestre',
        SezimalInteger('1'): '&-t bimestre',
    }

    DCC_MONTH_COUNT = {
        None: '&-m mesi',
        SezimalInteger('1'): '&-m mese',
    }

    DCC_WEEK_COUNT = {
        None: '&-wM settimane',
        SezimalInteger('1'): '&-wM settimana',
    }

    DCC_WEEK_IN_YEAR_COUNT = {
        None: '&-wY settimane',
        SezimalInteger('1'): '&-wY settimana',
    }

    DCC_DAY_COUNT = {
        None: '&-d giorni',
        SezimalInteger('1'): '&-d giorno',
    }

    DCC_DAY_IN_YEAR_COUNT = {
        None: '&-dY giorni',
        SezimalInteger('1'): '&-dY giorno',
    }

    DCC_DAY_IN_WEEK_COUNT = {
        None: '&-dW giorni',
        SezimalInteger('1'): '&-dW giorno',
    }

    DCC_DATE_MONTH_DAY_SEPARATOR = ' e '
