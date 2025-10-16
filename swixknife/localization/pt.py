

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
    YEAR_TEXT_MONTH_FORMAT = '#M de #Y'

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
        'SEZ': 'Simétrico',
        'SYM': 'Simétrico',
        'ISO': 'Gregoriano',
        'DCC': 'Quantos‐Dias',
        'ADC': 'Quantos‐Dias Astronômico',
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
        # Páscoa referencial
        #
        'SEZ+EASTER': 'Páscoa Sezimal - 11 de abril',
        'SYM+EASTER': 'Páscoa Simétrica - 7 de abril',
        'ISO+EASTER': 'Páscoa (Gregoriano)',
        'JUL+EASTER': 'Páscoa Ortodoxa (Juliano)',
        'JEW+EASTER': 'Páscoa Judaica (Pêssach)',
    }

    CALENDAR_TYPE_ABBREVIATION = {
        #
        # Civil calendars
        #
        'SEZ': 'Sez.',
        'SYM': 'Sim.',
        'ISO': 'Gre.',
        'DCC': 'Q.D.',
        'ADC': 'Q.D.A.',
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

    CALENDAR_DATE_ERROR = 'Data inválida para o calendário {calendar_type}'
    CALENDAR_TIME_ERROR = 'Horário inválido'
    CALENDAR_TIME_AFTER_ERROR = 'Horário inválido: o horário de início do evento não pode vir depois do horário final'

    JEWISH_CALENDAR_ANNO_MUNDI = 'J.K.'

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

    HIJRI_CALENDAR_ANNO_HEGIRAE = 'I.K.'

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

    DCC_TERM_NAME = [
        'bimestre‐zero',
        'bimestre‐um',
        'bimestre‐dois',
        'bimestre‐três',
        'bimestre‐quatro',
    ]

    DCC_TERM_ABBREVIATED_NAME = [
        'B0',
        'B1',
        'B2',
        'B3',
        'B4',
    ]

    DCC_MONTH_NAME = [
        'mês‐zero',
        'mês‐um',
        'mês‐dois',
        'mês‐três',
        'mês‐quatro',
        'mês‐cinco',
        'mês‐seis',
        'mês‐seis‐e‐um',
        'mês‐seis‐e‐dois',
        'mês‐seis‐e‐três',
        'mês‐seis‐e‐quatro',
    ]

    DCC_WEEKDAY_NAME = [
        'dia‐da‐semana‐zero',
        'dia‐da‐semana‐um',
        'dia‐da‐semana‐dois',
        'dia‐da‐semana‐três',
        'dia‐da‐semana‐quatro',
        'dia‐da‐semana‐cinco',
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
        'zero',
        'um',
        'dois',
        'três',
        'quatro',
        'cinco',
        'seis',
        'seis‐e‐um',
        'seis‐e‐dois',
        'seis‐e‐três',
        'seis‐e‐quatro',
    ]

    DCC_YEAR_COUNT = {
        None: '&>Y anos',
        SezimalInteger('1'): '&>Y ano',
    }

    DCC_TERM_COUNT = {
        None: '&-t bimestres',
        SezimalInteger('1'): '&-t bimestre',
    }

    DCC_MONTH_COUNT = {
        None: '&-m meses',
        SezimalInteger('1'): '&-m mês',
    }

    DCC_WEEK_COUNT = {
        None: '&-wM semanas',
        SezimalInteger('1'): '&-wM semana',
    }

    DCC_WEEK_IN_YEAR_COUNT = {
        None: '&-wY semanas',
        SezimalInteger('1'): '&-wY semana',
    }

    DCC_DAY_COUNT = {
        None: '&-d dias',
        SezimalInteger('1'): '&-d dia',
    }

    DCC_DAY_IN_YEAR_COUNT = {
        None: '&-dY dias',
        SezimalInteger('1'): '&-dY dia',
    }

    DCC_DAY_IN_WEEK_COUNT = {
        None: '&-dW dias',
        SezimalInteger('1'): '&-dW dia',
    }

    DCC_DATE_MONTH_DAY_SEPARATOR = ' e '

    ADC_MONTH_NAME = [
        'Peixes',
        'Baleia',
        'Rio',
        'Unicórnio',
        'Hidra',
        'Leão',
        'Virgem',
        'Serpente',
        'Águia',
        'Aquário',
        # 'libra',
        # 'órion',
        'Sextante',
    ]

    ADC_MONTH_ABBREVIATED_NAME = [
        'Pei',
        'Bal',
        'Rio',
        'Uni',
        'Hid',
        'Leã',
        'Vir',
        'Ser',
        'Águ',
        'Aqu',
        # 'lib',
        # 'óri',
        'Sex',
    ]

    ADC_MONTH_SYMBOL = [
        'P',
        'B',
        'R',
        'U',
        'H',
        # 'le',
        'L',
        'V',
        'Sr',
        'Ág',
        'Aq',
        # 'lb',
        # 'ó',
        'Sx',
    ]

    ADC_WEEK_NAME = [
        'Espírito',
        'Fogo',
        'Ar',
        'Água',
        'Terra',
        'Corpo',
    ]

    ADC_WEEK_ABBREVIATED_NAME = [
        'Esp',
        'Fog',
        'Ar',
        'Águ',
        'Ter',
        'Cor',
    ]

    ADC_WEEK_SYMBOL = [
        'E',
        'F',
        'A',
        'Á',
        'T',
        'C',
    ]

    ADC_WEEKDAY_NAME = [
        'Sol',
        # 'mercúrio',
        'Vênus',
        'Marte',
        'Júpiter',
        'Saturno',
        'Lua',
    ]

    ADC_WEEKDAY_ABBREVIATED_NAME = [
        'Sol',
        # 'mer',
        'Vên',
        'Mar',
        'Júp',
        'Sat',
        'Lua',
    ]

    DCC_DATE_LONG_FORMAT_ON_DATE = '&󱹭>Y, mês &-m, dia &-d'
    DCC_DATE_LONG_FORMAT_ON_DATE_DAYS = '&󱹭>Y, dia &-dY'
    DCC_DATE_LONG_FORMAT_ON_DATE_WEEKS = '&󱹭>Y, semana &-wY, dia &-dW'
    DCC_DATE_LONG_FORMAT_ON_DATE_MONTHS_WEEKS = '&󱹭>Y, mês &-m, semana &-wM, dia &-dW'

    ADC_DATE_LONG_FORMAT_ON_DATE = '&󱹭>Y, mês &$DEM &cM, dia &-d'
    ADC_DATE_LONG_FORMAT_ON_DATE_WEEKDAY = '&󱹭>Y, mês &$DEM &cM, semana &$DEW &cW, dia &$DED &cD'

    _DE_DO_DA_MES = [
        'de',  # peixes
        'da',  # baleia
        'do',  # rio
        'do',  # unicórnio
        'da',  # hidra
        'do',  # leão
        'de',  # virgem
        'da',  # serpente
        'da',  # águia
        'de',  # aquário
        'do',  # sextante
    ]

    _DE_DO_DA_SEMANA = [
         'da',  # alma
         'do',  # fogo
         'do',  # ar
         'da',  # água
         'da',  # terra
         'do',  # corpo
    ]

    _DE_DO_DA_DIA_SEMANA = [
         'do',  # sol
         'de',  # vênus
         'de',  # marte
         'de',  # júpiter
         'de',  # saturno
         'da',  # lua
    ]

    def apply_dcc_date_format(self, date: SezimalDate, fmt: str) -> str:
        if f'&$DED' in fmt:
            fmt = fmt.replace(f'&$DED', self._DE_DO_DA_DIA_SEMANA[int(date.dcc_weekday)])

        if f'&$DEW' in fmt:
            fmt = fmt.replace(f'&$DEW', self._DE_DO_DA_SEMANA[int(date.dcc_week)])

        if f'&$DEM' in fmt:
            fmt = fmt.replace(f'&$DEM', self._DE_DO_DA_MES[int(date.dcc_month)])

        return fmt

    CHRISTIAN_HOLIDAYS = [
        ('CHR+01-01',     '🕆\ufe0f Santa Mãe de Deus'),
        ('CHR+01-06',     '🕆\ufe0f Epifania'),
        ('CHR+01-06+SUN', '🕆\ufe0f Batismo do Senhor'),
        # ('CHR+02-02',     '🕆\ufe0f Candelária'),
        # ('CHR+EASTER-124', '🕆\ufe0f Quinta-feira Gorda'),
        # ('CHR+EASTER-120', '🕆\ufe0f Segunda-feira Gorda'),
        ('CHR+EASTER-115', '🕆\ufe0f Terça-feira Gorda'),
        ('CHR+EASTER-114', '🕆\ufe0f Quarta-feira de Cinzas'),
        ('CHR+EASTER-11',  '🕆\ufe0f Domingo de Ramos'),
        # ('CHR+EASTER-4',   '🕆\ufe0f Quarta-feira Santa'),
        ('CHR+EASTER-3',   '🕆\ufe0f Quinta-feira Santa'),
        ('CHR+EASTER-2',   '🕆\ufe0f🥀\ufe0f Sexta-feira Santa'),
        ('CHR+EASTER-1',   '🕆\ufe0f Sábado Santo'),
        ('CHR+EASTER',     '🕆\ufe0f🐣\ufe0f🌱\ufe0f Páscoa'),
        # ('CHR+EASTER+1',   '🕆\ufe0f Segunda-feira de Páscoa'),
        ('CHR+EASTER+11',  '🕆\ufe0f Festa da Misericórdia'),
        ('CHR+EASTER+103', '🕆\ufe0f Ascensão do Senhor'),
        ('CHR+EASTER+121', '🕆\ufe0f Pentecostes'),
        # ('CHR+EASTER+122', '🕆\ufe0f Whit Monday'),
        ('CHR+EASTER+132', '🕆\ufe0f🛆 Santíssima Trindade'),
        ('CHR+EASTER+140', '🕆\ufe0f🥖\ufe0f🍷\ufe0f Corpus Christi'),
        ('CHR+11-01',      '🕆\ufe0f Todos os Santos'),
        ('CHR+11-02',      '🕆\ufe0f Finados'),
        ('CHR+12-25-SUN_4','🕆\ufe0f Advento'),
        ('CHR+12-25',      '🕆\ufe0f🌟\ufe0f👼🏼\ufe0f Natal'),

        ('CHR+SYM+01-01',     '🕆\ufe0f Santa Mãe de Deus #𝑠𝑖𝑚'),
        ('CHR+SYM+01-06',     '🕆\ufe0f Epifania #𝑠𝑖𝑚'),
        ('CHR+SYM+01-06+SUN', '🕆\ufe0f Batismo do Senhor #𝑠𝑖𝑚'),
        # ('CHR+SYM+02-02',     '🕆\ufe0f Candelária #𝑠𝑖𝑚'),
        # ('CHR+SYM+EASTER-124', '🕆\ufe0f Quinta-feira Gorda #𝑠𝑖𝑚'),
        # ('CHR+SYM+EASTER-120', '🕆\ufe0f Segunda-feira Gorda #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER-115', '🕆\ufe0f Terça-feira Gorda #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER-114', '🕆\ufe0f Quarta-feira de Cinzas #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER-11',  '🕆\ufe0f Domingo de Ramos #𝑠𝑖𝑚'),
        # ('CHR+SYM+EASTER-4',   '🕆\ufe0f Quarta-feira Santa #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER-3',   '🕆\ufe0f Quinta-feira Santa #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER-2',   '🕆\ufe0f🥀\ufe0f Sexta-feira Santa #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER-1',   '🕆\ufe0f Sábado Santo #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER',     '🕆\ufe0f🐣\ufe0f🌱\ufe0f Páscoa #𝑠𝑖𝑚'),
        # ('CHR+SYM+EASTER+1',   '🕆\ufe0f Segunda-feira de Páscoa #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER+11',  '🕆\ufe0f Festa da Misericórdia #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER+103', '🕆\ufe0f Ascensão do Senhor #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER+121', '🕆\ufe0f Pentecostes #𝑠𝑖𝑚'),
        # ('CHR+SYM+EASTER+122', '🕆\ufe0f Whit Monday #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER+132', '🕆\ufe0f🛆 Santíssima Trindade #𝑠𝑖𝑚'),
        ('CHR+SYM+EASTER+140', '🕆\ufe0f🥖\ufe0f🍷\ufe0f Corpus Christi #𝑠𝑖𝑚'),
        ('CHR+SYM+11-01',      '🕆\ufe0f Todos os Santos #𝑠𝑖𝑚'),
        ('CHR+SYM+11-02',      '🕆\ufe0f Finados #𝑠𝑖𝑚'),
        ('CHR+SYM+12-25-SUN_4','🕆\ufe0f Advento #𝑠𝑖𝑚'),
        ('CHR+SYM+12-25',      '🕆\ufe0f🌟\ufe0f👼🏼\ufe0f Natal #𝑠𝑖𝑚'),
    ]

    JEWISH_HOLIDAYS = [
        ('JEW+11-15', '🌳\ufe0f💮\ufe0f Tu biShvat'),
        # ('JEW+12-14', '🍷\ufe0f🍬\ufe0f Purim'),  # Adar bet (13) in leap years, Adar (12) in regular years
        ('JEW+13-14', '🍷\ufe0f🍬\ufe0f Purim'),  # Adar bet (13) in leap years, Adar (12) in regular years
        ('JEW+01-15', '🐑\ufe0f🫓\ufe0f Pesach'),
        ('JEW+02-14', '🐑\ufe0f🫓\ufe0f Pesach Sheni'),
        ('JEW+02-18', '🔥\ufe0f Lag baOmer'),
        ('JEW+03-06', '💐\ufe0f📜\ufe0f Shavuot'),
        ('JEW+05-09', '🕍\ufe0f🔥\ufe0f Tisha b’Av'),

        ('JEW+07-01', '🍎\ufe0f🍯\ufe0f Rosh haShaná'),
        ('JEW+07-10', '🤍\ufe0f🙏🏻\ufe0f Yom Kippur'),
        ('JEW+07-15', '🍋\ufe0f⛺\ufe0f Sukkot'),
        ('JEW+07-22', '🙏🏻\ufe0f🌧\ufe0f️ Shemini Atzeret'),
        ('JEW+07-23', '😊📜\ufe0f Simchat Torah'),
        ('JEW+09-25', '🕯\ufe0f🕍\ufe0f Hanukkah'),
    ]

    ISLAMIC_HOLIDAYS = [
        ('HIJ+09-01', '🍯\ufe0f🥙\ufe0f 1º dia do Ramadã'),
        ('HIJ+09-30', '🍯\ufe0f🥙\ufe0f Laylat ul-Jāʾizah'),
        ('HIJ+10-01-FRI', '🍯\ufe0f🥙\ufe0f Jumuʿat ul-Widāʿ'),
        ('HIJ+10-01', '🍯\ufe0f🥙\ufe0f ʻĪd ul-Fiṭr'),
        ('HIJ+12-10', '🐑\ufe0f🕋\ufe0f ʿĪd ul-ʾAḍḥā'),
    ]

    SPIRITIST_HOLIDAYS = [
        ('SPI+ISO+1804-10-03', f'🍇\ufe0f🕇\ufe0f Nascimento de Allan Kardec (%i)'),
        ('SPI+ISO+1857-04-18', f'🍇\ufe0f🕇\ufe0f Publicação do Livro dos Espíritos (%i)'),
        ('SPI+ISO+1910-04-02', f'🍇\ufe0f🕇\ufe0f Nascimento de Chico Xavier (%i)'),
        ('SPI+ISO+1922-10-22', f'🍇\ufe0f🕇\ufe0f Nascimento de Meimei (%i)'),
    ]
