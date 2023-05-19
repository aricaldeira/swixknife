

from swixknife import *


def create_units(lang='en'):
    if lang == 'pt':
        text = '''#
# Units
#
UNIT-dia dia
UNIT-day dia
UNIT-uta uta
UNIT-psh poxa
UNIT-agm agrima
UNIT-ang anuga
UNIT-bda boda
UNIT-avt avrita
UNIT-pad pada
UNIT-veg vega
UNIT-tvr tevara
UNIT-ksh quexe
UNIT-ayt aitan
UNIT-vrt várti
UNIT-drv drávia
UNIT-gna gana
UNIT-trg taranga
UNIT-mnu mânu
UNIT-bra bara
UNIT-dba daba
UNIT-kry kária
UNIT-sht xáti
UNIT-dra dara
UNIT-vsh avexa
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-chl chalana
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
UNIT-psh pòxa
UNIT-agm agrima
UNIT-ang anuga
UNIT-bda bòda
UNIT-avt avrita
UNIT-pad pada
UNIT-veg vèga
UNIT-tvr tevara
UNIT-ksh kexi
UNIT-ayt aytan
UNIT-vrt varti
UNIT-drv dravya
UNIT-gna gana
UNIT-trg taranga
UNIT-mnu manu
UNIT-bra bara
UNIT-dba daba
UNIT-kry karya
UNIT-sht xati
UNIT-dra dara
UNIT-vsh avexa
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-chl xalana
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
UNIT-psh posha
UNIT-agm agrima
UNIT-ang anuga
UNIT-bda boda
UNIT-avt avrita
UNIT-pad pada
UNIT-veg vega
UNIT-tvr tevara
UNIT-ksh keshe
UNIT-ayt aytan
UNIT-vrt varti
UNIT-drv dravya
UNIT-gna gana
UNIT-trg taranga
UNIT-mnu manu
UNIT-bra bara
UNIT-dba daba
UNIT-kry karya
UNIT-sht shati
UNIT-dra dara
UNIT-vsh avesha
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-chl chalana
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
            text += 'PREFIX-s shunti\n'
            text += 'PREFIX-S shunma\n'
        else:
            symbol = sezimal_exponent_to_symbol(i)
            name = sezimal_exponent_to_prefix(i)

            if lang == 'pt':
                name = name.replace('shun', 'xun')
                name = name.replace('eka', 'eca')
                name = name.replace('panp', 'pamp')

            elif lang == 'bz':
                name = name.replace('shun', 'xun')
                name = name.replace('cha', 'xa')

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
            text += 'PREFIX-DIV10-s e\n'
            text += 'PREFIX-DIV10-S e\n'
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

    PREFIX_RULE = '[SEDTCP]{1,3}|[sedtcp]{1,3}'
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
        digits_rule = '\d' * int(i)
        prefix_negative = sezimal_exponent_to_symbol(i * -1)
        prefix_positive = sezimal_exponent_to_symbol(i)
        div10 = _digits_div10(i, '\\2')

#         text += f'''#
# # {i} sezimal place{'s' if i > 1 else ''}
# #
# "(SH-({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$3 $(PREFIX-{prefix_negative})$(UNIT-\\2)
# "(SH-{prefix_positive}({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$3 $(UNIT-\\2)  # cancel shunma/shunti
# "(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$4 $(PREFIX-{div10})$(UNIT-\\3)
#
# '''
        text += f'''#
# {i} sezimal place{'s' if i > 1 else ''}
#
"(SH-({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-{prefix_negative}\\2 \\3)
"(SH-{prefix_positive}({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-\\2 \\3)  # cancel shunma/shunti
"(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-{div10}\\3 \\4)

'''

    return text


if __name__ == '__main__':
    print(create_units(lang='en'))
    print(create_prefixes(lang='en'))
    print(create_rules(conjunction='and', preposition=''))
