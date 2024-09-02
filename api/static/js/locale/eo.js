
const sezimal_calculator_eo_text = {
    'title': 'Sesuma Kalkulilo',
    'button-sezimal-clear': 'Z',
    'button-decimal-clear': 'Z',
    'button-base-ten': 'dek',
    'button-base-six': 'ses',
    'translation-txt': 'ltr',
    'translation-nif': 'nif',

    'translation-sezimal-calculator': 'Sesuma Kalkulilo',
    'label-sezimal-locale': 'Defina o locale para a formatação dos números',
    'label-sezimal-places': 'Defina a quantidade de casas sezimais',
    'label-sezimal-angle': 'Defina a conversão de unidades de ângulo<br/>para as funções trigonométricas',
    'translation-sezimal-units': 'Ŝastadariaj Mezurunuoj',
    'label-sezimal-units': 'Escolha qual unidade você deseja converter<br/>de ou para as unidades Ŝastadaria,<br/>e veja as explicações e orientações<br/>sobre cada unidade',

    'translation-display-mod': 'mód',
    'translation-display-turn': 'volta',
    // 'translation-display-deg': '°',
    // 'translation-display-arcmin': '′',
    // 'translation-display-arcsec': '″',
    // 'translation-display-gon': 'gon',
    // 'translation-display-rad': 'rad',
    // 'translation-display-tau_rad': 'τ rad',
    // 'translation-display-pi_rad': 'π rad',
    'translation-display-deg2': 'grad²',

    // 'button-sezimal-sin': 'sin',
    'button-sezimal-cos': 'kos',
    // 'button-sezimal-tan': 'tan',
    // 'button-decimal-sin': 'sin',
    'button-decimal-cos': 'kos',
    // 'button-decimal-tan': 'tan',

    // 'translation-display-sin': 'sen',
    // 'translation-display-asin': 'asen',
    'translation-display-csc': 'ksk',
    'translation-display-acsc': 'aksk',
    'translation-display-cos': 'kos',
    'translation-display-acos': 'akos',
    'translation-display-sec': 'sek',
    'translation-display-asec': 'asek',
    // 'translation-display-tan': 'tan',
    // 'translation-display-atan': 'atan',
    'translation-display-cot': 'kot',
    'translation-display-acot': 'akot',

    // 'button-sezimal-ln': 'log<sub class="constant">𝑒</sub>',
    // 'button-sezimal-lsez': 'log₁₀',
    // 'button-sezimal-ldec': 'log₁₄',
    // 'button-decimal-ln': 'log<sub class="constant">𝑒</sub>',
    // 'button-decimal-lsez': 'log₆',
    // 'button-decimal-ldec': 'log₁₀',

    'help-setting': `
<h2>O que é isso?</h2>
<p>Uma calculadora e um conversor de base numérica e unidades de medida, entre as bases sezimal (seis) e decimal (dez).</p>
<p>Você pode usar o aplicativo como uma calculadora decimal comum, e ele vai convertendo os cálculos usando base sezimal, ensinando você como ler os números no processo.</p>
<p>Clicando ou tocando em cada um dos mostradores (sezimal, nifimal, extenso ou decimal), o conteúdo é copiado para a área de transferência.</p>
<h3>Uso dos botões</h3>
<p>Alguns botões dão acesso a mais de uma operação ou função, quando pressionados um certo número de vezes em sequência:</p>
<ul>
    <li>[ 󱹮 ] / [ , ] / [ . ] - o separador sezimal (de acordo com as configurações ou com o locale), quando pressionado duas vezes seguidas, ou pressionado na parte fracionária de um número, dá o separador de fração recorrente (“sézima periódica”) 󱹯 / „ / ‥ (veja mais abaixo detalhes sobre a notação);</li><br/>
    <li>[ × ] - o botão de multiplicação, pressionado duas vezes seguidas, dá o operador ! fatorial;</li><br/>
    <li>[ ÷ ] - o botão de divisão, pressionado duas vezes seguidas, dá a barra de frações ⁄ , que permite entrar números em formato de fração diretamente; pressionado uma terceira vez, dá o operador <i>mód</i> módulo;</li><br/>
    <li>[ ^ ] - o botão da exponenciação alterna entre as operações ^ (exponenciação), ² (elevado ao quadrado), √ (raiz quadrada), ³ (elevado ao cubo), ∛ (raiz cúbica), ^ 1⁄ (raiz arbitrária), e daí de volta para a  ^ exponenciação;</li><br/>
    <li>[ 󱹱 ] - o botão de por nife alterna entre as operações 󱹱 (por nife 10²), 󱹲 (por arda 10³), 󱹳 (por seis arda 10⁴), 󱹴 (por nife arda 10⁵), 󱹵 (por xadara 10¹⁰) - só na base sezimal;</li><br/>
    <li>[ % ] - o botão de porcentagem alterna entre as operações % (por cento 14²), ‰ (por milhar 14³), ‱ (por miríade/dez mil 10⁴) - só na base decimal;</li><br/>
    <li>[ sen ] - o botão da função seno alterna entre as funções sen, asen, csc, acsc;</li><br/>
    <li>[ cos ] - o botão da função cosseno alterna entre as funções cos, acos, sec, asec;</li><br/>
    <li>[ tan ] - o botão da função tangente alterna entre as funções tan, atan, cot, acot;</li><br/>
    <li>[ log<sub class="constant">𝑒</sub> ] - o botão da função logaritmo natural alterna entre as funções log<sub class="constant">𝑒</sub>, a constante <span class="constant">𝑒</span>, log₁₀/log₆ (logaritmo sezimal), log₁₄/log₁₀ (logaritmo decimal);</li><br/>
    <li>[ log₁₀ ] - o botão da função logaritmo sezimal alterna entre as funções log₁₀/log₆ (logaritmo sezimal) e log₁₄/log₁₀ (logaritmo decimal);</li><br/>
    <li>[ τ ] - o botão da constante τ alterna entre as constantes τ e π;</li>
</ul>
<p>Os botões de ajuste na primeira linha do mostrador têm as seguintes funções:</p>
<ul>
    <li>[ ? ] - mostra este texto de ajuda;</li><br/>
    <li>[ en ] - permite selecionar o idioma e o país, o que determina como os números vão ser formatados, e define o idioma do aplicativo;</li><br/>
    <li>[ 3 ] / [ 󱸃 ] - usa dígitos comuns [ 3 ] ou dígitos sezimais [ 󱸃 ] (veja mais abaixo) para os mostradores sezimal e nifimal, e para os botões sezimais (a base decimal sempre usa os dígitos comuns);</li><br/>
    <li>[ 3󱹬3 ] / [ 󱸃󱹬󱸃 ] - determina como os números são agrupados e separados:<br/>
        <ul>
            <li>[ 3󱹬3 ] / [ 󱸃󱹬󱸃 ] - separadores sezimais (veja mais abaixo), a cada três dígitos;</li><br/>
            <li>[ 3.3 ] / [ 󱸃.󱸃 ] - separadores decimais/tradicionais, de acordo com o locale (idioma e país) selecionados, a cada três dígitos;</li><br/>
            <li>[ 4.4 ] / [ 󱸄.󱸄 ] - separadores decimais/tradicionais, de acordo com o locale (idioma e país) selecionados, a cada quatro dígitos (como no site seximal.net); isso também altera, em inglês, o resultado do mostrador do número por extenso, que passa a usar seis nife e unexião no lugar de arda e xadara;</li>
        </ul>
    </li><br/>
    <li>[ nife 5̆ ] / [ nife 󱸣 ] - define o uso e conversão do mostrador nifimal:<br/>
        <ul>
            <li>[ nife 5̆ ] / [ nife 󱸣 ] - o mostrator nifimal usa dígitos regularizados (veja abaixo);</li><br/>
            <li>[ nife Z ] - o mostrator nifimal usa os dígitos 0123456789 e letras a partir do número 14 (em decimal, dez);</li><br/>
            <li>[ <span style="text-decoration: line-through;">nife</span> ] - oculta o mostrador nifimal;</li>
        </ul>
    </li><br/>
    <li>[ ext ] - ativa [ ext ] / desativa [ <span style="text-decoration: line-through;">ext</span> ] a exibição dos números sezimais por extenso (por enquanto, somente disponível em português, brasileiro [ortografia fonêmica], inglês e Esperanto);</li><br/>
</ul>
<p>E os botões de ajuste na segunda linha do mostrador:</p>
<ul>
    <li>[ mdl <img src="https://midia.tauga.online/img/sezimal/mandala-logo-black-on-white-small.svg" width="12rem" /> ° ] - unidades de medida de ângulos para as funções trigonométricas sezimais e decimais;</li><br/>
    <li>[ <img src="https://midia.tauga.online/img/sezimal/shastadari-logo-black-on-white-small.svg" width="12rem" /> ] - unidades e prefixos Ŝastadaria convertidos de ou para unidades e prefixo do Sistema Internacional de Medidas (e algumas unidades tradicionais fora do SI);</li><br/>
    <li>[ 0󱹮3 ] - em quantos dígitos depois do separador sezimais o resultado vai ser arredondado; a precisão em base decimal vai ser ajustada baseada na precisão da base sezimal;</li><br/>
</ul>
<h2>Notação usada</h2>
<ul>
    <li>Nomes dos números - 0 zero; 1 um; 2 dois; 3 três; 4 quatro; 5 cinco; 10 seis; 11 sete; 12 oito; 13 nove; 14 dez; 15 onze; 20 doze; 21 doze e um; 22 doze e dois; 23 doze e três; 24 doze e quatro; 25 doze e cinco; 30 tresseis; 40 quasseis; 50 quinseis; 100 nife (da língua ndom <i>nif</i> para trinta e seis); 1󱹭000 arda (do sânscrito अर्ध <i>ardha</i> para meio, metade, para metade de seis dígitos); 10󱹭000 seis arda; 100󱹭000 nife arda; 1󱹬000󱹭000 xadara (do sânscrito षडार <i>ṣaḍāra</i> para um grupo de seis, ou um hexágono); de xadara se segue 10󱹬000󱹭000 seis xadara, 100󱹬000󱹭000 nife xadara, 1󱹭000󱹬000󱹭000 arda xadara (em escala longa, como em português europeu), 10󱹭000󱹬000󱹭000 seis arda xadara, 100󱹭000󱹬000󱹭000 nife arda xadara, dixadara 1󱹬000󱹭000󱹬000󱹭000 (<i>di</i> do sânscrito द्वि <i>dvi</i> para dois); trixadara para 10³⁰ (<i>tri</i> do sânscrito त्रि <i>tri</i> para três); tcharxadara para 10⁴⁰ (<i>tchar</i> do sânscrito चतुर् <i>catur</i> para quatro); panxadara para 10⁵⁰ (<i>pan</i> do sânscrito पञ्चन् <i>pañcan</i>, cinco); xaxadara para 10¹⁰⁰ (<i>xa</i> do sânscrito षष् <i>ṣaṣ</i> para seis); use a função de números por extenso para saber como ler qualquer número sezimal</li><br/>
    <li>Separador sezimal 󱹮 - uma barra em forma de agulha, apontando para cima, que se inicia sobre a linha base da escrita, pelo meio da altura X da fonte, e se extende para baixo até o ponto mais baixo dos descendentes da fonte; seu código Unicode é U+F1E6E; compare o separador sezimal com a vírgula e o ponto: ,󱹮.</li><br/>
    <li>Separador periódico 󱹯 „ ‥  - dobrando o separador fracionário (sezimal ou decimal) resulta no separador periódico; por exemplo, a fração sezimal 1⁄5 pode ser escrita 0󱹯1 (0󱹮1̅) = 0󱹮111...; 1⁄11 0󱹯05 = 0󱹮0̅5̅ = 0󱹮050󱹭505...; a fração decimal 1⁄3 0„3 (0,3̅) = 0,333...; decimal 1⁄12 0,08„3 (0,083̅) = 0.083 333...; esse último exemplo, se o separador periódico, é ambíguo: é só o 3 que se repete, ou 08333? Para o separador periódico num único caracter(como neste aplicativo), os códigos Unicode são 󱹯 U+F1E6F, „ U+201E e ‥ U+2025;</li><br/>
    <li>Separador de arda ⍽ - o espaço inseparável estreito, código Unicode U+202F, é usado para marcar o primeiro grupo de três dígitos à esquerda e à direita do separador sezimal, e, a partir daí, a cada grupo de seis dígitos, na prática se alternando com o separador de xadara;</li><br/>
    <li>Separador de xadara 󱹬 - tem a mesma forma básica do separador sezimal, com um sexto do tamanho, apontando para baixo, se extendendo para baixo a partir do ponto mais alto da fonte usada, e marca a posição dos xadaras a cada grupo de seis dígitos nos números sezimais, tanto à esquerda quanto à direita do separador sezimal; seu código Unicode é U+F1E6C; compare o separador de xadara com o apóstrofe reto/aspas simples reta '󱹬;</li><br/>
    <li>Dígitos sezimais - 󱸀󱸁󱸂󱸃󱸄󱸅 para 012345; é uma representação dedicada exclusiva para números sezimais; é uma escrita distintiva (<i>featural script</i>), mapeando três áreas que representam valores: <span class="horizontal-flip">◔</span> superior à esquerda representa o valor 1, ◔ superior à direita representa o valor 2, ◒ e abaixo também representa o valor 2; cada dígito, afora o zero, “abraça” ou “aponta” para as áreas cujos valores, somados, representam seu valor: <span class="horizontal-flip">◔</span> 󱸁 um; ◔ 󱸂 dois; <span class="horizontal-flip">◔</span> + ◔ = ◓ 󱸃 três; ◔ + ◒ = ◕ 󱸄 quatro; <span class="horizontal-flip">◔</span> + ◔ + ◒ = ● 󱸅 cinco;</li><br/>
    <li>Dígitos nifemais regularizados - a representação convencional da base nife (trinta e seis) usa letras para os dígitos a partir de dez; a representação regularizada usa os mesmos seis dígitos usados na numeração sezimal 012345/󱸀󱸁󱸂󱸃󱸄󱸅 e os extende por meio de cinco sinais diacríticos (ou “acentos”):<br/>
        <ul>
            <li>+00: 012345 󱸀󱸁󱸂󱸃󱸄󱸅 <span style="font-family: 'Sezimal Mono', monospace;">012345</span></li><br/>
            <li>+10: 0̇1̇2̇3̇4̇5̇ 󱸆󱸇󱸈󱸉󱸊󱸋 <span style="font-family: 'Sezimal Mono', monospace;">6789AB</span></li><br/>
            <li>+20: 0̈1̈2̈3̈4̈5̈ 󱸌󱸍󱸎󱸏󱸐󱸑 <span style="font-family: 'Sezimal Mono', monospace;">CDEFGH</span></li><br/>
            <li>+30: 0̊1̊2̊3̊4̊5̊ 󱸒󱸓󱸔󱸕󱸖󱸗 <span style="font-family: 'Sezimal Mono', monospace;">IJKLMN</span></li><br/>
            <li>+40: 0̄1̄2̄3̄4̄5̄ 󱸘󱸙󱸚󱸛󱸜󱸝 <span style="font-family: 'Sezimal Mono', monospace;">OPQRST</span></li><br/>
            <li>+50: 0̆1̆2̆3̆4̆5̆ 󱸞󱸟󱸠󱸡󱸢󱸣 <span style="font-family: 'Sezimal Mono', monospace;">UVWXYZ</span></li><br/>
            <li>˚ é a parte de cima do 󱸃;  ˉ é a parte de cima do 󱸄; ˘ vem da parte de cima do 󱸅</li>
        </ul>
    </li>
</ul>
<p />
<p />
`,

    //
    // Unidades
    //
    'td-shastadari-units': 'Ŝastadariaj Mezurunuoj',
    'optgroup-units-no-conversion': 'Nenia konverto',
    'option-units-no-conversion': 'Nenia konverto (nur kalkulilo)',
    'optgroup-units-derived': 'Mecânica',
    'option-units-ang': 'Tempo',
    'option-units-avt': 'Frequência',
    'option-units-pad': 'Comprimento',
    'option-units-ktr': 'Área',
    'option-units-ayt': 'Volume',
    'option-units-veg': 'Velocidade',
    'option-units-tvr': 'Aceleração',
    'option-units-drv': 'Massa',
    'option-units-gnt': 'Densidade',
    'option-units-bar': 'Força/peso',
    'option-units-pdn': 'Pressão',
    'option-units-vrc': 'Energia/trabalho',
    'option-units-xkt': 'Potência',
    // 'option-units-svg': 'Momento',
    // 'option-units-agh': 'Ação',
    // 'option-units-pbv': 'Influência',
    // 'option-units-tnv': 'Tensão',
    // 'option-units-upr': 'Intensidade',
    // 'option-units-nad': 'Viscosidade dinâmica',
    // 'option-units-bum': 'Viscosidade cinética',
    'optgroup-units-thermodynamics': 'Termodinâmica',
    'option-units-tap': 'Temperatura comum',
    'option-units-gtk': 'Temperatura termodinâmica',
    'option-units-agn': 'Capacidade térmica',
    'option-units-idn': 'Capacidade térmica por massa',
    'option-units-tln': 'Capacidade térmica por volume',
    'optgroup-units-electromagnetism': 'Eletromagnetismo',
    'option-units-vdt': 'Carga el.',
    'option-units-dar': 'Corrente el.',
    'option-units-atr': 'Diferença de potencial el.',
    'option-units-vrd': 'Resistência el.',
    'option-units-vht': 'Condutância el.',
    'option-units-upp': 'Indutância el.',
    'option-units-smi': 'Capacitância el.',
    'option-units-pvh': 'Fluxo mag.',
    'option-units-vtr': 'Densidade do fluxo mag.',
    'optgroup-units-angle': 'Ângulo',
    'option-units-mdl': 'Ângulo plano',
    'option-units-gol': 'Ângulo sólido',
    'optgroup-units-proportion': 'Proporção',
    'option-units-spn': 'Proporção',
    'optgroup-units-data-information': 'Dados/informação',
    'option-units-atk': 'Armazenagem',
    'option-units-pvn': 'Velocidade',

    'label-prefix-sezimal': 'Sesuma prefikso',
    'label-prefix-sezimal-angle': 'Sesuma prefikso',
    'label-unit-sezimal': 'Sesuma unuo',
    'label-prefix-decimal': 'Dekuma prefikso',
    'label-prefix-decimal-angle': 'Dekuma prefikso',
    'label-prefix-decimal-binary': 'Dekuma/duuma prefikso',
    'label-unit-decimal': 'Dekuma unuo',
    'optgroup-units-generic-shastadari': 'Ŝastadaria',
    'optgroup-units-generic-s-i': 'I.S.',
    'optgroup-units-generic-others': 'Aliaj',
    'optgroup-units-generic-imp-us': 'Anglaj/Usonaj',
    'optgroup-units-generic-us': 'Usonaj',
    'optgroup-units-generic-imp': 'Anglaj',
    'optgroup-units-generic-us-fluid': 'Usonaj - lik. volumeno',
    'optgroup-units-generic-us-dry': 'Usonaj - seka volumeno',
    'optgroup-units-generic-imp-fluid': 'Anglaj',

    //
    // Sezimal Prefixes
    //
    'option-sezimal-prefix-ndxm': 'NDX – nidiŝama  – 10¹²⁰',
    'option-sezimal-prefix-nxpm': 'NXP – niŝapama  – 10¹¹⁵',
    'option-sezimal-prefix-nxcm': 'NXC – niŝaĉarma – 10¹¹⁴',
    'option-sezimal-prefix-nxtm': 'NXT – niŝatrima – 10¹¹³',
    'option-sezimal-prefix-nxdm': 'NXD – niŝadima  – 10¹¹²',
    'option-sezimal-prefix-nxem': 'NXE – niŝaekama – 10¹¹¹',
    'option-sezimal-prefix-nxm': 'NX – niŝama – 10¹¹⁰',
    'option-sezimal-prefix-npm': 'NP – nipama – 10¹⁰⁵',
    'option-sezimal-prefix-ncm': 'NC – niĉarma  – 10¹⁰⁴',
    'option-sezimal-prefix-ntm': 'NT – nitrima – 10¹⁰³',
    'option-sezimal-prefix-ndm': 'ND – nidima – 10¹⁰²',
    'option-sezimal-prefix-nem': 'NE – niekama – 10¹⁰¹',
    'option-sezimal-prefix-nm': 'N – nima – 10¹⁰⁰',
    'option-sezimal-prefix-ppm': 'PP – panpama – 10⁵⁵',
    'option-sezimal-prefix-pcm': 'PC – panĉarma – 10⁵⁴',
    'option-sezimal-prefix-ptm': 'PT – pantrima  – 10⁵³',
    'option-sezimal-prefix-pdm': 'PD – pandima – 10⁵²',
    'option-sezimal-prefix-pem': 'PE – panekama  – 10⁵¹',
    'option-sezimal-prefix-pxm': 'PX – panŝama  – 10⁵⁰',
    'option-sezimal-prefix-cpm': 'CP – ĉarpama  – 10⁴⁵',
    'option-sezimal-prefix-ccm': 'CC – ĉarĉarma  – 10⁴⁴',
    'option-sezimal-prefix-ctm': 'CT – ĉartrima – 10⁴³',
    'option-sezimal-prefix-cdm': 'CD – ĉardima  – 10⁴²',
    'option-sezimal-prefix-cem': 'CE – ĉarekama – 10⁴¹',
    'option-sezimal-prefix-cxm': 'CX – ĉarŝama – 10⁴⁰',
    'option-sezimal-prefix-tpm': 'TP – tripama – 10³⁵',
    'option-sezimal-prefix-tcm': 'TC – triĉarma – 10³⁴',
    'option-sezimal-prefix-ttm': 'TT – tritrima  – 10³³',
    'option-sezimal-prefix-tdm': 'TD – tridima – 10³²',
    'option-sezimal-prefix-tem': 'TE – triekama  – 10³¹',
    'option-sezimal-prefix-txm': 'TX – triŝama  – 10³⁰',
    'option-sezimal-prefix-dpm': 'DP – dipama – 10²⁵',
    'option-sezimal-prefix-dcm': 'DC – diĉarma  – 10²⁴',
    'option-sezimal-prefix-dtm': 'DT – ditrima – 10²³',
    'option-sezimal-prefix-ddm': 'DD – didima – 10²²',
    'option-sezimal-prefix-dem': 'DE – diekama – 10²¹',
    'option-sezimal-prefix-dxm': 'DX – diŝama – 10²⁰',
    'option-sezimal-prefix-xpm': 'XP – ŝapama – 10¹⁵',
    'option-sezimal-prefix-xcm': 'XC – ŝaĉarma – 10¹⁴',
    'option-sezimal-prefix-xtm': 'XT – ŝatrima  – 10¹³',
    'option-sezimal-prefix-xdm': 'XD – ŝadima – 10¹²',
    'option-sezimal-prefix-xem': 'XE – ŝaekama  – 10¹¹',
    'option-sezimal-prefix-xm': 'X – ŝama – 10¹⁰',
    'option-sezimal-prefix-pm': 'P – pama – 10⁵',
    'option-sezimal-prefix-cm': 'C – ĉarma – 10⁴',
    'option-sezimal-prefix-tm': 'T – trima – 10³',
    'option-sezimal-prefix-dm': 'D – dima – 10²',
    'option-sezimal-prefix-em': 'E – ekama – 10¹',
    'option-sezimal-prefix-ei': 'e – ekati – 10⁻¹',
    'option-sezimal-prefix-di': 'd – diti – 10⁻²',
    'option-sezimal-prefix-ti': 't – triti – 10⁻³',
    'option-sezimal-prefix-ci': 'c – ĉarti – 10⁻⁴',
    'option-sezimal-prefix-pi': 'p – panti – 10⁻⁵',
    'option-sezimal-prefix-xi': 'x – ŝati – 10⁻¹⁰',
    'option-sezimal-prefix-xei': 'xe – ŝaekati – 10⁻¹¹',
    'option-sezimal-prefix-xdi': 'xd – ŝaditi – 10⁻¹²',
    'option-sezimal-prefix-xti': 'xt – ŝatriti – 10⁻¹³',
    'option-sezimal-prefix-xci': 'xc – ŝaĉarti – 10⁻¹⁴',
    'option-sezimal-prefix-xpi': 'xp – ŝapanti – 10⁻¹⁵',
    'option-sezimal-prefix-dxi': 'dx – diŝati – 10⁻²⁰',
    'option-sezimal-prefix-dei': 'de – diekati – 10⁻²¹',
    'option-sezimal-prefix-ddi': 'dd – diditi – 10⁻²²',
    'option-sezimal-prefix-dti': 'dt – ditriti – 10⁻²³',
    'option-sezimal-prefix-dci': 'dc – diĉarti – 10⁻²⁴',
    'option-sezimal-prefix-dpi': 'dp – dipanti – 10⁻²⁵',
    'option-sezimal-prefix-txi': 'tx – triŝati – 10⁻³⁰',
    'option-sezimal-prefix-tei': 'te – triekati – 10⁻³¹',
    'option-sezimal-prefix-tdi': 'td – triditi – 10⁻³²',
    'option-sezimal-prefix-tti': 'tt – tritriti – 10⁻³³',
    'option-sezimal-prefix-tci': 'tc – triĉarti – 10⁻³⁴',
    'option-sezimal-prefix-tpi': 'tp – tripanti – 10⁻³⁵',
    'option-sezimal-prefix-cxi': 'cx – ĉarŝati – 10⁻⁴⁰',
    'option-sezimal-prefix-cei': 'ce – ĉarekati – 10⁻⁴¹',
    'option-sezimal-prefix-cdi': 'cd – ĉarditi – 10⁻⁴²',
    'option-sezimal-prefix-cti': 'ct – ĉartriti – 10⁻⁴³',
    'option-sezimal-prefix-cci': 'cc – ĉarĉarti – 10⁻⁴⁴',
    'option-sezimal-prefix-cpi': 'cp – ĉarpanti – 10⁻⁴⁵',
    'option-sezimal-prefix-pxi': 'px – panŝati – 10⁻⁵⁰',
    'option-sezimal-prefix-pei': 'pe – panekati – 10⁻⁵¹',
    'option-sezimal-prefix-pdi': 'pd – panditi – 10⁻⁵²',
    'option-sezimal-prefix-pti': 'pt – pantriti – 10⁻⁵³',
    'option-sezimal-prefix-pci': 'pc – panĉarti – 10⁻⁵⁴',
    'option-sezimal-prefix-ppi': 'pp – panpanti – 10⁻⁵⁵',
    'option-sezimal-prefix-ni': 'n – niti – 10⁻¹⁰⁰',
    'option-sezimal-prefix-nei': 'ne – niekati – 10⁻¹⁰¹',
    'option-sezimal-prefix-ndi': 'nd – niditi – 10⁻¹⁰²',
    'option-sezimal-prefix-nti': 'nt – nitriti – 10⁻¹⁰³',
    'option-sezimal-prefix-nci': 'nc – niĉarti – 10⁻¹⁰⁴',
    'option-sezimal-prefix-npi': 'np – nipanti – 10⁻¹⁰⁵',
    'option-sezimal-prefix-nxi': 'nx – niŝati – 10⁻¹¹⁰',
    'option-sezimal-prefix-nxei': 'nxe – niŝaekati – 10⁻¹¹¹',
    'option-sezimal-prefix-nxdi': 'nxd – niŝaditi – 10⁻¹¹²',
    'option-sezimal-prefix-nxti': 'nxt – niŝatriti – 10⁻¹¹³',
    'option-sezimal-prefix-nxci': 'nxc – niŝaĉarti – 10⁻¹¹⁴',
    'option-sezimal-prefix-nxpi': 'nxp – niŝapanti – 10⁻¹¹⁵',
    'option-sezimal-prefix-ndxi': 'ndx – nidiŝati – 10⁻¹²⁰',

    //
    // Decimal Prefixes
    //
    'option-decimal-prefix-quetta': 'Q – queta – 10³⁰',
    'option-decimal-prefix-ronna': 'R – rona – 10²⁷',
    'option-decimal-prefix-yotta': 'Y – yota – 10²⁴',
    'option-decimal-prefix-zetta': 'Z – zeta – 10²¹',
    'option-decimal-prefix-exa': 'E – exa – 10¹⁸',
    'option-decimal-prefix-peta': 'P – peta – 10¹⁵',
    'option-decimal-prefix-tera': 'T – tera – 10¹²',
    'option-decimal-prefix-giga': 'G – giga – 10⁹',
    'option-decimal-prefix-mega': 'M – mega – 10⁶',
    'option-decimal-prefix-kilo': 'k – quilo – 10³',
    'option-decimal-prefix-hecto': 'h – hecto – 10²',
    'option-decimal-prefix-deca': 'da – deca – 10¹',
    'option-decimal-prefix-deci': 'd – deci – 10⁻¹',
    'option-decimal-prefix-centi': 'c – centi – 10⁻²',
    'option-decimal-prefix-milli': 'm – mili – 10⁻³',
    'option-decimal-prefix-micro': 'µ – micro – 10⁻⁶',
    'option-decimal-prefix-nano': 'n – nano – 10⁻⁹',
    'option-decimal-prefix-pico': 'p – pico – 10⁻¹²',
    'option-decimal-prefix-femto': 'f – fento – 10⁻¹⁵',
    'option-decimal-prefix-atto': 'a – ato – 10⁻¹⁸',
    'option-decimal-prefix-zepto': 'z – zeto – 10⁻²¹',
    'option-decimal-prefix-yocto': 'y – yoto – 10⁻²⁴',
    'option-decimal-prefix-ronto': 'r – ronto – 10⁻²⁷',
    'option-decimal-prefix-quecto': 'q – queto – 10⁻³⁰',

    //
    // Binary Prefixes
    //
    'optgroup-units-generic-binary': 'Duumaj',
    'option-binary-prefix-yobi': 'Yi – yobi – 2⁸⁰',
    'option-binary-prefix-zebi': 'Zi – zebi – 2⁷⁰',
    'option-binary-prefix-exbi': 'Ei – exbi – 2⁶⁰',
    'option-binary-prefix-pebi': 'Ei – pebi – 2⁵⁰',
    'option-binary-prefix-tebi': 'Ti – tebi – 2⁴⁰',
    'option-binary-prefix-gibi': 'Gi – gibi – 2³⁰',
    'option-binary-prefix-mebi': 'Mi – mebi – 2²⁰',
    'option-binary-prefix-kibi': 'Ki – kibi – 2¹⁰',

    // 'optgroup-units-ang-common': 'Comum/civil',
    'option-units-ang-dina': 'dinao – din = tago',
    'option-units-ang-uta': 'utao – uta ~ horo',
    'option-units-ang-posha': 'poŝao – pox ~ minuto',
    'option-units-ang-agrima': 'agrimao – agm ~ sekundo',
    'option-units-ang-anuga': 'anugao – ang ~ sek. centonoj',
    'option-units-ang-boda': 'bodao – bod ~ sek. milonoj',

    'option-decimal-units-ang-day': 'tago',
    'option-decimal-units-ang-hour': 'horo – h',
    'option-decimal-units-ang-minute': 'minuto – min',
    'option-decimal-units-ang-second': 'segundo – s',

    'translation-day': 'tago',
    'translation-hour': 'h',
    'translation-minute': 'min',
    'translation-second': 's',

    'option-units-avt-avriti': 'avritio – avt',
    'option-decimal-units-avt-hertz': 'Hertz – Hz',
    'option-decimal-units-avt-rpm': 'rpm',

    'option-units-pad-pada': 'pada – pad',
    'option-decimal-units-pad-metre': 'metro – m',
    'option-decimal-units-pad-mile': 'milha – ml',
    'option-decimal-units-pad-yard': 'jarda – yd',
    'option-decimal-units-pad-foot': 'pé – ft',
    'option-decimal-units-pad-inch': 'polegada – in',

    'option-units-ktr-ketra': 'quetra – ktr',
    'option-units-ktr-sq-pada': 'pada quad. – pad²',
    'option-decimal-units-ktr-sq-metre': 'metro quad. – m²',
    'option-decimal-units-ktr-are': 'are - a',
    'option-decimal-units-ktr-acre': 'acre - ac',
    'option-decimal-units-ktr-sq-mile': 'milha quad. – ml²',
    'option-decimal-units-ktr-sq-yard': 'jarda quad. – yd²',
    'option-decimal-units-ktr-sq-foot': 'pé quad. – ft²',
    'option-decimal-units-ktr-sq-inch': 'polegada quad. – in²',

    'option-units-ayt-aytan': 'aitã – ayt',

    'option-decimal-units-mdl-mdl': 'mandalas',
    'option-decimal-units-mdl-tau_rad': 'τ radianos',
    'option-decimal-units-mdl-pi_rad': 'π radianos',
    'option-decimal-units-mdl-rad': 'radianos',
    'option-decimal-units-mdl-deg': 'graus',
    'option-decimal-units-mdl-arcmin': 'minutos',
    'option-decimal-units-mdl-arcsec': 'segundos',
    'option-decimal-units-mdl-turn': 'voltas',
    'option-decimal-units-mdl-gon': 'gradianos (gon)',
};

export { sezimal_calculator_eo_text };
