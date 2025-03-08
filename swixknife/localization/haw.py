

__all__ = ('SezimalLocaleHAW',)


from .en_us import SezimalLocaleEN_US

from ..base import SEPARATOR_COMMA, SEPARATOR_DOT


class SezimalLocaleHAW(SezimalLocaleEN_US):
    LANG = 'haw'
    LANGUAGE = 'ʻōlelo Hawaiʻi'

    DEFAULT_TIME_ZONE = 'Pacific/Honolulu'
    FIRST_WEEKDAY = 'MON'

    WEEKDAY_NAME = [
        'Pōʻakahi',
        'Pōʻalua',
        'Pōʻakolu',
        'Pōʻahā',
        'Pōʻalima',
        'Pōʻaono',
        'Lāpule',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'P1',
        'P2',
        'P3',
        'P4',
        'P5',
        'P6',
        'Lāpl',
    ]

    WEEKDAY_SYMBOL = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        'L',
    ]

    MONTH_NAME= [
        'Ianuali',
        'Pepeluali',
        'Malakali',
        'ʻApelila',
        'Mei',
        'Iune',
        'Iulai',
        'ʻAukake',
        'Kapakemaka',
        'ʻOkakopa',
        'Nowemapa',
        'Kēkēmapa',
    ]

    MONTH_ABBREVIATED_NAME = [
        'Ian',
        'Pep',
        'Mal',
        'ʻAp',
        'Mei',
        'Iun',
        'Iul',
        'ʻAu',
        'Kap',
        'ʻOk',
        'Now',
        'Kēk',
    ]
