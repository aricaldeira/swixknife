

from swixknife import *


def create_units(lang='en'):
    if lang == 'pt':
        text = '''#
# Units
#
UNIT-vrx varxa
UNIT-mas massa
UNIT-spt sapta
UNIT-din dina
UNIT-uta uta
UNIT-pox poxa
UNIT-agm agrima
UNIT-ang anuga
UNIT-bod boda
UNIT-avt avríti
UNIT-brx branxa
UNIT-pad pada
UNIT-veg vega
UNIT-tvr tevarã
UNIT-grt guruta
UNIT-ktr quetra
UNIT-ayt aitã
UNIT-vrt várti
UNIT-drv drávia
UNIT-gnt ganata
UNIT-trg taranga
UNIT-bht barruta
UNIT-bal bala
UNIT-bar bara
UNIT-pdn pidana
UNIT-vay váiu
UNIT-pbl pratibala
UNIT-vrc varcha
UNIT-xrm xarama
UNIT-xky xáquia
UNIT-uxn uxuna
UNIT-xkt xakíti
UNIT-svg sanvega
UNIT-jut júti
UNIT-agh agrarra
UNIT-pbv prabava
UNIT-tnv tanava
UNIT-upr upári
UNIT-nad nádi
UNIT-bum búmi
UNIT-agn aguíni
UNIT-prv parivártana
UNIT-kdn cadana
UNIT-idn indana
UNIT-tln telã
UNIT-gtk gatica
UNIT-tap tapa
UNIT-dar dara
UNIT-vdt vijuta
UNIT-atr antarã
UNIT-bad bada
UNIT-vrd viroda
UNIT-gat gata
UNIT-vht varrata
UNIT-upp upapadã
UNIT-dry daraiata
UNIT-pvh pravarra
UNIT-vst vistara
UNIT-mdl mandala
UNIT-gol gola
UNIT-pkx pracaxa
UNIT-dpk dipaca
UNIT-spn sampurna
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
UNIT-atk astaca
UNIT-pvn pavana
UNIT-dul dúli
UNIT-clt chaláti
UNIT-pbt pibáti

EXP-2 quadrado
EXP-² quadrado
EXP-3 cúbico
EXP-³ cúbico
'''

    elif lang == 'bz':
        text = '''#
# Units
#
UNIT-vrx varxa
UNIT-mas masa
UNIT-spt sápita
UNIT-din dina
UNIT-uta uta
UNIT-pox poxa
UNIT-agm agrima
UNIT-ang anuga
UNIT-bod boda
UNIT-avt avriti
UNIT-brx branxa
UNIT-pad pada
UNIT-veg vega
UNIT-tvr tevaran
UNIT-grt guruta
UNIT-ktr ketra
UNIT-ayt aytan
UNIT-vrt varti
UNIT-drv dravya
UNIT-gnt ganata
UNIT-trg taranga
UNIT-bht barruta
UNIT-bal bala
UNIT-bar bara
UNIT-pdn pidana
UNIT-vay vayu
UNIT-pbl pratibala
UNIT-vrc varxa
UNIT-xrm xarama
UNIT-xky xakya
UNIT-uxn uxuna
UNIT-xkt xakiti
UNIT-svg sanvega
UNIT-jut juti
UNIT-agh agrarra
UNIT-pbv prabava
UNIT-tnv tanava
UNIT-upr upari
UNIT-nad nadi
UNIT-bum bumi
UNIT-agn agini
UNIT-prv parivártana
UNIT-kdn kadana
UNIT-idn indana
UNIT-tln telan
UNIT-gtk gatika
UNIT-tap tapa
UNIT-dar dara
UNIT-vdt vijuta
UNIT-atr antaran
UNIT-bad bada
UNIT-vrd viroda
UNIT-gat gata
UNIT-vht varrata
UNIT-upp upapadan
UNIT-dry darayata
UNIT-pvh pravarra
UNIT-vst vistara
UNIT-mdl mandala
UNIT-gol gola
UNIT-pkx prakaxa
UNIT-dpk dipaka
UNIT-spn sanpurna
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
UNIT-atk astaka
UNIT-pvn pavana
UNIT-dul duli
UNIT-clt xalati
UNIT-pbt pibati

EXP-2 kwadradu
EXP-² kwadradu
EXP-3 kúbiku
EXP-³ kúbiku
'''

    elif lang == 'eo':
        text = '''#
# Mezurunuoj
#
UNIT-vrx varŝao
UNIT-mas masao
UNIT-spt saptao
UNIT-din dinao
UNIT-uta utao
UNIT-pox poŝao
UNIT-agm agrimao
UNIT-ang anugao
UNIT-bod bodao
UNIT-avt avritio
UNIT-brx branŝao
UNIT-pad padao
UNIT-veg vegao
UNIT-tvr tevarano
UNIT-grt gurutao
UNIT-ktr ketrao
UNIT-ayt ajtanao
UNIT-vrt vartio
UNIT-drv dravjao
UNIT-gnt ganatao
UNIT-trg tarangao
UNIT-bht bahutao
UNIT-bal balao
UNIT-bar barao
UNIT-pdn pidanao
UNIT-vay vajuo
UNIT-pbl pratibalao
UNIT-vrx varŝao
UNIT-xrm ŝaramao
UNIT-xky ŝakjao
UNIT-uxn uŝunao
UNIT-xkt ŝakitio
UNIT-svg samvegao
UNIT-jut ĝutio
UNIT-agh agrahao
UNIT-pbv prabavao
UNIT-tnv tanavao
UNIT-upr upario
UNIT-nad nadio
UNIT-bum bumio
UNIT-agn aginio
UNIT-prv parivartanao
UNIT-kdn kadanao
UNIT-idn indanao
UNIT-tln telano
UNIT-gtk gatikao
UNIT-tap tapao
UNIT-dar darao
UNIT-vdt vidjutao
UNIT-atr antarano
UNIT-bad badao
UNIT-vrd virodao
UNIT-gat gatao
UNIT-vht vahatao
UNIT-upp upapadano
UNIT-dry darayatao
UNIT-pvh pravahao
UNIT-vst vistarao
UNIT-mdl mandalao
UNIT-gol golao
UNIT-pkx prakaŝao
UNIT-dpk dipakao
UNIT-spn sampurnao
UNIT-p/s per ses
UNIT-p/n per nif
UNIT-p/a per arad
UNIT-p/sa per ses arad
UNIT-p/na per nif arad
UNIT-p/x per ŝadar
UNIT-p/sx per ses ŝadar
UNIT-p/nx per nif ŝadar
UNIT-p/ax per arad ŝadar
UNIT-p/sax per ses arad ŝadar
UNIT-p/nax per nif arad ŝadar
UNIT-p/Dx per diŝadar
UNIT-p/Tx per triŝadar
UNIT-p/Cx per ĉarŝadar
UNIT-p/Px per panŝadar
UNIT-p/Xx per ŝaŝadar
UNIT-atk aŝtakao
UNIT-pvn pavanao
UNIT-dul dulio
UNIT-clt ĉalatio
UNIT-pbt pibatio

EXP-2 kvadrata
EXP-² kvadrata
EXP-3 kuba
EXP-³ kuba
'''

    else:
        text = '''#
# Units
#
UNIT-vrx varsha
UNIT-mas masa
UNIT-spt sapta
UNIT-din dina
UNIT-uta uta
UNIT-pox posha
UNIT-agm agrima
UNIT-ang anuga
UNIT-bod boda
UNIT-avt avriti
UNIT-brx bramsha
UNIT-pad pada
UNIT-veg vega
UNIT-tvr tevaran
UNIT-grt guruta
UNIT-ktr ketra
UNIT-ayt aytan
UNIT-vrt varti
UNIT-drv dravya
UNIT-gnt ganata
UNIT-trg taranga
UNIT-bht bahuta
UNIT-bal bala
UNIT-bar bara
UNIT-pdn pidana
UNIT-vay vayu
UNIT-pbl pratibala
UNIT-vrc varcha
UNIT-xrm sharama
UNIT−xky shakya
UNIT-uxn ushuna
UNIT-xkt shakiti
UNIT-svg samvega
UNIT-jut juti
UNIT-agh agraha
UNIT-pbv prabava
UNIT-tnv tanava
UNIT-upr upari
UNIT-nad nadi
UNIT-bum bumi
UNIT-agn agini
UNIT-prv parivartana
UNIT-kdn kadana
UNIT-idn indana
UNIT-tln telan
UNIT-gtk gatika
UNIT-tap tapa
UNIT-dar dara
UNIT-vdt vidyuta
UNIT-atr antaran
UNIT-bad bada
UNIT-vrd viroda
UNIT-gat gata
UNIT-vht vahata
UNIT-upp upapadan
UNIT-dry darayata
UNIT-pvh pravaha
UNIT-vst vistara
UNIT-mdl mandala
UNIT-gol gola
UNIT-pkx prakasha
UNIT-dpk dipaka
UNIT-spn sampurna
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
UNIT-atk ashtaka
UNIT-pvn pavana
UNIT-dul duli
UNIT-clt chalati
UNIT-pbt pibati

EXP-2 square
EXP-² square
EXP-3 cube
EXP-³ cube
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
                name = name.replace('cha', 'cha')
                name = name.replace('eka', 'eca')
                name = name.replace('panp', 'pamp')

            elif lang == 'bz':
                name = name.replace('shu', 'xu')
                name = name.replace('sha', 'xa')
                name = name.replace('cha', 'xa')

            elif lang == 'eo':
                name = name.replace('shu', 'ŝu')
                name = name.replace('sha', 'ŝa')
                name = name.replace('cha', 'ĉa')

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


def create_rules(conjunction='and', preposition='', lang='', plural_marker='s', exponent_first=True, exponent_plural=''):
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

    PREFIX_RULE = '[ZEDTCPSXNA]{1,3}|[zedtcpsxna]{1,3}'
    UNIT_RULE = '[a-z]{3}'
    PER_UNIT_RULE = 'p/[a-zA-Z]{1,3}'
    EXP_RULE = '[2²3³]'
    # PRECISION_RULE = '[0-5]{1,3}'

#     text = f'''#
# # Rules for units without fractional parts, or only zeroes
# #
# "(SH(-({PREFIX_RULE})?({UNIT_RULE}))(-({PREFIX_RULE})?({UNIT_RULE})-?({PRECISION_RULE})?)?) ([-−]?0*1)([.,󱹮]0*?)?" $(1) $(PREFIX-\\3)$(UNIT-\\4)
# "(SH(-({PREFIX_RULE})?({UNIT_RULE}))(-({PREFIX_RULE})?({UNIT_RULE})-?({PRECISION_RULE})?)?) ([-−]?\\d+0{{8,}})([.,󱹮]0*?)?" $9{preposition}$(PREFIX-\\3)$(UNIT-\\4)s
# "(SH(-({PREFIX_RULE})?({UNIT_RULE}))(-({PREFIX_RULE})?({UNIT_RULE})-?({PRECISION_RULE})?)?) ([-−]?\\d+)([.,󱹮]0*?)?" $9 $(PREFIX-\\3)$(UNIT-\\4)s
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
"SH-({PER_UNIT_RULE}) ([-−]?0+)([.,󱹮]0*)?" $(0) $(cleanup $(UNIT-\1))
"SH-({PER_UNIT_RULE}) ([-−]?0*1)([.,󱹮]0*)?" $(1) $(cleanup $(UNIT-\1))
"SH-({PER_UNIT_RULE}) ([-−]?\d+)([.,󱹮]0*?)?" $(\2) $(cleanup $(UNIT-\1))
"SH-({PER_UNIT_RULE}) ([-−]?\d+[.,󱹮]\d+)" $(\2) $(cleanup $(UNIT-\1))

