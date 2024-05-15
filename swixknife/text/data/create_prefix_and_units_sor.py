

from swixknife import *


def create_units(lang='en'):
    if lang == 'pt':
        text = '''#
# Units
#
UNIT-dia dia
UNIT-day dia
UNIT-uta uta
UNIT-pox poxa
UNIT-agm agrima
UNIT-ang anuga
UNIT-bod boda
UNIT-avt avrita
UNIT-pad pada
UNIT-veg vega
UNIT-tvr tevara
UNIT-kex quexê
UNIT-ayt aitã
UNIT-vrt várti
UNIT-drv drávia
UNIT-gan gana
UNIT-trg taranga
UNIT-mnu mânu
UNIT-bar bara
UNIT-dab daba
UNIT-kry cária
UNIT-xat xáti
UNIT-dar dara
UNIT-avx avexa
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-cln chalana
UNIT-prk preraca
UNIT-sma samai
UNIT-abv abiva
UNIT-vst vistara
'''

    elif lang == 'bz':
        text = '''#
# Units
#
UNIT-dia dia
UNIT-day dia
UNIT-uta uta
UNIT-pox poxa
UNIT-agm agrima
UNIT-ang anuga
UNIT-bod boda
UNIT-avt avrita
UNIT-pad pada
UNIT-veg vega
UNIT-tvr tevara
UNIT-kex kexe
UNIT-ayt aytan
UNIT-vrt varti
UNIT-drv dravya
UNIT-gan gana
UNIT-trg taranga
UNIT-mnu manu
UNIT-bar bara
UNIT-dab daba
UNIT-kry karya
UNIT-xat xati
UNIT-dar dara
UNIT-avx avexa
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-cln xalana
UNIT-prk preraka
UNIT-sma samay
UNIT-abv abiva
UNIT-vst vistara
'''

    else:
        text = '''#
# Units
#
UNIT-day day
UNIT-uta uta
UNIT-pox posha
UNIT-agm agrima
UNIT-ang anuga
UNIT-bod boda
UNIT-avt avrita
UNIT-pad pada
UNIT-veg vega
UNIT-tvr tevara
UNIT-kex keshe
UNIT-ayt aytan
UNIT-vrt varti
UNIT-drv dravya
UNIT-gan gana
UNIT-trg taranga
UNIT-mnu manu
UNIT-bar bara
UNIT-dab daba
UNIT-kry karya
UNIT-xat shati
UNIT-dar dara
UNIT-avx avesha
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-cln chalana
UNIT-prk preraka
UNIT-sma samai
UNIT-abv abiva
UNIT-vst vistara
'''
    return text


def create_prefixes(lang='en'):
    text = '''#
# Prefixes
#
'''

    for i in SezimalRange(-104, 105):
        if i == 0:
            text += 'PREFIX-x shunti\n'
            text += 'PREFIX-X shunma\n'
        else:
            symbol = sezimal_exponent_to_symbol(i)
            name = sezimal_exponent_to_prefix(i)

            if lang == 'pt':
                name = name.replace('shu', 'xu')
                name = name.replace('sha', 'xa')
                name = name.replace('eka', 'eca')
                name = name.replace('panp', 'pamp')

            elif lang == 'bz':
                name = name.replace('shu', 'xu')
                name = name.replace('sha', 'xa')
                name = name.replace('cha', 'xa')

            name = name.replace('nm', 'm')

            text += f'PREFIX-{symbol} {name}\n'

    text += '''
#
# Prefixes divided by 10,
# for the automatic detection
# of the prefix based on the
# number of sezimal places
#
'''
    for i in SezimalRange(-104, 105):
        if i == 0:
            text += 'PREFIX-DIV10-x e\n'
            text += 'PREFIX-DIV10-X e\n'
        else:
            symbol = sezimal_exponent_to_symbol(i)
            div10 = sezimal_exponent_to_symbol(i-1)
            text += f'PREFIX-DIV10-{symbol} {div10}\n'

    return text


