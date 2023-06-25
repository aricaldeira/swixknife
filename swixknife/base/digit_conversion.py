

DEFAULT_DIGITS = tuple('012345⁰¹²³⁴⁵₀₁₂₃₄₅')
DEDICATED_DIGITS = tuple('󱨀󱨁󱨂󱨃󱨄󱨅󱨤󱨥󱨦󱨧󱨨󱨩󱩈󱩉󱩊󱩋󱩌󱩍')

DEFAULT_NIFTIMAL_DIGITS = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ⁰¹²³⁴⁵⁶⁷⁸⁹ABCDEFGHIJKLMNOPQRSTUVWXYZ₀₁₂₃₄₅₆₇₈₉ABCDEFGHIJKLMNOPQRSTUVWXYZ')
DEDICATED_NIFTIMAL_DIGITS = tuple('󱨀󱨁󱨂󱨃󱨄󱨅󱨆󱨇󱨈󱨉󱨊󱨋󱨌󱨍󱨎󱨏󱨐󱨑󱨒󱨓󱨔󱨕󱨖󱨗󱨘󱨙󱨚󱨛󱨜󱨝󱨞󱨟󱨠󱨡󱨢󱨣󱨤󱨥󱨦󱨧󱨨󱨩󱨪󱨫󱨬󱨭󱨮󱨯󱨰󱨱󱨲󱨳󱨴󱨵󱨶󱨷󱨸󱨹󱨺󱨻󱨼󱨽󱨾󱨿󱩀󱩁󱩂󱩃󱩄󱩅󱩆󱩇󱩈󱩉󱩊󱩋󱩌󱩍󱩎󱩏󱩐󱩑󱩒󱩓󱩔󱩕󱩖󱩗󱩘󱩙󱩚󱩛󱩜󱩝󱩞󱩟󱩠󱩡󱩢󱩣󱩤󱩥󱩦󱩧󱩨󱩩󱩪󱩫')

_PLUS_00 = ''
# _PLUS_10 = '\u0307'
# _PLUS_20 = '\u0308'
# _PLUS_30 = '\u0304'
# _PLUS_10 = '\u0323'
# _PLUS_20 = '\u0324'
# _PLUS_30 = '\u0331'
# _PLUS_10 = '\u030d'
# _PLUS_20 = '\u030e'
# _PLUS_30 = '\u0304'
# _PLUS_40 = _PLUS_30 + _PLUS_10
# _PLUS_50 = _PLUS_30 + _PLUS_20

_PLUS_10 = '\u0307'
_PLUS_20 = '\u0308'
_PLUS_30 = '\u030a'
_PLUS_40 = '\u0304'
_PLUS_50 = '\u0306'

REGULARIZED_NIFTIMAL_DIGITS = tuple(c.replace(' ', '') for c in f'''0{_PLUS_00}\n1{_PLUS_00}\n2{_PLUS_00}\n3{_PLUS_00}\n4{_PLUS_00}\n5{_PLUS_00}
0{_PLUS_10}\n1{_PLUS_10}\n2{_PLUS_10}\n3{_PLUS_10}\n4{_PLUS_10}\n5{_PLUS_10}
0{_PLUS_20}\n1{_PLUS_20}\n2{_PLUS_20}\n3{_PLUS_20}\n4{_PLUS_20}\n5{_PLUS_20}
0{_PLUS_30}\n1{_PLUS_30}\n2{_PLUS_30}\n3{_PLUS_30}\n4{_PLUS_30}\n5{_PLUS_30}
0{_PLUS_40}\n1{_PLUS_40}\n2{_PLUS_40}\n3{_PLUS_40}\n4{_PLUS_40}\n5{_PLUS_40}
0{_PLUS_50}\n1{_PLUS_50}\n2{_PLUS_50}\n3{_PLUS_50}\n4{_PLUS_50}\n5{_PLUS_50}
⁰{_PLUS_00}\n¹{_PLUS_00}\n²{_PLUS_00}\n³{_PLUS_00}\n⁴{_PLUS_00}\n⁵{_PLUS_00}
⁰{_PLUS_10}\n¹{_PLUS_10}\n²{_PLUS_10}\n³{_PLUS_10}\n⁴{_PLUS_10}\n⁵{_PLUS_10}
⁰{_PLUS_20}\n¹{_PLUS_20}\n²{_PLUS_20}\n³{_PLUS_20}\n⁴{_PLUS_20}\n⁵{_PLUS_20}
⁰{_PLUS_30}\n¹{_PLUS_30}\n²{_PLUS_30}\n³{_PLUS_30}\n⁴{_PLUS_30}\n⁵{_PLUS_30}
⁰{_PLUS_40}\n¹{_PLUS_40}\n²{_PLUS_40}\n³{_PLUS_40}\n⁴{_PLUS_40}\n⁵{_PLUS_40}
⁰{_PLUS_50}\n¹{_PLUS_50}\n²{_PLUS_50}\n³{_PLUS_50}\n⁴{_PLUS_50}\n⁵{_PLUS_50}
₀{_PLUS_00}\n₁{_PLUS_00}\n₂{_PLUS_00}\n₃{_PLUS_00}\n₄{_PLUS_00}\n₅{_PLUS_00}
₀{_PLUS_10}\n₁{_PLUS_10}\n₂{_PLUS_10}\n₃{_PLUS_10}\n₄{_PLUS_10}\n₅{_PLUS_10}
₀{_PLUS_20}\n₁{_PLUS_20}\n₂{_PLUS_20}\n₃{_PLUS_20}\n₄{_PLUS_20}\n₅{_PLUS_20}
₀{_PLUS_30}\n₁{_PLUS_30}\n₂{_PLUS_30}\n₃{_PLUS_30}\n₄{_PLUS_30}\n₅{_PLUS_30}
₀{_PLUS_40}\n₁{_PLUS_40}\n₂{_PLUS_40}\n₃{_PLUS_40}\n₄{_PLUS_40}\n₅{_PLUS_40}
₀{_PLUS_50}\n₁{_PLUS_50}\n₂{_PLUS_50}\n₃{_PLUS_50}\n₄{_PLUS_50}\n₅{_PLUS_50}'''.split('\n'))

