
import { sezimal_calculator_pt_text } from './pt.js';

const sezimal_calculator_bz_text = Object.assign({}, sezimal_calculator_pt_text, {
    'title': 'Kawkuladora Sezimal',
    'button-sezimal-clear': 'Z',
    'button-decimal-clear': 'Z',
    'button-base-ten': 'des',
    // 'button-base-six': 'sez',
    'translation-txt': 'est',
    'translation-nif': 'nifi',

    'translation-sezimal-calculator': 'Kawkuladora Sezimaw',
    'label-sezimal-locale': 'Defina u lokali pra formatasawn dus númerus',
    'label-sezimal-places': 'Defina a kwantidadi di kazas sezimays',
    'label-sezimal-angle': 'Defina a konversawn di unidadis di ângulu<br/>pras funsoyns trigonométrikas',
    'translation-sezimal-units': 'Unidadis di Medida Xastadari',
    'label-sezimal-units': 'Eskolya kwaw unidadi se kèr konverter<br/>das o pras unidadi Xastadari,<br/>y veja as esplikasawn y orientasawn<br/>sobri kada unidadi',

    'translation-display-mod': 'mód',
    'translation-display-turn': 'vòwta',
    // 'translation-display-deg': '°',
    // 'translation-display-arcmin': '′',
    // 'translation-display-arcsec': '″',
    // 'translation-display-gon': 'gon',
    // 'translation-display-rad': 'rad',
    // 'translation-display-tau_rad': 'τ rad',
    // 'translation-display-pi_rad': 'π rad',
    'translation-display-deg2': 'graw²',

    'button-sezimal-sin': 'sen',
    'button-sezimal-cos': 'kos',
    'button-sezimal-tan': 'tan',
    'button-decimal-sin': 'sen',
    'button-decimal-cos': 'kos',
    'button-decimal-tan': 'tan',

    'translation-display-sin': 'sen',
    'translation-display-asin': 'asen',
    'translation-display-csc': 'ksk',
    'translation-display-acsc': 'aksk',
    'translation-display-cos': 'kos',
    'translation-display-acos': 'akos',
    'translation-display-sec': 'sek',
    'translation-display-asec': 'asek',
    'translation-display-tan': 'tan',
    'translation-display-atan': 'atan',
    'translation-display-cot': 'kot',
    'translation-display-acot': 'akot',


    'help-setting': `
<h2>U ki kyè isu?</h2>
<p>Uma kawkuladora y un konversor di bazi numérika y unidadis di medida, entri as bazis sezimaw (sêys) y desimaw (dèys).</p>
<p>Vose pòdi uzar u aplikativu komu uma kawkuladora desimaw komun, y eli vay konvertendu us káwkulus uzando bazi sezimaw, ensinandu vose komu ler us númerus nu prosèsu.</p>
<p>Klikandu o tokandu in kada un dus mostradoris (sezimaw, nifimaw, estensu o desimaw), u konteudu è kopiadu pra arya di transferensya.</p>
<h3>Uzu dus botoyns</h3>
<p>Awguns botoyns dawn asèsu a máys duma operasawn o funsawn, kwandu presionadus un sèrtu númeru di vezis in sekwensya:</p>
<ul>
    <li>[ 󱹮 ] / [ , ] / [ . ] - u separador sezimaw (di akordu kwas konfigurasoyns o ku lokali), kwandu presionadu duas vezis segidas, o presionadu na parti frasyonarya dun númeru, dá u separador di frasawn rekorrenti (“sézima periódika”) 󱹯 / „ / ‥ (veja máys abaxu detalyis sobri a notasawn);</li><br/>
    <li>[ × ] - u botawn di muwtiplikasawn, presionadu duas vezis segidas, dá u operador ! fatoriaw;</li><br/>
    <li>[ ÷ ] - u botawn di divizawn, presionadu duas vezis segidas, dá a barra di frasoyns ⁄ , ki permiti entrar númerus in formatu di frasawn dirètamenti; presionadu uma tersera vez, dá u operador <i>mód</i> módulu;</li><br/>
    <li>[ ^ ] - u botawn da esponensyasawn awtèrna entri as operasoyns ^ (esponensyasawn), ² (elevadu aw kwadradu), √ (raiz kwadrada), ³ (elevadu aw kubu), ∛ (raiz kúbika), ^ 1⁄ (raiz arbitrarya), y daí di vòwta pra  ^ esponensyasawn;</li><br/>
    <li>[ 󱹱 ] - u botawn di pur nifi awtèrna entri as operasoyns 󱹱 (pur nifi 10²), 󱹲 (pur arda 10³), 󱹳 (pur sêys arda 10⁴), 󱹴 (pur nifi arda 10⁵), 󱹵 (pur xadara 10¹⁰) - sò na bazi sezimaw;</li><br/>
    <li>[ % ] - u botawn di porsentajen awtèrna entri as operasoyns % (pur sentu 14²), ‰ (pur milyar 14³), ‱ (pur miríadi/dèys miw 10⁴) - sò na bazi desimaw;</li><br/>
    <li>[ sen ] - u botawn da funsawn senu awtèrna entri as funsoyns sen, asen, ksk, aksk;</li><br/>
    <li>[ kos ] - u botawn da funsawn kosenu awtèrna entri as funsoyns kos, akos, sek, asek;</li><br/>
    <li>[ tan ] - u botawn da funsawn tanjenti awtèrna entri as funsoyns tan, atan, kot, akot;</li><br/>
    <li>[ log<sub class="constant">𝑒</sub> ] - u botawn da funsawn logarítimu naturaw awtèrna entri as funsoyns log<sub class="constant">𝑒</sub>, a konstanti <span class="constant">𝑒</span>, log₁₀/log₆ (logarítimu sezimaw), log₁₄/log₁₀ (logarítimu desimaw);</li><br/>
    <li>[ log₁₀ ] - u botawn da funsawn logarítimu sezimaw awtèrna entri as funsoyns log₁₀/log₆ (logarítimu sezimaw) y log₁₄/log₁₀ (logarítimu desimaw);</li><br/>
    <li>[ τ ] - u botawn da konstanti τ awtèrna entri as konstantis τ y π;</li>
</ul>
<p>Us botoyns di ajusti na primera liỹa du mostrador teyn as segintis funsoyns:</p>
<ul>
    <li>[ ? ] - mòstra esi testu di ajuda;</li><br/>
    <li>[ en ] - permiti selesyonar u idioma y u paiz, u ki determina komu us númerus vawn ser formatadus, y defini u idioma du aplikativu;</li><br/>
    <li>[ 3 ] / [ 󱸃 ] - uza díjitus komuns [ 3 ] o díjitus sezimays [ 󱸃 ] (veja máys abaxu) prus mostradoris sezimaw y nifimaw, y prus botoyns sezimays (a bazi desimaw senpri uza us díjitus komuns);</li><br/>
    <li>[ 3󱹬3 ] / [ 󱸃󱹬󱸃 ] - determina komu us númerus sawn agrupadus y separadus:<br/>
        <ul>
            <li>[ 3󱹬3 ] / [ 󱸃󱹬󱸃 ] - separadoris sezimays (veja máys abaxu), a kada treys díjitus;</li><br/>
            <li>[ 3.3 ] / [ 󱸃.󱸃 ] - separadoris desimays/tradisyonays, di akordu ku lokali (idioma y paiz) selesyonadus, a kada treys díjitus;</li><br/>
            <li>[ 4.4 ] / [ 󱸄.󱸄 ] - separadoris desimays/tradisyonays, di akordu ku lokali (idioma y paiz) selesyonadus, a kada kwatru díjitus (komu nu sayti seximal.net); isu tanbeyn awtèra, in inglez, u rezuwtadu du mostrador du númeru pur estensu, ki pasa a uzar sêys nifi y uneksiawn nu lugar di arda y xadara;</li>
        </ul>
    </li><br/>
    <li>[ nifi 5̆ ] / [ nifi 󱸣 ] - defini u uzu y konversawn du mostrador nifimaw:<br/>
        <ul>
            <li>[ nifi 5̆ ] / [ nifi 󱸣 ] - u mostrador nifimaw uza díjitus regularizadus (veja abaxu);</li><br/>
            <li>[ nifi Z ] - u mostrator nifimaw uza us díjitus 0123456789 y letras a partir du númeru 14 (in desimaw, dèys);</li><br/>
            <li>[ <span style="text-decoration: line-through;">nifi</span> ] - okuwta u mostrador nifimaw;</li>
        </ul>
    </li><br/>
    <li>[ est ] - ativa [ est ] / desativa [ <span style="text-decoration: line-through;">est</span> ] a ezibisawn dus númerus sezimays pur estensu (pur inkuantu, sòmenti disponívew in brazileru, portugez, inglez y Esperantu);</li><br/>
</ul>
<p>Y us botoyns di ajusti na segunda liỹa du mostrador:</p>
<ul>
    <li>[ mdl ◕ ° ] - unidadis di medida di ângulus pras funsoyns trigonométrikas sezimays y desimays;</li><br/>
    <li>[ ⬢ ] - unidadis y prefiksus Xastadari konvertidus di o pra unidadis y prefiksus du Sistema Internasyonaw di Medidas (y awgumas unidadis tradisyonays fòra du SI);</li><br/>
    <li>[ 0󱹮3 ] - in kwantus díjitus depoys du separador sezimays u rezuwtadu vay ser arredondadu; a presizawn in bazi desimaw vay ser ajustada bazeada na presizawn da bazi sezimaw;</li><br/>
</ul>
<h2>Notasawn uzada</h2>
<ul>
    <li>Nomis dus númerus - 0 zèru; 1 un; 2 doys; 3 treys; 4 kwatru; 5 sinku; 10 sêys; 11 sèti; 12 oytu; 13 nòvi; 14 dèys; 15 onzi; 20 dozi; 21 dozi y un; 22 dozi y doys; 23 dozi y treys; 24 dozi y kwatru; 25 dozi y sinko; 30 treseys; 40 kwaseys; 50 kinseys; 100 nifi (da lingwa ndom <i>nif</i> pra trinta y sêys); 1󱹭000 arda (du sânskritu अर्ध <i>ardha</i> pra meyu, metadi, pra metadi di sêys díjitus); 10󱹭000 sêys arda; 100󱹭000 nifi arda; 1󱹬000󱹭000 xadara (du sânskritu षडार <i>ṣaḍāra</i> prun grupu di sêys, o un ekságonu); di xadara si sègi 10󱹬000󱹭000 sêys xadara, 100󱹬000󱹭000 nifi xadara, 1󱹭000󱹬000󱹭000 arda xadara (in eskala longa, komu in portugez ewropew), 10󱹭000󱹬000󱹭000 sêys arda xadara, 100󱹭000󱹬000󱹭000 nifi arda xadara, dixadara 1󱹬000󱹭000󱹬000󱹭000 (<i>di</i> du sânskritu द्वि <i>dvi</i> pra doys); trixadara pra 10³⁰ (<i>tri</i> du sânskritu त्रि <i>tri</i> pra treys); txarxadara pra 10⁴⁰ (<i>txar</i> du sânskritu चतुर् <i>catur</i> pra kwatru); panxadara pra 10⁵⁰ (<i>pan</i> du sânskritu पञ्चन् <i>pañcan</i>, sinku); xaxadara pra 10¹⁰⁰ (<i>xa</i> du sânskritu षष् <i>ṣaṣ</i> pra sêys); uzi a funsawn di númerus pur estensu pra saber komu ler kwawkèr númeru sezimaw</li><br/>
    <li>Separador sezimaw 󱹮 - uma barra in fòrma di agulya, apontandu pra sima, ki si inisia sobri a liỹa bazi da eskrita, pelu meyu da altura X da fonti, y si estendi pra baxu atè u pontu máys baxu dus desendentis da fonti; sew kódigu Unicode è U+F1E6E; konpari u separador sezimaw kwa vírgula y u pontu: ,󱹮.</li><br/>
    <li>Separador periódiko 󱹯 „ ‥  - dobrando u separador frasyonaryu (sezimaw o desimaw) rezuwta nu separador periódiku; pur ezenplu, a frasawn sezimaw 1⁄5 pòdi ser eskrita 0󱹯1 (0󱹮1̅) = 0󱹮111...; 1⁄11 0󱹯05 = 0󱹮0̅5̅ = 0󱹮050󱹭505...; a frasawn desimaw 1⁄3 0„3 (0,3̅) = 0,333...; desimaw 1⁄12 0,08„3 (0,083̅) = 0.083 333...; esi úwtimu ezenplu, seyn u separador periódiku, è anbigwu: è sò u 3 ki si repèti, o 08333? Pru separador periódiku nun úniku karakitèr (komu nesi aplikativu), us kódigus Unicode sawn 󱹯 U+F1E6F, „ U+201E y ‥ U+2025;</li><br/>
    <li>Separador di arda ⍽ - u espasu inseparávew estreytu, kódigu Unicode U+202F, è uzadu pra markar u primeru grupu di treys díjitus, kontandu a partir du díjitu máys a direyta, a eskerda y a direyta du separador sezimaw, y, a partir daí, a kada grupu di sêys díjitus, na prátika si awternandu ku separador di xadara;</li><br/>
    <li>Separador di xadara 󱹬 - teyn a mesma fòrma básika du separador sezimaw, kun sestu du tamaỹu, apontandu pra baxu, si estendendu pra baxu a partir du pontu máys awtu da fonti uzada, y marka a pozisawn dus xadaras a kada grupu di sêys díjitus nus númerus sezimays, tantu a eskerda kwantu a direyta du separador sezimaw, kontandu senpri a partir du díjitu máys a direyta; sew kódigu Unicode è U+F1E6C; konpari u separador di xadara ku apóstrofi rètu/aspas sinplis rèta i kwa letra modifikadora liỹa vertikaw 'ˈ󱹬;</li><br/>
    <li>Díjitus sezimays - 󱸀󱸁󱸂󱸃󱸄󱸅 pra 012345; è uma reprezentasawn dedikada eskluziva pra númerus sezimays; è uma eskrita distintiva (<i>featural script</i>), mapeandu treys áreas ki reprezentam valoris: <span class="horizontal-flip">◔</span> superior a eskerda reprezenta u valor 1, ◔ superior a direyta reprezenta u valor 2, ◒ y abaxu tanbeyn reprezenta u valor 2; kada díjitu, afòra u zèru, “abrasa” o “aponta” pras aryas ki us valoris, somadus, reprezentam sew valor: <span class="horizontal-flip">◔</span> 󱸁 un; ◔ 󱸂 doys; <span class="horizontal-flip">◔</span> + ◔ = ◓ 󱸃 treys; ◔ + ◒ = ◕ 󱸄 kwatru; <span class="horizontal-flip">◔</span> + ◔ + ◒ = ● 󱸅 sinku;</li><br/>
    <li>Díjitus nifimays regularizadus - a reprezentasawn konvensyonaw da bazi nifi (trinta y sêys) uza letras prus díjitus a partir di dèys; a reprezentasawn regularizada uza us mesmus sêys díjitus uzadus na numerasawn sezimaw 012345/󱸀󱸁󱸂󱸃󱸄󱸅 y estendi elis pur meyu di sinko sinays diakrítikus (o “asentus”):<br/>
        <ul>
            <li>+00: 012345 󱸀󱸁󱸂󱸃󱸄󱸅 <span style="font-family: 'Sezimal Mono', monospace;">012345</span></li><br/>
            <li>+10: 0̇1̇2̇3̇4̇5̇ 󱸆󱸇󱸈󱸉󱸊󱸋 <span style="font-family: 'Sezimal Mono', monospace;">6789AB</span></li><br/>
            <li>+20: 0̈1̈2̈3̈4̈5̈ 󱸌󱸍󱸎󱸏󱸐󱸑 <span style="font-family: 'Sezimal Mono', monospace;">CDEFGH</span></li><br/>
            <li>+30: 0̊1̊2̊3̊4̊5̊ 󱸒󱸓󱸔󱸕󱸖󱸗 <span style="font-family: 'Sezimal Mono', monospace;">IJKLMN</span></li><br/>
            <li>+40: 0̄1̄2̄3̄4̄5̄ 󱸘󱸙󱸚󱸛󱸜󱸝 <span style="font-family: 'Sezimal Mono', monospace;">OPQRST</span></li><br/>
            <li>+50: 0̆1̆2̆3̆4̆5̆ 󱸞󱸟󱸠󱸡󱸢󱸣 <span style="font-family: 'Sezimal Mono', monospace;">UVWXYZ</span></li><br/>
            <li>˚ è a parte di sima du 󱸃;  ˉ è a parte di sima du 󱸄; ˘ veyn da parte di sima du 󱸅</li>
        </ul>
    </li>
</ul>
<p />
<p />
`,

    //
    // Unidadis
    //
    'td-shastadari-units': 'Unidadis di Medida Xastadari',
    'optgroup-units-no-conversion': 'Seyn konversawn',
    'option-units-no-conversion': 'Seyn konversawn (sò kawkuladora)',

    'optgroup-units-base': 'Unidadis bazi',
    'option-units-ang': 'Tenpu – ang',
    'option-units-pad': 'Konprimentu – pad',
    'option-units-drv': 'Masa – drv',
    'option-units-gtk': 'Tenperatura abisoluta – gtk',
    'option-units-dar': 'Korrenti elétrika – dar',
    'option-units-pkx': 'Intensidadi luminòza – pkx',
    'option-units-bht': 'Kwantidadi di subistansya – bht',

    'optgroup-units-derived': 'Unidadis Derivadas',
    'option-units-avt': 'Frekwensya – ang⁻¹',
    'option-units-ktr': 'Arya – pad²',
    'option-units-ayt': 'Volumi – pad³',
    'option-units-veg': 'Velosidadi – pad·ang⁻¹',
    'option-units-tvr': 'Aselerasawn – pad·ang⁻²',
    'option-units-gnt': 'Densidadi – drv·pad⁻³',
    'option-units-bar': 'Forsa/pezu',
    'option-units-pdn': 'Presawn',
    'option-units-vrc': 'Enerjia/trabalyu',
    'option-units-xkt': 'Potensya',
    // 'option-units-svg': 'Momentu',
    // 'option-units-agh': 'Asawn',
    // 'option-units-pbv': 'Influensya',
    // 'option-units-tnv': 'Tensawn',
    // 'option-units-upr': 'Intensidadi',
    // 'option-units-nad': 'Viskozidadi dinâmika',
    // 'option-units-bum': 'Viskozidadi sinétika',

    'optgroup-units-thermodynamics': 'Tèrmodinâmika',
    'option-units-tap': 'Tenperatura komun',
    'option-units-agn': 'Kapasidadi térmika',
    'option-units-idn': 'Kapasidadi térmika pur masa',
    'option-units-tln': 'Kapasidadi térmika pur volumi',

    'optgroup-units-electromagnetism': 'Elètromaginetismu',
    'option-units-vdt': 'Karga elétrika',
    'option-units-atr': 'Diferensa di potensiaw el.',
    'option-units-vrd': 'Rezistensya elétrika',
    'option-units-vht': 'Kondutansya elétrika',
    'option-units-upp': 'Indutansya elétrika',
    'option-units-smi': 'Kapasitansya elétrika',
    'option-units-pvh': 'Fluksu maginétiku',
    'option-units-vtr': 'Densidadi du fluksu maginétiku',
    'optgroup-units-angle': 'Ângulu',
    'option-units-mdl': 'Ângulu planu',
    'option-units-gol': 'Ângulu sólidu',
    'optgroup-units-proportion': 'Proporsawn',
    'option-units-spn': 'Proporsawn',
    'optgroup-units-data-information': 'Dadus/informasawn',
    'option-units-atk': 'Armazenajen',
    'option-units-pvn': 'Velosidadi',

    'label-prefix-sezimal': 'Prefiksu sezimaw',
    'label-prefix-sezimal-angle': 'Prefiksu sezimaw',
    'label-unit-sezimal': 'Unidadi sezimaw',
    'label-unit-sezimal-angle': 'Unidadi sezimaw',
    'label-prefix-decimal': 'Prefiksu desimaw',
    'label-prefix-decimal-angle': 'Prefiksu desimaw',
    'label-prefix-decimal-binary': 'Prefiksu desimaw/binaryu',
    'label-unit-decimal': 'Unidadi desimaw',
    'label-unit-decimal-angle': 'Unidadi desimaw',
    'optgroup-units-generic-s-i': 'S.I.',
    'optgroup-units-generic-others': 'Otras',
    'optgroup-units-generic-imp-us': 'Reynu Unidu (inperiaw)/EUA',
    'optgroup-units-generic-us': 'EUA',
    'optgroup-units-generic-imp': 'Reynu Unidu (inperiaw)',
    'optgroup-units-generic-us-fluid': 'EUA - volumi lík.',
    'optgroup-units-generic-us-dry': 'EUA - volumi seku',
    'optgroup-units-generic-imp-fluid': 'Reynu Unidu (inperiaw)',

    //
    // Sezimal Prefixes
    //
    'option-sezimal-prefix-ndxm': 'NDX – nidixama  – 10¹²⁰',
    'option-sezimal-prefix-nxpm': 'NXP – nixapama  – 10¹¹⁵',
    'option-sezimal-prefix-nxcm': 'NXC – nixatxarma – 10¹¹⁴',
    'option-sezimal-prefix-nxtm': 'NXT – nixatrima – 10¹¹³',
    'option-sezimal-prefix-nxdm': 'NXD – nixadima  – 10¹¹²',
    'option-sezimal-prefix-nxem': 'NXE – nixaekama – 10¹¹¹',
    'option-sezimal-prefix-nxm': 'NX – nixama – 10¹¹⁰',
    'option-sezimal-prefix-npm': 'NP – nipama – 10¹⁰⁵',
    'option-sezimal-prefix-ncm': 'NC – nitxarma  – 10¹⁰⁴',
    'option-sezimal-prefix-ntm': 'NT – nitrima – 10¹⁰³',
    'option-sezimal-prefix-ndm': 'ND – nidima – 10¹⁰²',
    'option-sezimal-prefix-nem': 'NE – niekama – 10¹⁰¹',
    'option-sezimal-prefix-nm': 'N – nima – 10¹⁰⁰',
    'option-sezimal-prefix-ppm': 'PP – panpama – 10⁵⁵',
    'option-sezimal-prefix-pcm': 'PC – pantxarma – 10⁵⁴',
    'option-sezimal-prefix-ptm': 'PT – pantrima  – 10⁵³',
    'option-sezimal-prefix-pdm': 'PD – pandima – 10⁵²',
    'option-sezimal-prefix-pem': 'PE – panekama  – 10⁵¹',
    'option-sezimal-prefix-pxm': 'PX – panxama  – 10⁵⁰',
    'option-sezimal-prefix-cpm': 'CP – txarpama  – 10⁴⁵',
    'option-sezimal-prefix-ccm': 'CC – txartxarma  – 10⁴⁴',
    'option-sezimal-prefix-ctm': 'CT – txartrima – 10⁴³',
    'option-sezimal-prefix-cdm': 'CD – txardima  – 10⁴²',
    'option-sezimal-prefix-cem': 'CE – txarekama – 10⁴¹',
    'option-sezimal-prefix-cxm': 'CX – txarxama – 10⁴⁰',
    'option-sezimal-prefix-tpm': 'TP – tripama – 10³⁵',
    'option-sezimal-prefix-tcm': 'TC – tritxarma – 10³⁴',
    'option-sezimal-prefix-ttm': 'TT – tritrima  – 10³³',
    'option-sezimal-prefix-tdm': 'TD – tridima – 10³²',
    'option-sezimal-prefix-tem': 'TE – triekama  – 10³¹',
    'option-sezimal-prefix-txm': 'TX – trixama  – 10³⁰',
    'option-sezimal-prefix-dpm': 'DP – dipama – 10²⁵',
    'option-sezimal-prefix-dcm': 'DC – ditxarma  – 10²⁴',
    'option-sezimal-prefix-dtm': 'DT – ditrima – 10²³',
    'option-sezimal-prefix-ddm': 'DD – didima – 10²²',
    'option-sezimal-prefix-dem': 'DE – diekama – 10²¹',
    'option-sezimal-prefix-dxm': 'DX – dixama – 10²⁰',
    'option-sezimal-prefix-xpm': 'XP – xapama – 10¹⁵',
    'option-sezimal-prefix-xcm': 'XC – xatxarma – 10¹⁴',
    'option-sezimal-prefix-xtm': 'XT – xatrima  – 10¹³',
    'option-sezimal-prefix-xdm': 'XD – xadima – 10¹²',
    'option-sezimal-prefix-xem': 'XE – xaekama  – 10¹¹',
    'option-sezimal-prefix-xm': 'X – xama – 10¹⁰',
    'option-sezimal-prefix-pm': 'P – pama – 10⁵',
    'option-sezimal-prefix-cm': 'C – txarma – 10⁴',
    'option-sezimal-prefix-tm': 'T – trima – 10³',
    'option-sezimal-prefix-dm': 'D – dima – 10²',
    'option-sezimal-prefix-em': 'E – ekama – 10¹',
    'option-sezimal-prefix-ei': 'e – ekati – 10⁻¹',
    'option-sezimal-prefix-di': 'd – diti – 10⁻²',
    'option-sezimal-prefix-ti': 't – triti – 10⁻³',
    'option-sezimal-prefix-ci': 'c – txarti – 10⁻⁴',
    'option-sezimal-prefix-pi': 'p – panti – 10⁻⁵',
    'option-sezimal-prefix-xi': 'x – xati – 10⁻¹⁰',
    'option-sezimal-prefix-xei': 'xe – xaekati – 10⁻¹¹',
    'option-sezimal-prefix-xdi': 'xd – xaditi – 10⁻¹²',
    'option-sezimal-prefix-xti': 'xt – xatriti – 10⁻¹³',
    'option-sezimal-prefix-xci': 'xc – xatxarti – 10⁻¹⁴',
    'option-sezimal-prefix-xpi': 'xp – xapanti – 10⁻¹⁵',
    'option-sezimal-prefix-dxi': 'dx – dixati – 10⁻²⁰',
    'option-sezimal-prefix-dei': 'de – diekati – 10⁻²¹',
    'option-sezimal-prefix-ddi': 'dd – diditi – 10⁻²²',
    'option-sezimal-prefix-dti': 'dt – ditriti – 10⁻²³',
    'option-sezimal-prefix-dci': 'dc – ditxarti – 10⁻²⁴',
    'option-sezimal-prefix-dpi': 'dp – dipanti – 10⁻²⁵',
    'option-sezimal-prefix-txi': 'tx – trixati – 10⁻³⁰',
    'option-sezimal-prefix-tei': 'te – triekati – 10⁻³¹',
    'option-sezimal-prefix-tdi': 'td – triditi – 10⁻³²',
    'option-sezimal-prefix-tti': 'tt – tritriti – 10⁻³³',
    'option-sezimal-prefix-tci': 'tc – tritxarti – 10⁻³⁴',
    'option-sezimal-prefix-tpi': 'tp – tripanti – 10⁻³⁵',
    'option-sezimal-prefix-cxi': 'cx – txarxati – 10⁻⁴⁰',
    'option-sezimal-prefix-cei': 'ce – txarekati – 10⁻⁴¹',
    'option-sezimal-prefix-cdi': 'cd – txarditi – 10⁻⁴²',
    'option-sezimal-prefix-cti': 'ct – txartriti – 10⁻⁴³',
    'option-sezimal-prefix-cci': 'cc – txartxarti – 10⁻⁴⁴',
    'option-sezimal-prefix-cpi': 'cp – txarpanti – 10⁻⁴⁵',
    'option-sezimal-prefix-pxi': 'px – panxati – 10⁻⁵⁰',
    'option-sezimal-prefix-pei': 'pe – panekati – 10⁻⁵¹',
    'option-sezimal-prefix-pdi': 'pd – panditi – 10⁻⁵²',
    'option-sezimal-prefix-pti': 'pt – pantriti – 10⁻⁵³',
    'option-sezimal-prefix-pci': 'pc – pantxarti – 10⁻⁵⁴',
    'option-sezimal-prefix-ppi': 'pp – panpanti – 10⁻⁵⁵',
    'option-sezimal-prefix-ni': 'n – niti – 10⁻¹⁰⁰',
    'option-sezimal-prefix-nei': 'ne – niekati – 10⁻¹⁰¹',
    'option-sezimal-prefix-ndi': 'nd – niditi – 10⁻¹⁰²',
    'option-sezimal-prefix-nti': 'nt – nitriti – 10⁻¹⁰³',
    'option-sezimal-prefix-nci': 'nc – nitxarti – 10⁻¹⁰⁴',
    'option-sezimal-prefix-npi': 'np – nipanti – 10⁻¹⁰⁵',
    'option-sezimal-prefix-nxi': 'nx – nixati – 10⁻¹¹⁰',
    'option-sezimal-prefix-nxei': 'nxe – nixaekati – 10⁻¹¹¹',
    'option-sezimal-prefix-nxdi': 'nxd – nixaditi – 10⁻¹¹²',
    'option-sezimal-prefix-nxti': 'nxt – nixatriti – 10⁻¹¹³',
    'option-sezimal-prefix-nxci': 'nxc – nixatxarti – 10⁻¹¹⁴',
    'option-sezimal-prefix-nxpi': 'nxp – nixapanti – 10⁻¹¹⁵',
    'option-sezimal-prefix-ndxi': 'ndx – nidixati – 10⁻¹²⁰',

    //
    // Decimal Prefixes
    //
    'option-decimal-prefix-quetta': 'Q – keta – 10³⁰',
    'option-decimal-prefix-ronna': 'R – rona – 10²⁷',
    'option-decimal-prefix-yotta': 'Y – yota – 10²⁴',
    'option-decimal-prefix-zetta': 'Z – zeta – 10²¹',
    'option-decimal-prefix-exa': 'E – èksa – 10¹⁸',
    'option-decimal-prefix-peta': 'P – peta – 10¹⁵',
    'option-decimal-prefix-tera': 'T – tèra – 10¹²',
    'option-decimal-prefix-giga': 'G – jiga – 10⁹',
    'option-decimal-prefix-mega': 'M – mèga – 10⁶',
    'option-decimal-prefix-kilo': 'k – kilo – 10³',
    'option-decimal-prefix-hecto': 'h – hékito – 10²',
    'option-decimal-prefix-deca': 'da – dèka – 10¹',
    'option-decimal-prefix-deci': 'd – desi – 10⁻¹',
    'option-decimal-prefix-centi': 'c – senti – 10⁻²',
    'option-decimal-prefix-milli': 'm – mili – 10⁻³',
    'option-decimal-prefix-micro': 'µ – mikro – 10⁻⁶',
    'option-decimal-prefix-nano': 'n – nano – 10⁻⁹',
    'option-decimal-prefix-pico': 'p – piko – 10⁻¹²',
    'option-decimal-prefix-femto': 'f – fento – 10⁻¹⁵',
    'option-decimal-prefix-atto': 'a – ato – 10⁻¹⁸',
    'option-decimal-prefix-zepto': 'z – zeto – 10⁻²¹',
    'option-decimal-prefix-yocto': 'y – yoto – 10⁻²⁴',
    'option-decimal-prefix-ronto': 'r – ronto – 10⁻²⁷',
    'option-decimal-prefix-quecto': 'q – keto – 10⁻³⁰',

    //
    // Binary Prefixes
    //
    'optgroup-units-generic-binary': 'Binaryus',
    'option-binary-prefix-yobi': 'Yi – yobi – 2⁸⁰',
    'option-binary-prefix-zebi': 'Zi – zebi – 2⁷⁰',
    'option-binary-prefix-exbi': 'Ei – esbi – 2⁶⁰',
    'option-binary-prefix-pebi': 'Ei – pebi – 2⁵⁰',
    'option-binary-prefix-tebi': 'Ti – tebi – 2⁴⁰',
    'option-binary-prefix-gibi': 'Gi – jibi – 2³⁰',
    'option-binary-prefix-mebi': 'Mi – mebi – 2²⁰',
    'option-binary-prefix-kibi': 'Ki – kibi – 2¹⁰',

    //
    // Time
    //
    'optgroup-units-ang-common': 'Komun/siviw',
    'option-units-ang-dina': 'dina – din = dia',
    'option-units-ang-uta': 'uta – uta ~ òra',
    'option-units-ang-posha': 'poxa – pox ~ minutu',
    'option-units-ang-agrima': 'agrima – agm ~ segundu',
    'option-units-ang-anuga': 'anuga – ang ~ sent. seg.',
    'option-units-ang-boda': 'boda – bod ~ mil. seg.',

    'option-decimal-units-ang-day': 'dia',
    'option-decimal-units-ang-hour': 'òra – h',
    'option-decimal-units-ang-minute': 'minutu – min',
    'option-decimal-units-ang-second': 'segundu – s',

    'translation-day': 'dia',
    'translation-hour': 'h',
    'translation-minute': 'min',
    'translation-second': 's',

    'option-units-pad-pada': 'pada – pad',
    'option-decimal-units-pad-metre': 'mètru – m',
    'option-decimal-units-pad-mile': 'milya – ml',
    'option-decimal-units-pad-yard': 'jarda – yd',
    'option-decimal-units-pad-foot': 'pè – ft',
    'option-decimal-units-pad-inch': 'polegada – in',

    'option-units-drv-dravya': 'dravya – drv',
    'option-decimal-units-drv-ton': 'tonelada – ton',
    'option-decimal-units-drv-gram': 'grama – g',
    'option-decimal-units-drv-dalton': 'dáwton – Da',
    'option-decimal-units-drv-gr': 'grawn – gr',
    'option-decimal-units-drv-dwt': 'pennyweight – dwt',
    'option-decimal-units-drv-ozt': 'onsa tròy – ozt',
    'option-decimal-units-drv-lbt': 'libra tròy – lbt',
    'option-decimal-units-drv-dr': 'drákima – dr',
    'option-decimal-units-drv-oz': 'onsa – oz',
    'option-decimal-units-drv-lb': 'libra – lb',
    'option-decimal-units-drv-st': 'stone – st',
    'option-decimal-units-drv-sl': 'slug – sl',
    'option-decimal-units-drv-US-qr': 'kwartu kurtu – US qr',
    'option-decimal-units-drv-US-cwt': 'hundredweight kurtu – US cwt',
    'option-decimal-units-drv-US-ton': 'tonelada kurta – US ton',
    'option-decimal-units-drv-imp-qr': 'kwartu longu – imp. qr',
    'option-decimal-units-drv-imp-cwt': 'hundredweight longu – imp. cwt',
    'option-decimal-units-drv-imp-ton': 'tonelada longa – imp. ton',

    'option-units-avt-avriti': 'avriti – avt',
    'option-decimal-units-avt-hertz': 'Hèrtz – Hz',
    'option-decimal-units-avt-rpm': 'rpm',

    'option-units-ktr-ketra': 'ketra – ktr',
    'option-units-ktr-sq-pada': 'pada kwad. – pad²',
    'option-decimal-units-ktr-sq-metre': 'mètru kwad. – m²',
    'option-decimal-units-ktr-are': 'ari - a',
    'option-decimal-units-ktr-acre': 'akri - ac',
    'option-decimal-units-ktr-sq-mile': 'milya kwad. – ml²',
    'option-decimal-units-ktr-sq-yard': 'jarda kwad. – yd²',
    'option-decimal-units-ktr-sq-foot': 'pè kwad. – ft²',
    'option-decimal-units-ktr-sq-inch': 'polegada kwad. – in²',

    'option-units-ayt-aytan': 'aytan – ayt',

    'option-decimal-units-mdl-mdl': 'mandalas',
    'option-decimal-units-mdl-tau_rad': 'τ radianus',
    'option-decimal-units-mdl-pi_rad': 'π radianus',
    'option-decimal-units-mdl-rad': 'radianus',
    'option-decimal-units-mdl-deg': 'graws',
    'option-decimal-units-mdl-arcmin': 'minutus',
    'option-decimal-units-mdl-arcsec': 'segundus',
    'option-decimal-units-mdl-turn': 'vòwtas',
    'option-decimal-units-mdl-gon': 'gradianus (gon)',

});

export { sezimal_calculator_bz_text };
