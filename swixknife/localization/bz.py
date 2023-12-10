

__all__ = ('SezimalLocaleBZ',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleBZ(SezimalLocale):
    LANG = 'bz'
    LANGUAGE = 'brazileru'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

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

    HOLIDAYS = [
        #
        # Moving Holidays
        # Using fixed Easter day according to Symmetry454 original proposal
        #
        ('EASTER-120', '\ufe0f🎉🎭 Karnavaw'),
        ('EASTER-115', '\ufe0f🎉🎭 Karnavaw'),
        ('EASTER-114', '\ufe0f🎉🎭 Kwarta-fera di Sinzas'),
        ('EASTER-2',   '\ufe0f🕆 🥀 Paxawn di Kristu'),
        ('EASTER',     '\ufe0f🐣🌱 Paskwa'),
        ('EASTER+140', '\ufe0f🥖🍷 Corpus Christi'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('01-01', '\ufe0f🕊️ 🌎 Konfraternizasawn Universaw'),
        ('05-01', '\ufe0f🐝🐜 Dia du Trabalyu'),
        ('14-20', '\ufe0f⛪👸🏿 Nòsa Seỹòra Aparesida'),
        ('15-02', '\ufe0f🪦🕊️  Finadus'),
        ('20-40', '\ufe0f🥂🍽️  Véspera di Nataw'),
        ('20-41', '\ufe0f🌟👼🏼 Nataw'),
        ('20-55', '\ufe0f🍾🎆 Véspera di Anu Novu'),

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
        # ('13_0332-04-32', '\ufe0f🇧🇷🔺 Tiradentis'),                 # sábadu  13_0332-04-32 ~ 1792-04-21_dec
        # ('13_1124-11-10', '\ufe0f🪖📜 Revolusawn di 1932 (3̇1̇4̈)'),   # sábadu  13_1124-11-10 ~ 1932-07-09_dec
        # ('13_0422-13-10', '\ufe0f🇧🇷🕊️  Independensya du Braziw'),   # sábadu  13_0422-13-10 ~ 1822-09-07_dec
        # ('13_1013-15-31', '\ufe0f🇧🇷📜 Proklamasawn da Repúblika'),  # sesta   13_1013-15-31 ~ 1889-11-15_dec
        # ('13_0051-15-33', '\ufe0f👨🏿 Konsiensya Negra'),             # domingu 13_0051-15-33 ~ 1695-11-20_dec

        ('13_0332-04-33', '\ufe0f🇧🇷🔺 Tiradentis'),                      # domingu, 04-33 ~ 04-21_dec
        ('13_1124-11-13', '\ufe0f🪖📜 Revolusawn di 1932 (3̇1̇4̈) (#i)'),   # tersa,   11-13 ~ 07-09_dec
        ('13_0422-13-11', '\ufe0f🇧🇷🕊️  Independensya du Braziw (#i)'),   # domingu, 13-11 ~ 09-07_dec
        ('13_1013-15-23', '\ufe0f🇧🇷📜 Proklamasawn da Repúblika (#i)'),  # segunda, 15-23 ~ 11-15_dec
        ('13_0051-15-32', '\ufe0f👨🏿 Konsiensya Negra'),                  # sábadu,  15-32 ~ 11-20_dec
    ]

    HOLIDAYS_OTHER_CALENDAR = [
        #
        # Moving Holidays
        #
        ('ISO-EASTER-120', '\ufe0f🎉🎭 Karnavaw (%d/%m)'),
        ('ISO-EASTER-115', '\ufe0f🎉🎭 Karnavaw (%d/%m)'),
        ('ISO-EASTER-114', '\ufe0f🎉🎭 Kwarta-fera di Sinzas (%d/%m)'),
        ('ISO-EASTER-2',   '\ufe0f🕆 🥀 Payxawn di Kristu (%d/%m)'),
        ('ISO-EASTER',     '\ufe0f🐣🌱 Paskwa (%d/%m)'),
        ('ISO-EASTER+140', '\ufe0f🥖🍷 Corpus Christi (%d/%m)'),

        #
        # National Holidays
        # that (usually) don’t have a year of reference
        #
        ('ISO-01-01', '\ufe0f🕊️ 🌎 Konfraternizasawn Universaw (%d/%m)'),
        ('ISO-05-01', '\ufe0f🐝🐜 Dia du Trabalyu (%d/%m)'),
        ('ISO-10-12', '\ufe0f⛪👸🏿 Nòsa Seỹòra Aparesida (%d/%m)'),
        ('ISO-11-02', '\ufe0f🪦🕊️  Finadus (%d/%m)'),
        ('ISO-12-24', '\ufe0f🥂🍽️  Véspera di Nataw (%d/%m)'),
        ('ISO-12-25', '\ufe0f🌟👼🏼 Nataw (%d/%m)'),
        ('ISO-12-31', '\ufe0f🍾🎆 Véspera di Anu Novu (%d/%m)'),

        #
        # National Holidays
        # that have a year of reference
        #
        # When informing the year, the age is calculated,
        # and can be shown using %i as a format tag
        # Also, the original date in the original calendar can also be shown,
        # using the tags %Y, %m and %d for year, month and day, respectively
        #
        ('ISO-1792-04-21', '\ufe0f🇧🇷🔺 Tiradentis (%d/%m)'),                      # sábadu  13_0332-04-32 ~ 1792-04-21_dec
        ('ISO-1932-07-09', '\ufe0f🪖📜 Revolusawn di 1932 (3̇1̇4̈) (%d/%m - %i)'),   # sábadu  13_1124-11-10 ~ 1932-07-09_dec
        ('ISO-1822-09-07', '\ufe0f🇧🇷🕊️  Independensya du Braziw (%d/%m - %i)'),   # sábadu  13_0422-13-10 ~ 1822-09-07_dec
        ('ISO-1889-11-15', '\ufe0f🇧🇷📜 Proklamasawn da Repúblika (%d/%m - %i)'),  # sesta   13_1013-15-31 ~ 1889-11-15_dec
        ('ISO-1695-11-20', '\ufe0f👨🏿 Konsiensya Negra (%d/%m)'),                  # domingu 13_0051-15-33 ~ 1695-11-20_dec
    ]

    WEEKDAY_ERROR = 'Dia da semana inválidu {weekday}'
    MONTH_ERROR = 'Mez inválidu {month}'

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
