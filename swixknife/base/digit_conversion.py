
import re


PER_SYMBOLS = ('%', '‰', '‱', '󱺈', '󱺉', '󱺊', '󱺋', '󱺌', '󱺍', '󱺎', '󱺏', '󱺐', '󱺑', '󱺒', '󱺓', '󱺔', '󱺕', '󱺖', '󱺗', '󱹷', '󱹸', '󱹹', '󱹺', '󱹻', '󱹼', '󱹽', '󱹾', '󱹿', '󱺀', '󱺁', '󱺂', '󱺃', '󱺄', '󱺅', '󱺆', '󱺇')


SEZIMAL_DIGITS_MAP = (
    ('0', '󱸀'), ('1', '󱸁'), ('2', '󱸂'), ('3', '󱸃'), ('4', '󱸄'), ('5', '󱸅'),
    ('⁰', '󱸤'), ('¹', '󱸥'), ('²', '󱸦'), ('³', '󱸧'), ('⁴', '󱸨'), ('⁵', '󱸩'),
    ('₀', '󱹈'), ('₁', '󱹉'), ('₂', '󱹊'), ('₃', '󱹋'), ('₄', '󱹌'), ('₅', '󱹍'),
    # ('%', '󱹹'), ('‰', '󱹺'), ('‱', '󱹻'),
    ('%', '󱺉'), ('‰', '󱺊'), ('‱', '󱺋'),
    ('½', '󱹬'), ('⅓', '󱹭'), ('⅔', '󱹮'), ('¼', '󱹯'), ('¾', '󱹰'),
    ('⅕', '󱹱'), ('⅖', '󱹲'), ('⅗', '󱹳'), ('⅘', '󱹴'),
    ('⅙', '󱹵'), ('⅚', '󱹶'),
)
DEFAULT_DIGITS = tuple(digit[0] for digit in SEZIMAL_DIGITS_MAP)
SEZIMAL_DIGITS = tuple(digit[1] for digit in SEZIMAL_DIGITS_MAP)

_DEFAULT_TO_SEZIMAL_DIGITS_TT = str.maketrans({DEFAULT_DIGITS[i]: SEZIMAL_DIGITS[i] for i in range(32)})
_DEDICATED_TO_DEFAULT_DIGITS_TT = str.maketrans({SEZIMAL_DIGITS[i]: DEFAULT_DIGITS[i] for i in range(32)})

