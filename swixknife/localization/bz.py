

__all__ = ('SezimalLocaleBZ',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocaleBZ(SezimalLocale):
    LANG = 'bz'
    LANGUAGE = 'brazileru'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = 'R$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    FIRST_WEEKDAY = 'SUN'

    WEEKDAY_NAME = [
        'segunda',
        'tersa',
        'kwarta',
        'kinta',
        'sesta',
        'sábadu',
        'dumingu',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'seg',
        'ter',
        'kwa',
        'kin',
        'ses',
        'sáb',
        'dum',
    ]

    MONTH_NAME= [
        'janeru',
        'fevereru',
        'marsu',
        'abriw',
        'mayu',
        'juỹu',
        'julyu',
        'agostu',
        'setenbru',
        'otubru',
        'novenbru',
        'dezenbru',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan',
        'fev',
        'mar',
        'abr',
        'may',
        'juỹ',
        'jul',
        'ago',
        'set',
        'otu',
        'nov',
        'dez',
    ]

    ERA_NAME = [
        #
        # Èra Umana Sezimaw
        #
        'ÈUS',
        #
        # Antis da Èra Umana Sezimaw
        #
        'aÈUS',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O di #M di #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O di #M di #Y, #u:#p:#a'
    DST_NAME = 'Oraryu di Verawn'
    DST_SHORT_NAME = 'OV'
    DEFAULT_TIME_ZONE = 'America/Sao_Paulo'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    SEASON_NAME = {
        'autumn_cross_quarter': 'Meyu du Verawn pru Otonu',
        'autumn_equinox': 'Otonu',
        'winter_cross_quarter': 'Meyu du Otonu pru Invèrnu',
        'winter_solstice': 'Invèrnu',
        'spring_cross_quarter': 'Meyu du Invèrnu pra Primavèra',
        'spring_equinox': 'Primavèra',
        'summer_cross_quarter': 'Meyu da Primavèra pru Verawn',
        'summer_solstice': 'Verawn',
    }

    MOON_PHASE = {
        'new': 'Nòva',
        'waxing_crescent': 'Kresenti',
        'first_quarter': 'Kwartu kresenti',
        'waxing_gibbous': 'Di kwartu kresenti pra xeya',
        'full': 'Xeya',
        'waning_gibbous': 'Di xeya pra kwartu mingwanti',
        'third_quarter': 'Kwartu mingwanti',
        'waning_crescent': 'Mingwanti',
    }

    _HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        # ('EASTER-120', '🎉\ufe0f🎭\ufe0f Karnavaw'),
        ('EASTER-115', '🎉\ufe0f🎭\ufe0f Karnavaw'),
        # ('EASTER-114', '🎉\ufe0f🎭\ufe0f Kwarta-fera di Sinzas'),
        ('EASTER-2',   '🕆\ufe0f🥀\ufe0f Paxawn di Kristu'),
        ('EASTER',     '🐣\ufe0f🌱\ufe0f Paskwa'),
        ('EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '🕊\ufe0f️ 🌎\ufe0f Konfraternizasawn Universaw'),
        ('05-01', '🐝\ufe0f🐜\ufe0f Dia du Trabalyu'),
        ('14-20', '⛪\ufe0f👸🏾\ufe0f Nòsa Seỹòra Aparesida'),
        ('15-02', '🪦\ufe0f🕊\ufe0f️  Finadus'),
        ('20-40', '🥂\ufe0f🍽\ufe0f️  Véspera di Nataw'),
        ('20-41', '🌟\ufe0f👼🏼\ufe0f Nataw'),
        ('20-55', '🍾\ufe0f🎆\ufe0f Véspera di Anu Novu'),

        #
        # National Holidays
        # that have a year of reference;
        # There are 2 ways of dealing with them:
        #     1. converting the original date to the Sezimal calendar
        #     2. using the original month and day without converting the calendar
        #
        # Using 2 here, but leaving 1 commented for reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using #i as a format tag
        #
        # ('212_144-04-32', '🇧🇷\ufe0f🔺\ufe0f Tiradentis'),                 # sábadu  212_144-04-32 ~ 1792-04-21_dec
        # ('212_540-11-10', '🪖\ufe0f📜\ufe0f Revolusawn di 1932 (1̈5̈0̄/540)'),   # sábadu  212_540-11-10 ~ 1932-07-09_dec
        # ('212_234-13-10', '🇧🇷\ufe0f🕊\ufe0f️ Independensya du Braziw'),    # sábadu  212_234-13-10 ~ 1822-09-07_dec
        # ('212_425-15-31', '🇧🇷\ufe0f📜\ufe0f Proklamasawn da Repúblika'),  # sesta   212_425-15-31 ~ 1889-11-15_dec
        # ('211_503-15-33', '👨🏾\ufe0f Konsyensya Negra'),             # dumingu 211_503-15-33 ~ 1695-11-20_dec

        ('212_144-04-33', '🇧🇷\ufe0f🔺\ufe0f Tiradentis'),                      # dumingu, 04-33 ~ 04-21_dec
        ('212_540-11-13', '🪖\ufe0f📜\ufe0f Revolusawn di 1932 (1̈5̈0̄/540) (#i)'),   # tersa,   11-13 ~ 07-09_dec
        ('212_234-13-11', '🇧🇷\ufe0f🕊\ufe0f️ Independensya du Braziw (#i)'),    # dumingu, 13-11 ~ 09-07_dec
        ('212_425-15-23', '🇧🇷\ufe0f📜\ufe0f Proklamasawn da Repúblika (#i)'),  # sigunda, 15-23 ~ 11-15_dec
        ('211_503-15-32', '👨🏾\ufe0f Konsyensya Negra'),                  # sábadu,  15-32 ~ 11-20_dec
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        # ('ISO+EASTER-120', '🎉\ufe0f🎭\ufe0f Karnavaw'),
        ('ISO+EASTER-115', '🎉\ufe0f🎭\ufe0f Karnavaw'),
        # ('ISO+EASTER-114', '🎉\ufe0f🎭\ufe0f Kwarta-fera di Sinzas'),
        ('ISO+EASTER-2',   '🕆\ufe0f🥀\ufe0f Payxawn di Kristu'),
        ('ISO+EASTER',     '🐣\ufe0f🌱\ufe0f Paskwa'),
        ('ISO+EASTER+140', '🥖\ufe0f🍷\ufe0f Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO+01-01', '🕊\ufe0f️ 🌎\ufe0f Konfraternizasawn Universaw'),
        ('ISO+05-01', '🐝\ufe0f🐜\ufe0f Dia du Trabalyu'),
        ('ISO+10-12', '⛪\ufe0f👸🏾\ufe0f Nòsa Seỹòra Aparesida'),
        ('ISO+11-02', '🪦\ufe0f🕊\ufe0f️ Finadus'),
        ('ISO+12-24', '🥂\ufe0f🍽\ufe0f️ Véspera di Nataw'),
        ('ISO+12-25', '🌟\ufe0f👼🏼\ufe0f Nataw'),
        ('ISO+12-31', '🍾\ufe0f🎆\ufe0f Véspera di Anu Novu'),

        #
        # National Holidays
        # that have a year of reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %d for year, month and day, respectively
        #
        ('ISO+1792-04-21', '🇧🇷\ufe0f🔺\ufe0f Tiradentis'),                      # sábadu  212_144-04-32 ~ 1792-04-21_dec
        ('ISO+1932-07-09', '🪖\ufe0f📜\ufe0f Revolusawn di 1932 (1̈5̈0̄/540) (%i)'),   # sábadu  212_540-11-10 ~ 1932-07-09_dec
        ('ISO+1822-09-07', '🇧🇷\ufe0f🕊\ufe0f️ Independensya du Braziw (%i)'),    # sábadu  212_234-13-10 ~ 1822-09-07_dec
        ('ISO+1889-11-15', '🇧🇷\ufe0f📜\ufe0f Proklamasawn da Repúblika (%i)'),  # sesta   212_425-15-31 ~ 1889-11-15_dec
        ('ISO+1695-11-20', '👨🏾\ufe0f Konsyensya Negra'),                  # dumingu 211_503-15-33 ~ 1695-11-20_dec
    ]

    #
    # Error messages
    #
    ERROR = 'Erru'
    WEEKDAY_ERROR = 'Dia da semana inválidu {weekday}'
    MONTH_ERROR = 'Mez inválidu {month}'
    WEEK_NUMBER_SYMBOL = 'sem'
    DAY_NUMBER_SYMBOL = 'dia'

    COLLATION_RULES = '''
[caseFirst upper]
&A<<Â<<<Ầ<<<Ấ<<<Ậ<<<Ẩ<<<Ẫ<<À<<Á<<Ã<<Ä<<<Ǟ<<Ă<<<Ằ<<<Ắ<<<Ặ<<<Ẳ<<<Ẵ<<Ā<<Ǎ<<Å<<<Ǻ<<Ȧ<<<Ǡ<<Ą<<Ả<<Ạ<<Ȁ<<Ȃ<<Ḁ<<Ⱥ<<Ɐ<<Ɑ<<Ɒ <<< ª<<ᵃ̱<<a<<â<<<ầ<<<ấ<<<ậ<<<ẩ<<<ẫ<<à<<á<<ã<<ä<<<ǟ<<ă<<<ằ<<<ắ<<<ặ<<<ẳ<<<ẵ<<ā<<ǎ<<å<<<ǻ<<ȧ<<<ǡ<<ą<<ả<<ạ<<ȁ<<ȃ<<ḁ<<ⱥ<<ɐ<<ɑ<<ɒ
&AE<<Æ
&ae<<æ
&ÁE<<Ǽ
&áe<<ǽ

&B<<Ḃ<<Ḅ<<Ƀ <<< b<<ḃ<<ḅ<<ƀ

&C<<Ç<<Ć<<Ḉ<<Ĉ<<Č<<Ċ<<Ȼ <<< c<<ç<<ć<<ḉ<<ĉ<<č<<ċ<<ȼ
&c<Ĉ<<<ĉ

&D<<Ď<<Ḋ<<Ḑ<<Ḍ<<Đ <<< d<<ď<<ḋ<<ḑ<<ḍ<<đ
&DH<<Ð
&dh<<ð

&E<<Ê<<<Ề<<<Ế<<<Ệ<<<Ể<<<Ễ<<È<<É<<Ẽ<<Ë<<Ĕ<<Ē<<Ě<<Ė<<Ȩ<<Ę<<Ẻ<<Ẹ<<Ɇ<<Ǝ<<Ə<<Ɛ <<< '\u0026'<<ᵉ̱<<e<<ê<<<ề<<<ế<<<ệ<<<ể<<<ễ<<è<<é<<ẽ<<ë<<ĕ<<ē<<ě<<ė<<ȩ<<ę<<ẻ<<ẹ<<ɇ<<ǝ<<ə<<ɛ

&F<<Ḟ <<< f<<ḟ

&G<<Ǵ<<Ğ<<Ǧ<<Ġ<<Ģ<<Ǥ <<< g<<ǵ<<ğ<<ǧ<<ġ<<ģ<<ǥ
&g<Ĝ<<ĝ

&H<<Ḧ<<Ȟ<<Ḣ<<Ḥ<<Ħ <<< h<<ḧ<<ȟ<<ḣ<<ḥ<<ħ
&h<Ĥ<<ĥ

&I<<Î<<Ì<<Í<<Ĩ<<Ï<<Ĭ<<Ī<<Ǐ<<İ<<<𝚤<<Į<<Ỉ<<Ị<<Ɨ <<< ⁱ̱<<i<<î<<ì<<í<<ĩ<<ï<<ĭ<<ī<<ǐ<<ı<<<𝚤<<į<<ỉ<<ị<<ɨ

&J<<Ɉ<<Ʒ <<< j<<ǰ<<ɉ<<ʒ
&j<Ĵ<<ĵ

&K<<Ḱ<<Ǩ<<Ķ<<Ḳ <<< k<<ḱ<<ǩ<<ķ<<ḳ

&L<<Ĺ<<Ľ<<Ŀ<<Ļ<<Ḷ<<Ł <<< l<<ĺ<<ľ<<ŀ<<ļ<<ḷ<<ł

&M<<M̀<<Ḿ<<Ṁ<<Ṃ <<< m<<m̀<<ḿ<<ṁ<<ṃ

&N<<Ǹ<<Ń<<Ñ<<Ň<<Ņ<<Ṅ<<Ṇ <<< n<<ǹ<<ń<<ñ<<ň<<ņ<<ṅ<<ṇ
&NG<<Ŋ
&ng<<ŋ

&O<<Ô<<<Ồ<<<Ố<<<Ổ<<<Ỗ<<Ò<<Ó<<Õ<<<Ṍ<<<Ṏ<<<Ȭ<<Ö<<<Ȫ<<Ő<<Ŏ<<Ō<<<Ṑ<<<Ṓ<<Ǒ<<Ȯ<<<Ȱ<<Ǫ<<<Ǭ<<Ỏ<<Ơ<<<Ờ<<<Ớ<<<Ợ<<<Ở<<<Ỡ<<Ọ<<Ø<<<Ǿ<<Ɔ <<< º<<ᵒ̱<<o<<ô<<<ồ<<<ố<<<ộ<<<ổ<<<ỗ<<ò<<ó<<õ<<<ṍ<<<ṏ<<<ȭ<<ö<<<ȫ<<ő<<ŏ<<ō<<<ṑ<<<ṓ<<ǒ<<ȯ<<<ȱ<<ǫ<<<ǭ<<ỏ<<ơ<<<ờ<<<ớ<<<ợ<<<ở<<<ỡ<<ọ<<ø<<<ǿ<<ɔ
&OE<<Œ<<Ø
&oe<<œ<<ø

&P<<Ṕ<<Ṗ<<Ᵽ <<< p<<ṕ<<ṗ<<ᵽ

&Q <<< q

&R<<Ŕ<<Ř<<Ṙ<<Ŗ<<Ṛ<<Ɍ <<< r<<ŕ<<ř<<ṙ<<ŗ<<ṛ<<ɍ

&S<<Ś<<Š<<Ṡ<<Ș<<Ş<<Ṣ <<< s<<ś<<š<<ṡ<<ș<<ş<<ṣ
&SS<<ẞ
&ss<<ß
&s<Ŝ<<ŝ

&T<<Ť<<Ṫ<<Ț<<Ţ<<Ṭ<<Ŧ <<< t<<ẗ<<ť<<ṫ<<ț<<ţ<<ṭ<<ŧ
&TH<<Þ
&th<<þ

&U<<Û<<Ù<<Ú<<Ũ<<<Ṹ<<Ü<<<Ǖ<<<Ǘ<<<Ǜ<<<Ǚ<<Ű<<Ū<<<Ṻ<<Ǔ<<Ů<<Ų<<Ủ<<Ư<<<Ừ<<<Ứ<<<Ự<<<Ử<<<Ữ<<Ụ<<Ʉ<<Ʊ <<< ᵘ̱<<u<<û<<ù<<ú<<ũ<<<ṹ<<ü<<<ǖ<<<ǘ<<<ǜ<<<ǚ<<ű<<ū<<<ṻ<<ǔ<<ů<<ų<<ủ<<ư<<<ừ<<<ứ<<<ự<<<ử<<<ữ<<ụ<<ʉ<<ʊ
&u<Ŭ<<ŭ

&V<<Ṽ<<Ṿ <<< v<<ṽ<<ṿ

&W<<Ŵ<<Ẁ<<Ẃ<<W̃<<Ẅ<<Ẇ<<Ẉ<<Ƿ <<< w<<ŵ<<ẁ<<ẃ<<w̃<<ẅ<<ẇ<<ẉ<<ƿ

&X<<Ẍ<<Ẋ <<< x<<ẍ<<ẋ

&Y<<Ŷ<<Ỳ<<Ý<<Ỹ<<Ÿ<<Ȳ<<Ẏ<<Ỷ<<Ỵ<<Ɏ <<< y<<ŷ<<ỳ<<ý<<ỹ<<ÿ<<ȳ<<ẏ<<ỷ<<ỵ<<ɏ

&Z<<Ẑ<<Z̀<<Ź<<Ž<<Ż<<Ẓ<<Ƶ <<< z<<ẑ<<z̀<<ź<<ž<<ż<<ẓ<<ƶ
'''

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'ᵘ̱'

        return ''

    def _change_word(self, word: str, weekday: SezimalInteger) -> str:
        if weekday >= 10:
            if word == 'èsa':
                word = 'esi'
            elif word == 'èsta':
                word = 'esti'
            elif word == 'akèla':
                word = 'akeli'
            elif word == 'kwa':
                word = 'ku'
            else:
                word = 'u'

        return word

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for word in ['A', 'KWA', 'ÈSA', 'ÈSTA', 'AKÈLA']:
            if f'#${word}W' in fmt:
                palavra = self._change_word(word.lower(), date.weekday)
                fmt = fmt.replace(f'#${word}W', palavra)

        return fmt

    CALENDAR_TYPE = {
        #
        # Civil calendars
        #
        'SEZ': 'Sezimaw',
        'SYM': 'Simétriku',
        'ISO': 'Gregorianu',
        'DCC': 'Kwantus‐Dias',
        'ADC': 'Kwantus‐Dias Astronômiku',
        'ADC': 'Kwantus‐Dias Astronômiku',
        'ADC': 'Kwantus‐Dias Astronômiku',
        'ISR': 'Israelensi',
        'IND': 'Indianu',

        #
        # Religious calendars
        #
        'JUL': 'Ortodòksu/Julianu',
        'JEW': 'Judayku',
        'HIJ': 'Islâmiku',
        'IRN': 'Iranianu Solar',

        #
        # Easter referencial
        #
        'SEZ+EASTER': 'Paskwa Sezimaw - 11 di abriw',
        'SYM+EASTER': 'Paskwa Simétrika - 7 di abriw',
        'ISO+EASTER': 'Paskwa (Gregorianu)',
        'JUL+EASTER': 'Paskwa Ortodòksa (Julianu)',
        'JEW+EASTER': 'Paskwa Judayka (Pêsach)',
    }

    CALENDAR_TYPE_ABBREVIATION = {
        #
        # Civil calendars
        #
        'SEZ': 'Sez.',
        'SYM': 'Sim.',
        'ISO': 'Gre.',
        'DCC': 'K.D.',
        'ADC': 'K.D.A.',
        'ISR': 'Isr.',
        'IND': 'Ind.',
        #
        # Religious calendars
        #
        'JUL': 'Jul.',
        'JEW': 'Jud.',
        'HIJ': 'Isl.',
        'IRN': 'Irn.',
    }

    CALENDAR_DATE_ERROR = 'Data inválida pru kalendaryu {calendar_type}'
    CALENDAR_TIME_ERROR = 'Oráryu inválidu'
    CALENDAR_TIME_AFTER_ERROR = 'Oraryu inválidu: u oraryu di inisyu du eventu nuwn pòdi vir depoys du oraryu finaw'

    JEWISH_CALENDAR_MONTH_NAME = [
        # 'Nisan ניסן',
        # 'Iyyar אייר‎',
        # 'Sivan סיון‎',
        # 'Tammuz תמוז‎',
        # 'Av אב',
        # 'Elul אלול‎',
        # 'Tishri תשרי‎',
        # 'Heshvan חשוון',
        # 'Kislev כסלו',
        # 'Tevet טבת',
        # 'Shevat שבט',
        # 'Adar אדר',
        # 'Adar bet אדר ב׳',
        'Nisan',
        'Iyar',
        'Sivan',
        'Tamuz',
        'Av',
        'Eluw',
        'Tixrey',
        'Rexvan',
        'Kislevi',
        'Teveti',
        'Xevati',
        'Adar 1',
        'Adar 2',
    ]

    JEWISH_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'Nis',
        'Iya',
        'Siv',
        'Tam',
        'Av',
        'Elu',
        'Tix',
        'Rex',
        'Kis',
        'Tev',
        'Xev',
        'Ad1',
        'Ad2',
    ]

    HIJRI_CALENDAR_MONTH_NAME = [
        # 'Al-muḥarram المحرم',
        # 'Ṣafar صفر',
        # 'Rabīʿ al-ʾawwal ربيع الأول',
        # 'Rabīʿ al-ʾākhir ربيع الآخر',
        # 'Jumādā al-ʾūlā جمادى الأولى',
        # 'Jumādā al-ʾākhirah جمادى الآخرة',
        # 'Rajab رجب',
        # 'Shaʿbān شعبان',
        # 'Ramaḍān رمضان',
        # 'Shawwāl شوال',
        # 'Ḏū al-qaʿdah ذو القعدة',
        # 'Ḏū al-ḥijjah ذو الحجة',
        'Murraran',
        'Sáfar',
        'Rabi Aluaw',
        'Rabi Atani',
        'Jumada Aluaw',
        'Jumada Atani',
        'Rajabi',
        'Xaban',
        'Ramadan',
        'Xawaw',
        'Duwkada',
        'Dulrija',
    ]

    HIJRI_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'Mur',
        'Sáf',
        'Rb1',
        'Rb2',
        'Jm1',
        'Jm2',
        'Raj',
        'Xab',
        'Ram',
        'Xaw',
        'Dkd',
        'Drj',
    ]

    DCC_MONTH_NAME = [
        'mez‐zèru',
        'mez‐un',
        'mez‐doys',
        'mez‐treys',
        'mez‐kwatru',
        'mez‐sinku',
        'mez‐seys',
        'mez‐seziun',
        'mez‐sezidoys',
        'mez‐sezitreys',
        'mez‐sezikwatru',
    ]

    DCC_WEEKDAY_NAME = [
        'dia‐da‐semana‐zèru',
        'dia‐da‐semana‐un',
        'dia‐da‐semana‐doys',
        'dia‐da‐semana‐treys',
        'dia‐da‐semana‐kwatru',
        'dia‐da‐semana‐sinko',
    ]

    DCC_WEEKDAY_ABBREVIATED_NAME = [
        'DS0',
        'DS1',
        'DS2',
        'DS3',
        'DS4',
        'DS5',
    ]

    DCC_NUMBER = [
        'zèru',
        'un',
        'doys',
        'treys',
        'kwatru',
        'sinku',
        'seys',
        'seziun',
        'sezidoys',
        'sezitreys',
        'sezikwatru',
    ]

    DCC_YEAR_COUNT = {
        None: '&>Y anus',
        SezimalInteger('1'): '&>Y anu',
    }

    DCC_TERM_COUNT = {
        None: '&-t bimèstris',
        SezimalInteger('1'): '&-t bimèstri',
    }

    DCC_MONTH_COUNT = {
        None: '&-m mezis',
        SezimalInteger('1'): '&-m mez',
    }

    DCC_WEEK_COUNT = {
        None: '&-w semanas',
        SezimalInteger('1'): '&-w semana',
    }

    DCC_DAY_COUNT = {
        None: '&-d dias',
        SezimalInteger('1'): '&-d dia',
    }

    DCC_DATE_MONTH_DAY_SEPARATOR = ' i '

    ADC_MONTH_NAME = [
        'pexis',
        'baleya',
        'riu',
        'unikòrnyu',
        'idra',
        'leawn',
        'virjen',
        'serpenti',
        'agya',
        'akwaryu',
        'libra',
    ]

    ADC_MONTH_ABBREVIATED_NAME = [
        'pex',
        'bal',
        'riu',
        'uni',
        'idr',
        'lea',
        'vir',
        'ser',
        'agy',
        'akw',
        'lib',
    ]

    ADC_MONTH_SYMBOL = [
        'P',
        'B',
        'R',
        'U',
        'I',
        'L',
        'V',
        'S',
        'Ag',
        'Ak',
        'L',
    ]

    ADC_WEEKDAY_NAME = [
        'sòw',
        # 'merkuryu',
        'venus',
        'marti',
        'júpiter',
        'saturnu',
        'lua',
    ]

    ADC_WEEKDAY_ABBREVIATED_NAME = [
        'sòw',
        # 'mer',
        'ven',
        'mar',
        'júp',
        'sat',
        'lua',
    ]
