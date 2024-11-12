
const sezimal_calculator_en_text = {
    'button-base-ten': 'dec',
    'button-base-six': 'sez',
    'translation-txt': 'txt',
    'translation-nif': 'nif',

    'translation-display-mod': 'mod',
    'translation-display-turn': 'trn',
    'translation-display-arcmin': '′',
    'translation-display-arcsec': '″',
    'translation-display-gon': 'gon',
    'translation-display-rad': 'rad',
    'translation-display-tau_rad': 'τ rad',
    'translation-display-pi_rad': 'π rad',
    'translation-display-deg2': 'deg²',
    'translation-display-deg': '°',
    'translation-display-px_72_dpi': 'px (72 dpi)',
    'translation-display-px_96_dpi': 'px (96 dpi)',
    'translation-display-px_150_dpi': 'px (150 dpi)',
    'translation-display-px_300_dpi': 'px (300 dpi)',
    'translation-display-m/s2': 'm/s²',
    'translation-display-ft/s2': 'ft/s²',
    'translation-display-mmHg': 'mm Hg',
    'translation-display-inHg': 'in Hg',
    'translation-display-g·m/s2': 'g·m/s²',
    'translation-display-lb·ft/s2': 'lb·ft/s²',

    // 'button-sezimal-lsez': 'log₁₀',
    // 'button-sezimal-ldec': 'log₁₄',
    // 'button-decimal-ln': 'log<sub class="constant">𝑒</sub>',
    // 'button-decimal-lsez': 'log₆',
    // 'button-decimal-ldec': 'log₁₀',

    'translation-display-imp-fl-dr': 'fl dr',
    'translation-display-imp-fl-oz': 'fl oz',
    'translation-display-imp-pt': 'pt',
    'translation-display-imp-qt': 'qt',
    'translation-display-imp-gal': 'gal',

    'option-decimal-units-clt-usmpg': 'miles per US gallon – mpg US',
    'option-decimal-units-clt-impmpg': 'miles per gallon – mpg',

    'translation-display-L/100km': 'L/100 km',
    'translation-display-km/20L': 'km/20 L',
    'translation-display-US-mpg': 'mpg US',
    'translation-display-imp-mpg': 'mpg',

    'translation-display-sez': 'sixeniums',
    'translation-display-nif': 'nifeniums',
    'translation-display-ard': 'ardeniums',
    'translation-display-srd': 'sixardeniums',
    'translation-display-nrd': 'nifardeniums',
    'translation-display-xad': 'shadareniums',

    'translation-display-decade': 'decs.',
    'translation-display-century': 'cens.',
    'translation-display-millenium': 'mils.',

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
        <li>[ log<sub class="constant">𝑒</sub> ] - the natural logarithm function button cycles between the functions log<sub class="constant">𝑒</sub>, the constant e, log₁₀/log₆ (sezimal logarithm), log₁₄/log₁₀ (decimal logarithm);</li><br/>
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
                <li>[ <span style="color: #666;">nif</span> ] - no niftimal display;</li>
            </ul>
        </li><br/>
        <li>[ txt ] - enables [ txt ] / disables [ <span style="color: #666;">txt</span> ] the spelling out of the sezimal display (as of now, only for English, Portuguese, Brazilian [phonemic orthography] and Esperanto);</li><br/>
    </ul>
    <p>And the settings buttons on the second display line:</p>
    <ul>
        <li>[ € ] - enables [ € ] / disables [ <span style="color: #666;">€</span> ] - currency mode, where the input is separated by a “currency separator” “󱹶” or “;” that shows that the number represents two independently converted units of monetary value, the currency and the currency’s subunit (euros󱹶cents or euros;cents);</li><br/>
        <li>[ mdl <img src="https://midia.tauga.online/img/sezimal/mandala-logo-black-on-white-small.svg" width="12rem" /> ° ] - angle units for sezimal and decimal trigonometric functions;</li><br/>
        <li>[ <img src="https://midia.tauga.online/img/sezimal/shastadari-logo-black-on-white-small.svg" width="12rem" /> ] - shastadari units and prefixes to and from SI/non SI units and prefixes;</li><br/>
        <li>[ 0󱹮3 ] - how many digits after the sezimal separator results get rounded to; decimal precision is adjusted based on the sezimal precision;</li><br/>
    </ul>
    <h2>Notation used</h2>
    <ul>
        <li>Number names - 0 zero; 1 one; 2 two; 3 three; 4 four; 5 five; 10 six; 11 seven; 12 eight; 13 nine; 14 ten; 15 eleven; 20 tweve; 21 dozen-one; 22 dozen-two; 23 dozen-three; 24 dozen-four; 25 dozen-five; 30 thirsy; 40 foursy; 50 fifsy; 100 nif (from the Ndom language for thirty-six); 1󱹭000 arda (from Sanskrit अर्ध ardha for half, as in half six digits); 10󱹭000 six arda; 100󱹭000 nif arda; 1󱹬000󱹭000 shadara (from Sanskrit षडार ṣaḍāra for a group of six, or a hexagon); from shadara we go for 10󱹬000󱹭000 six shadara, 100󱹬000󱹭000 nif shadara, 1󱹭000󱹬000󱹭000 arda shadara, 10󱹭000󱹬000󱹭000 six arda shadara, 100󱹭000󱹬000󱹭000 nif arda shadara, dishadara 1󱹬000󱹭000󱹬000󱹭000 (di from Sanskrit द्वि dvi for two); trishadara for 10³⁰ (tri from Sanskrit त्रि tri for three); charshadara for 10⁴⁰ (char from Sanskrit चतुर् catur for four); panshadara for 10⁵⁰ (pan from Sanskrit पञ्चन् pañcan, five); shashadara for 10¹⁰⁰ (sha from Sanskrit षष् ṣaṣ for six); use the spell out function to see how to read any sezimal number</li><br/>
        <li>Sezimal separator 󱹮 - a needle shaped dash, pointing upwards, that starts above the base line at half the font’s X height and extends down to the font’s descender depth; it’s Unicode code point is U+F1E6E; compare it to the dot and comma: .󱹮,</li><br/>
        <li>Recurring separator 󱹯 ‥ „ - doubling the radix separator (sezimal or decimal) gives you the recurring separator; for example, the sezimal fraction 1⁄5 can be written 0󱹯1 (0󱹮1̅) = 0󱹮111...; 1⁄11 0󱹯05 = 0󱹮0̅5̅ = 0󱹮050󱹭505...; the decimal fraction 1⁄3 0‥3 (0,3̅) = 0.333...; decimal 1⁄12 0.08‥3 (0.083̅) = 0.083 333...; that last example, without the recurring separator, is ambiguous: is only the 3 recurring, or 08333? For a one character rendering (like on this app), Unicode code points are 󱹯 U+F1E6F, ‥ U+2025 and „ U+201E; the sezimal recurring separator also resembles a ditto mark ".</li><br/>
        <li>Arda separator ⍽ - the same as the narrow no‐break space, Unicode U+202F, is used to mark the first group of three digits<!-- counting from the rightmost position-->, to the left and right of the sezimal separator, and, from there on for each group of six digits, in practice alternating with the Shadara separator;</li><br/>
        <li>Shadara separator 󱹬 - the same basic shape of the sezimal separator, one sixth of it’s size, pointing downwards, extending down from the font’s height, it marks the reading of shadaras each group of six digits in sezimal numbers, both to the left and right of the sezimal separator<!--, allways counting from the rightmost position-->; it’s Unicode codepoint is U+F1E6C; compare it with the straight single quote and the modifier letter vertical line 'ˈ󱹬;</li><br/>
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
    <p/>
    <p/>
`,

};

export { sezimal_calculator_en_text };
