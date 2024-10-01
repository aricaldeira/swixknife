

__all__ = ('SezimalLocaleRO',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleRO(SezimalLocale):
    LANG = 'ro'
    LANGUAGE = 'română'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    ARTICLE_INDEFINITE = 'I'
    ARTICLE_DEFINITE = 'D'

    CASE_NOMINATIVE = 'N'
    CASE_ACCUSATIVE = 'A'
    CASE_GENITIVE = 'G'
    CASE_DATIVE = 'D'
    CASE_VOCATIVE = 'V'

    ARTICLES = [
        ARTICLE_INDEFINITE,
        ARTICLE_DEFINITE,
    ]

    CASES = [
        CASE_NOMINATIVE,
        CASE_ACCUSATIVE,
        CASE_GENITIVE,
        CASE_DATIVE,
        CASE_VOCATIVE,
    ]

    WEEKDAY_NAME = [
        'luni',
        'marți',
        'miercuri',
        'joi',
        'vineri',
        'sâmbătă',
        'duminică',
    ]

    WEEKDAY_NAME_ARTICLE = [
        'lunea',
        'marțea',
        'miercurea',
        'joia',
        'vinerea',
        'sâmbăta',
        'duminica',
    ]

    WEEKDAY_NAME_GENITIVE_DATIVE = [
        'luni',
        'marți',
        'miercuri',
        'joi',
        'vineri',
        'sâmbete',
        'duminici',
    ]

    WEEKDAY_NAME_VOCATIVE = [
        'luni',
        'marți',
        'miercuri',
        'joi',
        'vineri',
        'sâmbăto',
        'duminico',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'lu.',
        'ma.',
        'mi.',
        'joi',
        'vi.',
        'sâ.',
        'du.',
    ]

    MONTH_NAME= [
        'ianuarie',
        'februarie',
        'martie',
        'aprilie',
        'mai',
        'iunie',
        'iulie',
        'august',
        'septembrie',
        'octombrie',
        'noiembrie',
        'decembrie',
    ]

    MONTH_NAME_TRADITIONAL = [
        'gerar',     # masculine, regular article pattern: ul, ului
        'făurar',    # masculine, regular article pattern: ul, ului
        'mărțișor',  # neuter, regular article pattern: ul, ului
        'prier',     # masculine, regular article pattern: ul, ului
        'florar',    # masculine, regular article pattern: ul, ului
        'cireșar',   # masculine, regular article pattern: ul, ului
        'cuptor',    # neuter, regular article pattern: ul, ului
        'gustar',    # masculine, regular article pattern: ul, ului
        'răpciune',  # masculine, behaves like the standard names (no declension)
        'brumărel',  # masculine, regular article pattern: ul, ului
        'brumar',    # masculine, regular article pattern: ul, ului
        'undrea',    # feminine, article pattern: +ua, -a+lei
    ]

    MONTH_ABBREVIATED_NAME = [
        'ian.',
        'feb.',
        'mar.',
        'apr.',
        'mai',
        'iun.',
        'iul.',
        'aug.',
        'sept.',
        'oct.',
        'nov.',
        'dec.',
    ]

    ERA_NAME = [
        #
        # Era Umană Sezimală
        #
        'e.u.s.',
        #
        # Înainte de Era Umană Sezimală
        #
        'î.e.u.s',
    ]

    DATE_FORMAT = '#d.#m.#Y'
    DATE_LONG_FORMAT = '#-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d.#m.#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #M #Y, #u:#p:#a'
    DST_NAME = 'Ora de Vară'
    DST_SHORT_NAME = 'OV'
    DEFAULT_TIME_ZONE = 'Europe/Bucharest'

    SEASON_NAME = {
        'spring_cross_quarter': 'Tranziție Iarnă – Primăvară',
        'spring_equinox': 'Primăvară',
        'summer_cross_quarter': 'Tranziție Primăvară – Vară',
        'summer_solstice': 'Vară',
        'autumn_cross_quarter': 'Tranziție Vară – Toamnă',
        'autumn_equinox': 'Toamnă',
        'winter_cross_quarter': 'Tranziție Toamnă – Iarnă',
        'winter_solstice': 'Iarnă',
    }

    #
    # TODO: revise, Romanian Wikipedia is very scant on the matter
    #
    MOON_PHASE = {
        'new': 'Nouă',
        'waxing_crescent': 'Semiluna',
        'first_quarter': 'Primul Pătrar',
        'waxing_gibbous': 'Primul Pătrar în Plină',
        'full': 'Plină',
        'waning_gibbous': 'Plină în Treilea Pătrar',
        'third_quarter': 'Treilea Pătrar',
        'waning_crescent': 'Descreștere',
    }

    #
    # Error messages
    #
    ERROR = 'Eroare'
    WEEKDAY_ERROR = 'Zi a săptămânii nevalidă {weekday}'
    MONTH_ERROR = 'Luna nevalidă {month}'
    WEEK_NUMBER_SYMBOL = 'săp'

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'ᵉʳ'

        return ''

    def weekday_name(self, weekday: SezimalInteger, case: str = None) -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        if case:
            case = case.upper()

            article = case[0]
            case = case[1]

            if article == self.ARTICLE_INDEFINITE:
                if case == self.CASE_GENITIVE or case == self.CASE_DATIVE:
                    return self.WEEKDAY_NAME_GENITIVE_DATIVE[int(weekday.decimal)]

                elif case == self.CASE_VOCATIVE:
                    return self.WEEKDAY_NAME_VOCATIVE[int(weekday.decimal)]

                return self.WEEKDAY_NAME[int(weekday.decimal)]

            else:
                if case == self.CASE_GENITIVE or case == self.CASE_DATIVE:
                    return self.WEEKDAY_NAME_GENITIVE_DATIVE[int(weekday.decimal)] + 'i'

                elif case == self.CASE_VOCATIVE:
                    return self.WEEKDAY_NAME_VOCATIVE[int(weekday.decimal)]

                return self.WEEKDAY_NAME_ARTICLE[int(weekday.decimal)]

        return self.WEEKDAY_NAME[int(weekday.decimal)]

    def month_name(self, month: SezimalInteger, case: str = None) -> str:
        month = SezimalInteger(month)

        if month < 1 or month > 20:
            raise ValueError(self.MONTH_ERROR.format(month=month))

        month -= 1

        if case:
            case = case.upper()

            if case[0] == 'T':
                article = case[1]
                case = case[2]

                month_name = self.MONTH_NAME_TRADITIONAL[int(month.decimal)]

                #
                # răpciune has no declensions
                #
                if month_name == 'răpciune':
                    return month_name

                #
                # Without the definite article, only undrea has declensions
                #
                if article == self.ARTICLE_INDEFINITE:
                    if month_name != 'undrea':
                        return month_name

                    if case == self.CASE_GENITIVE or self.CASE_DATIVE:
                        return month_name[:-1] + 'le'

                    return month_name

                #
                # With the article, only undrea has a different pattern
                #
                if month_name == 'undrea':
                    if case == self.CASE_NOMINATIVE or case == self.CASE_ACCUSATIVE:
                        return month_name + 'ua'
                    elif case == self.CASE_GENITIVE or case == self.CASE_DATIVE:
                        return month_name[:-1] + 'lei'

                    return month_name

                #
                # Now, the other months have all the same pattern
                #
                if case == self.CASE_NOMINATIVE or case == self.CASE_ACCUSATIVE:
                    return month_name + 'ul'
                elif case == self.CASE_GENITIVE or case == self.CASE_DATIVE:
                    return month_name + 'ului'

                return month_name

        return self.MONTH_NAME[int(month.decimal)]

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for article in self.ARTICLES:
            for case in self.CASES:
                if f'#${article}{case}W' in fmt:
                    fmt = fmt.replace(f'#${article}{case}W', self.weekday_name(date.weekday, article + case))

                if f'#${article}{case}M' in fmt:
                    fmt = fmt.replace(f'#${article}{case}M', self.month_name(date.month, article + case))

                if f'#$T{article}{case}M' in fmt:
                    fmt = fmt.replace(f'#$T{article}{case}M', self.month_name(date.month, 'T' + article + case))

        return fmt
