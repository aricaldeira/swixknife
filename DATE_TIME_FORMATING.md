# Date and time formats

Use the function format from the SezimalDate, SezimalTime, SezimalDateTime classes;

    def format(fmt: str, locale: str = None) -> str:

Where:

* fmt: is the string with the formatting characters and text;
* locale: an optional parameter, the ISO639-2 language code, used for the text formats; if not informed, the function will try to use either the system default language or English, in that order.

The Sezimal Date and Time class gives you:

*   Numbers and values that use sezimal base, except where explicitly indicated;
*   Sezimal dates on the [Symmetry454 Calendar](http://individual.utoronto.ca/kalendis/symmetry.htm) using the [Holocene Epoch](https://en.wikipedia.org/wiki/Holocene_calendar);
*   Sezimal times, meaning time of day using sezimal base, where:

*   1 day is divided into 100 36 utas (sezimal hours);
*   1 uta is divided into 100 36 poshas (sezimal minutes);
*   1 posha is divided into 100 36 agrimas (sezimal seconds)
*   1 agrima is divided into 100 36 anugas (sezimal centiseconds);
*   1 anuga is divided into 100 36 bodas (sezimal milliseconds)
*   1 boda is divided into 100 000 000 1 679 616 shaditibodas (sezimal nanoseconds)

Example:

     This page was last rendered on 213211-20-25 01:25:30.441524103005 UTC 2023-12-20 00:59:28.123355 UTC

Sezimal date and time formatting is much like using the [strftime in Python](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior), but uses a extended set of format tags, all starting with #, whereas strftime uses %;

1. Numeric formats
-------------------

### 1.1 Basic numeric format

    #[@Z9↋][?!][*][-​>]XX

        # - required, starts all sezimal format tags;

        XX - required; can be:

            Date

            d - day number with two digits
                (01 – 44 28 for short months, 01 – 55 35 for long months);
            w - weekday number with two digits (01 – 11 7);
            m - month number with two digits (01 – 20 12);
            q - quarter number with one digit (1 – 4);
            y - year number with 10 6 digits and no group separator (-23_2332 -20_000 – 23_2332 20_000);
            dQ - day within quarter with 3 digits
                 (001 – 231 91 for regular years, 001 – 242 98 for leap years);
            dY - day within year with 4 digits (
                 0001 – 1404 364 for regular years, 0001 – 1415 371 for leap years);
            wM - week within month with 1 digit
                 (1 – 4 for short months, 1 – 5 for long months);
            wQ - week within quarter with 2 digits
                 (01 – 21 13 for regular years, 01 – 22 14 for the last quarter on leap years);
            wY - week within year with 3 digits
                 (001 – 124 52 for regular years, 001 – 125 53 for leap years);
            mQ - month within quarter with 1 digit (1 – 3);

            Time

            u - uta, the first sezimal division of the day, the sezimal hour, with 2 digits (00 - 55 36);
            p - posha, the second sezimal division of the day, the sezimal minute, with 2 digits (00 - 55 36);
            a - agrima, the third sezimal division of the day, the sezimal second, with 2 digits (00 - 55 36);
            n - anuga, the fourth sezimal division of the day, the sezimal centisecond, with 2 digits (00 - 55 36);
            b - boda, the fifth sezimal division of the day, the sezimal millisecond, with 2 digits (00 - 55 36);
            x - shaditiboda, the sezimal nanosecond, with 12 8 digits (0000000000 - 55555555 1 679 616);

        @ - optional; uses base 100 36, also known as [niftimal](https://www.seximal.net/hexaseximal);
            with regularized niftimal digits, using diacritics:
                012345
                0̇1̇2̇3̇4̇5̇ (6789AB) ˙ means 1
                0̈1̈2̈3̈4̈5̈ (CDEFGH) ¨ means 2
                0̊1̊2̊3̊4̊5̊ (IJKLMN)  ̊ resembles top part of 󱸃, see below
                0̄1̄2̄3̄4̄5̄ (OPQRST)  ̄ resembles top part of 󱸄, see below
                0̆1̆2̆3̆4̆5̆ (UVWXYZ)  ̆ resembles bottom part of 󱸅, see below;

        Z - optional; uses base 100 36, also known as [niftimal](https://www.seximal.net/hexaseximal),
            using decimal digits from 10 6 up to 13 9,
            and letters from 14 10 up to 100 36:
                012345
                6789AB
                CDEFGH
                IJKLMN
                OPQRST
                UVWXYZ;

        9 - optional; uses decimal base;

        ↋ - optional; uses dozenal (twelve) base with Pitman digits ↊ (14) and ↋ (15);

        ! - optional; uses sezimal digits 󱸀󱸁󱸂󱸃󱸄󱸅 (012345);
            can be used alone, or paired with @ to give:
                󱸀󱸁󱸂󱸃󱸄󱸅 (012345)
                󱸀̇󱸁̇󱸂̇󱸃̇󱸄̇󱸅̇ (6789AB) ˙ means 1
                󱸀̈󱸁̈󱸂̈󱸃̈󱸄̈󱸅̈ (CDEFGH) ¨ means 2
                󱸀̊󱸁̊󱸂̊󱸃̊󱸄̊󱸅̊ (IJKLMN)  ̊ resembles top part of 󱸃
                󱸀̄󱸁̄󱸂̄󱸃̄󱸄̄󱸅̄ (OPQRST)  ̄ resembles top part of 󱸄
                󱸀̆󱸁̆󱸂̆󱸃̆󱸄̆󱸅̆ (UVWXYZ)  ̆ resembles bottom part of 󱸅;

        ? - optional; uses localized digits for some locales (Arabic, Farsi, Hindi etc.);
            can be used alone, or paired with Z, 9 and ↋;

        * - optional; renders an empty string if value is zero;

        - - optional; don’t pad value with zeroes to the left;

        > - optional, only paired with y; only the last 3 digits of the year (2 digits for other bases);

    Examples:
        #y-#m-#d #u:#p:#a        → 213211-20-25 01:25:30
        #>y-#m-#d #u:#p:#a       → 211-20-25 01:25:30
        #!y-#!m-#!d #!u:#!p:#!a  → 󱸂󱸁󱸃󱸂󱸁󱸁-󱸂󱸀-󱸂󱸅 󱸀󱸁:󱸂󱸅:󱸃󱸀
        #@y-#@m-#@d #@u:#@p:#@a  → 1̈2̊1̇-0̈-5̈ 1:5̈:0̊
        #@>y-#@m-#@d #@u:#@p:#@a → 2̊1̇-0̈-5̈ 1:5̈:0̊
        #Zy-#Zm-#Zd #Zu:#Zp:#Za  → DK7-C-H 1:H:I
        #Z>y-#Zm-#Zd #Zu:#Zp:#Za → K7-C-H 1:H:I
        #9-y-#9m-#9d #9u:#9p:#9a → 17575-12-17 01:17:18
        #9>y-#9m-#9d #9u:#9p:#9a → 75-12-17 01:17:18
        #↋-y-#↋m-#↋d #↋u:#↋p:#↋a → 08-10-15 29:0↋:20

### 1.2 Year number with group separator

    #[@Z9↋][!?][S]Y

        # - required, starts all sezimal format tags;

        Y - required; means the full year number with group separator;

        @ - optional; niftimal base with regularized digits, [see above](https://sezimal.tauga.online/index.html#regularized-niftimal-digits);

        Z - optional; niftimal base, [see above](https://sezimal.tauga.online/index.html#niftimal-digits);

        9 - optional; decimal base, [see above](https://sezimal.tauga.online/index.html#decimal-digits);

        ↋ - optional; dozenal base [see above](https://sezimal.tauga.online/index.html#dozenal-digits);

        ! - optional; sezimal digits, [see above](https://sezimal.tauga.online/index.html#sezimal-digits);

        ? - optional; localized digits for some locales (Arabic, Farsi, Hindi etc.), [see above](https://sezimal.tauga.online/index.html#localized-digits);

        S - optional; the group separator, specified when not using the locale’s default; can be:
            _  low line / underscore U+005f
            .  full stop / period U+002e
            ,  comma U+002c
            ˙  dot above U+02d9
            ʼ  comma above / modifier letter apostrophe U+02bc
            ’  typographical apostrophe / right single quotation mark U+2019
            '  apostrophe U+0027
            •  black circle bullet U+2022
            ◦  white circle bullet U+25e6
            or the space characters:
               space U+0020, no-break space U+00a0,
               en quad U+2000, em quad U+2001,
               en space U+2002, em space U+2003,
               three-per-em space U+2004, four-per-em space U+2005,
               six-per-em space U+2006,
               figure space U+2007, punctuation space U+2008,
               thin space U+2009, hair space U+200a,
               narrow no-break space U+202f, medium mathematical space U+205f

    Examples:
        #Y-#m-#d  → 213,211-20-25  (English locale’s default)
        #Y-#m-#d  → 213.211-20-25  (Brazilian locale’s default)
        #Y-#m-#d  → 213 211-20-25  (French locale’s default)
        #_Y-#m-#d → 213_211-20-25
        #,Y-#m-#d → 213,211-20-25
        #.Y-#m-#d → 213.211-20-25
        #'Y-#m-#d → 213'211-20-25_

### 1.3 Time zone offset

    #[:]t

        # - required, starts all sezimal format tags;

        t - required; means the time zone uta and posha offset, preceeded by + or -;

        : - optional; inserts a : between the uta and posha parts of the offset;

    Examples:
        #t  #:t  → +0000  +00:00  (UTC offset)
        #t  #:t  → -0430  -04:30  (America/Sao_Paulo offset)
        #t  #:t  → +2130  +21:30  (Asia/Tokyo offset)
        #t  #:t  → -2130  -21:30  (America/Anchorage offset)

### 1.4 Decimal and dozenal time

    #99[?]u
    #99[?]p
    #99[?]a

        99 - when paired with u, p or a renders the first, second and third divisions of the day,
             using decimal base, dividing 1 day into 244 100 “decimal hours”,
             each “decimal hour” into 244 100 “decimal minutes”,
             and each “decimal minute” into 244 100 “decimal seconds”;
             it’s a sort of [Decimal Time](https://en.wikipedia.org/wiki/Decimal_time#Fractional_days);

        ? - optional; localized digits for some locales (Arabic, Farsi, Hindi etc.), [see above](https://sezimal.tauga.online/index.html#localized-digits);

    #↋↋[?]u
    #↋↋[?]p
    #↋↋[?]a

        ↋↋ - when paired with u, p or a renders the first, second and third divisions of the day,
             using dozenal base, dividing 1 day into 400 144 “dozenal hours”,
             each “dozenal hour” into 400 144 “dozenal minutes”,
             and each “dozenal minute” into 400 144 “dozenal seconds”;

        ? - optional; localized digits for some locales (Arabic, Farsi, Hindi etc.), [see above](https://sezimal.tauga.online/index.html#localized-digits);

    Examples:
        #u-#p-#a UTC (0.#u#p#a day)             → 01-25-30 UTC (0.012_530 day)
        #99u-#99p-#99a UTC (0.#99u#99p#99a day) → 04-12-97 UTC (0.041_297 day)
        #↋↋u-#↋↋p-#↋↋a UTC (0.#↋↋u#↋↋p#↋↋a day) → 05-↋4-42 UTC (0.05↋_442 day)

### 1.4 Seasons and moon phases change/event time

    #T[@Z9↋|99|↋↋][!?][4][SL]

        # - required, starts all sezimal format tags;

        T - required; means the time of the Season or Moon Phase event/change;

        S or
        L - required; means year Season or Moon (Luna) Phase;
            without other options, gives an empty string when there’s
            no Season or Moon Phase change/event on the day, otherwise
            the uta and posha of the change/event, adjusted to the locale’s
            default time zone or other specificed time zone;

        S - uses the traditional Western 4 Seasons plus the [Cross-Quarters](https://en.wikipedia.org/wiki/Quarter_days),
            the middle of the transition between each of the 4 main Seasons;

        L - uses the traditional 4 Phases, plus the middle of the
            transition between each of the 4 main Phases;

        @ - optional; niftimal base with regularized digits, [see above](https://sezimal.tauga.online/index.html#regularized-niftimal-digits);

        Z - optional; niftimal base, [see above](https://sezimal.tauga.online/index.html#niftimal-digits);

        9 - optional; decimal base, [see above](https://sezimal.tauga.online/index.html#decimal-digits);

        ↋ - optional; dozenal base [see above](https://sezimal.tauga.online/index.html#dozenal-digits);

        99 - optional; decimal time and decimal base, [see above](https://sezimal.tauga.online/index.html#decimal-time);

        ↋↋ - optional; dozenal time and dozenal base, [see above](https://sezimal.tauga.online/index.html#dozenal-time);

        ! - optional; sezimal digits, [see above](https://sezimal.tauga.online/index.html#sezimal-digits);

        ? - optional; localized digits for some locales (Arabic, Farsi, Hindi etc.), [see above](https://sezimal.tauga.online/index.html#localized-digits);

        4 − optional; ignores the Seasons Cross-Quarters and the
            Intermediary Moon Phases, using only the 4 main Seasons
            and 4 main Moon Phases;

2. Text and emoji formats
--------------------------

### 2.1 Basic text format

    #[@123][!?>][MW]

        # - required, starts all sezimal format tags;

        M or
        W - required; means the Month or the Weekday;
            without other options, gives the locale’s full month or weekday name;

        @ − optional; gives the locale’s abreviated month or weekday name;

        1 − optional; gives the first letter of the locale’s month or weekday name;

        2 − optional; gives the first two letters of the locale’s month or weekday name;

        3 − optional; gives the first three letters of the locale’s month or weekday name;

        ! − optional; uses only upper case letters;

        ! − optional; uses only lower case letters;

        > − optional; the first letter is upper case, all others are lower case;

    #O - gives the locale’s ordinal suffix for the day
         (some locales use ordinal dates only for the first day of the month);

    #E - gives the locale’s era abbreviation:
         SHE - Sezimal Human Era for years >= 0;
         BSHE - Before Sezimal Human Era, for years < 0;

    #T - gives the time zone name;

    #[&@][-]V

        # - required, starts all sezimal format tags;

        V - required; means the time zone DST name/status;
            without other options, gives the locale’s short DST name;

        & - optional; means the locale’s DST full name;

        @ - optional; means the locale’s DST status as an emoji,
             usually ⏰🌞;

        - - optional; if the time is not in DST, gives an empty
             string, otherwise, gives the text/emoji preceeded by a space;
             used when #[&@]-V goes right after some other text, and
             the extra space separating the empty format is unwanted;

    Examples:
        #W, #M #d#O, #Y → Wednesday, December 25th, 13,1355
        #@W #@M #d #y → Wed Dec 25 213211
        #W #@W #3W #2W #1W → Wednesday Wed Wed We W
        #M #@M #3M #2M #1M → December Dec Dec De D
        #!W #@!W #3!W #2!W #1!W → WEDNESDAY WED WED WE W
        #!M #@!M #3!M #2!M #1!M → DECEMBER DEC DEC DE D
        #?W #@?W #3?W #2?W #1?W → wednesday wed wed we w
        #?M #@?M #3?M #2?M #1?M → december dec dec de d

### 2.2 Seasons and moon phases text formats

    #[@][~][NS][4][!?>][SL]

        # - required, starts all sezimal format tags;

        S or
        L - required; means year Season or Moon (Luna) Phase;
            without other options, gives an empty string when there’s
            no Season or Moon Phase change/event on the day, otherwise
            otherwise the locale’s Season/Moon Phase name or emoji,
            adjusted to the locale’s Hemisphere;

        S - uses the traditional Western 4 Seasons plus the [Cross-Quarters](https://en.wikipedia.org/wiki/Quarter_days),
            the middle of the transition between each of the 4 main Seasons;

        L - uses the traditional 4 Phases, plus the middle of the
            transition between each of the 4 main Phases;

        @ − optional; gives the locale’s emoji for the Season on Moon Phase;
            Seasons emoji default to:
                ❄️🌷🌞🍂 and
                ❄️〰🌷, 🌷〰🌞, 🌞〰🍂, 🍂〰❄️
            for the Northen Hemisphere, and:
                🌞🍂❄️🌺 and
                🌞〰🍂, 🍂〰❄️, ❄️〰🌺, 🌺〰🌞
            for the Southern Hemisphere;
            Moon Phase emoji are:
                🌑🌒🌓🌔🌕🌖🌗🌘 for the Northern Hemisphere,
                🌑🌘🌗🌖🌕🌔🌓🌒 for the Southern Hemisphere;

        ~ − optional; ongoing Season, meaning it gives the locale’s Season name
            emoji even if the Season change/event is not on the day;

        N or
        S − optional; Northern or Southern Hemisphere; when
            omitted uses the locale’s default Hemisphere;

        4 − optional; ignores the Cross-Quarters and Intermediary Moon Phases,
            using only the 4 main Seasons and the 4 main Moon Phases;

        ! − optional; uses only upper case letters;

        ? − optional; uses only lower case letters;

        > − optional; the first letter is upper case, all others are lower case;

Examples, using English locale:
        #~N4S #@~N4S → Autumn ️🍂
        #~NS #@~NS → Winter Cross-Quarter ️🍂️〰️❄️
        #~S4S #@~S4S → Spring ️🌺
        #~SS #@~SS → Summer Cross-Quarter 🌺️〰️🌞

        #~N4L #@~N4L → First Quarter ️🌓
        #~NL #@~NL → First Quarter ️🌓
        #~S4L #@~S4L → First Quarter ️🌗
        #~SL #@~SL → First Quarter ️🌗


### 2.3 Language specific formatting tokens

Some languages have complex grammar cases, or orthographic rules, that depend on the gender, preposition, first letter(s) of the word, etc.

The following languages have specialized formatting tokens:

### Portuguese

    #$XW

Weekday names are feminine, except sábado (Saturday) and domingo (Sunday); articles and prepositions/conjunctions referring to those weekdays have to change gender accordingly;

To do so, X can be: A, ESSA, ESTA, AQUELA

For sábado and domingo, those get changed to the masculine: o, esse, este, aquele

Otherwise, you get the lowercase feminine versions: a, essa, esta, aquela.

Other contractions: da, na, etc. or gender changing: próxima, última etc. can be achived using: d#$AW, n#$AW, próxim#$AW, últim#$AW etc.

### Italian

    #$XW
    #$XM

Weekday names are masculine, except domenica (Sunday); articles and prepositions/conjunctions referring to those weekdays have to change gender accordingly;

Apart from that, Italian uses contractions of articles and prepositions/conjunctions extensively;

To deal with that, X can be: IL, UN, AL, DEL, NEL, DAL, SUL, COL;

Those get changed to (allways lowercase): l’, un_, all’, dell’, nell’, dall’, sull’, con l’ before aprile, agosto and ottobre (for #$XM, also, notice the space after un, here represented by an underscore);

Those get changed to (allways lowercase, with a space, here represented by an underscore): la_, una_, alla_, della_, nella_, dalla_, sulla_, colla_ before domenica (for #$XW);

Otherwise, they yield (allways lowercase, with a space, here represented by an underscore): il_, un_, al_, del_, nel_, dal_, sul_, col_.

### French

    #$XM

Some words contract or make liaison, depend on wether the next word begins with a vowel or an “H muet”;

To deal with that, X can be: DE, LE, CE;

Those get changed to (allways lowercase): d’, l’, cet before avril, août, octobre;

Otherwise, they get changed to lowercase and add a space, here represented by an underscore, except for ce/cet: de_, le_, ce.

### Catalan

    #$XM

Some words contract or change form, depend on wether the next word begins with a vowel;

To deal with that, X can be: DE, EL;

Those get changed to (allways lowercase): d’, l’ before abril, agost, octubre;

Otherwise, they get changed to lowercase and add a space, here represented by an underscore: de_, el_

### Romanian

    #$XYW
    #$[T]XYM

    T: uses traditional names for months: gerar, făurar, mărțișor, prier, florar, cireșar, cuptor, gustar, răpciune, brumărel, brumar, undrea

Romanian has 5 grammatical cases: nominative, accusative, genitive, dative, vocative; also, the definite article is attached at the end of words, and also declines according to case;

To deal with that, X can be:

* I: with no definite article (indefinite);
* D: with definite article;

And Y can be:

* N: for the nominative case
* G: for the genitive case
* D: for the dative case
* A: for the accusative case
* V: for the vocative case

### Esperanto

    #$W
    #$M

Those render the weekday or month with the final o, or, in other words, you get just the root, so you can attach other grammatical endings or combine those roots using Esperanto’s regular word forming rules;

### Greek

    #$[C]XM
    #$XW

    C: for the colloquial name of the month

Greek uses three main grammatical cases: nominative, genitive, accusative, and, for nouns, there’s also the vocative; apart from that, articles also decline for gender and case;

Another interesting thing about Greek, the names of the months have colloquial forms, slightly different from those more formal ones;

To deal with that, X can be:

* N: for the nominative case
* G: for the genitive case
* A: for the accusative case
* V: for the vocative case

For the declension of articles and the demonstrative pronoun for weekdays, that are all feminine except for Σάββατο (Saturday), that is masculine, you can use:

    #$XYW

Where X can be (all using the Greek alphabet exclusively): Η (Greek letter capital Eta), ΜΊΑ, ΜΙΑ, ΑΥΤΉ, ΑΥΤΗ (without the accent, it will get corrected afterwards);

And Y can be:

* N: for the nominative case
* G: for the genitive case
* A: for the accusative case

Those change to (allways lowercase): ο, του, τον, ένας, έναν, ενός, αυτός, αυτoύ, αυτόν before Σάββατο;

And change to lowercase: η, τη(ν), της, μία, μία(ν), μίας, μια, μια(ν), μιας, αυτή, αυτής, αυτή(ν) for the other days;  the ν gets added before Δευτέρα (Monday);

For the declension of articles and the demonstrative pronoun for months, that are all masculine, you can use:

    #$XYM

Where X can be (all using the Greek alphabet exclusively): Ο (Greek letter capital Omicron), ΈΝΑΣ, ΕΝΑΣ (without the accent, it will get corrected afterwards), ΑΥΤΌΣ, ΑΥΤΟΣ (without the accent, it will get corrected afterwards);

And Y can be:

* N: for the nominative case
* G: for the genitive case
* A: for the accusative case

Those allways change to lowercase: ο, του, το(ν), ένας, ένα(ν), ενός, αυτός, αυτoύ, αυτό(ν), and the ν is ellided before Ιανουάριος, Απρίλιος, Ιούνιος, Ιούλιος, Αύγουστος and Οκτώβριος;

And, finally, Greek uses the ordinal number only for the first day of the month, πρώτη, which is an adjective, like the Romance languages; it is feminine, because it refers to ημέρα (day), that is feminine; it is sometimes written 1η, but, since adjectives also decline, it has to change to ης in the genitive;

To deal with that, you can use:

    #$XO

And X can be:

* N: for the nominative case
* G: for the genitive case
* A: for the accusative case

You’ll get, for day 1, ης for the genitive, and η for the other cases; if the day is not 1, you’ll get an empty string.

### Russian

    #$XW
    #$XM

Russian has six grammatical cases: nominative, genitive, dative, accusative, instrumental and prepositional;

To deal with that, X can be:

* N: for the nominative case
* G: for the genitive case
* D: for the dative case
* A: for the accusative case
* I: for the instrumental case
* P: for the prepositional case

Apart from that, some prepositions get an additional О before words with “difficult” consonant cluster, or, for В, before words beginning with В or Ф; the deal with that, you can use:

    #$XM
    #$XW

Where X can be (all using the Cyrillic alphabet exclusively): В, С, ОТ, К, НАД, ПЕРЕД, ПОД;

They’ll get changed to (allways lowercase): во, со, ото, ко, надо, передо, подо before вто́рник, среда́, воскресе́нье, февра́ль and дека́брь;

    #$ОM

This uses the preposition О (Cyrillic letter capital O), that changes to об before months that begin with a vowel: янва́рь, апре́ль, ию́нь, ию́ль, а́вгуст and октя́брь;

### Polish

    #$XW
    #$XM

Polish has seven grammatical cases: nominative, genitive, dative, accusative, instrumental and locative and vocative;

To deal with that, X can be:

* N: for the nominative case
* G: for the genitive case
* D: for the dative case
* A: for the accusative case
* I: for the instrumental case
* P: for the prepositional case

Also, the prepositions W and Z change to WE and ZE depending on the first letters of the next word; to deal with that, you can use:

    #$WW
    #$WM

This will get you we before wtorek, czwartek and wrzesień, and w otherwise;

    #$ZW
    #$ZM

This will get you ze before środa, sobota, styczeń and sierpień, and z otherwise;

Finally, apparently using Roman Numerals for the months in Polish is a thing, so:

    #$RM

You’ll get I, II, III, VI, V, VI, VII, VIII, IX, X, XI, XII for styczeń, luty, marzec, kwiecień, maj, czerwiec, lipiec, sierpień, wrzesień, październik, listopad and grudzień respectively.