def create_rules(conjunction='and', preposition=''):
    conjunction = conjunction.strip()

    if not conjunction:
        conjunction = ' '
    else:
        conjunction = f' {conjunction} '

    preposition = preposition.strip()

    if not preposition:
        preposition = ' '
    else:
        preposition = f' {preposition} '

    PREFIX_RULE = '[XEDTCPSNA]{1,3}|[xedtcpsna]{1,3}'
    UNIT_RULE = '[a-z]{3}'
    # PRECISION_RULE = '[0-5]{1,3}'

#     text = f'''#
# # Rules for units without fractional parts, or only zeroes
# #
# "(SH(-({PREFIX_RULE})?({UNIT_RULE}))(-({PREFIX_RULE})?({UNIT_RULE})-?({PRECISION_RULE})?)?) ([-−]?0*1)([.,]0*?)?" $(1) $(PREFIX-\\3)$(UNIT-\\4)
# "(SH(-({PREFIX_RULE})?({UNIT_RULE}))(-({PREFIX_RULE})?({UNIT_RULE})-?({PRECISION_RULE})?)?) ([-−]?\\d+0{{8,}})([.,]0*?)?" $9{preposition}$(PREFIX-\\3)$(UNIT-\\4)s
# "(SH(-({PREFIX_RULE})?({UNIT_RULE}))(-({PREFIX_RULE})?({UNIT_RULE})-?({PRECISION_RULE})?)?) ([-−]?\\d+)([.,]0*?)?" $9 $(PREFIX-\\3)$(UNIT-\\4)s
#
# #
# # Rules for units with fractional parts, but no subunit specified;
# # let’s deduce the subunit prefix by the number of sezimal places
# #
# '''
    text = f'''#
# Rules for units without fractional parts, or only zeroes
#
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?0*1)([.,]0*?)?" $(1) $(PREFIX-\\1)$(UNIT-\\2)
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?\\d+0{{8,}})([.,]0*?)?" $3{preposition}$(PREFIX-\\1)$(UNIT-\\2)s
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?\\d+)([.,]0*?)?" $3 $(PREFIX-\\1)$(UNIT-\\2)s

#
# Rules for units with fractional parts;
# let’s deduce the subunit prefix by the number of sezimal places
#
'''

    def _digits_div10(x, t):
        if x == 0:
            return t

        t = f'$(PREFIX-DIV10-{t})'
        return _digits_div10(x - 1, t)

    for i in SezimalRange(1, 105):
        digits_rule = r'\d' * int(i)
        prefix_negative = sezimal_exponent_to_symbol(i * -1)
        prefix_positive = sezimal_exponent_to_symbol(i)
        div10 = _digits_div10(i, '\\2')

#         text += rf'''#
# # {i} sezimal place{'s' if i > 1 else ''}
# #
# "(SH-({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$3 $(PREFIX-{prefix_negative})$(UNIT-\\2)
# "(SH-{prefix_positive}({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$3 $(UNIT-\\2)  # cancel shunma/shunti
# "(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$4 $(PREFIX-{div10})$(UNIT-\\3)
#
# '''
        text += rf'''#
# {i} sezimal place{'s' if i > 1 else ''}
#
"(SH-({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-{prefix_negative}\\2 \\3)
"(SH-{prefix_positive}({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-\\2 \\3)  # cancel shunma/shunti
"(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-{div10}\\3 \\4)

'''

    return text


if __name__ == '__main__':
    # print(create_units(lang='bz'))
    # print(create_prefixes(lang='bz'))
    # print(create_rules(conjunction='i', preposition=''))

    # print(create_units(lang='pt'))
    # print(create_prefixes(lang='pt'))
    # print(create_rules(conjunction='e', preposition=''))

    print(create_units(lang='en'))
    print(create_prefixes(lang='en'))
    print(create_rules(conjunction='and', preposition=''))
