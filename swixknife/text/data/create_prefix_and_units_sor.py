

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
UNIT-svg sanvega
UNIT-pkp praquepa
UNIT-pbv prabava
UNIT-tnv tanava
UNIT-upr upári
UNIT-nad nádi
UNIT-bum búmi
UNIT-idn índana
UNIT-tln têlan
UNIT-agn aguení
UNIT-gtk gática
UNIT-tap tapa
UNIT-dar dara
UNIT-avx ávexa
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-cln chálana
UNIT-prk prêraca
UNIT-sam samái
UNIT-abv abiva
UNIT-vst vistara
UNIT-prd parídi
UNIT-gol gola
UNIT-pkx pracaxa
UNIT-dpk dípaca
UNIT-prt práti
UNIT-p/s por seis
UNIT-p/n por nife
UNIT-p/a por arda
UNIT-p/sa por seis arda
UNIT-p/na por nife arda
UNIT-p/x por xadara
UNIT-p/sx por seis xadara
UNIT-p/nx por nife xadara
UNIT-p/ax por arda xadara
UNIT-p/sax por seis arda xadara
UNIT-p/nax por nife arda xadara
UNIT-p/Dx por dixadara
UNIT-p/Tx por trixadara
UNIT-p/Cx por charxadara
UNIT-p/Px por panxadara
UNIT-p/Xx por xaxadara
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
UNIT-svg sanvega
UNIT-pkp prakepa
UNIT-pbv prabava
UNIT-tnv tanava
UNIT-upr upari
UNIT-nad nadi
UNIT-bum bumi
UNIT-idn índana
UNIT-tln têlan
UNIT-agn agení
UNIT-gtk gátika
UNIT-tap tapa
UNIT-dar dara
UNIT-avx ávexa
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-cln xálana
UNIT-prk prêraka
UNIT-sam samay
UNIT-abv abiva
UNIT-vst vistara
UNIT-prd paridi
UNIT-gol gola
UNIT-pkx prakaxa
UNIT-dpk dípaka
UNIT-prt prati
UNIT-p/s pur sêys
UNIT-p/n pur nifi
UNIT-p/a pur arda
UNIT-p/sa pur sêys arda
UNIT-p/na pur nifi arda
UNIT-p/x pur xadara
UNIT-p/sx pur sêys xadara
UNIT-p/nx pur nifi xadara
UNIT-p/ax pur arda xadara
UNIT-p/sax pur sêys arda xadara
UNIT-p/nax pur nifi arda xadara
UNIT-p/Dx pur dixadara
UNIT-p/Tx pur trixadara
UNIT-p/Cx pur charxadara
UNIT-p/Px pur panxadara
UNIT-p/Xx pur xaxadara
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
UNIT-svg sanvega
UNIT-pkp prakepa
UNIT-pbv prabava
UNIT-tnv tanava
UNIT-upr upari
UNIT-nad nadi
UNIT-bum bumi
UNIT-idn indana
UNIT-tln telan
UNIT-agn agni
UNIT-gtk gatika
UNIT-tap tapa
UNIT-dar dara
UNIT-avx avesha
UNIT-vbv vibava
UNIT-ptr pratiroda
UNIT-cln chalana
UNIT-prk preraka
UNIT-sam samai
UNIT-abv abiva
UNIT-vst vistara
UNIT-prd paridi
UNIT-gol gola
UNIT-pkx prakasha
UNIT-dpk dipaka
UNIT-prt prati
UNIT-p/s per six
UNIT-p/n per nif
UNIT-p/a per arda
UNIT-p/sa per six arda
UNIT-p/na per nif arda
UNIT-p/x per shadara
UNIT-p/sx per six shadara
UNIT-p/nx per nif shadara
UNIT-p/ax per arda shadara
UNIT-p/sax per six arda shadara
UNIT-p/nax per nif arda shadara
UNIT-p/Dx per dishadara
UNIT-p/Tx per trishadara
UNIT-p/Cx per charshadara
UNIT-p/Px per panshadara
UNIT-p/Xx per shashadara
'''
    return text


def create_prefixes(lang='en'):
    text = '''#
# Prefixes
#
'''

    for i in SezimalRange(-104, 105):
        if i == 0:
            text += 'PREFIX-z ""\n'
            text += 'PREFIX-Z ""\n'
        else:
            symbol = sezimal_exponent_to_symbol(i) or 'z'
            name = sezimal_exponent_to_prefix(i) or 'z'

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
            text += 'PREFIX-DIV10-z e\n'
            text += 'PREFIX-DIV10-Z e\n'
        else:
            symbol = sezimal_exponent_to_symbol(i) or 'z'
            div10 = sezimal_exponent_to_symbol(i-1) or 'z'
            text += f'PREFIX-DIV10-{symbol} {div10}\n'

    return text


def create_rules(conjunction='and', preposition='', lang=''):
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

    PREFIX_RULE = '[ZEDTCPXNA]{1,3}|[zedtcpxna]{1,3}'
    UNIT_RULE = '[a-z]{3}'
    PER_UNIT_RULE = 'p/[a-zA-Z]{1,3}'
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
    text = rf'''
