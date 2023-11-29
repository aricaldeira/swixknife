# Date and time formats

Use the function format from the SezimalDate, SezimalTime, SezimalDateTime classes;

    def format(fmt: str, lang: str = None) -> str:

Where:

* **fmt**: is the string with the formatting characters and text;
* **lang**: an optional parameter, the ISO639-2 language code, used for the text formats; if not informed, the function will try to use either the system default language or English, in that order.

# Date and time numeric formats

    #[@][!][*][-]XX

    @: uses base 100 (compresses each two digits into base 100, see note below)
    !: uses dedicated digits 󱨀󱨁󱨂󱨃󱨄󱨅
    *: renders an empty string if value is zero (most useful with time values)
    -: don’t pad value with zeroes to the left

**XX** can be:

### Date

* **d**: day with 2 digits (01 – 44/55)
* **w**: weekday with 2 digits (01 – 11)
* **m**: month with 2 digits (01 – 20)
* **q**: quarter with 1 digit (1 – 4)
* **y**: month with 10 digits (00_0000 – 55_5555)
* **dQ**: day in quarter with 3 digits (001 – 231/242)
* **dY**: day in year with 4 digits (0001 – 1404/1415)
* **wM**: week in month with 1 digit (1 – 4/5)
* **wQ**: week in quarter with 2 digits (1 – 21/22)
* **wY**: week in year with 3 digits (1 – 124/125)
* **mQ**: month in quarter with 1 digit (1 – 3)

### Time

* **u**: uta (₂day) with 2 digits (00 – 55)
* **p**: posha (₄day) with 2 digits (00 – 55)
* **a**: agrima (₁₀day) with 2 digits (00 – 55)
* **n**: anuga (₁₂day) with 2 digits (00 – 55)
* **b**: boda (₁₄day) with 2 digits (00 – 55)
* **e**: ekaditiboda (₃₀day) with 12 digits (0000_0000 – 5555_5555)

### Special case for formatted years

    #[!]Xy

    !: uses dedicated digits 󱨀󱨁󱨂󱨃󱨄󱨅

Formats the year with 10 digits, *55***•***5555*, using **•** as separator;

**•** can be:

* **_**: undescore (U+005f);
* **.**: dot/full stop (U+002e);
* **,**: comma (U+002c);
* **˙**: dot above (U+02d9);
* **ʼ**: modifier letter apostrophe/comma above (U+02bc);
* **’**: typographical apostrophe/right single quotation mark (U+2019);
* **'**: apostrophe \[this is the straight apostrophe\] (U+0027);
* **•**: black circle bullet (U+2022);
* **◦**: open circle bullet (U+25e6);

Or one of the following space characters:

* U+0020: space;
* U+00a0: no-break space;
* U+2000: en quad;
* U+2001: em quad;
* U+2002: en space;
* U+2003: em space;
* U+2004: three-per-em space;
* U+2005: four-per-em space;
* U+2006: six-per-em space;
* U+2007: figure space;
* U+2008: punctuation space;
* U+2009: thin space;
* U+200a: hair space
* U+202f: narrow no-break space
* U+205f: medium mathematical space

### Time zones

* **#t**: time zone in utas/poshas, in the format \[+-\]uu:pp
* **#z**: time zone in utas/poshas, in the format \[+-\]uupp

# Date and time text formats

Those formats depend on the language informed, broadly speaking;

The formatting function will use the specified language, when informed; otherwise, it will try to use the system default locale for weekday and month names, with varying degrees of success;

* **#O**: the ordinal suffix for the day; this is conditioned to language specific rules; for Romance Languages, this is generally used only for the first day of the month; for English: *st*, *nd*, *rd*, *th*; for Portuguese, Spanish, Italian: *º* only for day 1, otherwise empty; for French: *ᵉʳ* only for day 1, otherwise empty;
* **#W**: the name of the weekday (Monday − Sunday);
* **#@W**: the abbreviated (generally to three letters) name of the weekday (Mon – Sun);
* **#M**: the name of the month (January – December);
* **#@M**: the abbreviated (generally to three letters) name of the month (Jan – Dec);
* **#E**: the abbreviation of the name of the era; for English, *SHE* - Sezimal Human Era, for years >= 0, *BSHE* - Before Sezimal Human Era, for years < 0
* **#T**: the name of the time zone;
* **#V**: *DST* if the time zone is using daylight saving time;

