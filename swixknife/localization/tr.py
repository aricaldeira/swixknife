

__all__ = ('SezimalLocaleTR',)


from .lokale import SezimalLocale
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleTR(SezimalLocale):
    LANG = 'tr'
    LANGUAGE = 'Türkçe'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

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

    DATE_FORMAT = '#d.#m.#y'
    DATE_LONG_FORMAT = '#-d #M #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d.#m.#y, #@W, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#-d #M #Y, #W, #u:#p:#a'
    DST_NAME = 'Yaz Saati Uygulaması'
    DST_SHORT_NAME = 'YSU'
    DEFAULT_TIME_ZONE = 'Europe/Istanbul'

    SEASON_NAME = {
        'spring_cross_quarter': 'Kıştan İlkbahara Geçiş',
        'spring_equinox': 'İlkbahar',
        'summer_cross_quarter': 'İlkbahardan Yaza Geçiş',
        'summer_solstice': 'Yaz',
        'autumn_cross_quarter': 'Yazdan Sonbahara Geçiş',
        'autumn_equinox': 'Sonbahar',
        'winter_cross_quarter': 'Sonbahardan Kışa Geçiş',
        'winter_solstice': 'Kış',
    }

    MOON_PHASE = {
        'new': 'Yeni Ay',
        'waxing_crescent': 'Hilal',
        'first_quarter': 'İlk Dördün',
        'waxing_gibbous': 'Şişkin Hilal',
        'full': 'Dolunay',
        'waning_gibbous': 'Şişkin Azalan',
        'third_quarter': 'Son Dördün',
        'waning_crescent': 'Azalan',
    }
