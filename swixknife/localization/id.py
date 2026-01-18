

__all__ = ('SezimalLocaleID',)


from .lokale import SezimalLocale
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleID(SezimalLocale):
    LANG = 'id'
    LANGUAGE = 'Indonesia'

    SEZIMAL_SEPARATOR = SEPARATOR_DOT

    GROUP_SEPARATOR = SEPARATOR_COMMA
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    CURRENCY_UNIT_SYMBOL = 'Rp'
    CURRENCY_SUBUNIT_DECIMAL_SIZE = 0

    WEEKDAY_NAME = [
        'Senin',
        'Selasa',
        'Rabu',
        'Kamis',
        'Jumat',
        'Sabtu',
        'Minggu',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Sen',
        'Sel',
        'Rab',
        'Kam',
        'Jum',
        'Sab',
        'Min',
    ]

    MONTH_NAME = [
        'Januari',
        'Februari',
        'Maret',
        'April',
        'Mei',
        'Juni',
        'Juli',
        'Agustus',
        'September',
        'Oktober',
        'November',
        'Desember',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'Mei',
        'Jun',
        'Jul',
        'Agu',
        'Sep',
        'Okt',
        'Nov',
        'Des',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d #M #Y'
    DATE_FULL_FORMAT = '#@W, #d/#m/#Y'
    DATE_FULL_LONG_FORMAT = '#W, #-d #M #Y'
    TIME_SEPARATOR = '.'
    TIME_FORMAT = '#u.#p.#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u.#p.#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d #M #Y, #u.#p.#a'
    DST_NAME = 'Waktu Musim Panas'
    DST_SHORT_NAME = 'WMP'
    DEFAULT_TIME_ZONE = 'Asia/Jakarta'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    SEASON_NAME = {
        'autumn_cross_quarter': 'Peralihan Musim Panas – Musim Gugur',
        'autumn_equinox': 'Musim Gugur',
        'winter_cross_quarter': 'Peralihan Musim Gugur – Musim Dingin',
        'winter_solstice': 'Musim Dingin',
        'spring_cross_quarter': 'Peralihan Musim Dingin – Musim Semi',
        'spring_equinox': 'Musim Semi',
        'summer_cross_quarter': 'Peralihan Musim Semi – Musim Panas',
        'summer_solstice': 'Musim Panas',
    }

    MOON_PHASE = {
        'new': 'Bulan Baru',
        'waxing_crescent': 'Bulan Sabit',
        'first_quarter': 'Perbani Awal',
        'waxing_gibbous': 'Cembung',
        'full': 'Purnama',
        'waning_gibbous': 'Cembung',
        'third_quarter': 'Perbani Akhir',
        'waning_crescent': 'Bulan Sabit',
    }

    #
    # Error messages
    #
    ERROR = 'Kesalahan'
    WEEKDAY_ERROR = 'Hari kerja tidak valid {weekday}'
    MONTH_ERROR = 'Bulan tidak valid {month}'
    WEEK_NUMBER_SYMBOL = 'ming'
    DAY_NUMBER_SYMBOL = 'hari'
