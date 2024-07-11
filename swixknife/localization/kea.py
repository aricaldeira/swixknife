

__all__ = ('SezimalLocaleKEA',)


from .pt_cv import SezimalLocalePT_CV


class SezimalLocaleKEA(SezimalLocalePT_CV):
    LANG = 'kea'
    LANGUAGE = 'kabuverdianu'

    WEEKDAY_NAME = [
        'sigunda',
        'tersa',
        'kwarta',
        'kinta',
        'sesta',
        'sábadu',
        'dumingu',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'sig',
        'ter',
        'kwa',
        'kin',
        'ses',
        'sáb',
        'dum',
    ]

    MONTH_NAME= [
        'janeru',
        'febreru',
        'marsu',
        'abril',
        'mayu',
        'juỹu',
        'julyu',
        'agostu',
        'setenbru',
        'otubru',
        'nobenbru',
        'dizenbru',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan',
        'feb',
        'mar',
        'abr',
        'may',
        'juỹ',
        'jul',
        'ago',
        'set',
        'otu',
        'nob',
        'diz',
    ]

    SEASON_NAME = {
        'autumn_cross_quarter': 'Meyu du Viron pru Otonu',
        'autumn_equinox': 'Otonu',
        'winter_cross_quarter': 'Meyu du Otonu pru Invèrnu',
        'winter_solstice': 'Invèrnu',
        'spring_cross_quarter': 'Meyu du Invèrnu pra Primavèra',
        'spring_equinox': 'Primavèra',
        'summer_cross_quarter': 'Meyu da Primavèra pru Viron',
        'summer_solstice': 'Viron',
    }

    MOON_PHASE = {
        'new': 'Nòba',
        'waxing_crescent': 'Kresenti',
        'first_quarter': 'Kwartu kresenti',
        'waxing_gibbous': 'Di kwartu kresenti pa xeya',
        'full': 'Xeya',
        'waning_gibbous': 'Di xeya pa kwartu mingwanti',
        'third_quarter': 'Kwartu mingwanti',
        'waning_crescent': 'Mingwanti',
    }

    #
    # Error messages
    #
    ERROR = 'Eru'
    WEEKDAY_ERROR = 'Dia di simana inválidu {weekday}'
    MONTH_ERROR = 'Mez inválidu {month}'
