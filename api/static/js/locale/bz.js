
import { sezimal_calculator_pt_text } from './pt.js';

const sezimal_calculator_bz_text = Object.assign({}, sezimal_calculator_pt_text, {
    'title': 'Kawkuladora Sezimaw',
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

    'translation-display-asin': 'asen',
    'translation-display-sin': 'sen',
    'translation-display-acsc': 'aksk',
    'translation-display-csc': 'ksk',
    'translation-display-acos': 'akos',
    'translation-display-cos': 'kos',
    'translation-display-asec': 'asek',
    'translation-display-sec': 'sek',
    'translation-display-atan': 'atan',
    'translation-display-tan': 'tan',
    'translation-display-acot': 'akot',
    'translation-display-cot': 'kot',


    'help-setting': `
<h2>U ki kyè isu?</h2>
<p>Uma kawkuladora y un konversor di bazi numérika y unidadis di medida, entri as bazis sezimaw (sêys) y desimaw (dèys).</p>
<p>Vose pòdi uzar u aplikativu komu uma kawkuladora desimaw komun, y eli vay konvertendu us káwkulus uzando bazi sezimaw, ensinandu vose komu ler us númerus nu prosèsu.</p>
<p>Klikandu o tokandu in kada un dus mostradoris (sezimaw, nifezimaw, estensu o desimaw), u konteudu è kopiadu pra arya di transferensya.</p>
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
    <li>[ 3 ] / [ 󱸃 ] - uza díjitus komuns [ 3 ] o díjitus sezimays [ 󱸃 ] (veja máys abaxu) prus mostradoris sezimaw y nifezimaw, y prus botoyns sezimays (a bazi desimaw senpri uza us díjitus komuns);</li><br/>
    <li>[ 3󱹬3 ] / [ 󱸃󱹬󱸃 ] - determina komu us númerus sawn agrupadus y separadus:<br/>
        <ul>
            <li>[ 3󱹬3 ] / [ 󱸃󱹬󱸃 ] - separadoris sezimays (veja máys abaxu), a kada treys díjitus;</li><br/>
            <li>[ 3.3 ] / [ 󱸃.󱸃 ] - separadoris desimays/tradisyonays, di akordu ku lokali (idioma y paiz) selesyonadus, a kada treys díjitus;</li><br/>
            <li>[ 4.4 ] / [ 󱸄.󱸄 ] - separadoris desimays/tradisyonays, di akordu ku lokali (idioma y paiz) selesyonadus, a kada kwatru díjitus (komu nu sayti seximal.net); isu tanbeyn awtèra, in inglez, u rezuwtadu du mostrador du númeru pur estensu, ki pasa a uzar sêys nifi y uneksiawn nu lugar di arda y xadara;</li>
        </ul>
    </li><br/>
    <li>[ nifi 5̆ ] / [ nifi 󱸣 ] - defini u uzu y konversawn du mostrador nifezimaw:<br/>
        <ul>
            <li>[ nifi 5̆ ] / [ nifi 󱸣 ] - u mostrador nifezimaw uza díjitus regularizadus (veja abaxu);</li><br/>
            <li>[ nifi Z ] - u mostrator nifezimaw uza us díjitus 0123456789 y letras a partir du númeru 14 (in desimaw, dèys);</li><br/>
            <li>[ <span style="color: #666;">nifi</span> ] - okuwta u mostrador nifezimaw;</li>
        </ul>
    </li><br/>
    <li>[ est ] - ativa [ est ] / dizativa [ <span style="color: #666;">est</span> ] a ezibisawn dus númerus sezimays pur estensu (pur inkuantu, sòmenti disponívew in brazileru, portugez, inglez y Esperantu);</li><br/>
</ul>
<p>Y us botoyns di ajusti na segunda liỹa du mostrador:</p>
<ul>
    <li>[ R$ ] - ativa [ R$ ] / dizativa [ <span style="color: #666;">R$</span> ] u mòdu moèda, ondi a entrada è dividida pur un “separador di moèda” “󱹶” o “;”, ki indika ki u númeru reprezenta na verdadi duas unidadis di medida, konvertidas di fòrma independente, a moèda in sí, y a sua subunidadi (reays󱹶sentavus o reays;sentavus);</li><br/>
    <li>[ mdl <img src="https://midia.tauga.online/img/sezimal/mandala-logo-black-on-white-small.svg" width="12rem" /> ° ] - unidadis di medida di ângulus pras funsoyns trigonométrikas sezimays y desimays;</li><br/>
    <li>[ <img src="https://midia.tauga.online/img/sezimal/shastadari-logo-black-on-white-small.svg" width="12rem" /> ] - unidadis y prefiksus Xastadari konvertidus di o pra unidadis y prefiksus du Sistema Internasyonaw di Medidas (y awgumas unidadis tradisyonays fòra du SI);</li><br/>
    <li>[ 0󱹮3 ] - in kwantus díjitus depoys du separador sezimays u rezuwtadu vay ser arredondadu; a presizawn in bazi desimaw vay ser ajustada bazeada na presizawn da bazi sezimaw;</li><br/>
</ul>
<h2>Notasawn uzada</h2>
<ul>
    <li>Nomis dus númerus - 0 zèru; 1 un; 2 doys; 3 treys; 4 kwatru; 5 sinku; 10 sêys; 11 sèti; 12 oytu; 13 nòvi; 14 dèys; 15 onzi; 20 dozi; 21 dozi y un; 22 dozi y doys; 23 dozi y treys; 24 dozi y kwatru; 25 dozi y sinku; 30 treseys; 40 kwaseys; 50 kinseys; 100 nifi (da lingwa ndom <i>nif</i> pra trinta y sêys); 1󱹭000 arda (du sânskritu अर्ध <i>ardha</i> pra meyu, metadi, pra metadi di sêys díjitus); 10󱹭000 sêys arda; 100󱹭000 nifi arda; 1󱹬000󱹭000 xadara (du sânskritu षडार <i>ṣaḍāra</i> prun grupu di sêys, o un ekságonu); di xadara si sègi 10󱹬000󱹭000 sêys xadara, 100󱹬000󱹭000 nifi xadara, 1󱹭000󱹬000󱹭000 arda xadara (in iskala longa, komu in portugez ewropew), 10󱹭000󱹬000󱹭000 sêys arda xadara, 100󱹭000󱹬000󱹭000 nifi arda xadara, dixadara 1󱹬000󱹭000󱹬000󱹭000 (<i>di</i> du sânskritu द्वि <i>dvi</i> pra doys); trixadara pra 10³⁰ (<i>tri</i> du sânskritu त्रि <i>tri</i> pra treys); xarxadara pra 10⁴⁰ (<i>xar</i> du sânskritu चतुर् <i>catur</i> pra kwatru); panxadara pra 10⁵⁰ (<i>pan</i> du sânskritu पञ्चन् <i>pañcan</i>, sinku); xaxadara pra 10¹⁰⁰ (<i>xa</i> du sânskritu षष् <i>ṣaṣ</i> pra sêys); uzi a funsawn di númerus pur estensu pra saber komu ler kwawkèr númeru sezimaw</li><br/>
    <li>Separador sezimaw 󱹮 - uma barra in fòrma di agulya, apontandu pra sima, ki si inisia sobri a liỹa bazi da eskrita, pelu meyu da altura X da fonti, y si estendi pra baxu atè u pontu máys baxu dus desendentis da fonti; sew kódigu Unicode è U+F1E6E; konpari u separador sezimaw kwa vírgula y u pontu: ,󱹮.</li><br/>
    <li>Separador periódiko 󱹯 „ ‥  - dobrando u separador frasyonaryu (sezimaw o desimaw) rezuwta nu separador periódiku; pur ezenplu, a frasawn sezimaw 1⁄5 pòdi ser eskrita 0󱹯1 (0󱹮1̅) = 0󱹮111...; 1⁄11 0󱹯05 = 0󱹮0̅5̅ = 0󱹮050󱹭505...; a frasawn desimaw 1⁄3 0„3 (0,3̅) = 0,333...; desimaw 1⁄12 0,08„3 (0,083̅) = 0.083 333...; esi úwtimu ezenplu, seyn u separador periódiku, è anbigwu: è sò u 3 ki si repèti, o 08333? Pru separador periódiku nun úniku karakitèr (komu nesi aplikativu), us kódigus Unicode sawn 󱹯 U+F1E6F, „ U+201E y ‥ U+2025;</li><br/>
    <li>Separador di arda ⍽ - u espasu inseparávew estreytu, kódigu Unicode U+202F, è uzadu pra markar u primeru grupu di treys díjitus, kontandu a partir du díjitu máys a direyta, a eskerda y a direyta du separador sezimaw, y, a partir daí, a kada grupu di sêys díjitus, na prátika si awternandu ku separador di xadara;</li><br/>
    <li>Separador di xadara 󱹬 - teyn a mesma fòrma básika du separador sezimaw, kun sestu du tamaỹu, apontandu pra baxu, si estendendu pra baxu a partir du pontu máys awtu da fonti uzada, y marka a pozisawn dus xadaras a kada grupu di sêys díjitus nus númerus sezimays, tantu a eskerda kwantu a direyta du separador sezimaw, kontandu senpri a partir du díjitu máys a direyta; sew kódigu Unicode è U+F1E6C; konpari u separador di xadara ku apóstrofi rètu/aspas sinplis rèta i kwa letra modifikadora liỹa vertikaw 'ˈ󱹬;</li><br/>
    <li>Díjitus sezimays - 󱸀󱸁󱸂󱸃󱸄󱸅 pra 012345; è uma reprezentasawn dedikada eskluziva pra númerus sezimays; è uma eskrita distintiva (<i>featural script</i>), mapeandu treys áreas ki reprezentam valoris: <span class="horizontal-flip">◔</span> superior a eskerda reprezenta u valor 1, ◔ superior a direyta reprezenta u valor 2, ◒ y abaxu tanbeyn reprezenta u valor 2; kada díjitu, afòra u zèru, “abrasa” o “aponta” pras aryas ki us valoris, somadus, reprezentam sew valor: <span class="horizontal-flip">◔</span> 󱸁 un; ◔ 󱸂 doys; <span class="horizontal-flip">◔</span> + ◔ = ◓ 󱸃 treys; ◔ + ◒ = ◕ 󱸄 kwatru; <span class="horizontal-flip">◔</span> + ◔ + ◒ = ● 󱸅 sinku;</li><br/>
    <li>Díjitus nifimays regularizadus - a reprezentasawn konvensyonaw da bazi nifi (trinta y sêys) uza letras prus díjitus a partir di dèys; a reprezentasawn regularizada uza us mesmus sêys díjitus uzadus na numerasawn sezimaw 012345/󱸀󱸁󱸂󱸃󱸄󱸅 y estendi elis pur meyu di sinku sinays diakrítikus (o “asentus”):<br/>
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

    'optgroup-units-base': '13 unidadis bazi',
    'option-units-ang': 'Tenpu – ang',
    'option-units-pad': 'Konprimentu – pad',
    'option-units-drv': 'Masa – drv',
    'option-units-gtk': 'Tenperatura abisoluta – gtk',
    'option-units-dar': 'Korrenti elétrika – dar',
    'option-units-mdl': 'Ângulu planu – mdl',
    'option-units-gol': 'Ângulu sólidu – gol',
    'option-units-pkx': 'Intensidadi luminòza – pkx',
    'option-units-bht': 'Kwantidadi di subistansya – bht',

    'optgroup-units-derived': 'Unidadis derivadas',
    'option-units-avt': 'Frekwensya – avt',
    'option-units-ktr': 'Arya – ktr',
    'option-units-ayt': 'Volumi – ayt',
    'option-units-veg': 'Velosidadi – veg',
    'option-units-tvr': 'Aselerasawn – tvr',
    'option-units-gnt': 'Densidadi – gnt',
    'option-units-bar': 'Forsa/pezu – bal/bar',
    'option-units-pdn': 'Presawn – pdn',
    'option-units-vrc': 'Enerjia/trabalyu – vrc',
    'option-units-xkt': 'Potensya – xkt',
    'option-units-svg': 'Momentu linear – svg',
    'option-units-agh': 'Asawn – agh',
    // 'option-units-pbv': 'Influensya',
    // 'option-units-tnv': 'Tensawn',
    // 'option-units-upr': 'Intensidadi',
    // 'option-units-nad': 'Viskozidadi dinâmika',
    // 'option-units-bum': 'Viskozidadi sinétika',

    'option-units-tap': 'Tenperatura komun – tap',
    'option-units-agn': 'Kapasidadi térmika – agn',
    'option-units-kdn': 'Enerjia espesífika – kdn',
    'option-units-idn': 'Kalor espesífiku – idn',
    // 'option-units-tln': 'Kapasidadi térmika pur volumi',

    'option-units-vdt': 'Karga elétrika – vdt',
    'option-units-atr': 'Diferensa di potensiaw el. – atr',
    'option-units-vrd': 'Rezistensya el. – vrd',
    'option-units-vht': 'Kondutansya el. – vht',
    // 'option-units-upp': 'Indutansya el. – upp',
    'option-units-dry': 'Kapasitansya el. – dry',
    'option-units-pvh': 'Fluksu maginétiku – pvh',
    'option-units-vtr': 'Dens. du fluksu maginétiku – vtr',
    'option-units-dpk': 'Fluksu luminozu – dpk',
    'option-units-dxt': 'Rendimentu luminozu – dxt',
    'option-units-dul': 'Masa atômika – dul',

    'optgroup-units-others': 'Otras unidadis',
    'option-units-spn': 'Proporsawn – spn',
    'option-units-atk': 'Armazenajen di dadus – atk',
    'option-units-pvn': 'Vel. di transm. di dadus – pvn',
    'option-units-clt': 'Konsumu di konbustívew – clt',

    'label-prefix-sezimal': 'Prefiksu sezimaw',
    'label-prefix-sezimal-angle': 'Prefiksu sezimaw',
    'label-unit-sezimal': 'Unidadi sezimaw',
    'label-unit-sezimal-angle': 'Unidadi sezimaw',
    'label-prefix-decimal': 'Prefiksu desimaw',
    'label-prefix-decimal-angle': 'Prefiksu desimaw',
    'label-prefix-decimal-binary': 'Prefiksu desimaw/binaryu',
    'label-unit-decimal': 'Unidadi desimaw',
    'label-unit-decimal-angle': 'Unidadi desimaw',
    'optgroup-units-generic-shastadari': 'Xastadari',
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
    'option-sezimal-prefix-nxcm': 'NXC – nixaxarma – 10¹¹⁴',
    'option-sezimal-prefix-nxtm': 'NXT – nixatrima – 10¹¹³',
    'option-sezimal-prefix-nxdm': 'NXD – nixadima  – 10¹¹²',
    'option-sezimal-prefix-nxem': 'NXE – nixaekama – 10¹¹¹',
    'option-sezimal-prefix-nxm': 'NX – nixama – 10¹¹⁰',
    'option-sezimal-prefix-npm': 'NP – nipama – 10¹⁰⁵',
    'option-sezimal-prefix-ncm': 'NC – nixarma  – 10¹⁰⁴',
    'option-sezimal-prefix-ntm': 'NT – nitrima – 10¹⁰³',
    'option-sezimal-prefix-ndm': 'ND – nidima – 10¹⁰²',
    'option-sezimal-prefix-nem': 'NE – niekama – 10¹⁰¹',
    'option-sezimal-prefix-nm': 'N – nima – 10¹⁰⁰',
    'option-sezimal-prefix-ppm': 'PP – panpama – 10⁵⁵',
    'option-sezimal-prefix-pcm': 'PC – panxarma – 10⁵⁴',
    'option-sezimal-prefix-ptm': 'PT – pantrima  – 10⁵³',
    'option-sezimal-prefix-pdm': 'PD – pandima – 10⁵²',
    'option-sezimal-prefix-pem': 'PE – panekama  – 10⁵¹',
    'option-sezimal-prefix-pxm': 'PX – panxama  – 10⁵⁰',
    'option-sezimal-prefix-cpm': 'CP – xarpama  – 10⁴⁵',
    'option-sezimal-prefix-ccm': 'CC – xarxarma  – 10⁴⁴',
    'option-sezimal-prefix-ctm': 'CT – xartrima – 10⁴³',
    'option-sezimal-prefix-cdm': 'CD – xardima  – 10⁴²',
    'option-sezimal-prefix-cem': 'CE – xarekama – 10⁴¹',
    'option-sezimal-prefix-cxm': 'CX – xarxama – 10⁴⁰',
    'option-sezimal-prefix-tpm': 'TP – tripama – 10³⁵',
    'option-sezimal-prefix-tcm': 'TC – trixarma – 10³⁴',
    'option-sezimal-prefix-ttm': 'TT – tritrima  – 10³³',
    'option-sezimal-prefix-tdm': 'TD – tridima – 10³²',
    'option-sezimal-prefix-tem': 'TE – triekama  – 10³¹',
    'option-sezimal-prefix-txm': 'TX – trixama  – 10³⁰',
    'option-sezimal-prefix-dpm': 'DP – dipama – 10²⁵',
    'option-sezimal-prefix-dcm': 'DC – dixarma  – 10²⁴',
    'option-sezimal-prefix-dtm': 'DT – ditrima – 10²³',
    'option-sezimal-prefix-ddm': 'DD – didima – 10²²',
    'option-sezimal-prefix-dem': 'DE – diekama – 10²¹',
    'option-sezimal-prefix-dxm': 'DX – dixama – 10²⁰',
    'option-sezimal-prefix-xpm': 'XP – xapama – 10¹⁵',
    'option-sezimal-prefix-xcm': 'XC – xaxarma – 10¹⁴',
    'option-sezimal-prefix-xtm': 'XT – xatrima  – 10¹³',
    'option-sezimal-prefix-xdm': 'XD – xadima – 10¹²',
    'option-sezimal-prefix-xem': 'XE – xaekama  – 10¹¹',
    'option-sezimal-prefix-xm': 'X – xama – 10¹⁰',
    'option-sezimal-prefix-pm': 'P – pama – 10⁵',
    'option-sezimal-prefix-cm': 'C – xarma – 10⁴',
    'option-sezimal-prefix-tm': 'T – trima – 10³',
    'option-sezimal-prefix-dm': 'D – dima – 10²',
    'option-sezimal-prefix-em': 'E – ekama – 10¹',
    'option-sezimal-prefix-ei': 'e – ekati – 10⁻¹',
    'option-sezimal-prefix-di': 'd – diti – 10⁻²',
    'option-sezimal-prefix-ti': 't – triti – 10⁻³',
    'option-sezimal-prefix-ci': 'c – xarti – 10⁻⁴',
    'option-sezimal-prefix-pi': 'p – panti – 10⁻⁵',
    'option-sezimal-prefix-xi': 'x – xati – 10⁻¹⁰',
    'option-sezimal-prefix-xei': 'xe – xaekati – 10⁻¹¹',
    'option-sezimal-prefix-xdi': 'xd – xaditi – 10⁻¹²',
    'option-sezimal-prefix-xti': 'xt – xatriti – 10⁻¹³',
    'option-sezimal-prefix-xci': 'xc – xaxarti – 10⁻¹⁴',
    'option-sezimal-prefix-xpi': 'xp – xapanti – 10⁻¹⁵',
    'option-sezimal-prefix-dxi': 'dx – dixati – 10⁻²⁰',
    'option-sezimal-prefix-dei': 'de – diekati – 10⁻²¹',
    'option-sezimal-prefix-ddi': 'dd – diditi – 10⁻²²',
    'option-sezimal-prefix-dti': 'dt – ditriti – 10⁻²³',
    'option-sezimal-prefix-dci': 'dc – dixarti – 10⁻²⁴',
    'option-sezimal-prefix-dpi': 'dp – dipanti – 10⁻²⁵',
    'option-sezimal-prefix-txi': 'x – trixati – 10⁻³⁰',
    'option-sezimal-prefix-tei': 'te – triekati – 10⁻³¹',
    'option-sezimal-prefix-tdi': 'td – triditi – 10⁻³²',
    'option-sezimal-prefix-tti': 'tt – tritriti – 10⁻³³',
    'option-sezimal-prefix-tci': 'tc – trixarti – 10⁻³⁴',
    'option-sezimal-prefix-tpi': 'tp – tripanti – 10⁻³⁵',
    'option-sezimal-prefix-cxi': 'cx – xarxati – 10⁻⁴⁰',
    'option-sezimal-prefix-cei': 'ce – xarekati – 10⁻⁴¹',
    'option-sezimal-prefix-cdi': 'cd – xarditi – 10⁻⁴²',
    'option-sezimal-prefix-cti': 'ct – xartriti – 10⁻⁴³',
    'option-sezimal-prefix-cci': 'cc – xarxarti – 10⁻⁴⁴',
    'option-sezimal-prefix-cpi': 'cp – xarpanti – 10⁻⁴⁵',
    'option-sezimal-prefix-pxi': 'px – panxati – 10⁻⁵⁰',
    'option-sezimal-prefix-pei': 'pe – panekati – 10⁻⁵¹',
    'option-sezimal-prefix-pdi': 'pd – panditi – 10⁻⁵²',
    'option-sezimal-prefix-pti': 'pt – pantriti – 10⁻⁵³',
    'option-sezimal-prefix-pci': 'pc – panxarti – 10⁻⁵⁴',
    'option-sezimal-prefix-ppi': 'pp – panpanti – 10⁻⁵⁵',
    'option-sezimal-prefix-ni': 'n – niti – 10⁻¹⁰⁰',
    'option-sezimal-prefix-nei': 'ne – niekati – 10⁻¹⁰¹',
    'option-sezimal-prefix-ndi': 'nd – niditi – 10⁻¹⁰²',
    'option-sezimal-prefix-nti': 'nt – nitriti – 10⁻¹⁰³',
    'option-sezimal-prefix-nci': 'nc – nixarti – 10⁻¹⁰⁴',
    'option-sezimal-prefix-npi': 'np – nipanti – 10⁻¹⁰⁵',
    'option-sezimal-prefix-nxi': 'nx – nixati – 10⁻¹¹⁰',
    'option-sezimal-prefix-nxei': 'nxe – nixaekati – 10⁻¹¹¹',
    'option-sezimal-prefix-nxdi': 'nxd – nixaditi – 10⁻¹¹²',
    'option-sezimal-prefix-nxti': 'nxt – nixatriti – 10⁻¹¹³',
    'option-sezimal-prefix-nxci': 'nxc – nixaxarti – 10⁻¹¹⁴',
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
    'option-units-ang-dina': 'dinas – din = dia',
    'option-units-ang-uta': 'utas – uta ~ òra',
    'option-units-ang-posha': 'poxas – pox ~ minutu',
    'option-units-ang-agrima': 'agrimas – agm ~ segundu',
    'option-units-ang-anuga': 'anugas – ang ~ sent. seg.',
    'option-units-ang-boda': 'bodas – bod ~ mil. seg.',
    'option-units-ang-sez': 'sezenyu – sez',
    'option-units-ang-nif': 'nifenyu – nif',
    'option-units-ang-ard': 'ardenyu – ard',
    'option-units-ang-srd': 'sezardenyu – srd',
    'option-units-ang-nrd': 'nifardenyu – nrd',
    'option-units-ang-xad': 'xadarenyu – xad',

    'translation-display-sez': 'sezenyus',
    'translation-display-nif': 'nifenyus',
    'translation-display-ard': 'ardenyus',
    'translation-display-srd': 'sezardenyus',
    'translation-display-nrd': 'nifardenyus',
    'translation-display-xad': 'xadarenyus',

    'option-decimal-units-ang-day': 'dias',
    'option-decimal-units-ang-hour': 'òras – h',
    'option-decimal-units-ang-minute': 'minutus – min',
    'option-decimal-units-ang-second': 'segundus – s',
    'option-decimal-units-ang-week': 'semanas – sem.',
    'option-decimal-units-ang-month': 'mezis – mez',
    'option-decimal-units-ang-year': 'anus – anu',
    'option-decimal-units-ang-decade': 'dékadas – dék.',
    'option-decimal-units-ang-century': 'sékulus – sék.',
    'option-decimal-units-ang-millenium': 'milenyus – mil.',

    'translation-display-day': 'dias',
    'translation-display-hour': 'h',
    'translation-display-minute': 'min',
    'translation-display-second': 's',
    'translation-display-week': 'semanas',
    'translation-display-month': 'mezis',
    'translation-display-year': 'anus',
    'translation-display-decade': 'dékadas',
    'translation-display-century': 'sékulus',
    'translation-display-millenium': 'milenyus',

    'option-units-pad-pada': 'padas – pad',
    'option-decimal-units-pad-metre': 'mètrus – m',
    'option-decimal-units-pad-mile': 'milyas – mi',
    'option-decimal-units-pad-yard': 'jardas – yd',
    'option-decimal-units-pad-foot': 'pès – ft',
    'option-decimal-units-pad-inch': 'polegadas – in',

    'option-units-drv-dravya': 'dravyas – drv',
    'option-decimal-units-drv-ton': 'toneladas – ton',
    'option-decimal-units-drv-gram': 'gramas – g',
    'option-decimal-units-drv-dalton': 'dáwtons – Da',
    'option-decimal-units-drv-gr': 'grawns – gr',
    'option-decimal-units-drv-dwt': 'pennyweights – dwt',
    'option-decimal-units-drv-ozt': 'onsas tròy – ozt',
    'option-decimal-units-drv-lbt': 'libras tròy – lbt',
    'option-decimal-units-drv-dr': 'drákimas – dr',
    'option-decimal-units-drv-oz': 'onsas – oz',
    'option-decimal-units-drv-lb': 'libras – lb',
    'option-decimal-units-drv-st': 'stones – st',
    'option-decimal-units-drv-sl': 'slugs – sl',
    'option-decimal-units-drv-US-qr': 'kwartus kurtus – qr EUA',
    'option-decimal-units-drv-US-cwt': 'hundredweights kurtus – cwt EUA',
    'option-decimal-units-drv-US-ton': 'toneladas kurtas – ton EUA',
    'option-decimal-units-drv-imp-qr': 'kwartus longus – qr inp.',
    'option-decimal-units-drv-imp-cwt': 'hundredweights longus – cwt inp.',
    'option-decimal-units-drv-imp-ton': 'toneladas longas – ton inp.',

    'option-units-gtk-gatika': 'gatikas (abisoluta) – gtk',
    'option-units-gtk-tapa': 'tapas (komun) – tap/°S',
    'option-decimal-units-gtk-kelvin': 'kèwvins – K',
    'option-decimal-units-gtk-celsius': 'graws Celsius – °C',
    'option-decimal-units-gtk-fahrenheit': 'graws Fahrenheit – °F',
    'option-decimal-units-gtk-rankine': 'graws Rankine – °R',

    'option-sezimal-units-mdl-mandala': 'mandalas – mdl',
    'option-decimal-units-mdl-tau_rad': 'τ radianus',
    'option-decimal-units-mdl-pi_rad': 'π radianus',
    'option-decimal-units-mdl-rad': 'radianus',
    'option-decimal-units-mdl-deg': 'graws',
    'option-decimal-units-mdl-arcmin': 'minutus',
    'option-decimal-units-mdl-arcsec': 'segundus',
    'option-decimal-units-mdl-turn': 'vòwtas',
    'option-decimal-units-mdl-gon': 'gradianus (gon)',

    'option-sezimal-units-gol-gola': 'golas – gol',
    'option-decimal-units-gol-sterradian': 'esfèrorradianus – sr',
    'option-decimal-units-gol-spat': 'espasus – spat',
    'option-decimal-units-gol-deg2': 'graws aw kwadradu – graw²',

    'option-units-pkx-prakasha': 'prakaxas – pkx',
    'option-decimal-units-pkx-candela': 'kandèlas – cd',

    'option-units-bht-bahuta': 'barrutas – bht',
    'option-decimal-units-bht-mole': 'mòws – mol',

    'option-units-avt-avriti': 'avritis (frekwensya) – avt',
    'option-units-avt-bramsha': 'branxas (dekaymentu rad.) – brx',
    'option-decimal-units-avt-hertz': 'rèrtis – Hz',
    'option-decimal-units-avt-becquerel': 'bekerèws – Bq',
    'option-decimal-units-avt-rpm': 'rpm',

    'option-units-ktr-ketra': 'ketras – ktr',
    'option-units-ktr-sq-pada': 'padas kwad. – pad²',
    'option-decimal-units-ktr-sq-metre': 'mètrus kwad. – m²',
    'option-decimal-units-ktr-are': 'aris - a',
    'option-decimal-units-ktr-acre': 'akris - ac',
    'option-decimal-units-ktr-sq-mile': 'milyas kwad. – mi²',
    'option-decimal-units-ktr-sq-yard': 'jardas kwad. – yd²',
    'option-decimal-units-ktr-sq-foot': 'pès kwad. – ft²',
    'option-decimal-units-ktr-sq-inch': 'polegadas kwad. – in²',

    'option-units-ayt-aytan': 'aytans – ayt',
    'option-units-ayt-cb-pada': 'padas kúbikus – pad³',
    'option-decimal-units-ayt-cb-metre': 'mètrus kúbikus – m³',
    'option-decimal-units-ayt-litre': 'litrus – L',
    'option-decimal-units-ayt-cb-mile': 'milyas kúbikas – mi³',
    'option-decimal-units-ayt-cb-yard': 'jardas kúbikas – yd³',
    'option-decimal-units-ayt-cb-foot': 'pès kúbikus – ft³',
    'option-decimal-units-ayt-cb-inch': 'polegadas kúbikas – in³',

    'translation-display-US-fl-dr': 'fl dr EUA',
    'translation-display-US-tsp': 'kx EUA',
    'translation-display-US-tbsp': 'ks EUA',
    'translation-display-US-fl-oz': 'fl oz EUA',
    'translation-display-US-cup': 'xík EUA',
    'translation-display-US-pt': 'pt EUA',
    'translation-display-US-qt': 'qt EUA',
    'translation-display-US-gal': 'gal EUA',
    'translation-display-US-pt-dry': 'pt (seku)',
    'translation-display-US-qt-dry': 'qt (seku)',
    'translation-display-US-gal-dry': 'gal (seku)',
    'translation-display-US-pk-dry': 'pk (seku)',
    'translation-display-US-bu-dry': 'bu (seku)',

    'translation-display-imp-fl-dr': 'fl dr inp.',
    'translation-display-imp-fl-oz': 'fl oz inp.',
    'translation-display-imp-pt': 'pt inp.',
    'translation-display-imp-qt': 'qt inp.',
    'translation-display-imp-gal': 'gal inp.',

    'option-decimal-units-ayt-imp-fl-dr': 'drákimas – fl dr inp.',
    'option-decimal-units-ayt-imp-fl-oz': 'onsas – fl oz inp.',
    'option-decimal-units-ayt-imp-pt': 'pintas – pt inp.',
    'option-decimal-units-ayt-imp-qt': 'kwartus – qt inp.',
    'option-decimal-units-ayt-imp-gal': 'galoyns – gal inp.',

    'option-decimal-units-ayt-us-fl-dr': 'drákimas – fl dr EUA',
    'option-decimal-units-ayt-us-tsp': 'colyèris di xá – kx EUA',
    'option-decimal-units-ayt-us-tbsp': 'colyèris di sopa – ks EUA',
    'option-decimal-units-ayt-us-fl-oz': 'onsas – fl oz EUA',
    'option-decimal-units-ayt-us-cup': 'xíkaras – xík EUA',
    'option-decimal-units-ayt-us-pt': 'pintas – pt EUA',
    'option-decimal-units-ayt-us-qt': 'kwartus – qt EUA',
    'option-decimal-units-ayt-us-gal': 'galoyns – gal EUA',

    'option-decimal-units-ayt-us-pt-dry': 'pintas – pt (seku) EUA',
    'option-decimal-units-ayt-us-qt-dry': 'kwartus – qt (seku) EUA',
    'option-decimal-units-ayt-us-gal-dry': 'galoyns – gal (seku) EUA',
    'option-decimal-units-ayt-us-pk-dry': 'pèkis – pk (seku) EUA',
    'option-decimal-units-ayt-us-bu-dry': 'búxews – bu (seku) EUA',

    'option-units-veg-vega': 'vegas – veg',
    'option-decimal-units-veg-mh': 'mètrus pur òra – m/h',
    'option-decimal-units-veg-ms': 'mètrus pur segundu – m/s',
    'option-decimal-units-veg-mph': 'milyas pur òra – mph',
    'option-decimal-units-veg-fps': 'pès pur segundu – fps',
    'option-decimal-units-veg-kn': 'nòs – kn',
    'option-decimal-units-veg-c': 'velosidadi da luz – c',

    'option-units-tvr-tevaran': 'tevarans (aselerasawn) – tvr',
    'option-units-tvr-guruta': 'gurutas (gravitasawn) – grt',
    'option-decimal-units-tvr-ms2': 'mètrus pur segundu aw kwad. – m/s²',
    'option-decimal-units-tvr-nkg': 'níwtons pur kilograma – N/kg',
    'option-decimal-units-tvr-fts2': 'pès pur segundu au kwad. – ft/s²',
    'option-decimal-units-tvr-g': 'gravidadi da Tèrra – g',
    'option-decimal-units-tvr-gal': 'gal (cm/s²) – Gal',

    'option-units-gnt-ganata': 'ganatas – gnt',
    'option-decimal-units-gnt-gm3': 'gramas pur mètru kúb. – g/m³',
    'option-decimal-units-gnt-gl': 'gramas pur litru – g/L',
    'option-decimal-units-gnt-onin3': 'onsas pur polegada kúb. – oz/in³',
    'option-decimal-units-gnt-lbin3': 'libras pur polegada kúb. – lb/in³',
    'option-decimal-units-gnt-lbft3': 'libras pur pè kúb. – lb/ft³',
    'option-decimal-units-gnt-lbyd3': 'libras pur jarda kúb. – lb/yd³',
    'option-decimal-units-gnt-slft3': 'slugs pur pè kúb. – lb/yd³',
    'option-decimal-units-gnt-lbgal': 'libras pur galawn – lb/gal',
    'option-decimal-units-gnt-lbbu': 'libras pur búxew – lb/bu',

    'option-units-bar-bala': 'balas (forsa) – bal',
    'option-units-bar-bara': 'baras (pezu) – bar',
    'option-decimal-units-bar-newton': 'níwtons – N',
    'option-decimal-units-bar-gms2': 'gramas-mètrus pur segundu aw kwad. – g·m/s²',
    'option-decimal-units-bar-gf': 'gramas-forsa – gf',
    'option-decimal-units-bar-dyn': 'dinas – dyn',
    'option-decimal-units-bar-lbf': 'libras-forsa – lbf',
    'option-decimal-units-bar-lbfts2': 'libras-pès pur segundu aw kwad. – lb·ft/s²',

    'option-units-pdn-pidana': 'pídanas – pdn',
    'option-units-pdn-vayu': 'vayús (atimosfèra) – vay',
    'option-units-pdn-pratibala': 'pratibala (tensawn) – pbl',
    'option-decimal-units-pdn-pa': 'paskays – Pa',
    'option-decimal-units-pdn-atm': 'atimosfèras –  atm',
    'option-decimal-units-pdn-psi': 'libras pur polegada kwad. – psi',
    'option-decimal-units-pdn-bar': 'bars – bar',
    'option-decimal-units-pdn-mmhg': 'milímetrus di merkuryu – mm Hg',
    'option-decimal-units-pdn-inhg': 'polegadas di merkuryu – in Hg',
    'option-decimal-units-pdn-torr': 'torris – Torr',

    'option-units-vrc-varcha': 'varxas (enerjia) – vrc',
    'option-units-vrc-sharama': 'xaramas (trabalyu) – xrm',
    'option-units-vrc-ushuna': 'uxunas (kalor) – uxn',
    'option-units-vrc-shakya': 'xakyas (enerjia pot. elétrika) – xky',
    'option-decimal-units-vrc-joule': 'jawlis – J',
    'option-decimal-units-vrc-wh': 'vatis-òra – W·h',
    'option-decimal-units-vrc-cal': 'kalorias – cal',
    'option-decimal-units-vrc-btu': 'BTUs – BTU',
    'option-decimal-units-vrc-tnt': 'toneladas di TNT – TNT',
    'option-decimal-units-vrc-erg': 'ergs – erg',
    'option-decimal-units-vrc-ev': 'elétrons-vowt – eV',
    'option-decimal-units-vrc-ftlb': 'pès-libras-forsa – ft⋅lbf',

    'option-units-xkt-shakiti': 'xakitis  – xkt',
    'option-decimal-units-xkt-watt': 'vatis – W',
    'option-decimal-units-xkt-ftlbfs': 'pès-libras-forsa pur segundu – ft⋅lbf/s',
    'option-decimal-units-xkt-cv': 'kavalus-vapor – cv',
    'option-decimal-units-xkt-hp': 'kavalus di forsa – hp',
    'option-decimal-units-xkt-buth': 'BTUs pur òra – BTU/h',
    'option-decimal-units-xkt-cals': 'kalorias pur segundu – cal/s',
    'option-decimal-units-xkt-kcalh': 'kilokalorias pur òra – kcal/h',

    'option-units-svg-samvega': 'sanvegas  – svg',
    'option-units-svg-juti': 'jutis  – jut',
    'option-decimal-units-svg-gms': 'gramas-mètrus pur segundu – g·m/s',
    'option-decimal-units-svg-ns': 'níwtons-segundu – N·s',
    'option-decimal-units-svg-lbfts': 'libras-pès pur segundu – lb·ft/s',
    'option-decimal-units-svg-slfts': 'slugs-pès pur segundu – sl·ft/s',

    'option-units-agh-agraha': 'agrarra – agh',
    'option-decimal-units-agh-js': 'jawlis-segundu – J·s',
    'option-decimal-units-agh-jhz': 'jawlis pur rèrtis – J/Hz',

    'option-units-tap-tapa': 'tapas (komun) – tap/°S',
    'option-units-tap-gatika': 'gatikas (abisoluta) – gtk',
    'option-decimal-units-tap-kelvin': 'kèwvins – K',
    'option-decimal-units-tap-celsius': 'graws Celsius – °C',
    'option-decimal-units-tap-fahrenheit': 'graws Fahrenheit – °F',
    'option-decimal-units-tap-rankine': 'graws Rankine – °R',

    'option-units-agn-agini': 'aginis (kapasidadi térm.) – agn',
    'option-units-agn-parivartana': 'parivártanas (entropia) – prv',
    'option-units-agn-jk': 'jawlis pur kèwvin – J/K',
    'option-units-agn-btur': 'BTU pur graw Rankine – BTU/°R',

    'option-units-kdn-kadana': 'kadanas – kdn',
    'option-units-kdn-jg': 'jawlis pur grama – J/g',
    'option-units-kdn-jkg': 'jawlis pur kilograma – J/kg',
    'option-units-kdn-cal': 'kaloria alimentar – Cal',

    'option-units-idn-indana': 'indanas – idn',
    'option-units-idn-jkkg': 'jawlis pur kèwvin pur kilograma – J/K/kg',

    'option-units-vdt-vidyuta': 'vidyutas – vdt',
    'option-decimal-units-vdt-c': 'kúlombis – C',
    'option-decimal-units-vdt-ah': 'ampèris-òra – A·h',

    'option-units-atr-antaran': 'antarans – atr',
    'option-decimal-units-atr-volt': 'vowtis – V',

    'option-units-vrd-viroda': 'virodas – vrd',
    'option-decimal-units-vrd-ohm': 'oms – Ω',

    'option-units-vht-vahata': 'varratas – vht',
    'option-decimal-units-vht-siemens': 'simens – S',

    'option-units-dry-darayata': 'darayatas – dry',
    'option-decimal-units-dry-farad': 'faradis – F',

    'option-units-pvh-pravaha': 'pravarras – pvh',
    'option-decimal-units-pvh-wb': 'vébers – Wb',

    'option-units-vtr-vistara': 'vistaras – vtr',
    'option-decimal-units-vtr-tesla': 'tèslas – T',

    'option-units-dpk-dipaka': 'dipakas – dpk',
    'option-decimal-units-dpk-lm': 'lumens – lm',

    'option-units-dxt-drishiti': 'drixitis – dxt',
    'option-decimal-units-dxt-lmw': 'lumens pur vati – lm/W',

    'option-units-dul-duli': 'dulis – dul',
    'option-units-dul-dravya': 'dravyas – drv',
    'option-decimal-units-dul-ton': 'toneladas – ton',
    'option-decimal-units-dul-gram': 'gramas – g',
    'option-decimal-units-dul-dalton': 'dáwtons – Da',
    'option-decimal-units-dul-gr': 'grawns – gr',
    'option-decimal-units-dul-dwt': 'pennyweights – dwt',
    'option-decimal-units-dul-ozt': 'onsas tròy – ozt',
    'option-decimal-units-dul-lbt': 'libras tròy – lbt',
    'option-decimal-units-dul-dr': 'drákimas – dr',
    'option-decimal-units-dul-oz': 'onsas – oz',
    'option-decimal-units-dul-lb': 'libras – lb',
    'option-decimal-units-dul-st': 'stones – st',
    'option-decimal-units-dul-sl': 'slugs – sl',
    'option-decimal-units-dul-US-qr': 'kwartus kurtus – qr EUA',
    'option-decimal-units-dul-US-cwt': 'hundredweights kurtus – cwt EUA',
    'option-decimal-units-dul-US-ton': 'toneladas kurtas – ton EUA',
    'option-decimal-units-dul-imp-qr': 'kwartus longus – qr inp.',
    'option-decimal-units-dul-imp-cwt': 'hundredweights longus – cwt inp.',
    'option-decimal-units-dul-imp-ton': 'toneladas longas – ton inp.',

    'option-units-spn-sampurna': 'sanpurnas – spn',
    'option-decimal-units-spn-cent': 'pur sentu – %',
    'option-decimal-units-spn-thousand': 'pur milyar – ‰',
    'option-decimal-units-spn-ten-thousand': 'pur miríadi – ‱',
    'option-decimal-units-spn-pcm': 'partis pur sêyn miw – pcm',
    'option-decimal-units-spn-ppm': 'partis pur milyawn – ppm',

    'option-units-atk-astaka': 'astakas – atk',
    'option-decimal-units-atk-byte': 'baytis – B',
    'option-decimal-units-atk-bit': 'bitis – b',

    'option-units-pvn-pavana': 'pavanas – pvn',
    'option-decimal-units-pvn-bps': 'bitis pur segundu – bps',
    'option-decimal-units-pvn-Bps': 'baytis pur segundu – Bps',
    'option-decimal-units-pvn-Bpm': 'baytis pur minutu – Bpm',

    'option-units-clt-chalati': 'xalatis (distansya pur volumi) – clt',
    'option-units-clt-pibati': 'pibatis (volumi pur distansya) – pbt',
    'option-decimal-units-clt-kml': 'kilômetrus pur litru – km/L',
    'option-decimal-units-clt-l100km': 'litrus pur 100 kilômetrus – L/100 L',
    'option-decimal-units-clt-km20l': 'kilômetrus pur 20 litrus – km/20 L',
    'option-decimal-units-clt-usmpg': 'milyas pur galawn EUA – mpg EUA',
    'option-decimal-units-clt-impmpg': 'milyas pur galawn inperiaw – mpg inp.',
});

export { sezimal_calculator_bz_text };