# Date spellout formats

Those will use the sezimal_spellout function, and depend on the language informed, and if the language is available for the sezimal_spellout function; for the time being, only English and Portuguese are available;

    #&[oa]XX

    o: uses ordinal number (masculine where applicable)
    a: uses ordinal number (feminine where applicable)

**XX** can be:

### Date

* **d**: day (01 – 44/55)
* **w**: weekday (01 – 11)
* **m**: month (01 – 20)
* **q**: quarter (1 – 4)
* **y**: month (00_0000 – 55_5555)
* **dQ**: day in quarter (001 – 231/242)
* **dY**: day in year (0001 – 1404/1415)
* **wM**: week in month (1 – 4/5)
* **wQ**: week in quarter (1 – 21/22)
* **wY**: week in year (1 – 124/125)
* **mQ**: month in quarter (1 – 3)

### Special case for ordinal days depending on language

    #&Od

Uses the ordinal number for the day, but only if the language in question uses an ordinal suffix with the day in question; for example, for Portuguese/Spanish/Italian/French, it will render primeiro/primero/primo/premier only for day 1, from day 2 and above, it will render dois/dos/due/deux etc. etc.

# Time spellout formats

Those will use the sezimal_spellout function, and depend on the language informed, and if the language is available for the sezimal_spellout function; for the time being, only English and Portuguese are available;

Since the time is measured in several units, the units are also spelled out, using singular and plural where applicable;

    #&[@]X

    @: ignores the unit, spelling out only the number

**X** can be:

* **u**: uta (₂day) (00 – 55)
* **p**: posha (₄day) (00 – 55)
* **a**: agrima (₁₀day) (00 – 55)
* **n**: anuga (₁₂day) (00 – 55)
* **b**: boda (₁₄day) (00 – 55)
* **e**: ekaditiboda (₃₀day) (0000_0000 – 5555_5555)


# ISO/Gregorian date and time formats

