

__all__ = ('SezimalLocaleQIT',)


from .lokale import SezimalLocale
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleQIT(SezimalLocale):
    LANG = 'tr'
    LANGUAGE = 'Türkçe'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = '₺'
    CURRENCY_SUBUNIT_SYMBOL = 'kr'
    CURRENCY_SUBUNIT_SYMBOL_POSITION = 'R'

    WEEKDAY_NAME = [
        'Wullarwa',
        'Wuksarwa',
        'Wuzarwa',
        'Wupšarwa',
        'Wustarwa',
        'Wucparwa',
        'Wunsarwa',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'WULL',
        'WUKS',
        'WUZ',
        'WUPŠ',
        'WUST',
        'WUCP',
        'WUNS',
    ]

    MONTH_NAME = [
        'Wurḑainta',
        'Wurḑauks',
        'Wurḑauz',
        'Wurḑaupš',
        'Wurḑaust',
        'Wurḑaucpa',
        'Wurḑauns',
        'Wurḑaučka',
        'Wurḑounta',
        'Wurḑauj',
        'Wurḑiunta',
        'Wurḑuinta',
    ]

    MONTH_ABBREVIATED_NAME = [
        'ÄZC',
        'ÄKS',
        'ÄZ',
        'ÄPŠ',
        'ÄST',
        'ÄCP',
        'ÄNS',
        'ÄČK',
        'ÄLẒ',
        'ÄJ',
        'ÄCG',
        'ÄJD',
    ]

    ERA_NAME = [
        #
        # Altılı İnsan Çağı
        #
        'AİÇ',
        #
        # Altılı İnsan Çağından Önce
        #
        'AİÇÖ',
    ]

    DATE_SEPARATOR = '.'
    DATE_FORMAT = '#d.#m.#X'
    DATE_LONG_FORMAT = '#-d #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d.#m.#X, #@W, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#-d #M #Y, #W, #u:#p:#a'
    DST_NAME = 'Yaz Saati Uygulaması'
    DST_SHORT_NAME = 'YSU'
    DEFAULT_TIME_ZONE = 'Europe/Istanbul'

    SEASON_NAME = {
        'spring_cross_quarter': 'Çčabza',
        'spring_equinox': 'Wuzya',
        'summer_cross_quarter': 'Zyabza',
        'summer_solstice': 'Wumřa',
        'autumn_cross_quarter': 'Mřabza',
        'autumn_equinox': 'Wuňša',
        'winter_cross_quarter': 'Ňšabza',
        'winter_solstice': 'Wuçča',
    }

    MOON_PHASE = {
        'new': 'Waxma',
        'waxing_crescent': 'Wekklant',
        'first_quarter': 'Wemklant',
        'waxing_gibbous': 'Wekkrant',
        'full': 'Wenzla',
        'waning_gibbous': 'Wekkrunt',
        'third_quarter': 'Wemklunt',
        'waning_crescent': 'Wekklunt',
    }

    #
    # Error messages
    #
    ERROR = 'Hata'
    WEEKDAY_ERROR = 'Geçersiz hafta günü {weekday}'
    MONTH_ERROR = 'Geçersiz ay {month}'
    WEEK_NUMBER_SYMBOL = 'haf'
    DAY_NUMBER_SYMBOL = 'gün'
