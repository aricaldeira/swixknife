

__all__ = ('SezimalLocaleGA',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE
from .ga import SezimalLocaleGA

#
# Information about lenition, eclipsis etc. from Wikitionary;
#
# Using mí/mhí:
#    https://blogs.transparent.com/irish/nios-mo-faoi-na-mionna-more-about-the-months-in-irish/
#    https://blogs.transparent.com/irish/to-%E2%80%9Cmi%E2%80%9D-or-not-to-%E2%80%9Cmi%E2%80%9D-using-the-word-%E2%80%9Cmonth%E2%80%9D-in-irish/
#
# Ordinal suffix:
#    https://en.wikipedia.org/wiki/Date_and_time_notation_in_Ireland
#
# Date format:
#    https://forum.wordreference.com/threads/irish-gaelic-dates.1477128/
#


class SezimalLocaleGA_TRADITIONAL(SezimalLocaleGA):
    LANG = 'ga'
    LANGUAGE = 'Gaeilge'

    WEEKDAY_NAME = [
        'Luan',
        'Máirt',
        'Céadaoin',
        'Déardaoin',
        'Aoine',
        'Saṫarn',
        'Doṁnaċ',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Lua',
        'Mái',
        'Céa',
        'Déa',
        'Aoi',
        'Saṫ',
        'Doṁ',
    ]

    MONTH_NAME = [
        'Eanáir',
        'Feaḃra',
        'Márta',
        'Aibreán',
        'Bealtaine',
        'Meiṫeaṁ',
        'Iúil',
        'Lúnasa',
        'Meán Fóṁair',
        'Deireaḋ Fóṁair',
        'mí na Saṁain',
        'mí na Nollag',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Ean',
        'Fea',
        'Már',
        'Aib',
        'Bea',
        'Mei',
        'Iúi',
        'Lún',
        'MFó',
        'DFó',
        'Saṁ',
        'Nol',
    ]

    SEASON_NAME = {
        'spring_cross_quarter': 'Imbolc',
        'spring_equinox': 'Earraċ',
        'summer_cross_quarter': 'Bealtaine',
        'summer_solstice': 'Saṁraḋ',
        'autumn_cross_quarter': 'Lúnasa',
        'autumn_equinox': 'Fóṁar',
        'winter_cross_quarter': 'Saṁain',
        'winter_solstice': 'Geiṁreaḋ',
    }

    MOON_PHASE = {
        'new': 'Gealaċ Úr',
        'waxing_crescent': 'Corrán Gealaí',
        'first_quarter': 'Gealaċ Ċéad Ċeṫrú',
        'waxing_gibbous': 'Ó Ġealaċ Ċéad Ċeṫrú go Gealaċ Lán',
        'full': 'Gealaċ Lán',
        'waning_gibbous': 'Ó Ġealaċ Lán go Gealaċ Tríú Ċeṫrú',
        'third_quarter': 'Gealaċ Tríú Ċeṫrú',
        'waning_crescent': 'Deireaḋ Gealaí',
    }

    def weekday_name(self, weekday: SezimalInteger, mutation: str = '', case: str = '') -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        weekday_name = self.WEEKDAY_NAME[int(weekday.decimal)]

        mutation = mutation.upper()
        case = case.upper()

        #
        # Lenition
        #
        if mutation == 'L':
            if weekday == 1:
                weekday_name = 'Ṁ' + weekday_name[1:]
            elif weekday == 2:
                weekday_name = 'Ċ' + weekday_name[1:]
            elif weekday == 3:
                weekday_name = 'Ḋ' + weekday_name[1:]
            elif weekday == 5:
                weekday_name = 'Ṡ' + weekday_name[1:]
            elif weekday == 10:
                weekday_name = 'Ḋ' + weekday_name[1:]

        #
        # Eclipsis
        #
        elif mutation == 'E':
            if weekday == 2:
                weekday_name = 'g' + weekday_name
            elif weekday == 3:
                weekday_name = 'n' + weekday_name
            elif weekday == 4:
                weekday_name = 'n' + weekday_name
            elif weekday == 10:
                weekday_name = 'n' + weekday_name

        #
        # H-Protesis
        #
        elif mutation == 'H':
            if weekday == 3:
                weekday_name = 'h' + weekday_name

        #
        # Definite article
        #
        elif mutation == 'AN':
            if case in ['', 'N', 'D']:
                if weekday == 1:
                    weekday_name = 'an Ṁ' + weekday_name[1:]
                elif weekday == 2:
                    weekday_name = 'an Ċ' + weekday_name[1:]
                else:
                    weekday_name = 'an ' + weekday_name

            elif case == 'G':
                if weekday == 0:
                    weekday_name = 'an ' + weekday_name[0:-1] + 'in'
                elif weekday == 1:
                    weekday_name = 'na ' + weekday_name
                elif weekday == 2:
                    weekday_name = 'na ' + weekday_name
                elif weekday == 4:
                    weekday_name = 'na h' + weekday_name
                elif weekday == 5:
                    weekday_name = 'an t' + weekday_name[0:-2] + 'irn'
                elif weekday == 10:
                    weekday_name = 'an ' + weekday_name[0:-2] + 'iġ'
                else:
                    weekday_name = 'an ' + weekday_name

        elif mutation == 'DÉ':
            if weekday == 4:
                weekday_name = 'Dé ' + self.weekday_name(weekday + 1, 'H', '')
            elif weekday != 3:
                weekday_name = 'Dé ' + self.weekday_name(weekday + 1, '', 'G')
            else:
                weekday_name = 'Dé ' + weekday_name

        else:
            if case == 'G':
                if weekday == 0:
                    weekday_name = weekday_name[0:-1] + 'in'
                elif weekday == 5:
                    weekday_name = weekday_name[0:-2] + 'irn'
                elif weekday == 10:
                    weekday_name = weekday_name[0:-2] + 'iġ'

        return weekday_name

    def weekday_abbreviated_name(self, weekday: SezimalInteger, mutation: str = '', case: str = '') -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        weekday_abbreviated_name = self.WEEKDAY_ABBREVIATED_NAME[int(weekday.decimal)]

        mutation = mutation.upper()
        case = case.upper()

        #
        # Lenition
        #
        if mutation == 'L':
            if weekday == 1:
                weekday_abbreviated_name = 'Ṁ' + weekday_abbreviated_name[1:]
            elif weekday == 2:
                weekday_abbreviated_name = 'Ċ' + weekday_abbreviated_name[1:]
            elif weekday == 3:
                weekday_abbreviated_name = 'Ḋ' + weekday_abbreviated_name[1:]
            elif weekday == 5:
                weekday_abbreviated_name = 'Ṡ' + weekday_abbreviated_name[1:]
            elif weekday == 10:
                weekday_abbreviated_name = 'Ḋ' + weekday_abbreviated_name[1:]

        #
        # Eclipsis
        #
        elif mutation == 'E':
            if weekday == 2:
                weekday_abbreviated_name = 'g' + weekday_abbreviated_name
            elif weekday == 3:
                weekday_abbreviated_name = 'n' + weekday_abbreviated_name
            elif weekday == 4:
                weekday_abbreviated_name = 'n' + weekday_abbreviated_name
            elif weekday == 10:
                weekday_abbreviated_name = 'n' + weekday_abbreviated_name

        #
        # H-Protesis
        #
        elif mutation == 'H':
            if weekday == 3:
                weekday_abbreviated_name = 'h' + weekday_abbreviated_name

        #
        # Definite article
        #
        elif mutation == 'AN':
            if case in ('', 'N', 'D'):
                if weekday == 1:
                    weekday_abbreviated_name = 'an Ṁ' + weekday_abbreviated_name[1:]
                elif weekday == 2:
                    weekday_abbreviated_name = 'an Ċ' + weekday_abbreviated_name[1:]
                else:
                    weekday_abbreviated_name = 'an ' + weekday_abbreviated_name

            elif case == 'G':
                if weekday == 0:
                    weekday_abbreviated_name = 'an ' + weekday_abbreviated_name  # [0:-1] + 'in'
                elif weekday == 1:
                    weekday_abbreviated_name = 'na ' + weekday_abbreviated_name
                elif weekday == 2:
                    weekday_abbreviated_name = 'na ' + weekday_abbreviated_name
                elif weekday == 4:
                    weekday_abbreviated_name = 'na h' + weekday_abbreviated_name
                elif weekday == 5:
                    weekday_abbreviated_name = 'an t' + weekday_abbreviated_name  # [0:-2] + 'irn'
                elif weekday == 10:
                    weekday_abbreviated_name = 'an ' + weekday_abbreviated_name  # [0:-2] + 'iġ'
                else:
                    weekday_abbreviated_name = 'an ' + weekday_abbreviated_name

        elif mutation == 'DÉ':
            if weekday == 4:
                weekday_abbreviated_name = 'Dé ' + self.weekday_abbreviated_name(weekday + 1, 'H', '')
            elif weekday != 3:
                weekday_abbreviated_name = 'Dé ' + self.weekday_abbreviated_name(weekday + 1, '', 'G')
            else:
                weekday_abbreviated_name = 'Dé ' + weekday_abbreviated_name

        # else:
        #     if case == 'G':
        #         if weekday == 0:
        #             weekday_abbreviated_name = weekday_abbreviated_name[0:-1] + 'in'
        #         elif weekday == 5:
        #             weekday_abbreviated_name = weekday_abbreviated_name[0:-2] + 'irn'
        #         elif weekday == 10:
        #             weekday_abbreviated_name = weekday_abbreviated_name[0:-2] + 'iġ'

        return weekday_abbreviated_name

    def month_name(self, month: SezimalInteger, mutation: str = '', case: str = '') -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month_name = self.MONTH_NAME[int(month.decimal) - 1]

        mutation = mutation.upper()
        case = case.upper()

        #
        # Lenition
        #
        if mutation == 'L':
            if month == 2:
                month_name = 'Ḟ' + month_name[1:]
            elif month == 3:
                month_name = 'Ṁ' + month_name[1:]
            elif month == 5:
                month_name = 'Ḃ' + month_name[1:]
            elif month == 10:
                if case == 'G':
                    month_name = self.month_name(month, '', 'G')
                    month_name = 'Ṁ' + month_name[1:]
                else:
                    month_name = 'Ṁ' + month_name[1:]
            elif month == 13:
                month_name = 'Ṁ' + month_name[1:]
            elif month == 14:
                month_name = 'Ḋ' + month_name[1:]
            elif month == 15:
                month_name = 'Ṁ' + month_name[1:]
            elif month == 20:
                month_name = 'Ṁ' + month_name[1:]

        #
        # Eclipsis
        #
        elif mutation == 'E':
            if month == 1:
                month_name = 'n' + month_name
            elif month == 2:
                month_name = 'ḃ' + month_name
            elif month == 4:
                month_name = 'n' + month_name
            elif month == 5:
                month_name = 'm' + month_name
            elif month == 11:
                month_name = 'n' + month_name
            elif month == 14:
                month_name = 'n' + month_name

        #
        # H-Protesis
        #
        elif mutation == 'H':
            if month == 1:
                month_name = 'h' + month_name
            elif month == 4:
                month_name = 'h' + month_name
            elif month == 11:
                month_name = 'h' + month_name

        #
        # T-Protesis
        #
        elif mutation == 'T':
            if month == 1:
                month_name = 't' + month_name
            elif month == 4:
                month_name = 't' + month_name
            elif month == 11:
                month_name = 't' + month_name

        #
        # Definite article
        #
        elif mutation == 'AN':
            if case in ('', 'N', 'D'):
                if month == 1:
                    month_name = 'an ' + self.month_name(month, 'T', '')
                elif month == 2:
                    month_name = 'an ' + self.month_name(month, 'L', '')
                elif month == 4:
                    month_name = 'an ' + self.month_name(month, 'T', '')
                elif month == 5:
                    month_name = 'an ' + self.month_name(month, 'L', '')
                elif month == 11:
                    month_name = 'an ' + self.month_name(month, 'T', '')
                else:
                    month_name = 'an ' + month_name

            elif case == 'G':
                if month == 2:
                    month_name = 'na ' + month_name
                elif month == 3:
                    month_name = 'an ' + self.month_name(month, 'L', '')
                elif month == 4:
                    month_name = 'an ' + self.month_name(month, '', 'G')
                elif month == 5:
                    month_name = 'na ' + month_name
                elif month == 10:
                    month_name = 'an ' + self.month_name(month, 'L', 'G')
                else:
                    month_name = 'an ' + month_name

        elif mutation == 'MÍ':
            if month == 2:
                month_name = 'mí na ' + month_name
            elif month == 3:
                month_name = 'mí an ' + self.month_name(month, 'L')
            elif month == 4:
                month_name = 'mí ' + self.month_name(month, '', 'G')
            elif month == 5:
                month_name = 'mí na ' + month_name
            elif month == 10:
                month_name = 'mí an ' + self.month_name(month, 'L', 'G')
            elif month == 13:
                month_name = 'mí ' + self.month_name(month, 'L', '')
            elif month == 14:
                month_name = 'mí ' + self.month_name(month, 'L', '')
            elif month != 15 and month != 20:
                month_name = 'mí ' + month_name

        elif mutation == 'MHÍ':
            month_name = self.month_name(month, 'MÍ', case)
            month_name = 'ṁ' + month_name[1:]

        else:
            if case == 'G':
                if month == 4:
                    month_name = month_name[:-1] + 'in'
                elif month == 10:
                    month_name = month_name.replace('ea', 'i').replace('eɑ', 'i')
                elif month == 15:
                    month_name = 'Ṁ' + month_name[1:-3] + 'na'
                elif month == 20:
                    month_name = 'Ṁ' + month_name[1:]

        return month_name
