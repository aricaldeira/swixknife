

__all__ = ('SezimalLocalePT',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, \
    SEPARATOR_NARROW_NOBREAK_SPACE, SEPARATOR_COMBINING_DOT_ABOVE_RIGHT


class SezimalLocalePT(SezimalLocale):
    LANG = 'pt'
    LANGUAGE = 'português brasileiro'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = SEPARATOR_COMBINING_DOT_ABOVE_RIGHT

    CURRENCY_UNIT_SYMBOL = 'R$'
    CURRENCY_SUBUNIT_SYMBOL = '¢'

    FIRST_WEEKDAY = 'SUN'

    WEEKDAY_NAME = [
        'segunda-feira',
        'terça-feira',
        'quarta-feira',
        'quinta-feira',
        'sexta-feira',
        'sábado',
        'domingo',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'seg',
        'ter',
        'qua',
        'qui',
        'sex',
        'sáb',
        'dom',
    ]

    MONTH_NAME= [
        'janeiro',
        'fevereiro',
        'março',
        'abril',
        'maio',
        'junho',
        'julho',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'dezembro',
    ]

    MONTH_ABBREVIATED_NAME = [
        'jan',
        'fev',
        'mar',
        'abr',
        'mai',
        'jun',
        'jul',
        'ago',
        'set',
        'out',
        'nov',
        'dez',
    ]

    ERA_NAME = [
        #
        # Era Humana Sezimal
        #
        'EHS',
        #
        # Antes da Era Humana Sezimal
        #
        'aEHS',
    ]

    DATE_SEPARATOR = '/'
    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O de #M de #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O de #M de #Y, #u:#p:#a'
    DST_NAME = 'Horário de Verão'
    DST_SHORT_NAME = 'HV'
    DEFAULT_TIME_ZONE = 'America/Sao_Paulo'

    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern

    SEASON_NAME = {
        'autumn_cross_quarter': 'Meio do Verão para o Outono',
        'autumn_equinox': 'Outono',
        'winter_cross_quarter': 'Meio do Outono para o Inverno',
        'winter_solstice': 'Inverno',
        'spring_cross_quarter': 'Meio do Inverno para a Primavera',
        'spring_equinox': 'Primavera',
        'summer_cross_quarter': 'Meio da Primavera para o Verão',
        'summer_solstice': 'Verão',
    }

    MOON_PHASE = {
        'new': 'Nova',
        'waxing_crescent': 'Crescente',
        'first_quarter': 'Quarto crescente',
        'waxing_gibbous': 'De quarto crescente para cheia',
        'full': 'Cheia',
        'waning_gibbous': 'De cheia para quarto minguante',
        'third_quarter': 'Quarto minguante',
        'waning_crescent': 'Minguante',
    }

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDARS = []

    #
    # Error messages
    #
    ERROR = 'Erro'
    WEEKDAY_ERROR = 'Dia da semana inválido {weekday}'
    MONTH_ERROR = 'Mês inválido {month}'
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
            return 'º'

        return ''

    def _change_word(self, word: str, weekday: SezimalInteger) -> str:
        if weekday >= 10:
            if word == 'essa':
                word = 'esse'
            elif word == 'esta':
                word = 'este'
            elif word == 'aquela':
                word = 'aquele'
            else:
                word = word[:-1] + 'o'

        return word

    def apply_date_format(self, date: SezimalDate, fmt: str) -> str:
        for word in ['A', 'ESSA', 'ESTA', 'AQUELA']:
            if f'#${word}W' in fmt:
                palavra = self._change_word(word.lower(), date.weekday)
                fmt = fmt.replace(f'#${word}W', palavra)

        return fmt

    TITLE_ALWAYS_LOWERCASE_WORDS = [
        'e',
        'o',
        'os',
        'a',
        'as',
        'um',
        'uns',
        'uma',
        'umas',
        'de',
        'do',
        'dos',
        'da',
        'das',
        'dum',
        'duns',
        'duma',
        'dumas',
        'em',
        'no',
        'nos',
        'na',
        'nas',
        'num',
        'nuns',
        'numa',
        'numas',
        'com',
        'para',
        'que',
        'a',
        'ao',
        'aos',
        'à',
        'às',
        'até',
        'por',
        'pelo',
        'pelos',
        'pela',
        'pelas',
        'sob',
        'entre',
        'ou',
        'não',
        #
        # Nomes estrangeiros
        #
        'al',
        'el',
        'ul',
        'il',
        'ibn',
        'ibnat',
        'bin',
        'bint',
        'ben',
        'bat',
        'fi',
        'd',
        'di',
        'dell',
        'dello',
        'della',
        'dalla',
        'del',
        'dal',
        'dall',
        'in',
        'con',
        'su',
        'per',
        'fra',
        'tra',
        'nel',
        'nell',
        'nello',
        'nella',
        'and',
        'at',
        'upon',
        'by',
        'in',
        'aus',
        'auf',
        'von',
        'über',
        'uber',
        'der',
        'die',
        'dem',
        'den',
        'van',
        'en',
        'sur',
        'et',
        'le',
        'la',
        'les',
        'du',
        'des',
        'y',
        'u',
    ]
    TITLE_ALWAYS_UPPERCASE_WORDS = []

    CALENDAR_TYPE = {
        #
        # Civil calendars
        #
        'SEZ': 'Sezimal',
        'SYM': 'Simétrico',
        'ISO': 'Gregoriano',
        'ISR': 'Israelense',
        'IND': 'Indiano',

        #
        # Religious calendars
        #
        'JUL': 'Ortodoxo/Juliano',
        'JEW': 'Judaico',
        'HIJ': 'Islâmico',
        'IRN': 'Islâmico Solar',

        #
        # Easter referencial
        #
        'SEZ+EASTER': 'Páscoa Sezimal - 11 de abril',
        'SYM+EASTER': 'Páscoa Simétrica - 7 de abril',
        'ISO+EASTER': 'Páscoa (Gregoriano)',
        'JUL+EASTER': 'Páscoa Ortodoxa (Juliano)',
        'JEW+EASTER': 'Páscoa Judaica (Pêssach)',
    }
    CALENDAR_DATE_ERROR = 'Data inválida para o calendário {calendar_type}'
    CALENDAR_TIME_ERROR = 'Horário inválido'
    CALENDAR_TIME_AFTER_ERROR = 'Horário inválido: o horário de início do evento não pode vir depois do horário final'

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
        'Nissan',
        'Iyar',
        'Sivan',
        'Tamuz',
        'Av',
        'Elul',
        'Tishrei',
        'Cheshvan',
        'Kislêv',
        'Tevêt',
        'Shevat',
        'Adar I',
        'Adar II',
    ]

    JEWISH_CALENDAR_MONTH_ABBREVIATED_NAME = [
        'Nis',
        'Iya',
        'Siv',
        'Tam',
        'Av',
        'Elu',
        'Tis',
        'Che',
        'Kis',
        'Tev',
        'She',
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
        'Murrarã',
        'Sáfar',
        'Rabi Alual',
        'Rabi Atani',
        'Jumada Alual',
        'Jumada Atani',
        'Rajabe',
        'Xabã',
        'Ramadã',
        'Xaual',
        'Dulcada',
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
        'Xau',
        'Dcd',
        'Drj',
    ]