REGULARIZED_DEDICATED_NIFTIMAL_DIGITS = tuple(c.replace(' ', '') for c in f'''󱨀{_PLUS_00}\n󱨁{_PLUS_00}\n󱨂{_PLUS_00}\n󱨃{_PLUS_00}\n󱨄{_PLUS_00}\n󱨅{_PLUS_00}
󱨀{_PLUS_10}\n󱨁{_PLUS_10}\n󱨂{_PLUS_10}\n󱨃{_PLUS_10}\n󱨄{_PLUS_10}\n󱨅{_PLUS_10}
󱨀{_PLUS_20}\n󱨁{_PLUS_20}\n󱨂{_PLUS_20}\n󱨃{_PLUS_20}\n󱨄{_PLUS_20}\n󱨅{_PLUS_20}
󱨀{_PLUS_30}\n󱨁{_PLUS_30}\n󱨂{_PLUS_30}\n󱨃{_PLUS_30}\n󱨄{_PLUS_30}\n󱨅{_PLUS_30}
󱨀{_PLUS_40}\n󱨁{_PLUS_40}\n󱨂{_PLUS_40}\n󱨃{_PLUS_40}\n󱨄{_PLUS_40}\n󱨅{_PLUS_40}
󱨀{_PLUS_50}\n󱨁{_PLUS_50}\n󱨂{_PLUS_50}\n󱨃{_PLUS_50}\n󱨄{_PLUS_50}\n󱨅{_PLUS_50}
󱨤{_PLUS_00}\n󱨥{_PLUS_00}\n󱨦{_PLUS_00}\n󱨧{_PLUS_00}\n󱨨{_PLUS_00}\n󱨩{_PLUS_00}
󱨤{_PLUS_10}\n󱨥{_PLUS_10}\n󱨦{_PLUS_10}\n󱨧{_PLUS_10}\n󱨨{_PLUS_10}\n󱨩{_PLUS_10}
󱨤{_PLUS_20}\n󱨥{_PLUS_20}\n󱨦{_PLUS_20}\n󱨧{_PLUS_20}\n󱨨{_PLUS_20}\n󱨩{_PLUS_20}
󱨤{_PLUS_30}\n󱨥{_PLUS_30}\n󱨦{_PLUS_30}\n󱨧{_PLUS_30}\n󱨨{_PLUS_30}\n󱨩{_PLUS_30}
󱨤{_PLUS_40}\n󱨥{_PLUS_40}\n󱨦{_PLUS_40}\n󱨧{_PLUS_40}\n󱨨{_PLUS_40}\n󱨩{_PLUS_40}
󱨤{_PLUS_50}\n󱨥{_PLUS_50}\n󱨦{_PLUS_50}\n󱨧{_PLUS_50}\n󱨨{_PLUS_50}\n󱨩{_PLUS_50}
󱩈{_PLUS_00}\n󱩉{_PLUS_00}\n󱩊{_PLUS_00}\n󱩋{_PLUS_00}\n󱩌{_PLUS_00}\n󱩍{_PLUS_00}
󱩈{_PLUS_10}\n󱩉{_PLUS_10}\n󱩊{_PLUS_10}\n󱩋{_PLUS_10}\n󱩌{_PLUS_10}\n󱩍{_PLUS_10}
󱩈{_PLUS_20}\n󱩉{_PLUS_20}\n󱩊{_PLUS_20}\n󱩋{_PLUS_20}\n󱩌{_PLUS_20}\n󱩍{_PLUS_20}
󱩈{_PLUS_30}\n󱩉{_PLUS_30}\n󱩊{_PLUS_30}\n󱩋{_PLUS_30}\n󱩌{_PLUS_30}\n󱩍{_PLUS_30}
󱩈{_PLUS_40}\n󱩉{_PLUS_40}\n󱩊{_PLUS_40}\n󱩋{_PLUS_40}\n󱩌{_PLUS_40}\n󱩍{_PLUS_40}
󱩈{_PLUS_50}\n󱩉{_PLUS_50}\n󱩊{_PLUS_50}\n󱩋{_PLUS_50}\n󱩌{_PLUS_50}\n󱩍{_PLUS_50}'''.split('\n'))