#
# Rules for units used with fractions
#
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?\d+[/⁄][-−]?\d+)" $(\3){preposition}$(cleanup $(PREFIX-\1)$(UNIT-\2))

#
# Rules for units without fractional parts, or only zeroes
#
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?0+)([.,󱹮]0*)?" $(0) $(cleanup $(PREFIX-\1)$(UNIT-\2){plural_marker})
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?0*1)([.,󱹮]0*)?" $(1) $(cleanup $(PREFIX-\1)$(UNIT-\2))
"SH-({PREFIX_RULE})?({UNIT_RULE}) ([-−]?\d+)([.,󱹮]0*?)?" $(\3) $(cleanup $(PREFIX-\1)$(UNIT-\2){plural_marker})

#
# Exponents - square and cube
#
'''

#     if exponent_first:
#         text = rf'''
# "SH-({PREFIX_RULE})?({UNIT_RULE})({EXP_RULE}) ([-−]?\d+[/⁄][-−]?\d+)" $(\4){preposition}$(EXP-\3) $(cleanup $(PREFIX-\1)$(UNIT-\2))
#
# "SH-({PREFIX_RULE})?({UNIT_RULE})({EXP_RULE}) ([-−]?0+)([.,󱹮]0*)?" $(0) $(EXP-\3){exponent_plural} $(cleanup $(PREFIX-\1)$(UNIT-\2){plural_marker})
# "SH-({PREFIX_RULE})?({UNIT_RULE})({EXP_RULE}) ([-−]?0*1)([.,󱹮]0*)?" $(1) $(EXP-\3) $(cleanup $(PREFIX-\1)$(UNIT-\2))
# "SH-({PREFIX_RULE})?({UNIT_RULE})({EXP_RULE}) ([-−]?\d+)([.,󱹮]0*?)?" $(\4) $(EXP-\3){exponent_plural} $(cleanup $(PREFIX-\1)$(UNIT-\2){plural_marker})
# '''
#     else:
#         text = rf'''
# "SH-({PREFIX_RULE})?({UNIT_RULE})({EXP_RULE}) ([-−]?\d+[/⁄][-−]?\d+)" $(\4){preposition}$(cleanup $(PREFIX-\1)$(UNIT-\2)) $(EXP-\3)
#
# "SH-({PREFIX_RULE})?({UNIT_RULE})({EXP_RULE}) ([-−]?0+)([.,󱹮]0*)?" $(0) $(cleanup $(PREFIX-\1)$(UNIT-\2){plural_marker}) $(EXP-\3){exponent_plural}
# "SH-({PREFIX_RULE})?({UNIT_RULE})({EXP_RULE}) ([-−]?0*1)([.,󱹮]0*)?" $(1) $(cleanup $(PREFIX-\1)$(UNIT-\2)) $(EXP-\3)
# "SH-({PREFIX_RULE})?({UNIT_RULE})({EXP_RULE}) ([-−]?\d+)([.,󱹮]0*?)?" $(\4) $(cleanup $(PREFIX-\1)$(UNIT-\2){plural_marker}) $(EXP-\3){exponent_plural}
# '''


    text += rf'''
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
# "(SH-({UNIT_RULE}) [-−]?\d+)[.,󱹮]({digits_rule})" $1{conjunction}|$3 $(PREFIX-{prefix_negative})$(UNIT-\\2)
# "(SH-{prefix_positive}({UNIT_RULE}) [-−]?\d+)[.,󱹮]({digits_rule})" $1{conjunction}|$3 $(UNIT-\\2)  # cancel shunma/shunti
# "(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?\d+)[.,󱹮]({digits_rule})" $1{conjunction}|$4 $(PREFIX-{div10})$(UNIT-\\3)
#
# '''
        text += rf'''#
# {i} sezimal place{'s' if i > 1 else ''}
#
"(SH-({UNIT_RULE}) [-−]?0+)[.,󱹮]({digits_rule})" $(SH-{prefix_negative}\\2 \\3)
"(SH-{prefix_positive}({UNIT_RULE}) [-−]?0+)[.,󱹮]({digits_rule})" $(SH-\\2 \\3)  # cancel shunma/shunti
"(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?0+)[.,󱹮]({digits_rule})" $(SH-{div10}\\3 \\4)

"(SH-({UNIT_RULE}) [-−]?\d+)[.,󱹮]({digits_rule})" $1{conjunction}|$(SH-{prefix_negative}\\2 \\3)
"(SH-{prefix_positive}({UNIT_RULE}) [-−]?\d+)[.,󱹮]({digits_rule})" $1{conjunction}|$(SH-\\2 \\3)  # cancel shunma/shunti
"(SH-({PREFIX_RULE})({UNIT_RULE}) [-−]?\d+)[.,󱹮]({digits_rule})" $1{conjunction}|$(SH-{div10}\\3 \\4)

'''

    if lang == 'pt':
        text += r'''== cleanup ==

"tapa" grau sezimal \(tapa\)
"tapas" graus sezimais \(tapas\)
(.+)ma([aâàáãä])(.+) \\1m\\2\\3
(.+)ma(r[aâàáãäeêèéẽëiîìíĩïoôòóõöuûùúũüyw])(.+) \\1mar\\2\\3
(.+)ma(s[aâàáãäeêèéẽëiîìíĩïoôòóõöuûùúũüyw])(.+) \\1mas\\2\\3
(.+)ti([iîìíĩï])(.+) \\1t\\2\\3
(.+)ti(r[aâàáãäeêèéẽëiîìíĩïoôòóõöuûùúũüyw])(.+) \\1tir\\2\\3
(.+)ti(s[aâàáãäeêèéẽëiîìíĩïoôòóõöuûùúũüyw])(.+) \\1tis\\2\\3
(.+) \\1
'''

    elif lang == 'bz':
        text += r'''== cleanup ==

"tapa" graw sezimaw \(tapa\)
"tapas" graws sezimays \(tapas\)
(.+)ma([aâàáãä])(.+) \\1m\\2\\3
(.+)ma(r[aâàáãäeêèéẽëiîìíĩïoôòóõöuûùúũüyw])(.+) \\1mar\\2\\3
(.+)ti([iîìíĩï])(.+) \\1t\\2\\3
(.+)ti(r[aâàáãäeêèéẽëiîìíĩïoôòóõöuûùúũüyw])(.+) \\1tir\\2\\3
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
    arq.write(create_rules(conjunction='y', preposition='dun', lang='bz', plural_marker='s', exponent_first=False, exponent_plural='s'))
    arq.close()

    arq = open('pt_units_and_prefixes.sor', 'w')
    arq.write(create_units(lang='pt'))
    arq.write(create_prefixes(lang='pt'))
    arq.write(create_rules(conjunction='e', preposition='de um', lang='pt', plural_marker='s', exponent_first=False, exponent_plural='s'))
    arq.close()

    arq = open('en_units_and_prefixes.sor', 'w')
    arq.write(create_units(lang='en'))
    arq.write(create_prefixes(lang='en'))
    arq.write(create_rules(conjunction='and', preposition='of one', lang='en', plural_marker='s', exponent_first=True, exponent_plural=''))
    arq.close()

    arq = open('en_misali_units_and_prefixes.sor', 'w')
    arq.write(create_units(lang='en'))
    arq.write(create_prefixes(lang='en'))
    arq.write(create_rules(conjunction='and', preposition='of one', plural_marker='s', exponent_first=True, exponent_plural=''))
    arq.close()

    arq = open('eo_units_and_prefixes.sor', 'w')
    arq.write(create_units(lang='eo'))
    arq.write(create_prefixes(lang='eo'))
    arq.write(create_rules(conjunction='kaj', preposition='el unu', plural_marker='j', exponent_first=True, exponent_plural='j'))
    arq.close()