The regular Python’s strftime formatting is also available, for the same SezimalDate/SezimalTime/SezimalDateTime, so you can mix freely sezimal formatting tokens with ISO/Gregorian formatting tokens, for instance, to show date in sezimal and gregorian, and time in sezimal and ISO;

    SezimalDateTime.now().format(**#y-#m-#d #u:#p:#a in sezimal date and time == %Y-%d-%d %H:%M:%S in ISO date and time**)

# Language specific formatting tokens

Some languages have complex grammar cases, or orthographic rules, that depend on the gender, preposition, first letter(s) of the word, etc.

The following languages have specialized formatting tokens:

### Portuguese

    #$XW

Weekday names are feminine, except sábado (Saturday) and domingo (Sunday); articles and prepositions/conjunctions referring to those weekdays have to change gender accordingly;

To do so, **X** can be: **A**, **ESSA**, **ESTA**, **AQUELA**

For sábado and domingo, those get changed to the masculine: **o**, **esse**, **este**, **aquele**

Otherwise, you get the lowercase feminine versions: **a**, **essa**, **esta**, **aquela**.

Other contractions: da, na, etc. or gender changing: próxima, última etc. can be achived using: d#$AW, n#$AW, próxim#$AW, últim#$AW etc.

### Italian

    #$XW
    #$XM

Weekday names are masculine, except domenica (Sunday); articles and prepositions/conjunctions referring to those weekdays have to change gender accordingly;

Apart from that, Italian uses contractions of articles and prepositions/conjunctions extensively;

To deal with that, **X** can be: **IL**, **UN**, **AL**, **DEL**, **NEL**, **DAL**, **SUL**, **COL**;

Those get changed to (allways lowercase): **l’**, **un_**, **all’**, **dell’**, **nell’**, **dall’**, **sull’**, **con l’** before aprile, agosto and ottobre (for #$XM, also, notice the space after un, here represented by an underscore);

Those get changed to (allways lowercase, with a space, here represented by an underscore): **la_**, **una_**, **alla_**, **della_**, **nella_**, **dalla_**, **sulla_**, **colla_** before domenica (for #$XW);

Otherwise, they yield (allways lowercase, with a space, here represented by an underscore): **il_**, **un_**, **al_**, **del_**, **nel_**, **dal_**, **sul_**, **col_**.

### French

    #$XM

Some words contract or make liaison, depend on wether the next word begins with a vowel or an “H muet”;

To deal with that, **X** can be: **DE**, **LE**, **CE**;

Those get changed to (allways lowercase): **d’**, **l’**, **cet** before avril, août, octobre;

Otherwise, they get changed to lowercase and add a space, here represented by an underscore, except for **ce**/**cet**: **de_**, **le_**, **ce**.

### Catalan

    #$XM

Some words contract or change form, depend on wether the next word begins with a vowel;

To deal with that, **X** can be: **DE**, **EL**;

Those get changed to (allways lowercase): **d’**, **l’** before abril, agost, octubre;

Otherwise, they get changed to lowercase and add a space, here represented by an underscore: **de_**, **el_**

### Romanian

    #$XYW
    #$[T]XYM

    T: uses traditional names for months: gerar, făurar, mărțișor, prier, florar, cireșar, cuptor, gustar, răpciune, brumărel, brumar, undrea

Romanian has 5 grammatical cases: nominative, accusative, genitive, dative, vocative; also, the definite article is attached at the end of words, and also declines according to case;

To deal with that, **X** can be:

* **I**: with no definite article (indefinite);
* **D**: with definite article;

And **Y** can be:

* **N**: for the nominative case
* **G**: for the genitive case
* **D**: for the dative case
* **A**: for the accusative case
* **V**: for the vocative case

### Esperanto

    #$W
    #$M

Those render the weekday or month with the final **o**, or, in other words, you get just the root, so you can attach other grammatical endings or combine those roots using Esperanto’s regular word forming rules;

### Greek

    #$[C]XM
    #$XW

    C: for the colloquial name of the month

Greek uses three main grammatical cases: nominative, genitive, accusative, and, for nouns, there’s also the vocative; apart from that, articles also decline for gender and case;

Another interesting thing about Greek, the names of the months have colloquial forms, slightly different from those more formal ones;

To deal with that, **X** can be:

* **N**: for the nominative case
* **G**: for the genitive case
* **A**: for the accusative case
* **V**: for the vocative case

For the declension of articles and the demonstrative pronoun for weekdays, that are all feminine except for Σάββατο (Saturday), that is masculine, you can use:

    #$XYW

Where **X** can be (all using the Greek alphabet exclusively): **Η** (Greek letter capital Eta), **ΜΊΑ**, **ΜΙΑ**, **ΑΥΤΉ**, **ΑΥΤΗ** (without the accent, it will get corrected afterwards);

And **Y** can be:

* **N**: for the nominative case
* **G**: for the genitive case
* **A**: for the accusative case

Those change to (allways lowercase): **ο**, **του**, **τον**, **ένας**, **έναν**, **ενός**, **αυτός**, **αυτoύ**, **αυτόν** before Σάββατο;

And change to lowercase: **η**, **τη(ν)**, **της**, **μία**, **μία(ν)**, **μίας**, **μια**, **μια(ν)**, **μιας**, **αυτή**, **αυτής**, **αυτή(ν)** for the other days;  the ν gets added before Δευτέρα (Monday);

For the declension of articles and the demonstrative pronoun for months, that are all masculine, you can use:

    #$XYM

Where **X** can be (all using the Greek alphabet exclusively): **Ο** (Greek letter capital Omicron), **ΈΝΑΣ**, **ΕΝΑΣ** (without the accent, it will get corrected afterwards), **ΑΥΤΌΣ**, **ΑΥΤΟΣ** (without the accent, it will get corrected afterwards);

And **Y** can be:

* **N**: for the nominative case
* **G**: for the genitive case
* **A**: for the accusative case

Those allways change to lowercase: **ο**, **του**, **το(ν)**, **ένας**, **ένα(ν)**, **ενός**, **αυτός**, **αυτoύ**, **αυτό(ν)**, and the ν is ellided before Ιανουάριος, Απρίλιος, Ιούνιος, Ιούλιος, Αύγουστος and Οκτώβριος;

And, finally, Greek uses the ordinal number only for the first day of the month, πρώτη, which is an adjective, like the Romance languages; it is feminine, because it refers to ημέρα (day), that is feminine; it is sometimes written 1η, but, since adjectives also decline, it has to change to ης in the genitive;

To deal with that, you can use:

    #$XO

And **X** can be:

* **N**: for the nominative case
* **G**: for the genitive case
* **A**: for the accusative case

You’ll get, for day 1, ης for the genitive, and η for the other cases; if the day is not 1, you’ll get an empty string.

### Russian

    #$XW
    #$XM

Russian has six grammatical cases: nominative, genitive, dative, accusative, instrumental and prepositional;

To deal with that, **X** can be:

* **N**: for the nominative case
* **G**: for the genitive case
* **D**: for the dative case
* **A**: for the accusative case
* **I**: for the instrumental case
* **P**: for the prepositional case

Apart from that, some prepositions get an additional О before words with “difficult” consonant cluster, or, for В, before words beginning with В or Ф; the deal with that, you can use:

    #$XM
    #$XW

Where **X** can be (all using the Cyrillic alphabet exclusively): **В**, **С**, **ОТ**, **К**, **НАД**, **ПЕРЕД**, **ПОД**;

They’ll get changed to (allways lowercase): **во**, **со**, **ото**, **ко**, **надо**, **передо**, **подо** before вто́рник, среда́, воскресе́нье, февра́ль and дека́брь;

    #$ОM

This uses the preposition **О** (Cyrillic letter capital O), that changes to **об** before months that begin with a vowel: янва́рь, апре́ль, ию́нь, ию́ль, а́вгуст and октя́брь;

### Polish

    #$XW
    #$XM

Polish has seven grammatical cases: nominative, genitive, dative, accusative, instrumental and locative and vocative;

To deal with that, **X** can be:

* **N**: for the nominative case
* **G**: for the genitive case
* **D**: for the dative case
* **A**: for the accusative case
* **I**: for the instrumental case
* **P**: for the prepositional case

Also, the prepositions W and Z change to WE and ZE depending on the first letters of the next word; to deal with that, you can use:

    #$WW
    #$WM

This will get you **we** before wtorek, czwartek and wrzesień, and **w** otherwise;

    #$ZW
    #$ZM

This will get you **ze** before środa, sobota, styczeń and sierpień, and **z** otherwise;

Finally, apparently using Roman Numerals for the months in Polish is a thing, so:

    #$RM

You’ll get I, II, III, VI, V, VI, VII, VIII, IX, X, XI, XII for styczeń, luty, marzec, kwiecień, maj, czerwiec, lipiec, sierpień, wrzesień, październik, listopad and grudzień respectively.

# Note about base 100

So, in the context of the date and time formatting, if you ask for base 100 (36_dec), instead of using letters for the numbers above 13, we use diacritics instead, in the following way:

| Alpha Digits |  Regular Digits | Dedicated Digits | Note |
|:-:|:-:|:-:|-|
| 012345 | 012345 | 󱨀󱨁󱨂󱨃󱨄󱨅 ||
| 6789AB | 0̇1̇2̇3̇4̇5̇ | 󱨀̇󱨁̇󱨂̇󱨃̇󱨄̇󱨅̇ | One dot above  = +10, from 10 to 15 |
| CDEFGH | 0̈1̈2̈3̈4̈5̈ | 󱨀̈󱨁̈󱨂̈󱨃̈󱨄̈󱨅̈ | Two dots above = +20, from 20 to 25 |
| IJKLMN | 0̊1̊2̊3̊4̊5̊ | 󱨀̊󱨁̊󱨂̊󱨃̊󱨄̊󱨅̊ | Ring above (top part of 󱨃) = +30, from 30 to 35 |
| OPQRST | 0̄1̄2̄3̄4̄5̄ | 󱨀̄󱨁̄󱨂̄󱨃̄󱨄̄󱨅̄ | Line above (top part of 󱨄) = +40, from 40 to 45 |
| UVWXYZ | 0̆1̆2̆3̆4̆5̆ | 󱨀̆󱨁̆󱨂̆󱨃̆󱨄̆󱨅̆ | Breve above (bottom part of 󱨅) = +50, from 50 to 55 |