#
# Rules for the "per" units, that don’t use prefixes,
# and don’t get plural forms
#
"SH-({PER_UNIT_RULE}) ([-−]?0+)([.,]0*)?" $(0) $(cleanup $(UNIT-\1))
"SH-({PER_UNIT_RULE}) ([-−]?0*1)([.,]0*)?" $(1) $(cleanup $(UNIT-\1))
"SH-({PER_UNIT_RULE}) ([-−]?\d+)([.,]0*?)?" $(\2) $(cleanup $(UNIT-\1))
"SH-({PER_UNIT_RULE}) ([-−]?\d+[.,]\d+)" $(\2) $(cleanup $(UNIT-\1))

#
# Rules for units used with fractions
#
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?\d+[/⁄][-−]?\d+)" $(\3){preposition}$(cleanup $(PREFIX-\1)$(UNIT-\2))

#
# Rules for units without fractional parts, or only zeroes
#
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?0+)([.,]0*)?" $(0) $(cleanup $(PREFIX-\1)$(UNIT-\2)s)
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?0*1)([.,]0*)?" $(1) $(cleanup $(PREFIX-\1)$(UNIT-\2))
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?\d+)([.,]0*?)?" $(\3) $(cleanup $(PREFIX-\1)$(UNIT-\2)s)

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
        prefix_negative = sezimal_exponent_to_symbol(i * -1) or 'z'
        prefix_positive = sezimal_exponent_to_symbol(i) or 'z'
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
"(SH-({UNIT_RULE}) [-−]?0+)[.,]({digits_rule})" $(SH-{prefix_negative}\\2 \\3)
"(SH-{prefix_positive}({UNIT_RULE}) [-−]?0+)[.,]({digits_rule})" $(SH-\\2 \\3)  # cancel shunma/shunti
"(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?0+)[.,]({digits_rule})" $(SH-{div10}\\3 \\4)

"(SH-({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-{prefix_negative}\\2 \\3)
"(SH-{prefix_positive}({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-\\2 \\3)  # cancel shunma/shunti
"(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?\d+)[.,]({digits_rule})" $1{conjunction}|$(SH-{div10}\\3 \\4)

'''

    if lang == 'pt':
        text += r'''== cleanup ==

"tapa" grau sezimal \(tapa\)
"tapas" graus sezimais \(tapas\)
(.+)ma([aâàáãä])(.+) \\1m\\2\\3
(.+)ti([iîìíĩï])(.+) \\1t\\2\\3
(.+) \\1
'''

    elif lang == 'bz':
        text += r'''== cleanup ==

"tapa" graw sezimaw \(tapa\)
"tapas" graws sezimays \(tapas\)
(.+)ma([aâàáãä])(.+) \\1m\\2\\3
(.+)ti([iîìíĩï])(.+) \\1t\\2\\3
(.+) \\1
'''

    else:
        text += r'''== cleanup ==

"tapa" sezimal degree \(tapa\)
"tapas" sezimal degrees \(tapas\)
(.+)ma([aâàáãä])(.+) \\1m\\2\\3
(.+)ti([iîìíĩï])(.+) \\1t\\2\\3
(.+) \\1
'''

    return text


if __name__ == '__main__':
    arq = open('bz_units_and_prefixes.sor', 'w')
    arq.write(create_units(lang='bz'))
    arq.write(create_prefixes(lang='bz'))
    arq.write(create_rules(conjunction='i', preposition='di un', lang='bz'))
    arq.close()

    arq = open('pt_units_and_prefixes.sor', 'w')
    arq.write(create_units(lang='pt'))
    arq.write(create_prefixes(lang='pt'))
    arq.write(create_rules(conjunction='e', preposition='de um', lang='pt'))
    arq.close()

    arq = open('en_units_and_prefixes.sor', 'w')
    arq.write(create_units(lang='en'))
    arq.write(create_prefixes(lang='en'))
    arq.write(create_rules(conjunction='and', preposition='of one', lang='en'))
    arq.close()

    arq = open('en_misali_units_and_prefixes.sor', 'w')
    arq.write(create_units(lang='en'))
    arq.write(create_prefixes(lang='en'))
    arq.write(create_rules(conjunction='and', preposition='of one'))
    arq.close()