NIFTIMAL_DIGITS_MAP = (
    ('0', '0', '0̃'), ('1', '1', '1̃'), ('2', '2','2̃'), ('3', '3', '3̃'), ('4', '4', '4̃'), ('5', '5','5̃'),
    ('6', '0̇', '0ͯ'), ('7', '1̇', '1ͯ'), ('8', '2̇','2ͯ'), ('9', '3̇', '3ͯ'), ('A', '4̇', '4ͯ'), ('B', '5̇','5ͯ'),
    ('C', '0̈', '0̎'), ('D', '1̈', '1̎'), ('E', '2̈','2̎'), ('F', '3̈', '3̎'), ('G', '4̈', '4̎'), ('H', '5̈','5̎'),
    ('I', '0̊', '0̊'), ('J', '1̊', '1̊'), ('K', '2̊','2̊'), ('L', '3̊', '3̊'), ('M', '4̊', '4̊'), ('N', '5̊','5̊'),
    ('O', '0̄', '0̄̄'), ('P', '1̄', '1̄̄'), ('Q', '2̄','2̄̄'), ('R', '3̄', '3̄̄'), ('S', '4̄', '4̄̄'), ('T', '5̄','5̄̄'),
    ('U', '0̆', '0̆̇'), ('V', '1̆', '1̆̇'), ('W', '2̆','2̆̇'), ('X', '3̆', '3̆̇'), ('Y', '4̆', '4̆̇'), ('Z', '5̆','5̆̇'),
    # ('0', '⁰₀', '⁰₀'), ('1', '⁰₁', '⁰₁'), ('2', '⁰₂', '⁰₂'), ('3', '⁰₃', '⁰₃'), ('4', '⁰₄', '⁰₄'), ('5', '⁰₅', '⁰₅'),
    # ('6', '¹₀', '¹₀'), ('7', '¹₁', '¹₁'), ('8', '¹₂', '¹₂'), ('9', '¹₃', '¹₃'), ('A', '¹₄', '¹₄'), ('B', '¹₅', '¹₅'),
    # ('C', '²₀', '²₀'), ('D', '²₁', '²₁'), ('E', '²₂', '²₂'), ('F', '²₃', '²₃'), ('G', '²₄', '²₄'), ('H', '²₅', '²₅'),
    # ('I', '³₀', '³₀'), ('J', '³₁', '³₁'), ('K', '³₂', '³₂'), ('L', '³₃', '³₃'), ('M', '³₄', '³₄'), ('N', '³₅', '³₅'),
    # ('O', '⁴₀', '⁴₀'), ('P', '⁴₁', '⁴₁'), ('Q', '⁴₂', '⁴₂'), ('R', '⁴₃', '⁴₃'), ('S', '⁴₄', '⁴₄'), ('T', '⁴₅', '⁴₅'),
    # ('U', '⁵₀', '⁵₀'), ('V', '⁵₁', '⁵₁'), ('W', '⁵₂', '⁵₂'), ('X', '⁵₃', '⁵₃'), ('Y', '⁵₄', '⁵₄'), ('Z', '⁵₅', '⁵₅'),
    ('⁰', '⁰', '⁰̃'), ('¹', '¹', '¹̃'), ('²', '²','²̃'), ('³', '³', '³̃'), ('⁴', '⁴', '⁴̃'), ('⁵', '⁵','⁵̃'),
    ('⁶', '⁰̇', '⁰ͯ'), ('⁷', '¹̇', '¹ͯ'), ('⁸', '²̇','²ͯ'), ('⁹', '³̇', '³ͯ'), ('A', '⁴̇', '⁴ͯ'), ('B', '⁵̇','⁵ͯ'),
    ('C', '⁰̈', '⁰̎'), ('D', '¹̈', '¹̎'), ('E', '²̈','²̎'), ('F', '³̈', '³̎'), ('G', '⁴̈', '⁴̎'), ('H', '⁵̈','⁵̎'),
    ('I', '⁰̊', '⁰̊'), ('J', '¹̊', '¹̊'), ('K', '²̊','²̊'), ('L', '³̊', '³̊'), ('M', '⁴̊', '⁴̊'), ('N', '⁵̊','⁵̊'),
    ('O', '⁰̄', '⁰̄̄'), ('P', '¹̄', '¹̄̄'), ('Q', '²̄','²̄̄'), ('R', '³̄', '³̄̄'), ('S', '⁴̄', '⁴̄̄'), ('T', '⁵̄','⁵̄̄'),
    ('U', '⁰̆', '⁰̆̇'), ('V', '¹̆', '¹̆̇'), ('W', '²̆','²̆̇'), ('X', '³̆', '³̆̇'), ('Y', '⁴̆', '⁴̆̇'), ('Z', '⁵̆','⁵̆̇'),
    ('₀', '₀', '₀̃'), ('₁', '₁', '₁̃'), ('₂', '₂','₂̃'), ('₃', '₃', '₃̃'), ('₄', '₄', '₄̃'), ('₅', '₅','₅̃'),
    ('₆', '₀̇', '₀ͯ'), ('₇', '₁̇', '₁ͯ'), ('₈', '₂̇','₂ͯ'), ('₉', '₃̇', '₃ͯ'), ('A', '₄̇', '₄ͯ'), ('B', '₅̇','₅ͯ'),
    ('C', '₀̈', '₀̎'), ('D', '₁̈', '₁̎'), ('E', '₂̈','₂̎'), ('F', '₃̈', '₃̎'), ('G', '₄̈', '₄̎'), ('H', '₅̈','₅̎'),
    ('I', '₀̊', '₀̊'), ('J', '₁̊', '₁̊'), ('K', '₂̊','₂̊'), ('L', '₃̊', '₃̊'), ('M', '₄̊', '₄̊'), ('N', '₅̊','₅̊'),
    ('O', '₀̄', '₀̄̄'), ('P', '₁̄', '₁̄̄'), ('Q', '₂̄','₂̄̄'), ('R', '₃̄', '₃̄̄'), ('S', '₄̄', '₄̄̄'), ('T', '₅̄','₅̄̄'),
    ('U', '₀̆', '₀̆̇'), ('V', '₁̆', '₁̆̇'), ('W', '₂̆','₂̆̇'), ('X', '₃̆', '₃̆̇'), ('Y', '₄̆', '₄̆̇'), ('Z', '₅̆','₅̆̇'),
)
_NIFTIMAL_DIGITS_MAP = (
    ('0', 'ø', 'ø̃'), ('1', 'u', 'ũ'), ('2', 'ɔ','ɔ̃'), ('3', 'o', 'õ'), ('4', 'ƨ', 'ƨ̃'), ('5', 'e','ẽ'),
    ('6', 'ø̇', 'øͯ'), ('7', 'u̇', 'uͯ'), ('8', 'ɔ̇','ɔͯ'), ('9', 'ȯ', 'oͯ'), ('A', 'ƨ̇', 'ƨͯ'), ('B', 'ė','eͯ'),
    ('C', 'ø̈', 'ø̎'), ('D', 'ü', 'u̎'), ('E', 'ɔ̈','ɔ̎'), ('F', 'ö', 'o̎'), ('G', 'ƨ̈', 'ƨ̎'), ('H', 'ë','e̎'),
    ('I', 'ø̊', 'ø̊'), ('J', 'ů', 'ů'), ('K', 'ɔ̊','ɔ̊'), ('L', 'o̊', 'o̊'), ('M', 'ƨ̊', 'ƨ̊'), ('N', 'e̊','e̊'),
    ('O', 'ø̄', 'ø̄̄'), ('P', 'ū', 'ū̄'), ('Q', 'ɔ̄','ɔ̄̄'), ('R', 'ō', 'ō̄'), ('S', 'ƨ̄', 'ƨ̄̄'), ('T', 'ē','ē̄'),
    ('U', 'ø̆', 'ø̆̇'), ('V', 'ŭ', 'ŭ̇'), ('W', 'ɔ̆','ɔ̆̇'), ('X', 'ŏ', 'ŏ̇'), ('Y', 'ƨ̆', 'ƨ̆̇'), ('Z', 'ĕ','ĕ̇'),
    ('⁰', '⁰', '⁰̃'), ('¹', '¹', '¹̃'), ('²', '²','²̃'), ('³', '³', '³̃'), ('⁴', '⁴', '⁴̃'), ('⁵', '⁵','⁵̃'),
    ('⁶', '⁰̇', '⁰ͯ'), ('⁷', '¹̇', '¹ͯ'), ('⁸', '²̇','²ͯ'), ('⁹', '³̇', '³ͯ'), ('A', '⁴̇', '⁴ͯ'), ('B', '⁵̇','⁵ͯ'),
    ('C', '⁰̈', '⁰̎'), ('D', '¹̈', '¹̎'), ('E', '²̈','²̎'), ('F', '³̈', '³̎'), ('G', '⁴̈', '⁴̎'), ('H', '⁵̈','⁵̎'),
    ('I', '⁰̊', '⁰̊'), ('J', '¹̊', '¹̊'), ('K', '²̊','²̊'), ('L', '³̊', '³̊'), ('M', '⁴̊', '⁴̊'), ('N', '⁵̊','⁵̊'),
    ('O', '⁰̄', '⁰̄̄'), ('P', '¹̄', '¹̄̄'), ('Q', '²̄','²̄̄'), ('R', '³̄', '³̄̄'), ('S', '⁴̄', '⁴̄̄'), ('T', '⁵̄','⁵̄̄'),
    ('U', '⁰̆', '⁰̆̇'), ('V', '¹̆', '¹̆̇'), ('W', '²̆','²̆̇'), ('X', '³̆', '³̆̇'), ('Y', '⁴̆', '⁴̆̇'), ('Z', '⁵̆','⁵̆̇'),
    ('₀', '₀', '₀̃'), ('₁', '₁', '₁̃'), ('₂', '₂','₂̃'), ('₃', '₃', '₃̃'), ('₄', '₄', '₄̃'), ('₅', '₅','₅̃'),
    ('₆', '₀̇', '₀ͯ'), ('₇', '₁̇', '₁ͯ'), ('₈', '₂̇','₂ͯ'), ('₉', '₃̇', '₃ͯ'), ('A', '₄̇', '₄ͯ'), ('B', '₅̇','₅ͯ'),
    ('C', '₀̈', '₀̎'), ('D', '₁̈', '₁̎'), ('E', '₂̈','₂̎'), ('F', '₃̈', '₃̎'), ('G', '₄̈', '₄̎'), ('H', '₅̈','₅̎'),
    ('I', '₀̊', '₀̊'), ('J', '₁̊', '₁̊'), ('K', '₂̊','₂̊'), ('L', '₃̊', '₃̊'), ('M', '₄̊', '₄̊'), ('N', '₅̊','₅̊'),
    ('O', '₀̄', '₀̄̄'), ('P', '₁̄', '₁̄̄'), ('Q', '₂̄','₂̄̄'), ('R', '₃̄', '₃̄̄'), ('S', '₄̄', '₄̄̄'), ('T', '₅̄','₅̄̄'),
    ('U', '₀̆', '₀̆̇'), ('V', '₁̆', '₁̆̇'), ('W', '₂̆','₂̆̇'), ('X', '₃̆', '₃̆̇'), ('Y', '₄̆', '₄̆̇'), ('Z', '₅̆','₅̆̇'),
)
DEFAULT_NIFTIMAL_DIGITS = tuple(digit[0] for digit in NIFTIMAL_DIGITS_MAP)
REGULARIZED_NIFTIMAL_DIGITS = tuple(digit[1] for digit in NIFTIMAL_DIGITS_MAP)
FINANCIAL_NIFTIMAL_DIGITS = tuple(digit[2] for digit in NIFTIMAL_DIGITS_MAP)


