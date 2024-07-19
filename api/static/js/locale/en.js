
const sezimal_calculator_en_text = {
    'title': 'Sezimal Calculator',
    'button-sezimal-clear': 'C',
    'button-decimal-clear': 'C',
    'button-base-ten': 'dec',
    'button-base-six': 'sez',
    'translation-txt': 'txt',
    'translation-nif': 'nif',

    'translation-sezimal-calculator': 'Sezimal Calculator',
    'label-sezimal-locale': 'Set the locale for number formatting',
    'label-sezimal-places': 'Set the number of sezimal places',
    'label-sezimal-angle': 'Set the angle units’ conversion<br/>for the trigonometric functions',
    'translation-sezimal-units': 'Shastadari Units of Measure',
    'label-sezimal-units': 'Choose which unit you’d like to convert<br/>to and from the Shastadari units,<br/>and see explanations for each unit',

    'translation-turn': 'turn',
    'translation-deg': 'deg',
    'translation-arcmin': 'min',
    'translation-arcseg': 'sec',

    'translation-display-mod': 'mod',
    'translation-display-turn': 'trn',
    'translation-display-deg': '°',
    'translation-display-arcmin': '′',
    'translation-display-arcsec': '″',
    'translation-display-gon': 'gon',
    'translation-display-rad': 'rad',
    'translation-display-tau_rad': 'τ rad',
    'translation-display-pi_rad': 'π rad',

    'button-sezimal-sin': 'sin',
    'button-sezimal-cos': 'cos',
    'button-sezimal-tan': 'tan',
    'button-decimal-sin': 'sin',
    'button-decimal-cos': 'cos',
    'button-decimal-tan': 'tan',

    'translation-display-sin': 'sin',
    'translation-display-asin': 'asin',
    'translation-display-csc': 'csc',
    'translation-display-acsc': 'acsc',
    'translation-display-cos': 'cos',
    'translation-display-acos': 'acos',
    'translation-display-sec': 'sec',
    'translation-display-asec': 'asec',
    'translation-display-tan': 'tan',
    'translation-display-atan': 'atan',
    'translation-display-cot': 'cot',
    'translation-display-acot': 'acot',

    'button-sezimal-ln': 'log<i>ₑ</i>',
    'button-sezimal-lsez': 'log₁₀',
    'button-sezimal-ldec': 'log₁₄',
    'button-decimal-ln': 'log<i>ₑ</i>',
    'button-decimal-lsez': 'log₆',
    'button-decimal-ldec': 'log₁₀',

    'help-setting': `
<h2>What’s this?</h2>
<p>A calculator and base conversion app, between bases sezimal (six) and decimal (ten).</p>
<p>You can use it like a regular decimal calculator, and it will convert the same calculations using sezimal, teaching you how to read the numbers along the way.</p>
<p>By clicking or tapping on each of the displays (sezimal, niftimal, spell out or decimal), you can copy the display’s content to the clipboard.</p>
<h3>Buttons usage</h3>
<p>Some buttons give access to more operations/functions, when you press them a certain number of times in a row:</p>
<ul>
    <li>[ 󱹮 ] / [ . ] / [ , ] - the sezimal separator (according to locale/settings), when pressed two times in a row, or pressed in the fractional part of a number, gives you the recurring digits separator 󱹯 / ‥ / „ (see below more details on notation);</li><br/>
    <li>[ × ] - the multiplication button, pressed two times in a row, gives you the ! factorial operator;</li><br/>
    <li>[ ÷ ] - the division button, pressed two times in a row, gives you the ⁄ fraction slash, that allows you to enter numbers as fractions; pressed again, gives you the mod (modulo) operator;</li><br/>
    <li>[ ^ ] - the exponentiation button cycles between the operations ^ (exponentiation), ² (square), √ (square root), ³ (cube), ∛ (cube root), ^ 1⁄ (arbitrary root), then back to ^ exponentiation;</li><br/>
    <li>[ 󱹱 ] - the per nif button cycles between the operations 󱹱 (per niff 10²), 󱹲 (per arda 10³), 󱹳 (per six arda 10⁴), 󱹴 (per nif arda 10⁵), 󱹵 (per shadara 10¹⁰) - only for sezimal;</li><br/>
    <li>[ % ] - the percent button cycles between the operations % (percent 14²), ‰ (per thousand 14³), ‱ (per myriad/ten thousand 10⁴) - only for decimal;</li><br/>
    <li>[ sen ] - the sine function button cycles between the functions sin, asin, csc, acsc;</li><br/>
    <li>[ cos ] - the cosine function button cycles between the functions cos, acos, sec, asec;</li><br/>
    <li>[ tan ] - the tangent function button cycles between the functions tan, atan, cot, acot;</li><br/>
    <li>[ log<i>ₑ</i> ] - the natural logarithm function button cycles between the functions log<i>ₑ</i>, the constant e, log₁₀/log₆ (sezimal logarithm), log₁₄/log₁₀ (decimal logarithm);</li><br/>
    <li>[ log₁₀ ] - the sezimal logarithm function button cycles between the functions log₁₀/log₆ (sezimal logarithm) and log₁₄/log₁₀ (decimal logarithm);</li><br/>
    <li>[ τ ] - the constant τ button cycles between the constants τ and π;</li>
</ul>
<p>The toggles/settings buttons on the first display line have the following functions:</p>
<ul>
    <li>[ ? ] - shows this help text;</li><br/>
    <li>[ en ] - let’s you select the language and country, that determines how numbers are formatted, and sets the application language;</li><br/>
    <li>[ 3 ] / [ 󱸃 ] - uses regular digits [ 3 ] or sezimal digits [ 󱸃 ] (see more below) for the sezimal and niftimal displays and buttons (decimal allways uses regular digits);</li><br/>
    <li>[ 3󱹬3 ] / [ 󱸃󱹬󱸃 ] - how numbers are grouped and separated:<br/>
        <ul>
            <li>[ 3󱹬3 ] / [ 󱸃󱹬󱸃 ] - sezimal separators (see more below), every three digits;</li><br/>
            <li>[ 3.3 ] / [ 󱸃.󱸃 ] - decimal/traditional separators, according to the selected locale, every three digits;</li><br/>
            <li>[ 4.4 ] / [ 󱸄.󱸄 ] - decimal/traditional separators, according to the selected locale, every four digits (Misali’s seximal.net mode); this also changes, for English, the spelling out of the sezimal display, using six nif and unexian instead of arda and shadara;</li>
        </ul>
    </li><br/>
    <li>[ nif 5̆ ] / [ nif 󱸣 ] - selects the niftimal display/conversion:<br/>
        <ul>
            <li>[ nif 5̆ ] / [ nif 󱸣 ] - niftimal display uses regularized digits (see below);</li><br/>
            <li>[ nif Z ] - niftimal display uses digits 0123456789 and letters from 14 (decimal ten) up;</li><br/>
            <li>[ <span style="text-decoration: line-through;">nif</span> ] - no niftimal display;</li>
        </ul>
    </li><br/>
    <li>[ txt ] - enables [ txt ] / disables [ <span style="text-decoration: line-through;">txt</span> ] the spelling out of the sezimal display (as of now, only for English, Portuguese, Brazilian [phonemic orthography] and Esperanto);</li><br/>
</ul>
<p>And the settings buttons on the second display line:</p>
<ul>
    <li>[ prd ◕ ° ] - angle units for sezimal and decimal trigonometric functions;</li><br/>
    <li>[ ⬢ ] - shastadari units and prefixes to and from SI/non SI units and prefixes;</li><br/>
    <li>[ 0󱹮3 ] - how many digits after the sezimal separator results get rounded to; decimal precision is adjusted based on the sezimal precision;</li><br/>
</ul>
<h2>Notation used</h2>
<ul>
    <li>Number names - 0 zero; 1 one; 2 two; 3 three; 4 four; 5 five; 10 six; 11 seven; 12 eight; 13 nine; 14 ten; 15 eleven; 20 tweve; 21 dozen-one; 22 dozen-two; 23 dozen-three; 24 dozen-four; 25 dozen-five; 30 thirsy; 40 foursy; 50 fifsy; 100 nif (from the Ndom language for thirty-six); 1 000 arda (from Sanskrit अर्ध ardha for half, as in half six digits); 10 000 six arda; 100 000 nif arda; 1󱹬000 000 shadara (from Sanskrit षडार ṣaḍāra for a group of six, or a hexagon); from shadara we go for 10󱹬000 000 six shadara, 100󱹬000 000 nif shadara, 1 000󱹬000 000 arda shadara, 10 000󱹬000 000 six arda shadara, 100 000󱹬000 000 nif arda shadara, dishadara 1󱹬000 000󱹬000 000 (di from Sanskrit द्वि dvi for two); trishadara for 10³⁰ (tri from Sanskrit त्रि tri for three); charshadara for 10⁴⁰ (char from Sanskrit चतुर् catur for four); panshadara for 10⁵⁰ (pan from Sanskrit पञ्चन् pañcan, five); shashadara for 10¹⁰⁰ (sha from Sanskrit षष् ṣaṣ for six); use the spell out function to see how to read any sezimal number</li><br/>
    <li>Sezimal separator 󱹮 - a needle shaped dash, pointing upwards, that starts above the base line at half the font’s X height and extends down to the font’s descender depth; it’s Unicode code point is U+F1E6E; compare it to the dot and comma: .󱹮,</li><br/>
    <li>Recurring separator 󱹯 ‥ „ - doubling the radix separator (sezimal or decimal) gives you the recurring separator; for example, the sezimal fraction 1⁄5 can be written 0󱹯1 (0󱹮1̅) = 0󱹮111...; 1⁄11 0󱹯05 = 0󱹮0̅5̅ = 0󱹮050 505...; the decimal fraction 1⁄3 0‥3 (0,3̅) = 0.333...; decimal 1⁄12 0.08‥3 (0.083̅) = 0.083 333...; that last example, without the recurring separator, is ambiguous: is only the 3 recurring, or 08333? For a one character rendering (like on this app), Unicode code points are 󱹯 U+F1E6F, ‥ U+2025 and „ U+201E;</li><br/>
    <li>Arda separator ⍽ - the same as the narrow no‐break space, Unicode U+202F, is used to mark the first group of three digits to the left and right of the sezimal separator, and, from there on for each group of six digits, in practice alternating with the Shadara separator;</li><br/>
    <li>Shadara separator 󱹬 - the same basic shape of the sezimal separator, one sixth of it’s size, pointing downwards, extending down from the font’s height, it marks the reading of shadaras each group of six digits in sezimal numbers, both to the left and right of the sezimal separator; it’s Unicode codepoint is U+F1E6C; compare it with the straight single quote '󱹬;</li><br/>
    <li>Sezimal digits - 󱸀󱸁󱸂󱸃󱸄󱸅 for 012345; a dedicated representation for sezimal numbers; it’s a featural script, mapping three areas represeting values: <span class="horizontal-flip">◔</span> upper left represents 1, ◔ upper right represents 2, ◒ bottom also represents 2; each digit apart from zero “embraces” or “points to” the areas that sum up to it’s value: <span class="horizontal-flip">◔</span> 󱸁 one; ◔ 󱸂 two; <span class="horizontal-flip">◔</span> + ◔ = ◓ 󱸃 three; ◔ + ◒ = ◕ 󱸄 four; <span class="horizontal-flip">◔</span> + ◔ + ◒ = ● 󱸅 five;</li><br/>
    <li>Regularized niftimal digits - conventional representation of base nif (thirty-six) uses letters for digits from ten up; the regularized representation uses the same basic six digits used to respresent sezimal 012345/󱸀󱸁󱸂󱸃󱸄󱸅 and extends them using five diacritics:<br/>
        <ul>
            <li>+00: 012345 󱸀󱸁󱸂󱸃󱸄󱸅 <span style="font-family: 'Sezimal Mono', monospace;">012345</span></li><br/>
            <li>+10: 0̇1̇2̇3̇4̇5̇ 󱸆󱸇󱸈󱸉󱸊󱸋 <span style="font-family: 'Sezimal Mono', monospace;">6789AB</span></li><br/>
            <li>+20: 0̈1̈2̈3̈4̈5̈ 󱸌󱸍󱸎󱸏󱸐󱸑 <span style="font-family: 'Sezimal Mono', monospace;">CDEFGH</span></li><br/>
            <li>+30: 0̊1̊2̊3̊4̊5̊ 󱸒󱸓󱸔󱸕󱸖󱸗 <span style="font-family: 'Sezimal Mono', monospace;">IJKLMN</span></li><br/>
            <li>+40: 0̄1̄2̄3̄4̄5̄ 󱸘󱸙󱸚󱸛󱸜󱸝 <span style="font-family: 'Sezimal Mono', monospace;">OPQRST</span></li><br/>
            <li>+50: 0̆1̆2̆3̆4̆5̆ 󱸞󱸟󱸠󱸡󱸢󱸣 <span style="font-family: 'Sezimal Mono', monospace;">UVWXYZ</span></li><br/>
            <li>˚ is the top part of 󱸃;  ˉ is the top part of 󱸄; ˘ is from the top part of 󱸅</li>
        </ul>
    </li>
</ul>
<p />
<p />
`,

    //
    // Units
    //
    'td-shastadari-units': 'Shastadari Units of Measure',
    'optgroup-units-no-conversion': 'No conversion',
    'option-units-no-conversion': 'No conversion (plain calculator)',
    'optgroup-units-instructions': 'Instructions',
    'option-units-units': 'Shastari units',
    'option-units-prefixes': 'Shastari prefixes',
    'optgroup-units-mechanics': 'Mechanics',
    'option-units-ang': 'Time',
    'option-units-avt': 'Frequency',
    'option-units-pad': 'Length',
    'option-units-ktr': 'Area',
    'option-units-ayt': 'Volume',
    'option-units-veg': 'Speed',
    'option-units-tvr': 'Acceleration',
    'option-units-drv': 'Mass',
    'option-units-gan': 'Density',
    'option-units-bar': 'Force/weight',
    'option-units-dab': 'Pressure',
    'option-units-kry': 'Energy/work',
    'option-units-xat': 'Power',
    // 'option-units-svg': 'Momentum',
    // 'option-units-pkp': 'Action',
    // 'option-units-pbv': 'Influence',
    // 'option-units-tnv': 'Tension',
    // 'option-units-upr': 'Intensity',
    // 'option-units-nad': 'Dynamic viscosity',
    // 'option-units-bum': 'Kinematic viscosity',
    'optgroup-units-thermodynamics': 'Thermodynamics',
    'option-units-tap': 'Common Temperature',
    'option-units-gtk': 'Thermodynamic temperature',
    'option-units-agn': 'Heat capacity',
    'option-units-idn': 'Heat capacity per mass',
    'option-units-tln': 'Heat capacity per volume',
    'optgroup-units-electromagnetism': 'Electromagnetism',
    'option-units-avx': 'Elec. charge',
    'option-units-dar': 'Elec. current',
    'option-units-vbv': 'Elec. potential difference',
    'option-units-ptr': 'Elec. resistance',
    'option-units-cln': 'Elec. conductance',
    'option-units-prk': 'Elec. inductance',
    'option-units-smi': 'Elec. capacitance',
    'option-units-abv': 'Mag. flux',
    'option-units-vtr': 'Mag. flux density',
    'optgroup-units-angle': 'Angle',
    'option-units-prd': 'Plane angle',
    'option-units-gol': 'Solid angle',
    'optgroup-units-proportion': 'Proportion',
    'option-units-prt': 'Proportion',
    'optgroup-units-data-information': 'Data/information',
    'option-units-atk': 'Storage',
    'option-units-pvn': 'Speed',

    'label-prefix-sezimal': 'Sezimal Prefix',
    'label-prefix-sezimal-angle': 'Sezimal Prefix',
    'label-unit-sezimal': 'Sezimal Unit',
    'label-prefix-decimal': 'Decimal Prefix',
    'label-prefix-decimal-angle': 'Decimal Prefix',
    'label-prefix-decimal-binary': 'Decimal/Binary Prefix',
    'label-unit-decimal': 'Decimal Unit',
    'optgroup-units-generic-shastadari': 'Shastadari',
    'optgroup-units-generic-s-i': 'S.I.',
    'optgroup-units-generic-non-s-i': 'Non-S.I.',
    'optgroup-units-generic-us-uk': 'Imperial/US',
    'optgroup-units-generic-us': 'US',
    'optgroup-units-generic-uk': 'Imperial',
    'optgroup-units-generic-us-fluid': 'US fluid',
    'optgroup-units-generic-us-dry': 'US dry',
    'optgroup-units-generic-uk-fluid': 'Imperial',

    //
    // Sezimal Prefixes
    //
    'option-sezimal-prefix-ndxm': 'NDX – nidishama  – 10¹²⁰',
    'option-sezimal-prefix-nxpm': 'NXP – nishapama  – 10¹¹⁵',
    'option-sezimal-prefix-nxcm': 'NXC – nishacharma – 10¹¹⁴',
    'option-sezimal-prefix-nxtm': 'NXT – nishatrima – 10¹¹³',
    'option-sezimal-prefix-nxdm': 'NXD – nishadima  – 10¹¹²',
    'option-sezimal-prefix-nxem': 'NXE – nishaekama – 10¹¹¹',
    'option-sezimal-prefix-nxm': 'NX – nishama – 10¹¹⁰',
    'option-sezimal-prefix-npm': 'NP – nipama – 10¹⁰⁵',
    'option-sezimal-prefix-ncm': 'NC – nicharma  – 10¹⁰⁴',
    'option-sezimal-prefix-ntm': 'NT – nitrima – 10¹⁰³',
    'option-sezimal-prefix-ndm': 'ND – nidima – 10¹⁰²',
    'option-sezimal-prefix-nem': 'NE – niekama – 10¹⁰¹',
    'option-sezimal-prefix-nm': 'N – nima – 10¹⁰⁰',
    'option-sezimal-prefix-ppm': 'PP – panpama – 10⁵⁵',
    'option-sezimal-prefix-pcm': 'PC – pancharma – 10⁵⁴',
    'option-sezimal-prefix-ptm': 'PT – pantrima  – 10⁵³',
    'option-sezimal-prefix-pdm': 'PD – pandima – 10⁵²',
    'option-sezimal-prefix-pem': 'PE – panekama  – 10⁵¹',
    'option-sezimal-prefix-pxm': 'PX – panshama  – 10⁵⁰',
    'option-sezimal-prefix-cpm': 'CP – charpama  – 10⁴⁵',
    'option-sezimal-prefix-ccm': 'CC – charcharma  – 10⁴⁴',
    'option-sezimal-prefix-ctm': 'CT – chartrima – 10⁴³',
    'option-sezimal-prefix-cdm': 'CD – chardima  – 10⁴²',
    'option-sezimal-prefix-cem': 'CE – charekama – 10⁴¹',
    'option-sezimal-prefix-cxm': 'CX – charshama – 10⁴⁰',
    'option-sezimal-prefix-tpm': 'TP – tripama – 10³⁵',
    'option-sezimal-prefix-tcm': 'TC – tricharma – 10³⁴',
    'option-sezimal-prefix-ttm': 'TT – tritrima  – 10³³',
    'option-sezimal-prefix-tdm': 'TD – tridima – 10³²',
    'option-sezimal-prefix-tem': 'TE – triekama  – 10³¹',
    'option-sezimal-prefix-txm': 'TX – trishama  – 10³⁰',
    'option-sezimal-prefix-dpm': 'DP – dipama – 10²⁵',
    'option-sezimal-prefix-dcm': 'DC – dicharma  – 10²⁴',
    'option-sezimal-prefix-dtm': 'DT – ditrima – 10²³',
    'option-sezimal-prefix-ddm': 'DD – didima – 10²²',
    'option-sezimal-prefix-dem': 'DE – diekama – 10²¹',
    'option-sezimal-prefix-dxm': 'DX – dishama – 10²⁰',
    'option-sezimal-prefix-xpm': 'XP – shapama – 10¹⁵',
    'option-sezimal-prefix-xcm': 'XC – shacharma – 10¹⁴',
    'option-sezimal-prefix-xtm': 'XT – shatrima  – 10¹³',
    'option-sezimal-prefix-xdm': 'XD – shadima – 10¹²',
    'option-sezimal-prefix-xem': 'XE – shaekama  – 10¹¹',
    'option-sezimal-prefix-xm': 'X – shama – 10¹⁰',
    'option-sezimal-prefix-pm': 'P – pama – 10⁵',
    'option-sezimal-prefix-cm': 'C – charma – 10⁴',
    'option-sezimal-prefix-tm': 'T – trima – 10³',
    'option-sezimal-prefix-dm': 'D – dima – 10²',
    'option-sezimal-prefix-em': 'E – ekama – 10¹',
    'option-sezimal-prefix-ei': 'e – ekati – 10⁻¹',
    'option-sezimal-prefix-di': 'd – diti – 10⁻²',
    'option-sezimal-prefix-ti': 't – triti – 10⁻³',
    'option-sezimal-prefix-ci': 'c – charti – 10⁻⁴',
    'option-sezimal-prefix-pi': 'p – panti – 10⁻⁵',
    'option-sezimal-prefix-xi': 'x – shati – 10⁻¹⁰',
    'option-sezimal-prefix-xei': 'xe – shaekati – 10⁻¹¹',
    'option-sezimal-prefix-xdi': 'xd – shaditi – 10⁻¹²',
    'option-sezimal-prefix-xti': 'xt – shatriti – 10⁻¹³',
    'option-sezimal-prefix-xci': 'xc – shacharti – 10⁻¹⁴',
    'option-sezimal-prefix-xpi': 'xp – shapanti – 10⁻¹⁵',
    'option-sezimal-prefix-dxi': 'dx – dishati – 10⁻²⁰',
    'option-sezimal-prefix-dei': 'de – diekati – 10⁻²¹',
    'option-sezimal-prefix-ddi': 'dd – diditi – 10⁻²²',
    'option-sezimal-prefix-dti': 'dt – ditriti – 10⁻²³',
    'option-sezimal-prefix-dci': 'dc – dicharti – 10⁻²⁴',
    'option-sezimal-prefix-dpi': 'dp – dipanti – 10⁻²⁵',
    'option-sezimal-prefix-txi': 'tx – trishati – 10⁻³⁰',
    'option-sezimal-prefix-tei': 'te – triekati – 10⁻³¹',
    'option-sezimal-prefix-tdi': 'td – triditi – 10⁻³²',
    'option-sezimal-prefix-tti': 'tt – tritriti – 10⁻³³',
    'option-sezimal-prefix-tci': 'tc – tricharti – 10⁻³⁴',
    'option-sezimal-prefix-tpi': 'tp – tripanti – 10⁻³⁵',
    'option-sezimal-prefix-cxi': 'cx – charshati – 10⁻⁴⁰',
    'option-sezimal-prefix-cei': 'ce – charekati – 10⁻⁴¹',
    'option-sezimal-prefix-cdi': 'cd – charditi – 10⁻⁴²',
    'option-sezimal-prefix-cti': 'ct – chartriti – 10⁻⁴³',
    'option-sezimal-prefix-cci': 'cc – charcharti – 10⁻⁴⁴',
    'option-sezimal-prefix-cpi': 'cp – charpanti – 10⁻⁴⁵',
    'option-sezimal-prefix-pxi': 'px – panshati – 10⁻⁵⁰',
    'option-sezimal-prefix-pei': 'pe – panekati – 10⁻⁵¹',
    'option-sezimal-prefix-pdi': 'pd – panditi – 10⁻⁵²',
    'option-sezimal-prefix-pti': 'pt – pantriti – 10⁻⁵³',
    'option-sezimal-prefix-pci': 'pc – pancharti – 10⁻⁵⁴',
    'option-sezimal-prefix-ppi': 'pp – panpanti – 10⁻⁵⁵',
    'option-sezimal-prefix-ni': 'n – niti – 10⁻¹⁰⁰',
    'option-sezimal-prefix-nei': 'ne – niekati – 10⁻¹⁰¹',
    'option-sezimal-prefix-ndi': 'nd – niditi – 10⁻¹⁰²',
    'option-sezimal-prefix-nti': 'nt – nitriti – 10⁻¹⁰³',
    'option-sezimal-prefix-nci': 'nc – nicharti – 10⁻¹⁰⁴',
    'option-sezimal-prefix-npi': 'np – nipanti – 10⁻¹⁰⁵',
    'option-sezimal-prefix-nxi': 'nx – nishati – 10⁻¹¹⁰',
    'option-sezimal-prefix-nxei': 'nxe – nishaekati – 10⁻¹¹¹',
    'option-sezimal-prefix-nxdi': 'nxd – nishaditi – 10⁻¹¹²',
    'option-sezimal-prefix-nxti': 'nxt – nishatriti – 10⁻¹¹³',
    'option-sezimal-prefix-nxci': 'nxc – nishacharti – 10⁻¹¹⁴',
    'option-sezimal-prefix-nxpi': 'nxp – nishapanti – 10⁻¹¹⁵',
    'option-sezimal-prefix-ndxi': 'ndx – nidishati – 10⁻¹²⁰',

    //
    // Decimal Prefixes
    //
    'option-decimal-prefix-quetta': 'Q – quetta – 10³⁰',
    'option-decimal-prefix-ronna': 'R – ronna – 10²⁷',
    'option-decimal-prefix-yotta': 'Y – yotta – 10²⁴',
    'option-decimal-prefix-zetta': 'Z – zetta – 10²¹',
    'option-decimal-prefix-exa': 'E – exa – 10¹⁸',
    'option-decimal-prefix-peta': 'P – peta – 10¹⁵',
    'option-decimal-prefix-tera': 'T – tera – 10¹²',
    'option-decimal-prefix-giga': 'G – giga – 10⁹',
    'option-decimal-prefix-mega': 'M – mega – 10⁶',
    'option-decimal-prefix-kilo': 'k – kilo – 10³',
    'option-decimal-prefix-hecto': 'h – hecto – 10²',
    'option-decimal-prefix-deca': 'da – deca – 10¹',
    'option-decimal-prefix-deci': 'd – deci – 10⁻¹',
    'option-decimal-prefix-centi': 'c – centi – 10⁻²',
    'option-decimal-prefix-milli': 'm – milli – 10⁻³',
    'option-decimal-prefix-micro': 'µ – micro – 10⁻⁶',
    'option-decimal-prefix-nano': 'n – nano – 10⁻⁹',
    'option-decimal-prefix-pico': 'p – pico – 10⁻¹²',
    'option-decimal-prefix-femto': 'f – femto – 10⁻¹⁵',
    'option-decimal-prefix-atto': 'a – atto – 10⁻¹⁸',
    'option-decimal-prefix-zepto': 'z – zepto – 10⁻²¹',
    'option-decimal-prefix-yocto': 'y – yocto – 10⁻²⁴',
    'option-decimal-prefix-ronto': 'r – ronto – 10⁻²⁷',
    'option-decimal-prefix-quecto': 'q – quecto – 10⁻³⁰',

    //
    // Binary Prefixes
    //
    'optgroup-units-generic-binary': 'Binary',
    'option-binary-prefix-yobi': 'Yi – yobi – 2⁸⁰',
    'option-binary-prefix-zebi': 'Zi – zebi – 2⁷⁰',
    'option-binary-prefix-exbi': 'Ei – exbi – 2⁶⁰',
    'option-binary-prefix-pebi': 'Ei – pebi – 2⁵⁰',
    'option-binary-prefix-tebi': 'Ti – tebi – 2⁴⁰',
    'option-binary-prefix-gibi': 'Gi – gibi – 2³⁰',
    'option-binary-prefix-mebi': 'Mi – mebi – 2²⁰',
    'option-binary-prefix-kibi': 'Ki – kibi – 2¹⁰',

    //
    // Prefixes
    //
    'unit-prefixes-explanation': `
`,

    //
    // Time - anuga
    //
    'unit-ang-explanation': `
<br/>
<p>Civil time is divided into six units; one day is divided regularly into sixths, and we group those sixths into units as such:</p>
<ul>
    <li>the dina (DEE-nuh), symbol din, corresponding to day itself;</li>
    <li>the uta (OO-tuh), symbol uta, corresponding to the first two divisions, closer to the hour;</li>
    <li>the posha (POH-shuh), symbol pox, corresponding to the next two divisions, closer to the minute;</li>
    <li>the agrima (uh-GREE-muh), symbol agm, corresponding to the next two divisions, closer to the second;</li>
    <li>the anuga (uh-NOO-guh), symbol ang, corresponding to the next two divisions, closer to the centisecond;</li>
    <li>the boda (BOH-duh), symbol bod, corresponding to the last two divisions, closer to the millisecond;</li>
</ul>
<p>So, one day is divided:</p>
<p style="text-align: center;"><span style="color: #9E9E9E;">5.</span><span style="font-size: 16pt; font-weight: bold;">55:55:55</span><span style="color: #9E9E9E;">:55:55</span></p>
<p style="text-align: center;" class="mono-text"><span style="color: #9E9E9E;">   5 .  </span><span style="font-weight: bold;">55 :    55 :     55</span><span style="color: #9E9E9E;"> :    55 :   55</span></p>
<p style="text-align: center;" class="mono-text"><span style="color: #9E9E9E;">dina . </span><span style="font-weight: bold;">uta : posha : agrima</span><span style="color: #9E9E9E;"> : anuga : boda</span></p>
<p>Prefixes can be used with any of the units of time, and the conversion between the units and prefixes is done as follows:</p>
<table class="explanation">
    <colgroup>
        <col span="1" style="width: 10%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
    </colgroup>
    <tr>
        <td style="text-align: center;">―</td>
        <td style="text-align: center;">din</td>
        <td style="text-align: center;">uta</td>
        <td style="text-align: center;">pox</td>
        <td style="text-align: center;">agm</td>
        <td style="text-align: center;"><b>ang</b></td>
        <td style="text-align: center;">bod</td>
    </tr>
    <tr>
        <td style="text-align: center;">din</td>
        <td style="text-align: right;">1 din</td>
        <td style="text-align: right;">100 uta</br>1 Duta</td>
        <td style="text-align: right;">10⁴ pox</br>1 Cpox</td>
        <td style="text-align: right;">10¹⁰ agm</br>1 Xagm</td>
        <td style="text-align: right;"><b>10¹² ang</br>1 XDang</b></td>
        <td style="text-align: right;">10¹⁴ bod</br>1 XCbod</td>
    </tr>
    <tr>
        <td style="text-align: center;">uta</td>
        <td style="text-align: right;">0.01 din</br>1 ddin</td>
        <td style="text-align: right;">1 uta</td>
        <td style="text-align: right;">100 pox</br>1 Dpox</td>
        <td style="text-align: right;">10⁴ agm</br>1 Cagm</td>
        <td style="text-align: right;"><b>10¹⁰ ang</br>1 Xang</b></td>
        <td style="text-align: right;">10¹² bod</br>1 XDbod</td>
    </tr>
    <tr>
        <td style="text-align: center;">pox</td>
        <td style="text-align: right;">10⁻⁴ din</br>1 cdin</td>
        <td style="text-align: right;">0.01 uta</br>1 duta</td>
        <td style="text-align: right;">1 pox</td>
        <td style="text-align: right;">100 agm</br>1 Dagm</td>
        <td style="text-align: right;"><b>10⁴ ang</br>1 Cang</b></td>
        <td style="text-align: right;">10¹⁰ bod</br>1 Xbod</td>
    </tr>
    <tr>
        <td style="text-align: center;">agm</td>
        <td style="text-align: right;">10⁻¹⁰ din</br>1 xdin</td>
        <td style="text-align: right;">10⁻⁴ uta</br>1 cuta</td>
        <td style="text-align: right;">0.01 pox</br>1 dpox</td>
        <td style="text-align: right;">1 agm</td>
        <td style="text-align: right;"><b>100 ang</br>1 Dang</b></td>
        <td style="text-align: right;">10⁴ bod</br>1 Cbod</td>
    </tr>
    <tr>
        <td style="text-align: center;"><b>ang</b></td>
        <td style="text-align: right;"><b>10⁻¹² din</br>1 xddin</b></td>
        <td style="text-align: right;"><b>10⁻¹⁰ uta</br>1 xuta</b></td>
        <td style="text-align: right;"><b>10⁻⁴ pox</br>1 cpox</b></td>
        <td style="text-align: right;"><b>0.01 agm</br>1 dagm</b></td>
        <td style="text-align: right;"><b>1 ang</b></td>
        <td style="text-align: right;"><b>100 bod</br>1 Dbod</b></td>
    </tr>
    <tr>
        <td style="text-align: center;">bod</td>
        <td style="text-align: right;">10⁻¹⁴ din</br>1 xcdin</td>
        <td style="text-align: right;">10⁻¹² uta</br>1 xduta</td>
        <td style="text-align: right;">10⁻¹⁰ pox</br>1 xpox</td>
        <td style="text-align: right;">10⁻⁴ agm</br>1 cagm</td>
        <td style="text-align: right;"><b>0.01 ang</br>1 dang</b></td>
        <td style="text-align: right;">1 bod</td>
    </tr>
</table>
<p></p>
<p>The name of each of the units come from the following Sanskrit words:</p>
<ul>
    <li><span class="devanagari-word">दिन</span> ‹dina› /'d̪i.nə/: Day, cognate with Latin <i>diēs</i>;</li>
    <li><span class="devanagari-word">उत्थानम्</span> ‹utthānam› /ut̪'t̪ʰɑː.nəm/: Lift up;</li>
    <li><span class="devanagari-word">पोषण</span> ‹poṣaṇa› /'poː.ʂə.ɳə/: Nourishing;</li>
    <li><span class="devanagari-word">अग्रिम</span> ‹agrima› /ə'gri.mə/: Preceding;</li>
    <li><span class="devanagari-word">अनुगामी</span> ‹anugāmī› /ə.nu'gɑː.miː/: Follower;</li>
    <li><span class="devanagari-word">बोध</span> ‹bodha› /'boː.d̪ʰə/: Knowledge;</li>
</ul>
<p></p>
<p>In science, the base sezimal unit of time is the anuga, so all other units that derive from time in any way use the anuga in their definitions.</p>
<p>The formal definition of the anuga is on pair with the S.I. definition of the second, stating that:</p>
<p></p>
<p>   the unperturbed optical 6s ²S<sub>1⁄2</sub> (<i>F</i> = 0) – 5d ²D<sub>3⁄2</sub> (<i>F</i> = 2) transition of the ⁴⁴³Yb⁺ ion has a frequency of <i>f</i><sub>⁴⁴³Yb⁺</sub> = 203 150󱹬505 354󱹬503 234󱹮530 12 avt<sup><a href="#reference_1">1</a></sup>, when expressed in the unit avrita (avt), which is equal to ang⁻¹ (in decimal, ¹⁷¹Yb⁺ and 688,358,979,309,308.24 Hz<sup><a href="#reference_2">2</a></sup>).</p>
<p></p>
<p>Finally, the conversion between anuga and second; we take the average day of 1󱹬504 000 seconds (decimal 86,400), and divide it by the average day of 100󱹬000 000 (decimal 1,679,616) anugas:
</p>
<p>So, 1 ang = <math><mfrac><mn>1󱹬504 000</mn><mn>100󱹬000 000</mn></mfrac></math> = <math><mfrac><mn>41</mn><mn>2 130</mn></mfrac></math> = 0󱹮015 04 s (decimal <math><mfrac><mn>25</mn><mn>486</mn></mfrac></math> = 0.0‥514 403 292 181 069 958 847 736 625);</p>
<p>Conversely, 1 s = <math><mfrac><mn>100󱹬000 000</mn><mn>1󱹬504 000</mn></mfrac></math> = <math><mfrac><mn>2 130</mn><mn>41</mn></mfrac></math> = 31󱹯235 01 ang (decimal <math><mfrac><mn>486</mn><mn>25</mn></mfrac></math> = 19.44);</p>
<p></p>
<p>References:</p>
<p id="reference_1"><sup>1</sup> <a href="https://www.bipm.org/documents/20126/17315032/CIPM2006-EN.pdf/e58fcb97-69f8-008b-050b-378d5f0d8a77">Recommendations adopted by the International Committee for Weights
and Measures, 95th meeting (October 2006) of the CIPM, pages 123–124 of the French version, pages 249–250 (PDF 115–116) of the English version.</a>
</p>
<p id="reference_2"><sup>2</sup> <a href="https://www.bipm.org/documents/20126/69375151/171Yb+_688THz_2021.pdf/6ffc6ec4-76a5-d043-ba4c-af680662fc29">Recommended Values of Standard Frequencies
for Applications Including the Practical Realization
of the Metre and Secondary Representations of the
Definition of the Second, Ytterbium 171 Ion</a>
</p>
`,

    'option-units-ang-dina': 'dina – din = day',
    'option-units-ang-uta': 'uta – uta ~ hour',
    'option-units-ang-posha': 'posha – pox ~ minute',
    'option-units-ang-agrima': 'agrima – agm ~ second',
    'option-units-ang-anuga': 'anuga – ang ~ centisecond',
    'option-units-ang-boda': 'boda – bod ~ millisecond',

    'option-decimal-units-ang-day': 'day',
    'option-decimal-units-ang-hour': 'hour – h',
    'option-decimal-units-ang-minute': 'minute – min',
    'option-decimal-units-ang-second': 'second – s',

    'translation-day': 'day',
    'translation-hour': 'h',
    'translation-minute': 'min',
    'translation-second': 's',

    'unit-avt-explanation': `
<br/>
<p>Frequency is registered using the unit avrita (uh-VREE-tuh), symbol avt, that represents events, cycles, ocurrences etc. per anuga (the base unit of time).</p>
<p>An interesting property of all units envolving time in sezimal, is that is fairly easy to convert between the several units of civil time and the anuga:</p>
<table class="explanation">
    <colgroup>
        <col span="1" style="width: 10%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
        <col span="1" style="width: 15%;">
    </colgroup>
    <tr>
        <td style="text-align: center;">―</td>
        <td style="text-align: center;">Davt</br>per boda</td>
        <td style="text-align: center;">avt</br>per anuga</td>
        <td style="text-align: center;">davt</br>per agrima</td>
        <td style="text-align: center;">cavt</br>per poxa</td>
        <td style="text-align: center;">xavt</br>per uta</td>
        <td style="text-align: center;">xdavt</br>per dina/day</td>
    </tr>
    <tr>
        <td style="text-align: center;">Davt</td>
        <td style="text-align: right;">1 Davt</br>1/bod</td>
        <td style="text-align: right;">100 avt</br>100/ang</td>
        <td style="text-align: right;">10⁴ davt</br>10⁴/agm</td>
        <td style="text-align: right;">10¹⁰ cavt</br>10¹⁰/pox</td>
        <td style="text-align: right;">10¹² xavt</br>10¹²/uta</td>
        <td style="text-align: right;">10¹⁴ xdavt</br>10¹⁴/din</td>
    </tr>
    <tr>
        <td style="text-align: center;">avt</td>
        <td style="text-align: right;">0.01 Davt</br>1/100 bod</td>
        <td style="text-align: right;">1 avt</br>1/ang</td>
        <td style="text-align: right;">100 davt</br>100/agm</td>
        <td style="text-align: right;">10⁴ cavt</br>10⁴/pox</td>
        <td style="text-align: right;">10¹⁰ xavt</br>10¹⁰/uta</td>
        <td style="text-align: right;">10¹² xdavt</br>10¹²/din</td>
    </tr>
    <tr>
        <td style="text-align: center;">davt</td>
        <td style="text-align: right;">10⁻⁴ Davt</br>1/10⁴ bod</td>
        <td style="text-align: right;">0.01 avt</br>1/100 ang</td>
        <td style="text-align: right;">1 davt</br>1/agm</td>
        <td style="text-align: right;">100 cavt</br>100/pox</td>
        <td style="text-align: right;">10⁴ xavt</br>10⁴/uta</td>
        <td style="text-align: right;">10¹⁰ xdavt</br>10¹⁰/din</td>
    </tr>
    <tr>
        <td style="text-align: center;">cavt</td>
        <td style="text-align: right;">10⁻¹⁰ Davt</br>1/10¹⁰ bod</td>
        <td style="text-align: right;">10⁻⁴ avt</br>1/10⁴ ang</td>
        <td style="text-align: right;">0.01 davt</br>1/100 agm</td>
        <td style="text-align: right;">1 cavt<br/>1/pox</td>
        <td style="text-align: right;">100 xavt</br>100/uta</td>
        <td style="text-align: right;">10⁴ xdavt</br>1/10⁴ din</td>
    </tr>
    <tr>
        <td style="text-align: center;">xavt</td>
        <td style="text-align: right;">10⁻¹² Davt</br>1/10¹² bod</td>
        <td style="text-align: right;">10⁻¹⁰ avt</br>1/10¹⁰ ang</td>
        <td style="text-align: right;">10⁻⁴ davt</br>1/10⁴ agm</td>
        <td style="text-align: right;">0.01 cavt</br>1/100 pox</td>
        <td style="text-align: right;">1 xavt<br/>1/uta</td>
        <td style="text-align: right;">100 dxavt</br>100/din</td>
    </tr>
    <tr>
        <td style="text-align: center;">xdavt</td>
        <td style="text-align: right;">10⁻¹⁴ Davt</br>1/10¹⁴ bod</td>
        <td style="text-align: right;">10⁻¹² avt</br>1/10¹² ang</td>
        <td style="text-align: right;">10⁻¹⁰ davt</br>1/10¹⁰ agm</td>
        <td style="text-align: right;">10⁻⁴ cavt</br>1/10⁴ pox</td>
        <td style="text-align: right;">0.01 xavt</br>1/100 uta</b></td>
        <td style="text-align: right;">1 xdavt<br/>1/din</td>
    </tr>
</table>
<br/>
`,

    'option-units-avt-avrita': 'avrita – avt',
    'option-decimal-units-avt-hertz': 'Hertz – Hz',
    'option-decimal-units-avt-rpm': 'rpm',

    'unit-pad-explanation': `
<p>The pada (PAH-duh), symbol pad, is the unit of measure of length using the sezimal base;</p>

<p>It’s formally defined as the distance travelled by light in <math><mfrac><mn>1</mn><mn>135 005󱹬235 440</mn></mfrac></math> of one anuga (<math><mfrac><mn>41</mn><mn>2 130</mn></mfrac></math> s, see the formal anuga definition on the time units page).</p>

<p>Conversion to and from the S.I. is given by taking the S.I. speed of light of 45 425󱹬332 014 (decimal 299,792,458) m/s, dividing it by it’s equivalent using Shastadari units, that is 135 005󱹬235 440 (decimal 594,838,032) pad/ang (see the page about speed units), then multiplying it by the conversion of anugas to seconds (see the time units page):</p>

<p class="center">1 pad = <math><mfrac><mn>45 425󱹬332 014</mn><mn>135 005󱹬235 440</mn></mfrac></math> × <math><mfrac><mn>41</mn><mn>2 130</mn></mfrac></math> = <math><mfrac><mn>1󱹬415 503󱹬524 325</mn><mn>150󱹬223 042󱹬430 000</mn></mfrac></math><br/>= 0󱹮005 333󱹬324 241󱹬020 132 m
<br/>(decimal <math><mfrac><mn>3,747,405,725</mn><mn>144,545,641,776</mn></mfrac></math> = 0.025 925 414 830 613 m)</p>
<p></p>

<p>Another way to get to same conversion rate is by taking Earth’s <b>average</b> gravity’s acceleration (gravity’s acceleration is neither constant, neither 13󱹮450 123 (decimal 9.806 65) m/s² on all of the planet’s surface), calculated<sup><a href="#reference_1">1</a></sup> as 13󱹮444 135󱹬140 131󱹬050 515 (decimal 9.797 566 850 130 385) m/s², and multiply that value by the conversion of the anuga to the second, squared:</p>
<p>Taking the gravity’s acceleration in fraction form:</p>
<p class="center">1 g<sub>avg</sub> = <math><mfrac><mn>5󱹬324 444󱹬301 513</mn><mn>322 545󱹬201 312</mn></mfrac></math> = 13󱹮444 135󱹬140 131󱹬050 515 m/s²</p>
<p class="center">(decimal <math><mfrac><mn>12,141,594,549</mn><mn>1,239,245,900</mn></mfrac></math> = 9.797 566 850 130 385 m/s²)</p>
<p class="center"><math><mfrac><mn>5󱹬324 444󱹬301 513</mn><mn>322 545󱹬201 312</mn></mfrac></math> × <math><msup><mrow><mo>(</mo><mfrac><mn>41</mn><mn>2 130</mn></mfrac><mo>)</mo></mrow><mn>2</mn></msup></math> = <math><mfrac><mn>1󱹬415 503󱹬524 325</mn><mn>150󱹬223 042󱹬430 000</mn></mfrac></math><br/>= 0󱹮005 333󱹬324 241󱹬020 132 m
<br/>(decimal <math><mfrac><mn>3,747,405,725</mn><mn>144,545,641,776</mn></mfrac></math> = 0.025 925 414 830 613 m)</p>
<p>This means that the pada is also the distance that, on Earth, on average, an object travels on a free fall during one anuga, due to the acceleration of gravity, which is 1 pad/ang² (see more on the units of acceleration page).</p>
<p></p>
<p>References:</p>
<p id="reference_1"><sup>1</sup> <a href="https://primelmetrology.atlassian.net/wiki/x/pAB9">Primel Metrology - Second Mundane Reality: Acceleration due to Earth’s Gravity</a>
</p>
<p></p>
`,
    'option-units-pad-pada': 'pada – pad',
    'option-decimal-units-pad-meter': 'metre – m',
    'option-decimal-units-pad-mile': 'mile – ml',
    'option-decimal-units-pad-yard': 'yard – yd',
    'option-decimal-units-pad-foot': 'foot – ft',
    'option-decimal-units-pad-inch': 'inch – in',

    'unit-ktr-explanation': `
<p>
Since the unit of length is the pada (PAH-duh), symbol pad, the unit of area is the square pada, pad²; because using prefixes with compound units (like pad·pad) can be confusing, in that 1 Dpad² is not 100 pad², but instead 10 000 pad², we define a special name for the unit of area, namely the ketra (KAY-truh), symbol ktr, that is equal to pad²;
</p>
<p>Some common prefix equivalences between ktr and pad²:</p>
<table>
    <colgroup>
        <col span="1" style="width: 45%;">
        <col span="1" style="width: 10%;">
        <col span="1" style="width: 45%;">
    </colgroup>
    <tr><td style="text-align: right;">1 ktr</td>          <td style="text-align: center;">=</td> <td style="text-align: left;">1 pad²</td></tr>
    <tr><td style="text-align: right;">1 Ektr</td>         <td style="text-align: center;">=</td> <td style="text-align: left;">10 pad²</td></tr>
    <tr><td style="text-align: right;">1 <b>D</b>ktr</td>  <td style="text-align: center;">=</td> <td style="text-align: left;">1 <b>E</b>pad²</td></tr>
    <tr><td style="text-align: right;">1 Tktr</td>         <td style="text-align: center;">=</td> <td style="text-align: left;">10 Epad²</td></tr>
    <tr><td style="text-align: right;">1 <b>C</b>ktr</td>  <td style="text-align: center;">=</td> <td style="text-align: left;">1 <b>D</b>pad²</td></tr>
    <tr><td style="text-align: right;">1 Pktr</td>         <td style="text-align: center;">=</td> <td style="text-align: left;">10 Dpad²</td></tr>
    <tr><td style="text-align: right;">1 <b>X</b>ktr</td>  <td style="text-align: center;">=</td> <td style="text-align: left;">1 <b>T</b>pad²</td></tr>
    <tr><td style="text-align: right;">1 XEktr</td>        <td style="text-align: center;">=</td> <td style="text-align: left;">10 Tpad²</td></tr>
    <tr><td style="text-align: right;">1 <b>XD</b>ktr</td> <td style="text-align: center;">=</td> <td style="text-align: left;">1 <b>C</b>pad²</td></tr>
    <tr><td style="text-align: right;">1 XTktr</td>        <td style="text-align: center;">=</td> <td style="text-align: left;">10 Cpad²</td></tr>
    <tr><td style="text-align: right;">1 <b>XC</b>ktr</td> <td style="text-align: center;">=</td> <td style="text-align: left;">1 <b>P</b>pad²</td></tr>
    <tr><td style="text-align: right;">1 XPktr</td>        <td style="text-align: center;">=</td> <td style="text-align: left;">10 Ppad²</td></tr>
    <tr><td style="text-align: right;">1 <b>DX</b>ktr</td> <td style="text-align: center;">=</td> <td style="text-align: left;">1 <b>X</b>pad²</td></tr>
</table>
<p></p>
`,
    'option-units-ktr-ketra': 'ketra – ktr',
    'option-units-ktr-sq-pada': 'sq. pada – pad²',
    'option-decimal-units-ktr-sq-meter': 'sq. metre – m²',
    'option-decimal-units-ktr-are': 'are - a',
    'option-decimal-units-ktr-acre': 'acre - ac',
    'option-decimal-units-ktr-sq-mile': 'sq. mile – ml²',
    'option-decimal-units-ktr-sq-yard': 'sq. yard – yd²',
    'option-decimal-units-ktr-sq-foot': 'sq. foot – ft²',
    'option-decimal-units-ktr-sq-inch': 'sq. inch – in²',

    'option-units-ayt-aytan': 'aytan – ayt',
    'option-units-ayt-cb-pad': 'cb.pada – pad³',
    'option-decimal-units-ayt-cb-meter': 'cb. metre – m³',
    'option-decimal-units-ayt-liter': 'litre – L',
    'option-decimal-units-ayt-cb-mile': 'cb. mile – ml³',
    'option-decimal-units-ayt-cb-yard': 'cb. yard – yd³',
    'option-decimal-units-ayt-cb-foot': 'cb. foot – ft³',
    'option-decimal-units-ayt-cb-inch': 'cb. inch – in³',

    'option-decimal-units-ayt-us-fl-dr': 'US dram  – US fl dr',
    'option-decimal-units-ayt-us-tsp': 'US tea spoon – US tsp',
    'option-decimal-units-ayt-us-tbsp': 'US table spoon – US tbsp',
    'option-decimal-units-ayt-us-fl-oz': 'US ounce - US fl oz',
    'option-decimal-units-ayt-us-cup': 'US cup – US cup',
    'option-decimal-units-ayt-us-pt': 'US pint – US pt',
    'option-decimal-units-ayt-us-qt': 'US quarter – US qt',
    'option-decimal-units-ayt-us-gal': 'US gallon – US gal',
    'option-decimal-units-ayt-us-pt-dry': 'US pint - US pt dry',
    'option-decimal-units-ayt-us-qt-dry': 'US quarter - US qt dry',
    'option-decimal-units-ayt-us-gal-dry': 'US gallon - US gal dry',
    'option-decimal-units-ayt-us-pk-dry': 'US peck - US pk dry',
    'option-decimal-units-ayt-us-bu-dry': 'US bushel - US bu dry',

    'option-decimal-units-ayt-uk-fl-dr': 'fluid dram - fl dr',
    'option-decimal-units-ayt-uk-fl-oz': 'fluid ounce - fl oz',
    'option-decimal-units-ayt-uk-pt': 'pint - pt',
    'option-decimal-units-ayt-uk-qt': 'quarter - qt',
    'option-decimal-units-ayt-uk-gal': 'gallon - gal',

    'translation-display-UK-fl-dr': 'fl dr',
    'translation-display-UK-fl-oz': 'fl oz',
    'translation-display-UK-pt': 'pt',
    'translation-display-UK-qt': 'qt',
    'translation-display-UK-gal': 'gal',


    'option-decimal-units-prd-prd': 'paridis',
    'option-decimal-units-prd-tau_rad': 'τ radians',
    'option-decimal-units-prd-pi_rad': 'π radians',
    'option-decimal-units-prd-rad': 'radians',
    'option-decimal-units-prd-deg': 'degrees',
    'option-decimal-units-prd-arcmin': 'minutes',
    'option-decimal-units-prd-arcsec': 'seconds',
    'option-decimal-units-prd-turn': 'turns',
    'option-decimal-units-prd-gon': 'gradians (gon)',

};

export { sezimal_calculator_en_text };
