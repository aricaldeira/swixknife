

__all__ = ('SezimalLocaleEL',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleEL(SezimalLocale):
    LANG = 'el'
    LANGUAGE = 'Ελληνικά'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CASE_NOMINATIVE = 'N'
    CASE_GENITIVE = 'G'
    CASE_ACCUSATIVE = 'A'
    CASE_VOCATIVE = 'V'

    CASES = [
        CASE_NOMINATIVE,
        CASE_GENITIVE,
        CASE_ACCUSATIVE,
        CASE_VOCATIVE,
    ]

    DEFINITE_ARTICLE_MASCULINE = 'ο'
    DEFINITE_ARTICLE_MASCULINE_GENITIVE = 'του'
    DEFINITE_ARTICLE_MASCULINE_ACCUSATIVE = 'τον'

    DEFINITE_ARTICLE_FEMININE = 'η'
    DEFINITE_ARTICLE_FEMININE_GENITIVE = 'την'
    DEFINITE_ARTICLE_FEMININE_ACCUSATIVE = 'της'

    INDEFINITE_ARTICLE_MASCULINE = 'ένας'
    INDEFINITE_ARTICLE_MASCULINE_GENITIVE = 'έναν'
    INDEFINITE_ARTICLE_MASCULINE_ACCUSATIVE = 'ενός'

    INDEFINITE_ARTICLE_FEMININE = 'μία'
    INDEFINITE_ARTICLE_FEMININE_GENITIVE = 'μίαν'
    INDEFINITE_ARTICLE_FEMININE_ACCUSATIVE = 'μίας'

    INDEFINITE_ARTICLE_FEMININE_2 = 'μια'
    INDEFINITE_ARTICLE_FEMININE_2_GENITIVE = 'μιαν'
    INDEFINITE_ARTICLE_FEMININE_2_ACCUSATIVE = 'μιας'

    DEMONSTRATIVE_PRONOUN_MASCULINE = 'αυτός'
    DEMONSTRATIVE_PRONOUN_MASCULINE_GENITIVE = 'αυτoύ'
    DEMONSTRATIVE_PRONOUN_MASCULINE_ACCUSATIVE = 'αυτόν'

    DEMONSTRATIVE_PRONOUN_FEMININE = 'αυτή'
    DEMONSTRATIVE_PRONOUN_FEMININE_GENITIVE = 'αυτής'
    DEMONSTRATIVE_PRONOUN_FEMININE_ACCUSATIVE = 'αυτήν'

    WEEKDAY_NAME = [
        'Δευτέρα',
        'Τρίτη',
        'Τετάρτη',
        'Πέμπτη',
        'Παρασκευή',
        'Σάββατο',
        'Κυριακή',
    ]

    WEEKDAY_NAME_GENITIVE = [
        'Δευτέρας',
        'Τρίτης',
        'Τετάρτης',
        'Πέμπτης',
        'Παρασκευής',
        'Σαββάτου',
        'Κυριακής',
    ]

    WEEKDAY_NAME_ACCUSATIVE = [
        'Δευτέρα',
        'Τρίτη',
        'Τετάρτη',
        'Πέμπτη',
        'Παρασκευή',
        'Σάββατο',
        'Κυριακή',
    ]

    WEEKDAY_NAME_VOCATIVE = [
        'Δευτέρα',
        'Τρίτη',
        'Τετάρτη',
        'Πέμπτη',
        'Παρασκευή',
        'Σάββατε',
        'Κυριακή',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Δευ',
        'Τρί',
        'Τετ',
        'Πέμ',
        'Παρ',
        'Σάβ',
        'Κυρ',
    ]

    MONTH_NAME = [
        'Ιανουάριος',
        'Φεβρουάριος',
        'Μάρτιος',
        'Απρίλιος',
        'Μάιος',
        'Ιούνιος',
        'Ιούλιος',
        'Αύγουστος',
        'Σεπτέμβριος',
        'Οκτώβριος',
        'Νοέμβριος',
        'Δεκέμβριος'
    ]

    MONTH_NAME_GENITIVE = [
        'Ιανουαρίου',
        'Φεβρουαρίου',
        'Μαρτίου',
        'Απριλίου',
        'Μαΐου',
        'Ιουνίου',
        'Ιουλίου',
        'Αυγούστου',
        'Σεπτεμβρίου',
        'Οκτωβρίου',
        'Νοεμβρίου',
        'Δεκεμβρίου'
    ]

    MONTH_NAME_ACCUSATIVE = [
        'Ιανουάριο',
        'Φεβρουάριο',
        'Μάρτιο',
        'Απρίλιο',
        'Μάιο',
        'Ιούνιο',
        'Ιούλιο',
        'Αύγουστο',
        'Σεπτέμβριο',
        'Οκτώβριο',
        'Νοέμβριο',
        'Δεκέμβριο'
    ]

    MONTH_NAME_VOCATIVE = [
        'Ιανουάριε',
        'Φεβρουάριε',
        'Μάρτιε',
        'Απρίλιε',
        'Μάιε',
        'Ιούνιε',
        'Ιούλιε',
        'Αύγουστε',
        'Σεπτέμβριε',
        'Οκτώβριε',
        'Νοέμβριε',
        'Δεκέμβριε'
    ]

    MONTH_ABBREVIATED_NAME = [
        'Ιαν',
        'Φεβ',
        'Μαρ',
        'Απρ',
        'Μαΐ',
        'Ιουν',
        'Ιουλ',
        'Αυγ',
        'Σεπ',
        'Οκτ',
        'Νοε',
        'Δεκ',
    ]

    MONTH_COLLOQUIAL_NAME = [
        'Γενάρης',
        'Φλεβάρης',
        'Μάρτης',
        'Απρίλης',
        'Μάης',
        'Ιούνης',
        'Ιούλης',
        'Αύγουστος',
        'Σεπτέμβρης',
        'Οκτώβρης',
        'Νοέμβρης',
        'Δεκέμβρης'
    ]

    MONTH_COLLOQUIAL_NAME_GENITIVE = [
        'Γενάρη',
        'Φλεβάρη',
        'Μάρτη',
        'Απρίλη',
        'Μάη',
        'Ιούνη',
        'Ιούλη',
        'Αυγούστου',
        'Σεπτέμβρη',
        'Οκτώβρη',
        'Νοέμβρη',
        'Δεκέμβρη'
    ]

    MONTH_COLLOQUIAL_NAME_ACCUSATIVE = [
        'Γενάρη',
        'Φλεβάρη',
        'Μάρτη',
        'Απρίλη',
        'Μάη',
        'Ιούνη',
        'Ιούλη',
        'Αύγουστο',
        'Σεπτέμβρη',
        'Οκτώβρη',
        'Νοέμβρη',
        'Δεκέμβρη'
    ]

    MONTH_COLLOQUIAL_NAME_VOCATIVE = [
        'Γενάρη',
        'Φλεβάρη',
        'Μάρτη',
        'Απρίλη',
        'Μάη',
        'Ιούνη',
        'Ιούλη',
        'Αύγουστε',
        'Σεπτέμβρη',
        'Οκτώβρη',
        'Νοέμβρη',
        'Δεκέμβρη'
    ]

    MONTH_COLLOQUIAL_ABBREVIATED_NAME = [
        'Γεν',
        'Φλε',
        'Μαρ',
        'Απρ',
        'Μάη',
        'Ιουν',
        'Ιουλ',
        'Αυγ',
        'Σεπ',
        'Οκτ',
        'Νοε',
        'Δεκ',
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

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O #M #Y, #u:#p:#a'

    SEASON_NAME = {
        'spring_cross_quarter': 'Μετάβαση Χειμώνας – Άνοιξη',
        'spring_equinox': 'Άνοιξη',
        'summer_cross_quarter': 'Μετάβαση Άνοιξη – Καλοκαίρι',
        'summer_solstice': 'Καλοκαίρι',
        'autumn_cross_quarter': 'Μετάβαση Καλοκαίρι – Φθινόπωρο',
        'autumn_equinox': 'Φθινόπωρο',
        'winter_cross_quarter': 'Μετάβαση Φθινόπωρο – Χειμώνας',
        'winter_solstice': 'Χειμώνας',
    }

    MOON_PHASE = {
        'new': 'Νέα',
        'waxing crescent': 'Αύξων Μηνίσκος',
        'first quarter': 'Πρώτο Τέταρτο',
        'waxing gibbous': 'Αύξων Αμφίκυρτος',
        'full': 'Πανσέληνος',
        'waning gibbous': 'Φθίνων Αμφίκυρτος',
        'third quarter': 'Τελευταίο Τέταρτο',
        'waning crescent': 'Φθίνων Μηνίσκος',
    }

    def weekday_name(self, weekday: SezimalInteger, case: str = CASE_ACCUSATIVE) -> str:
        weekday = SezimalInteger(weekday)

        if weekday < 1 or weekday > 11:
            raise ValueError(self.WEEKDAY_ERROR.format(weekday=weekday))

        weekday -= 1

        if case:
            case = case.upper()

            if case == self.CASE_GENITIVE:
                return self.WEEKDAY_NAME_GENITIVE[int(weekday.decimal)]
            elif case == self.CASE_ACCUSATIVE:
                return self.WEEKDAY_NAME_ACCUSATIVE[int(weekday.decimal)]
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

            #
            # Colloquial names of the months
            #
            if case[0] == 'C':
                case = case[1:]

                if case == self.CASE_GENITIVE:
                    return self.MONTH_COLLOQUIAL_NAME_GENITIVE[int(month.decimal)]
                elif case == self.CASE_ACCUSATIVE:
                    return self.MONTH_COLLOQUIAL_NAME_ACCUSATIVE[int(month.decimal)]
                elif case == self.CASE_VOCATIVE:
                    return self.MONTH_COLLOQUIAL_NAME_VOCATIVE[int(month.decimal)]
                else:
                    return self.MONTH_COLLOQUIAL_NAME[int(month.decimal)]

            else:
                if case == self.CASE_GENITIVE:
                    return self.MONTH_NAME_GENITIVE[int(month.decimal)]
                elif case == self.CASE_ACCUSATIVE:
                    return self.MONTH_NAME_ACCUSATIVE[int(month.decimal)]
                elif case == self.CASE_VOCATIVE:
                    return self.MONTH_NAME_VOCATIVE[int(month.decimal)]

        return self.MONTH_NAME[int(month.decimal)]

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            if case == self.CASE_GENITIVE:
                return 'ης'

            return 'η'

        return ''

    def _article_declension_weekday(self, article: str, case: str, weekday: SezimalInteger) -> str:
        if article == self.DEFINITE_ARTICLE_MASCULINE:
            if case == self.CASE_GENITIVE:
                return self.DEFINITE_ARTICLE_MASCULINE_GENITIVE
            elif case == self.CASE_ACCUSATIVE:
                return self.DEFINITE_ARTICLE_MASCULINE_ACCUSATIVE
            else:
                return self.DEFINITE_ARTICLE_MASCULINE

        elif article == self.DEFINITE_ARTICLE_FEMININE:
            if case == self.CASE_GENITIVE:
                if weekday != 1:
                    return self.DEFINITE_ARTICLE_FEMININE_GENITIVE[:-1]
                else:
                    return self.DEFINITE_ARTICLE_FEMININE_GENITIVE

            elif case == self.CASE_ACCUSATIVE:
                return self.DEFINITE_ARTICLE_FEMININE_ACCUSATIVE
            else:
                return self.DEFINITE_ARTICLE_FEMININE

        elif article == self.INDEFINITE_ARTICLE_MASCULINE:
            if case == self.CASE_GENITIVE:
                return self.INDEFINITE_ARTICLE_MASCULINE_GENITIVE
            elif case == self.CASE_ACCUSATIVE:
                return self.INDEFINITE_ARTICLE_MASCULINE_ACCUSATIVE
            else:
                return self.INDEFINITE_ARTICLE_MASCULINE

        elif article == self.INDEFINITE_ARTICLE_FEMININE:
            if case == self.CASE_GENITIVE:
                if weekday != 1:
                    return self.INDEFINITE_ARTICLE_FEMININE_GENITIVE[:-1]
                else:
                    return self.INDEFINITE_ARTICLE_FEMININE_GENITIVE

            elif case == self.CASE_ACCUSATIVE:
                return self.INDEFINITE_ARTICLE_FEMININE_ACCUSATIVE
            else:
                return self.INDEFINITE_ARTICLE_FEMININE

        elif article == self.INDEFINITE_ARTICLE_FEMININE_2:
            if case == self.CASE_GENITIVE:
                if weekday != 1:
                    return self.INDEFINITE_ARTICLE_FENIMINE_2_GENITIVE[:-1]
                else:
                    return self.INDEFINITE_ARTICLE_FENIMINE_2_GENITIVE

            elif case == self.CASE_ACCUSATIVE:
                return self.INDEFINITE_ARTICLE_FENIMINE_2_ACCUSATIVE
            else:
                return self.INDEFINITE_ARTICLE_FENIMINE_2

        elif article == self.DEMONSTRATIVE_PRONOUN_MASCULINE:
            if case == self.CASE_GENITIVE:
                return self.DEMONSTRATIVE_PRONOUN_MASCULINE_GENITIVE
            elif case == self.CASE_ACCUSATIVE:
                return self.DEMONSTRATIVE_PRONOUN_MASCULINE_ACCUSATIVE
            else:
                return self.DEMONSTRATIVE_PRONOUN_MASCULINE

        elif article == self.DEMONSTRATIVE_PRONOUN_FEMININE:
            if case == self.CASE_GENITIVE:
                return self.DEMONSTRATIVE_PRONOUN_FEMININE_GENITIVE
            elif case == self.CASE_ACCUSATIVE:
                if weekday != 1:
                    return self.DEMONSTRATIVE_PRONOUN_FEMININE_ACCUSATIVE[:-1]
                else:
                    return self.DEMONSTRATIVE_PRONOUN_FEMININE_ACCUSATIVE

            else:
                return self.DEMONSTRATIVE_PRONOUN_FEMININE

        return ''

    def _article_declension_month(self, article: str, case: str, month: SezimalInteger) -> str:
        if article == self.DEFINITE_ARTICLE_MASCULINE:
            if case == self.CASE_GENITIVE:
                return self.DEFINITE_ARTICLE_MASCULINE_GENITIVE
            elif case == self.CASE_ACCUSATIVE:
                if month in (1, 4, 10, 11, 12, 14):
                    return self.DEFINITE_ARTICLE_MASCULINE_ACCUSATIVE[:-1]
                else:
                    return self.DEFINITE_ARTICLE_MASCULINE_ACCUSATIVE

            else:
                return self.DEFINITE_ARTICLE_MASCULINE

        elif article == self.INDEFINITE_ARTICLE_MASCULINE:
            if case == self.CASE_GENITIVE:
                if month in (1, 4, 10, 11, 12, 14):
                    return self.INDEFINITE_ARTICLE_MASCULINE_GENITIVE[:-1]
                else:
                    return self.INDEFINITE_ARTICLE_MASCULINE_GENITIVE

            elif case == self.CASE_ACCUSATIVE:
                return self.INDEFINITE_ARTICLE_MASCULINE_ACCUSATIVE
            else:
                return self.INDEFINITE_ARTICLE_MASCULINE

        elif article == self.DEMONSTRATIVE_PRONOUN_MASCULINE:
            if case == self.CASE_GENITIVE:
                return self.DEMONSTRATIVE_PRONOUN_MASCULINE_GENITIVE
            elif case == self.CASE_ACCUSATIVE:
                if month in (1, 4, 10, 11, 12, 14):
                    return self.DEMONSTRATIVE_PRONOUN_MASCULINE_ACCUSATIVE[:-1]
                else:
                    return self.DEMONSTRATIVE_PRONOUN_MASCULINE_ACCUSATIVE

            else:
                return self.DEMONSTRATIVE_PRONOUN_MASCULINE

        return ''

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for case in self.CASES:
            if f'#${case}M' in fmt:
                fmt = fmt.replace(f'#${case}M', self.month_name(date.month, case))

            if f'#$C{case}M' in fmt:
                fmt = fmt.replace(f'#$C{case}M', self.month_name(date.month, 'C' + case))

            if f'#${case}W' in fmt:
                fmt = fmt.replace(f'#${case}W', self.weekday_name(date.weekday, case))

            #
            # Declension of articles with weekday names (feminine, but Saturday is masculine)
            # Definite article Η (Capital Letter Greek Eta)
            # Indefinite article ΜΊΑ or ΜΙΑ
            # Demonstrative pronoun ΑΥΤΉ
            #
            for word, masculine, feminine in [
                ['Η', self.DEFINITE_ARTICLE_MASCULINE, self.DEFINITE_ARTICLE_FEMININE],
                ['ΜΊΑ', self.INDEFINITE_ARTICLE_MASCULINE, self.INDEFINITE_ARTICLE_FEMININE],
                ['ΜΙΑ', self.INDEFINITE_ARTICLE_MASCULINE, self.INDEFINITE_ARTICLE_FEMININE_2],
                ['ΑΥΤΉ', self.DEMONSTRATIVE_PRONOUN_MASCULINE, self.DEMONSTRATIVE_PRONOUN_FEMININE],
                ['ΑΥΤΗ', self.DEMONSTRATIVE_PRONOUN_MASCULINE, self.DEMONSTRATIVE_PRONOUN_FEMININE],
            ]:
                if f'#${case}{word}W' in fmt:
                    if date.weekday == 10:
                        declension = self._article_declension_weekday(masculine, case, date.weekday)
                    else:
                        declension = self._article_declension_weekday(feminine, case, date.weekday)

                    fmt = fmt.replace(f'#${case}{word}W', declension)

            #
            # Declension of articles with month names
            # Definite article Ο (Capital Letter Greek Omicron)
            # Indefinite article ΈΝΑΣ or ΕΝΑΣ
            # Demonstrative pronoun ΑΥΤΌΣ or ΑΥΤΟΣ
            #
            for word, masculine in [
                ['Ο', self.DEFINITE_ARTICLE_MASCULINE],
                ['ΈΝΑΣ', self.INDEFINITE_ARTICLE_MASCULINE],
                ['ΕΝΑΣ', self.INDEFINITE_ARTICLE_MASCULINE],
                ['ΑΥΤΌΣ', self.DEMONSTRATIVE_PRONOUN_MASCULINE],
                ['ΑΥΤΟΣ', self.DEMONSTRATIVE_PRONOUN_MASCULINE],
            ]:
                if f'#${case}{word}M' in fmt:
                    declension = self._article_declension_month(masculine, case, date.month)
                    fmt = fmt.replace(f'#${case}{word}M', declension)

            if f'#${case}O' in fmt:
                fmt = fmt.replace(f'#${case}O', self.day_ordinal_suffix(date.day, case))

        return fmt