DEFAULT_NUMERATOR_DIGITS = (
    '⁰', '¹', '²', '³', '⁴', '⁵',
    '⁰', '¹', '²', '³', '⁴', '⁵',
    '⁰', '¹', '²', '³', '⁴', '⁵',
    '⁺', '⁻',
)
DEFAULT_DENOMINATOR_DIGITS = (
    '₀', '₁', '₂', '₃', '₄', '₅',
    '₀', '₁', '₂', '₃', '₄', '₅',
    '₀', '₁', '₂', '₃', '₄', '₅',
    '⁺', '⁻',
)


def _change_digits(number: str, digits_from: tuple, digits_to: tuple) -> str:
    for i in range(len(digits_from)):
        df = digits_from[i]
        dt = digits_to[i]
        number = re.sub(df, dt, number)

    return number


def default_to_sezimal_digits(number: str) -> str:
    return number.translate(_DEFAULT_TO_SEZIMAL_DIGITS_TT)


def default_niftimal_to_sezimal_digits(number:str) -> str:
    number = default_niftimal_to_regularized_digits(number)
    return default_to_sezimal_digits(number)


def default_niftimal_to_regularized_digits(number:str) -> str:
    return _change_digits(number, DEFAULT_NIFTIMAL_DIGITS, REGULARIZED_NIFTIMAL_DIGITS)