DEFAULT_NUMERATOR_DIGITS = tuple('⁰¹²³⁴⁵⁰¹²³⁴⁵⁰¹²³⁴⁵‍⁺⁻')
DEDICATED_NUMERATOR_DIGITS = tuple('󱨤󱨥󱨦󱨧󱨨󱨩󱨤󱨥󱨦󱨧󱨨󱨩󱨤󱨥󱨦󱨧󱨨󱨩⁺⁻')

DEFAULT_DENOMINATOR_DIGITS = tuple('₀₁₂₃₄₅₀₁₂₃₄₅₀₁₂₃₄₅₊₋')
DEDICATED_DENOMINATOR_DIGITS = tuple('󱩈󱩉󱩊󱩋󱩌󱩍󱩈󱩉󱩊󱩋󱩌󱩍󱩈󱩉󱩊󱩋󱩌󱩍₊₋')


def _change_digits(number: str, digits_from: tuple, digits_to: tuple) -> str:
    for i in range(len(digits_from)):
        df = digits_from[i]
        dt = digits_to[i]
        number = number.replace(df, dt)

    return number


def default_to_dedicated_digits(number: str) -> str:
    return _change_digits(number, DEFAULT_DIGITS, DEDICATED_DIGITS)


def default_niftimal_to_dedicated_digits(number:str) -> str:
    return _change_digits(number, DEFAULT_NIFTIMAL_DIGITS, DEDICATED_NIFTIMAL_DIGITS)


def default_niftimal_to_regularized_digits(number:str) -> str:
    return _change_digits(number, DEFAULT_NIFTIMAL_DIGITS, REGULARIZED_NIFTIMAL_DIGITS)


def default_niftimal_to_regularized_dedicated_digits(number:str) -> str:
    return _change_digits(number, DEFAULT_NIFTIMAL_DIGITS, REGULARIZED_DEDICATED_NIFTIMAL_DIGITS)


def dedicated_to_default_digits(number: str) -> str:
    return _change_digits(number, DEDICATED_DIGITS, DEFAULT_DIGITS)


def dedicated_niftimal_to_default_digits(number: str) -> str:
    return _change_digits(number, DEDICATED_NIFTIMAL_DIGITS, DEFAULT_NIFTIMAL_DIGITS)


def default_to_numerator_digits(number: str) -> str:
    return _change_digits(number, DEFAULT_DIGITS, DEFAULT_NUMERATOR_DIGITS)


def default_to_denominator_digits(number: str) -> str:
    return _change_digits(number, DEFAULT_DIGITS, DEFAULT_DENOMINATOR_DIGITS)


def dedicated_to_numerator_digits(number: str) -> str:
    return _change_digits(number, DEDICATED_DIGITS, DEDICATED_NUMERATOR_DIGITS)


def dedicated_to_denominator_digits(number: str) -> str:
    return _change_digits(number, DEDICATED_DIGITS, DEDICATED_DENOMINATOR_DIGITS)


def default_to_dedicated_numerator_digits(number: str) -> str:
    return _change_digits(number, DEFAULT_DIGITS, DEDICATED_NUMERATOR_DIGITS)


def default_to_dedicated_denominator_digits(number: str) -> str:
    return _change_digits(number, DEFAULT_DIGITS, DEDICATED_DENOMINATOR_DIGITS)


def dedicated_to_default_numerator_digits(number: str) -> str:
    return _change_digits(number, DEDICATED_DIGITS, DEFAULT_NUMERATOR_DIGITS)


def dedicated_to_default_denominator_digits(number: str) -> str:
    return _change_digits(number, DEDICATED_DIGITS, DEFAULT_DENOMINATOR_DIGITS)
