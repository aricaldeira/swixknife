

__all__ = ('SezimalLocaleSW_TRADITIONAL',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger

from .sw import SezimalLocaleSW


class SezimalLocaleSW_TRADITIONAL(SezimalLocaleSW):
    LANG = 'sw'
    LANGUAGE = 'Kiswahili'

    MONTH_NAME= [
        'Mwezi wa kwanza',
        'Mwezi wa pili',
        'Mwezi wa tatu',
        'Mwezi wa nne',
        'Mwezi wa tano',
        'Mwezi wa sita',
        'Mwezi wa saba',
        'Mwezi wa nane',
        'Mwezi wa tisa',
        'Mwezi wa kumi',
        'Mwezi wa moja',
        'Mwezi wa mbili',
    ]

    MONTH_ABBREVIATED_NAME = [
        'M01',
        'M02',
        'M03',
        'M04',
        'M05',
        'M10',
        'M11',
        'M12',
        'M13',
        'M14',
        'M15',
        'M20',
    ]