def default_niftimal_to_niftimal_digits(number:str) -> str:
    number = default_niftimal_to_regularized_digits(number)
    return default_to_sezimal_digits(number)


def default_niftimal_to_financial_digits(number:str) -> str:
    return _change_digits(number, DEFAULT_NIFTIMAL_DIGITS, FINANCIAL_NIFTIMAL_DIGITS)


def default_niftimal_to_financial_sezimal_digits(number:str) -> str:
    number = default_niftimal_to_financial_digits(number)
    return default_to_sezimal_digits(number)


def sezimal_to_default_digits(number: str) -> str:
    return number.translate(_DEDICATED_TO_DEFAULT_DIGITS_TT)


def dedicated_niftimal_to_default_digits(number: str) -> str:
    number = sezimal_to_default_digits(number)
    return _change_digits(number, REGULARIZED_NIFTIMAL_DIGITS, DEFAULT_NIFTIMAL_DIGITS)


def default_to_numerator_digits(number: str) -> str:
    return _change_digits(number, DEFAULT_DIGITS, DEFAULT_NUMERATOR_DIGITS)


def default_to_denominator_digits(number: str) -> str:
    return _change_digits(number, DEFAULT_DIGITS, DEFAULT_DENOMINATOR_DIGITS)


def sezimal_to_numerator_digits(number: str) -> str:
    number = sezimal_to_default_digits(number)
    number = default_to_numerator_digits(number)
    return default_to_sezimal_digits(number)


def sezimal_to_denominator_digits(number: str) -> str:
    number = sezimal_to_default_digits(number)
    number = default_to_denominator_digits(number)
    return default_to_sezimal_digits(number)


def default_to_dedicated_numerator_digits(number: str) -> str:
    number = default_to_numerator_digits(number)
    return default_to_sezimal_digits(number)


def default_to_dedicated_denominator_digits(number: str) -> str:
    number = default_to_denominator_digits(number)
    return default_to_sezimal_digits(number)


def sezimal_to_default_numerator_digits(number: str) -> str:
    number = sezimal_to_default_digits(number)
    return default_to_numerator_digits(number)


def sezimal_to_default_denominator_digits(number: str) -> str:
    number = sezimal_to_default_digits(number)
    return default_to_denominator_digits(number)


def dozenal_letters_to_digits(number: str) -> str:
    number = number.upper()
    number = number.replace('A', '↊')
    number = number.replace('B', '↋')
    return number

def dozenal_digits_to_letters(number: str) -> str:
    number = number.upper()
    number = number.replace('↊', 'A')
    number = number.replace('↋', 'B')
    return number
