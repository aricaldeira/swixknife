

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

    HOLIDAYS_CALENDAR = [
        ('SYM+01-01', '🎆\ufe0f Yılbaşı'),
        ('SYM+05-01', '🛠️\ufe0f✊\ufe0f Emek ve Dayanışma Günü'),

        # ('ISO+1915-03-18', '🇹🇷\ufe0f🛑\ufe0f Çanakkale Zaferi ve Şehitleri Anma Günü (%i)'),
        # ('ISO+1920-04-23', '🇹🇷\ufe0f👧\ufe0f Ulusal Egemenlik ve Çocuk Bayramı (%i)'),
        # ('ISO+1919-05-19', '🇹🇷\ufe0f Atatürk’ü Anma, Gençlik ve Spor Bayramı (%i)'),
        # ('ISO+2016-07-15', '🇹🇷\ufe0f🕊️\ufe0f Demokrasi ve Milli Birlik Günü (%i)'),
        # ('ISO+1922-08-30', '🇹🇷\ufe0f🏆\ufe0f Zafer Bayramı (%i)'),
        # ('ISO+1923-10-29', '🇹🇷\ufe0f🎇\ufe0f Cumhuriyet Bayramı (%i)'),
        # ('ISO+1938-11-10', '🇹🇷\ufe0f🫡\ufe0f Atatürk’ü Anma Günü (%i)'),

        ('HIJ+SYM+10-01', '🕌\ufe0f🍬\ufe0f Şeker Bayramı'),
        ('HIJ+SYM+10-02', '🕌\ufe0f🍬\ufe0f Şeker Bayramı'),
        ('HIJ+SYM+10-03', '🕌\ufe0f🍬\ufe0f Şeker Bayramı'),
        ('HIJ+SYM+12-10', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
        ('HIJ+SYM+12-11', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
        ('HIJ+SYM+12-12', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
        ('HIJ+SYM+12-13', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        ('ISO+01-01', '🎆\ufe0f Yılbaşı'),
        ('ISO+05-01', '🛠️\ufe0f✊\ufe0f Emek ve Dayanışma Günü'),

        ('ISO+1915-03-18', '🇹🇷\ufe0f🛑\ufe0f Çanakkale Zaferi ve Şehitleri Anma Günü (%i)'),
        ('ISO+1920-04-23', '🇹🇷\ufe0f👧\ufe0f Ulusal Egemenlik ve Çocuk Bayramı (%i)'),
        ('ISO+1919-05-19', '🇹🇷\ufe0f Atatürk’ü Anma, Gençlik ve Spor Bayramı (%i)'),
        ('ISO+2016-07-15', '🇹🇷\ufe0f🕊️\ufe0f Demokrasi ve Milli Birlik Günü (%i)'),
        ('ISO+1922-08-30', '🇹🇷\ufe0f🏆\ufe0f Zafer Bayramı (%i)'),
        ('ISO+1923-10-29', '🇹🇷\ufe0f🎇\ufe0f Cumhuriyet Bayramı (%i)'),
        ('ISO+1938-11-10', '🇹🇷\ufe0f🫡\ufe0f Atatürk’ü Anma Günü (%i)'),

        ('HIJ+ISO+10-01', '🕌\ufe0f🍬\ufe0f Şeker Bayramı'),
        ('HIJ+ISO+10-02', '🕌\ufe0f🍬\ufe0f Şeker Bayramı'),
        ('HIJ+ISO+10-03', '🕌\ufe0f🍬\ufe0f Şeker Bayramı'),
        ('HIJ+ISO+12-10', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
        ('HIJ+ISO+12-11', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
        ('HIJ+ISO+12-12', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
        ('HIJ+ISO+12-13', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
    ]

    ISLAMIC_HOLIDAYS = [
        ('HIJ+09-01', '🍯\ufe0f🥙\ufe0f 1st day of Ramaḍān'),
        ('HIJ+09-30', '🍯\ufe0f🥙\ufe0f Laylat ul-Jāʾizah'),
        ('HIJ+10-01-FRI', '🍯\ufe0f🥙\ufe0f Jumuʿat ul-Widāʿ'),
        ('HIJ+10-01', '🕌\ufe0f🍬\ufe0f Şeker Bayramı'),
        ('HIJ+12-10', '🕌\ufe0f🐏\ufe0f Kurban Bayramı'),
    ]
