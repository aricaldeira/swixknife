

DEFAULT_DIGITS = '012345⁰¹²³⁴⁵₀₁₂₃₄₅'
DEDICATED_DIGITS = '󱨀󱨁󱨂󱨃󱨄󱨅󱨤󱨥󱨦󱨧󱨨󱨩󱩈󱩉󱩊󱩋󱩌󱩍'

DEFAULT_COMPRESSED_DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ⁰¹²³⁴⁵⁶⁷⁸⁹ABCDEFGHIJKLMNOPQRSTUVWXYZ₀₁₂₃₄₅₆₇₈₉ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DEDICATED_COMPRESSED_DIGITS = '󱨀󱨁󱨂󱨃󱨄󱨅󱨆󱨇󱨈󱨉󱨊󱨋󱨌󱨍󱨎󱨏󱨐󱨑󱨒󱨓󱨔󱨕󱨖󱨗󱨘󱨙󱨚󱨛󱨜󱨝󱨞󱨟󱨠󱨡󱨢󱨣󱨤󱨥󱨦󱨧󱨨󱨩󱨪󱨫󱨬󱨭󱨮󱨯󱨰󱨱󱨲󱨳󱨴󱨵󱨶󱨷󱨸󱨹󱨺󱨻󱨼󱨽󱨾󱨿󱩀󱩁󱩂󱩃󱩄󱩅󱩆󱩇󱩈󱩉󱩊󱩋󱩌󱩍󱩎󱩏󱩐󱩑󱩒󱩓󱩔󱩕󱩖󱩗󱩘󱩙󱩚󱩛󱩜󱩝󱩞󱩟󱩠󱩡󱩢󱩣󱩤󱩥󱩦󱩧󱩨󱩩󱩪󱩫'

DEFAULT_NUMERATOR_DIGITS = '⁰¹²³⁴⁵⁰¹²³⁴⁵⁰¹²³⁴⁵'
DEDICATED_NUMERATOR_DIGITS = '󱨤󱨥󱨦󱨧󱨨󱨩󱨤󱨥󱨦󱨧󱨨󱨩󱨤󱨥󱨦󱨧󱨨󱨩'

DEFAULT_DENOMINATOR_DIGITS = '₀₁₂₃₄₅₀₁₂₃₄₅₀₁₂₃₄₅'
DEDICATED_DENOMINATOR_DIGITS = '󱩈󱩉󱩊󱩋󱩌󱩍󱩈󱩉󱩊󱩋󱩌󱩍󱩈󱩉󱩊󱩋󱩌󱩍'


def _change_digits(number: str, digits_from: str, digits_to: str) -> str:
    for i in range(len(digits_from)):
        df = digits_from[i]
        dt = digits_to[i]
        number = number.replace(df, dt)

    return number


def default_to_dedicated_digits(number: str) -> str:
    return _change_digits(number, DEFAULT_DIGITS, DEDICATED_DIGITS)


def default_compressed_to_dedicated_digits(number:str) -> str:
    return _change_digits(number, DEFAULT_COMPRESSED_DIGITS, DEDICATED_COMPRESSED_DIGITS)


def dedicated_to_default_digits(number: str) -> str:
    return _change_digits(number, DEDICATED_DIGITS, DEFAULT_DIGITS)


def dedicated_compressed_to_default_digits(number: str) -> str:
    return _change_digits(number, DEDICATED_COMPRESSED_DIGITS, DEFAULT_COMPRESSED_DIGITS)


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
