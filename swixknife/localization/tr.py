

__all__ = ('SezimalLocaleTR',)


from .lokale import SezimalLocale
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleTR(SezimalLocale):
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
        'Pazartesi',
        'Salı',
        'Çarşamba',
        'Perşembe',
        'Cuma',
        'Cumartesi',
        'Pazar',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Pzt',
        'Sal',
        'Çar',
        'Per',
        'Cum',
        'Cmt',
        'Paz',
    ]

    MONTH_NAME = [
        'Ocak',
        'Şubat',
        'Mart',
        'Nisan',
        'Mayıs',
        'Haziran',
        'Temmuz',
        'Ağustos',
        'Eylül',
        'Ekim',
        'Kasım',
        'Aralık',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Oca',
        'Şub',
        'Mar',
        'Nis',
        'May',
        'Haz',
        'Tem',
        'Ağu',
        'Eyl',
        'Eki',
        'Kas',
        'Ara',
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
        'spring_cross_quarter': 'Kıştan i̇lkbahara geçiş',
        'spring_equinox': 'İlkbahar',
        'summer_cross_quarter': 'İlkbahardan yaza geçiş',
        'summer_solstice': 'Yaz',
        'autumn_cross_quarter': 'Yazdan sonbahara geçiş',
        'autumn_equinox': 'Sonbahar',
        'winter_cross_quarter': 'Sonbahardan kışa geçiş',
        'winter_solstice': 'Kış',
    }

    MOON_PHASE = {
        'new': 'Yeni ay',
        'waxing_crescent': 'Hilal',
        'first_quarter': 'İlk dördün',
        'waxing_gibbous': 'Şişkin hilal',
        'full': 'Dolunay',
        'waning_gibbous': 'Şişkin azalan',
        'third_quarter': 'Son dördün',
        'waning_crescent': 'Azalan',
    }

    #
    # Error messages
    #
    ERROR = 'Hata'
    WEEKDAY_ERROR = 'Geçersiz hafta günü {weekday}'
    MONTH_ERROR = 'Geçersiz ay {month}'
    WEEK_NUMBER_SYMBOL = 'haf'
    DAY_NUMBER_SYMBOL = 'gün'

    UPPERCASE_MAPPING = {
        ord('ı'): 'I',
        ord('i'): 'İ'
    }
    LOWERCASE_MAPPING = {
        ord('I'): 'ı',
        ord('İ'): 'i',
    }
