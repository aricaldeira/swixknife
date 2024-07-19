
const sezimal_calculator_pt_text = {
    'title': 'Calculadora Sezimal',
    'button-sezimal-clear': 'Z',
    'button-decimal-clear': 'Z',
    'button-base-ten': 'dec',
    'button-base-six': 'sez',
    'translation-txt': 'ext',
    'translation-nif': 'nife',

    'translation-sezimal-calculator': 'Calculadora Sezimal',
    'label-sezimal-locale': 'Defina o locale para a formatação dos números',
    'label-sezimal-places': 'Defina a quantidade de casas sezimais',
    'label-sezimal-angle': 'Defina a conversão de unidades de ângulo<br/>para as funções trigonométricas',
    'translation-sezimal-units': 'Unidades de Medida Xastadári',
    'label-sezimal-units': 'Escolha qual unidade você deseja converter<br/>de ou para as unidades Xastadári,<br/>e veja as explicações e orientações<br/>sobre cada unidade',


    'translation-turn': 'volta',
    'translation-deg': 'grau',
    'translation-arcmin': 'min',
    'translation-arcseg': 'seg',

    'translation-display-mod': 'mód',
    'translation-display-turn': 'volta',
    'translation-display-deg': '°',
    'translation-display-arcmin': '′',
    'translation-display-arcsec': '″',
    'translation-display-gon': 'gon',
    'translation-display-rad': 'rad',
    'translation-display-tau_rad': 'τ rad',
    'translation-display-pi_rad': 'π rad',

    'button-sezimal-sin': 'sen',
    'button-sezimal-cos': 'cos',
    'button-sezimal-tan': 'tan',
    'button-decimal-sin': 'sen',
    'button-decimal-cos': 'cos',
    'button-decimal-tan': 'tan',

    'translation-display-sin': 'sen',
    'translation-display-asin': 'asen',
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
    <li>[ log<i>ₑ</i> ] - o botão da função logaritmo natural alterna entre as funções log<i>ₑ</i>, a constante <i>e</i>, log₁₀/log₆ (logaritmo sezimal), log₁₄/log₁₀ (logaritmo decimal);</li><br/>
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
    <li>[ prd ◕ ° ] - unidades de medida de ângulos para as funções trigonométricas sezimais e decimais;</li><br/>
    <li>[ ⬢ ] - unidades e prefixos Xastadári convertidos de ou para unidades e prefixo do Sistema Internacional de Medidas (e algumas unidades tradicionais fora do SI);</li><br/>
    <li>[ 0󱹮3 ] - em quantos dígitos depois do separador sezimais o resultado vai ser arredondado; a precisão em base decimal vai ser ajustada baseada na precisão da base sezimal;</li><br/>
</ul>
<h2>Notação usada</h2>
<ul>
    <li>Nomes dos números - 0 zero; 1 um; 2 dois; 3 três; 4 quatro; 5 cinco; 10 seis; 11 sete; 12 oito; 13 nove; 14 dez; 15 onze; 20 doze; 21 doze e um; 22 doze e dois; 23 doze e três; 24 doze e quatro; 25 doze e cinco; 30 tresseis; 40 quasseis; 50 quinseis; 100 nife (da língua ndom <i>nif</i> para trinta e seis); 1 000 arda (do sânscrito अर्ध <i>ardha</i> para meio, metade, para metade de seis dígitos); 10 000 seis arda; 100 000 nife arda; 1󱹬000 000 xadara (do sânscrito षडार <i>ṣaḍāra</i> para um grupo de seis, ou um hexágono); de xadara se segue 10󱹬000 000 seis xadara, 100󱹬000 000 nife xadara, 1 000󱹬000 000 arda xadara (em escala longa, como em português europeu), 10 000󱹬000 000 seis arda xadara, 100 000󱹬000 000 nife arda xadara, dixadara 1󱹬000 000󱹬000 000 (<i>di</i> do sânscrito द्वि <i>dvi</i> para dois); trixadara para 10³⁰ (<i>tri</i> do sânscrito त्रि <i>tri</i> para três); tcharxadara para 10⁴⁰ (<i>tchar</i> do sânscrito चतुर् <i>catur</i> para quatro); panxadara para 10⁵⁰ (<i>pan</i> do sânscrito पञ्चन् <i>pañcan</i>, cinco); xaxadara para 10¹⁰⁰ (<i>xa</i> do sânscrito षष् <i>ṣaṣ</i> para seis); use a função de números por extenso para saber como ler qualquer número sezimal</li><br/>
    <li>Separador sezimal 󱹮 - uma barra em forma de agulha, apontando para cima, que se inicia sobre a linha base da escrita, pelo meio da altura X da fonte, e se extende para baixo até o ponto mais baixo dos descendentes da fonte; seu código Unicode é U+F1E6E; compare o separador sezimal com a vírgula e o ponto: ,󱹮.</li><br/>
    <li>Separador periódico 󱹯 „ ‥  - dobrando o separador fracionário (sezimal ou decimal) resulta no separador periódico; por exemplo, a fração sezimal 1⁄5 pode ser escrita 0󱹯1 (0󱹮1̅) = 0󱹮111...; 1⁄11 0󱹯05 = 0󱹮0̅5̅ = 0󱹮050 505...; a fração decimal 1⁄3 0„3 (0,3̅) = 0,333...; decimal 1⁄12 0,08„3 (0,083̅) = 0.083 333...; esse último exemplo, se o separador periódico, é ambíguo: é só o 3 que se repete, ou 08333? Para o separador periódico num único caracter(como neste aplicativo), os códigos Unicode são 󱹯 U+F1E6F, „ U+201E e ‥ U+2025;</li><br/>
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
    'td-shastadari-units': 'Unidades de Medida Xastadári',
    'optgroup-units-no-conversion': 'Sem conversão',
    'option-units-no-conversion': 'Sem conversão (só calculadora)',
    'optgroup-units-instructions': 'Instruções',
    'option-units-units': 'Unidades Xastadári',
    'option-units-prefixes': 'Prefixos Xastadári',
    'optgroup-units-mechanics': 'Mecânica',
    'option-units-ang': 'Tempo',
    'option-units-avt': 'Frequência',
    'option-units-pad': 'Comprimento',
    'option-units-ktr': 'Área',
    'option-units-ayt': 'Volume',
    'option-units-veg': 'Velocidade',
    'option-units-tvr': 'Aceleração',
    'option-units-drv': 'Massa',
    'option-units-gan': 'Densidade',
    'option-units-bar': 'Força/peso',
    'option-units-dab': 'Pressão',
    'option-units-kry': 'Energia/trabalho',
    'option-units-xat': 'Potência',
    // 'option-units-svg': 'Momento',
    // 'option-units-pkp': 'Ação',
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
    'option-units-avx': 'Carga el.',
    'option-units-dar': 'Corrente el.',
    'option-units-vbv': 'Diferença de potencial el.',
    'option-units-ptr': 'Resistência el.',
    'option-units-cln': 'Condutância el.',
    'option-units-prk': 'Indutância el.',
    'option-units-smi': 'Capacitância el.',
    'option-units-abv': 'Fluxo mag.',
    'option-units-vtr': 'Densidade do fluxo mag.',
    'optgroup-units-angle': 'Ângulo',
    'option-units-prd': 'Ângulo plano',
    'option-units-gol': 'Ângulo sólido',
    'optgroup-units-proportion': 'Proporção',
    'option-units-prt': 'Proporção',
    'optgroup-units-data-information': 'Dados/informação',
    'option-units-atk': 'Armazenagem',
    'option-units-pvn': 'Velocidade',

    'label-prefix-sezimal': 'Prefixo sezimal',
    'label-prefix-sezimal-angle': 'Prefixo sezimal',
    'label-unit-sezimal': 'Unidade sezimal',
    'label-prefix-decimal': 'Prefixo decimal',
    'label-prefix-decimal-angle': 'Prefixo decimal',
    'label-prefix-decimal-binary': 'Prefixo decimal/binário',
    'label-unit-decimal': 'Unidade decimal',
    'optgroup-units-generic-shastadari': 'Xastadári',
    'optgroup-units-generic-s-i': 'S.I.',
    'optgroup-units-generic-non-s-i': 'Outras',
    'optgroup-units-generic-us-uk': 'Reino Unido (imperial)/EUA',
    'optgroup-units-generic-us': 'EUA',
    'optgroup-units-generic-uk': 'Reino Unido (imperial)',
    'optgroup-units-generic-us-fluid': 'EUA - volume líq.',
    'optgroup-units-generic-us-dry': 'EUA - volume seco',
    'optgroup-units-generic-uk-fluid': 'Reino Unido (imperial)',

    //
    // Sezimal Prefixes
    //
    'option-sezimal-prefix-ndxm': 'NDX – nidixama  – 10¹²⁰',
    'option-sezimal-prefix-nxpm': 'NXP – nixapama  – 10¹¹⁵',
    'option-sezimal-prefix-nxcm': 'NXC – nixacharma – 10¹¹⁴',
    'option-sezimal-prefix-nxtm': 'NXT – nixatrima – 10¹¹³',
    'option-sezimal-prefix-nxdm': 'NXD – nixadima  – 10¹¹²',
    'option-sezimal-prefix-nxem': 'NXE – nixaecama – 10¹¹¹',
    'option-sezimal-prefix-nxm': 'NX – nixama – 10¹¹⁰',
    'option-sezimal-prefix-npm': 'NP – nipama – 10¹⁰⁵',
    'option-sezimal-prefix-ncm': 'NC – nicharma  – 10¹⁰⁴',
    'option-sezimal-prefix-ntm': 'NT – nitrima – 10¹⁰³',
    'option-sezimal-prefix-ndm': 'ND – nidima – 10¹⁰²',
    'option-sezimal-prefix-nem': 'NE – niecama – 10¹⁰¹',
    'option-sezimal-prefix-nm': 'N – nima – 10¹⁰⁰',
    'option-sezimal-prefix-ppm': 'PP – panpama – 10⁵⁵',
    'option-sezimal-prefix-pcm': 'PC – pancharma – 10⁵⁴',
    'option-sezimal-prefix-ptm': 'PT – pantrima  – 10⁵³',
    'option-sezimal-prefix-pdm': 'PD – pandima – 10⁵²',
    'option-sezimal-prefix-pem': 'PE – panecama  – 10⁵¹',
    'option-sezimal-prefix-pxm': 'PX – panxama  – 10⁵⁰',
    'option-sezimal-prefix-cpm': 'CP – charpama  – 10⁴⁵',
    'option-sezimal-prefix-ccm': 'CC – charcharma  – 10⁴⁴',
    'option-sezimal-prefix-ctm': 'CT – chartrima – 10⁴³',
    'option-sezimal-prefix-cdm': 'CD – chardima  – 10⁴²',
    'option-sezimal-prefix-cem': 'CE – charecama – 10⁴¹',
    'option-sezimal-prefix-cxm': 'CX – charxama – 10⁴⁰',
    'option-sezimal-prefix-tpm': 'TP – tripama – 10³⁵',
    'option-sezimal-prefix-tcm': 'TC – tricharma – 10³⁴',
    'option-sezimal-prefix-ttm': 'TT – tritrima  – 10³³',
    'option-sezimal-prefix-tdm': 'TD – tridima – 10³²',
    'option-sezimal-prefix-tem': 'TE – triecama  – 10³¹',
    'option-sezimal-prefix-txm': 'TX – trixama  – 10³⁰',
    'option-sezimal-prefix-dpm': 'DP – dipama – 10²⁵',
    'option-sezimal-prefix-dcm': 'DC – dicharma  – 10²⁴',
    'option-sezimal-prefix-dtm': 'DT – ditrima – 10²³',
    'option-sezimal-prefix-ddm': 'DD – didima – 10²²',
    'option-sezimal-prefix-dem': 'DE – diecama – 10²¹',
    'option-sezimal-prefix-dxm': 'DX – dixama – 10²⁰',
    'option-sezimal-prefix-xpm': 'XP – xapama – 10¹⁵',
    'option-sezimal-prefix-xcm': 'XC – xacharma – 10¹⁴',
    'option-sezimal-prefix-xtm': 'XT – xatrima  – 10¹³',
    'option-sezimal-prefix-xdm': 'XD – xadima – 10¹²',
    'option-sezimal-prefix-xem': 'XE – xaecama  – 10¹¹',
    'option-sezimal-prefix-xm': 'X – xama – 10¹⁰',
    'option-sezimal-prefix-pm': 'P – pama – 10⁵',
    'option-sezimal-prefix-cm': 'C – charma – 10⁴',
    'option-sezimal-prefix-tm': 'T – trima – 10³',
    'option-sezimal-prefix-dm': 'D – dima – 10²',
    'option-sezimal-prefix-em': 'E – ecama – 10¹',
    'option-sezimal-prefix-ei': 'e – ecati – 10⁻¹',
    'option-sezimal-prefix-di': 'd – diti – 10⁻²',
    'option-sezimal-prefix-ti': 't – triti – 10⁻³',
    'option-sezimal-prefix-ci': 'c – charti – 10⁻⁴',
    'option-sezimal-prefix-pi': 'p – panti – 10⁻⁵',
    'option-sezimal-prefix-xi': 'x – xati – 10⁻¹⁰',
    'option-sezimal-prefix-xei': 'xe – xaecati – 10⁻¹¹',
    'option-sezimal-prefix-xdi': 'xd – xaditi – 10⁻¹²',
    'option-sezimal-prefix-xti': 'xt – xatriti – 10⁻¹³',
    'option-sezimal-prefix-xci': 'xc – xacharti – 10⁻¹⁴',
    'option-sezimal-prefix-xpi': 'xp – xapanti – 10⁻¹⁵',
    'option-sezimal-prefix-dxi': 'dx – dixati – 10⁻²⁰',
    'option-sezimal-prefix-dei': 'de – diecati – 10⁻²¹',
    'option-sezimal-prefix-ddi': 'dd – diditi – 10⁻²²',
    'option-sezimal-prefix-dti': 'dt – ditriti – 10⁻²³',
    'option-sezimal-prefix-dci': 'dc – dicharti – 10⁻²⁴',
    'option-sezimal-prefix-dpi': 'dp – dipanti – 10⁻²⁵',
    'option-sezimal-prefix-txi': 'tx – trixati – 10⁻³⁰',
    'option-sezimal-prefix-tei': 'te – triecati – 10⁻³¹',
    'option-sezimal-prefix-tdi': 'td – triditi – 10⁻³²',
    'option-sezimal-prefix-tti': 'tt – tritriti – 10⁻³³',
    'option-sezimal-prefix-tci': 'tc – tricharti – 10⁻³⁴',
    'option-sezimal-prefix-tpi': 'tp – tripanti – 10⁻³⁵',
    'option-sezimal-prefix-cxi': 'cx – charxati – 10⁻⁴⁰',
    'option-sezimal-prefix-cei': 'ce – charecati – 10⁻⁴¹',
    'option-sezimal-prefix-cdi': 'cd – charditi – 10⁻⁴²',
    'option-sezimal-prefix-cti': 'ct – chartriti – 10⁻⁴³',
    'option-sezimal-prefix-cci': 'cc – charcharti – 10⁻⁴⁴',
    'option-sezimal-prefix-cpi': 'cp – charpanti – 10⁻⁴⁵',
    'option-sezimal-prefix-pxi': 'px – panxati – 10⁻⁵⁰',
    'option-sezimal-prefix-pei': 'pe – panecati – 10⁻⁵¹',
    'option-sezimal-prefix-pdi': 'pd – panditi – 10⁻⁵²',
    'option-sezimal-prefix-pti': 'pt – pantriti – 10⁻⁵³',
    'option-sezimal-prefix-pci': 'pc – pancharti – 10⁻⁵⁴',
    'option-sezimal-prefix-ppi': 'pp – panpanti – 10⁻⁵⁵',
    'option-sezimal-prefix-ni': 'n – niti – 10⁻¹⁰⁰',
    'option-sezimal-prefix-nei': 'ne – niecati – 10⁻¹⁰¹',
    'option-sezimal-prefix-ndi': 'nd – niditi – 10⁻¹⁰²',
    'option-sezimal-prefix-nti': 'nt – nitriti – 10⁻¹⁰³',
    'option-sezimal-prefix-nci': 'nc – nicharti – 10⁻¹⁰⁴',
    'option-sezimal-prefix-npi': 'np – nipanti – 10⁻¹⁰⁵',
    'option-sezimal-prefix-nxi': 'nx – nixati – 10⁻¹¹⁰',
    'option-sezimal-prefix-nxei': 'nxe – nixaecati – 10⁻¹¹¹',
    'option-sezimal-prefix-nxdi': 'nxd – nixaditi – 10⁻¹¹²',
    'option-sezimal-prefix-nxti': 'nxt – nixatriti – 10⁻¹¹³',
    'option-sezimal-prefix-nxci': 'nxc – nixacharti – 10⁻¹¹⁴',
    'option-sezimal-prefix-nxpi': 'nxp – nixapanti – 10⁻¹¹⁵',
    'option-sezimal-prefix-ndxi': 'ndx – nidixati – 10⁻¹²⁰',

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
    'optgroup-units-generic-binary': 'Binários',
    'option-binary-prefix-yobi': 'Yi – yobi – 2⁸⁰',
    'option-binary-prefix-zebi': 'Zi – zebi – 2⁷⁰',
    'option-binary-prefix-exbi': 'Ei – exbi – 2⁶⁰',
    'option-binary-prefix-pebi': 'Ei – pebi – 2⁵⁰',
    'option-binary-prefix-tebi': 'Ti – tebi – 2⁴⁰',
    'option-binary-prefix-gibi': 'Gi – gibi – 2³⁰',
    'option-binary-prefix-mebi': 'Mi – mebi – 2²⁰',
    'option-binary-prefix-kibi': 'Ki – kibi – 2¹⁰',

    'unit-ang-explanation': `
<br/>
<p>O tempo civil é dividido em seis unidades; um dia é dividido de forma regular em sextos, e esses sextos são agrupados em subunidades, da seguinte maneira:</p>
<ul>
    <li>o dina, símbolo din, correspondente ao dia mesmo;</li>
    <li>o uta, símbolo uta, correspondente às duas primeiras divisões/sextos, com valor mais próximo da hora;</li>
    <li>o poxa (pôxa, não póxa), símbolo pox, correspondente às duas próximas divisões/sextos, com valor mais próximo do minuto;</li>
    <li>o agrima, símbolo agm, correspondente às duas divisões/sextos seguintes, com valor mais próximo do segundo;</li>
    <li>o anuga, símbolo ang, correspondente às próximas duas divisões/sextos, com valor mais próximo do centésimo de segundo (centissegundo);</li>
    <li>o boda (bôda, não bóda), símbolo bod, correspondente às duas últimas divisões/sextos, com valor mais próximo do milésimo de segundo (milissegundo);</li>
</ul>
<p>Então, um dia é divido:</p>
<p style="text-align: center;"><span style="color: #9E9E9E;">5.</span><span style="font-weight: bold;">55:55:55</span><span style="color: #9E9E9E;">:55:55</span></p>
<p style="text-align: center;" class="mono-text"><span style="color: #9E9E9E;">   5 .  </span><span style="font-weight: bold;">55 :   55 :     55</span><span style="color: #9E9E9E;"> :    55 :   55</span></p>
<p style="text-align: center;" class="mono-text"><span style="color: #9E9E9E;">dina . </span><span style="font-weight: bold;">uta : poxa : agrima</span><span style="color: #9E9E9E;"> : anuga : boda</span></p>
<p>Para uso científico, a unidade base de tempo é o anuga, por isso, todas as outras unidades que derivam da dimensão tempo, em alguma forma, usam o anuga nas suas definições.</p>
<p>Os prefixos podem ser usados com qualquer uma das unidades de tempo, e a conversão entre as unidades e os prefixos é a seguinte:</p>
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
        <td style="text-align: right;">0,01 din</br>1 ddin</td>
        <td style="text-align: right;">1 uta</td>
        <td style="text-align: right;">100 pox</br>1 Dpox</td>
        <td style="text-align: right;">10⁴ agm</br>1 Cagm</td>
        <td style="text-align: right;"><b>10¹⁰ ang</br>1 Xang</b></td>
        <td style="text-align: right;">10¹² bod</br>1 XDbod</td>
    </tr>
    <tr>
        <td style="text-align: center;">pox</td>
        <td style="text-align: right;">10⁻⁴ din</br>1 cdin</td>
        <td style="text-align: right;">0,01 uta</br>1 duta</td>
        <td style="text-align: right;">1 pox</td>
        <td style="text-align: right;">100 agm</br>1 Dagm</td>
        <td style="text-align: right;"><b>10⁴ ang</br>1 Cang</b></td>
        <td style="text-align: right;">10¹⁰ bod</br>1 Xbod</td>
    </tr>
    <tr>
        <td style="text-align: center;">agm</td>
        <td style="text-align: right;">10⁻¹⁰ din</br>1 xdin</td>
        <td style="text-align: right;">10⁻⁴ uta</br>1 cuta</td>
        <td style="text-align: right;">0,01 pox</br>1 dpox</td>
        <td style="text-align: right;">1 agm</td>
        <td style="text-align: right;"><b>100 ang</br>1 Dang</b></td>
        <td style="text-align: right;">10⁴ bod</br>1 Cbod</td>
    </tr>
    <tr>
        <td style="text-align: center;"><b>ang</b></td>
        <td style="text-align: right;"><b>10⁻¹² din</br>1 xddin</b></td>
        <td style="text-align: right;"><b>10⁻¹⁰ uta</br>1 xuta</b></td>
        <td style="text-align: right;"><b>10⁻⁴ pox</br>1 cpox</b></td>
        <td style="text-align: right;"><b>0,01 agm</br>1 dagm</b></td>
        <td style="text-align: right;"><b>1 ang</b></td>
        <td style="text-align: right;"><b>100 bod</br>1 Dbod</b></td>
    </tr>
    <tr>
        <td style="text-align: center;">bod</td>
        <td style="text-align: right;">10⁻¹⁴ din</br>1 xcdin</td>
        <td style="text-align: right;">10⁻¹² uta</br>1 xduta</td>
        <td style="text-align: right;">10⁻¹⁰ pox</br>1 xpox</td>
        <td style="text-align: right;">10⁻⁴ agm</br>1 cagm</td>
        <td style="text-align: right;"><b>0,01 ang</br>1 dang</b></td>
        <td style="text-align: right;">1 bod</td>
    </tr>
</table>
<p></p>
<p>A Luz disse: eu não sei nada sobre o teu tempo, e ainda assim, eu ergo o teu dia da escuridão, alimento tudo o que vive, dirijo teus pensamentos ao infinito; segue-me ainda que ao teu passo, e eu vou-te permitir ver tudo, e medir tudo o que há.</p>
<p></p>
<p>O nome de cada uma das unidades vem das seguintes palavras em sânscrito::</p>
<ul>
    <li><span class="devanagari-word">दिन</span> ‹dina› /'d̪i.nə/: Dia, cognato do latim <i>diēs</i>;</li>
    <li><span class="devanagari-word">उत्थानम्</span> ‹utthānam› /ut̪'t̪ʰɑː.nəm/: que ergue, que dá origem (falando da luz, sobre o dia, acréscimo nosso);</li>
    <li><span class="devanagari-word">पोषण</span> ‹poṣaṇa› /'poː.ʂə.ɳə/: que nutre, que cuida (falando da luz, sobre o dia);</li>
    <li><span class="devanagari-word">अग्रिम</span> ‹agrima› /ə'gri.mə/: o que conduz, que vem antes (idem);</li>
    <li><span class="devanagari-word">अनुगामी</span> ‹anugāmī› /ə.nu'gɑː.miː/: o que segue;</li>
    <li><span class="devanagari-word">बोध</span> ‹bodha› /'boː.d̪ʰə/: entendimento, conhecimento;</li>
</ul>
<p></p>
<p>Para fins científicos, a unidade de tempo da base sezimal é o anuga, portanto todas as outras unidades que derivam do tempo de alguma maneira, usam o anuga nas suas definições.</p>
<p>A definição formal do anuga é similar em forma à definição do segundo no Sistema Internacional, estabelecendo que:</p>
<p></p>
<p>   a transição óptica não‐perturbada 6s ²S<sub>1⁄2</sub> (<i>F</i> = 0) – 5d ²D<sub>3⁄2</sub> (<i>F</i> = 2) do íon ⁴⁴³Yb⁺ tem uma frequência de <i>f</i><sub>⁴⁴³Yb⁺</sub> = 203 150󱹬505 354󱹬503 234󱹮530 12 avt<sup><a href="#reference_1">1</a></sup>, quando expressa na unidade de frequência avrita (avt), que é igual a ang⁻¹ (em decimal, ¹⁷¹Yb⁺ e 688.358.979.309.308,24 Hz<sup><a href="#reference_2">2</a></sup>).</p>
<p></p>
<p>Por fim, a conversão entre anugas e segundos; pegamos o dia médio de duração de 1󱹬504 000 segundos (decimal 86.400), e divimos o tempo em segundos pela duração média de um dia de 100󱹬000 000 (decimal 1.679.616) anugas:
</p>
<p>Portanto, 1 ang = <math><mfrac><mn>1󱹬504 000</mn><mn>100󱹬000 000</mn></mfrac></math> = <math><mfrac><mn>41</mn><mn>2 130</mn></mfrac></math> = 0󱹮015 04 s (decimal <math><mfrac><mn>25</mn><mn>486</mn></mfrac></math> = 0,0„514 403 292 181 069 958 847 736 625);</p>
<p>A conversão inversa, 1 s = <math><mfrac><mn>100󱹬000 000</mn><mn>1󱹬504 000</mn></mfrac></math> = <math><mfrac><mn>2 130</mn><mn>41</mn></mfrac></math> = 31󱹯235 01 ang (decimal <math><mfrac><mn>486</mn><mn>25</mn></mfrac></math> = 19,44);</p>
<p></p>
<p>Referências:</p>
<p id="reference_1"><sup>1</sup> <a href="https://www.bipm.org/documents/20126/17315032/CIPM2006-EN.pdf/e58fcb97-69f8-008b-050b-378d5f0d8a77">Recomendações adotadas pelo Comitê Internacional para Pesos e Medidas em sua 95ª reunião (outubro de 2006), páginas 123–124 da versão francesa, páginas 249–250 (no PDF, 115–116) da versão inglesa.</a>
</p>
<p id="reference_2"><sup>2</sup> <a href="https://www.bipm.org/documents/20126/69375151/171Yb+_688THz_2021.pdf/6ffc6ec4-76a5-d043-ba4c-af680662fc29">Valores recomendados das frequências padrão para aplicações incluindo a realização prática do metro e representações secundárias da definição do segundo, íon de itérbio 171</a>
</p>
`,
    // 'optgroup-units-ang-common': 'Comum/civil',
    'option-units-ang-dina': 'dina – din = dia',
    'option-units-ang-uta': 'uta – uta ~ hora',
    'option-units-ang-posha': 'poxa – pox ~ minuto',
    'option-units-ang-agrima': 'agrima – agm ~ segundo',
    'option-units-ang-anuga': 'anuga – ang ~ cent. seg.',
    'option-units-ang-boda': 'boda – bod ~ mil. seg.',

    'option-decimal-units-ang-day': 'dia',
    'option-decimal-units-ang-hour': 'hora – h',
    'option-decimal-units-ang-minute': 'minuto – min',
    'option-decimal-units-ang-second': 'segundo – s',

    'translation-day': 'dia',
    'translation-hour': 'h',
    'translation-minute': 'min',
    'translation-second': 's',

    'unit-avt-explanation': `
<br/>
<p>Frequência é registrada usando a unidade avrita, símbolo avt, que representa eventos, ciclos, ocorrências etc. por anuga (a unidade base de tempo).</p>
<p>Uma propriedade interessante de todas as unidades que envolvem tempo em sezimal é que é bastante simples a conversão das várias unidades de tempo comum/civil e o anuga:</p>
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
        <td style="text-align: center;">Davt</br>por boda</td>
        <td style="text-align: center;">avt</br>por anuga</td>
        <td style="text-align: center;">davt</br>por agrima</td>
        <td style="text-align: center;">cavt</br>por poxa</td>
        <td style="text-align: center;">xavt</br>por uta</td>
        <td style="text-align: center;">xdavt</br>por dina/dia</td>
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
        <td style="text-align: right;">0,01 Davt</br>1/100 bod</td>
        <td style="text-align: right;">1 avt</br>1/ang</td>
        <td style="text-align: right;">100 davt</br>100/agm</td>
        <td style="text-align: right;">10⁴ cavt</br>10⁴/pox</td>
        <td style="text-align: right;">10¹⁰ xavt</br>10¹⁰/uta</td>
        <td style="text-align: right;">10¹² xdavt</br>10¹²/din</td>
    </tr>
    <tr>
        <td style="text-align: center;">davt</td>
        <td style="text-align: right;">10⁻⁴ Davt</br>1/10⁴ bod</td>
        <td style="text-align: right;">0,01 avt</br>1/100 ang</td>
        <td style="text-align: right;">1 davt</br>1/agm</td>
        <td style="text-align: right;">100 cavt</br>100/pox</td>
        <td style="text-align: right;">10⁴ xavt</br>10⁴/uta</td>
        <td style="text-align: right;">10¹⁰ xdavt</br>10¹⁰/din</td>
    </tr>
    <tr>
        <td style="text-align: center;">cavt</td>
        <td style="text-align: right;">10⁻¹⁰ Davt</br>1/10¹⁰ bod</td>
        <td style="text-align: right;">10⁻⁴ avt</br>1/10⁴ ang</td>
        <td style="text-align: right;">0,01 davt</br>1/100 agm</td>
        <td style="text-align: right;">1 cavt<br/>1/pox</td>
        <td style="text-align: right;">100 xavt</br>100/uta</td>
        <td style="text-align: right;">10⁴ xdavt</br>1/10⁴ din</td>
    </tr>
    <tr>
        <td style="text-align: center;">xavt</td>
        <td style="text-align: right;">10⁻¹² Davt</br>1/10¹² bod</td>
        <td style="text-align: right;">10⁻¹⁰ avt</br>1/10¹⁰ ang</td>
        <td style="text-align: right;">10⁻⁴ davt</br>1/10⁴ agm</td>
        <td style="text-align: right;">0,01 cavt</br>1/100 pox</td>
        <td style="text-align: right;">1 xavt<br/>1/uta</td>
        <td style="text-align: right;">100 dxavt</br>100/din</td>
    </tr>
    <tr>
        <td style="text-align: center;">xdavt</td>
        <td style="text-align: right;">10⁻¹⁴ Davt</br>1/10¹⁴ bod</td>
        <td style="text-align: right;">10⁻¹² avt</br>1/10¹² ang</td>
        <td style="text-align: right;">10⁻¹⁰ davt</br>1/10¹⁰ agm</td>
        <td style="text-align: right;">10⁻⁴ cavt</br>1/10⁴ pox</td>
        <td style="text-align: right;">0,01 xavt</br>1/100 uta</b></td>
        <td style="text-align: right;">1 xdavt<br/>1/din</td>
    </tr>
</table>
<br/>
`,

    'option-units-avt-avrita': 'avrita – avt',
    'option-decimal-units-avt-hertz': 'Hertz – Hz',
    'option-decimal-units-avt-rpm': 'rpm',

    'unit-pad-explanation': `
<p>O pada, símbolo pad, é a unidade de medida de comprimento na base sezimal;</p>

<p>A definição formal do pada é a distância percorrida pela luz numa fração de <math><mfrac><mn>1</mn><mn>135 005󱹬235 440</mn></mfrac></math> de anuga (<math><mfrac><mn>41</mn><mn>2 130</mn></mfrac></math> s, veja a definição formal do anuga na página das unidades de tempo).</p>
<p>A conversão de e para metros é feita pegando a velocidade da luz, pelo S.I., de 45 425󱹬332 014 (decimal 299,792,458) m/s, e dividindo esse valor pela equivalente velocidade da luz em Xastadári, que é de 135 005󱹬235 440 (decimal 594,838,032) pad/ang (veja a página sobre unidades de velocidade), e daí multiplicando esse valor pela conversão de anugas em segundos (veja a página sobre as unidades de tempo):</p>
<p class="center">1 pad = <math><mfrac><mn>45 425󱹬332 014</mn><mn>135 005󱹬235 440</mn></mfrac></math> × <math><mfrac><mn>41</mn><mn>2 130</mn></mfrac></math> = <math><mfrac><mn>1󱹬415 503󱹬524 325</mn><mn>150󱹬223 042󱹬430 000</mn></mfrac></math><br/>= 0󱹮005 333󱹬324 241󱹬020 132 m
<br/>(decimal <math><mfrac><mn>3.747.405.725</mn><mn>144.545.641.776</mn></mfrac></math> = 0,025 925 414 830 613 m)</p>
<p></p>

<p>Uma outra forma de se chegar à mesma conversão é tomar a aceleração <b>média</b> da gravidade do planeta Terra<sup><a href="#reference_1">1</a></sup> (a aceleração da gravidade não é nem constante, nem 13󱹮450 123 (decimal 9,806 65) m/s² em toda a superfície do planeta), calculada em 13󱹮444 135󱹬140 131󱹬050 515 (decimal 9,797 566 850 130 385) m/s², e multiplicar esse valor pela conversão do anuga para o segundo, ao quadrado:</p>
<p>Tomando a aceleração da gravidade em forma fracionária:</p>
<p class="center">1 g<sub>méd</sub> = <math><mfrac><mn>5󱹬324 444󱹬301 513</mn><mn>322 545󱹬201 312</mn></mfrac></math> = 13󱹮444 135󱹬140 131󱹬050 515 m/s²</p>
<p class="center">(decimal <math><mfrac><mn>12.141.594.549</mn><mn>1.239.245.900</mn></mfrac></math> = 9,797 566 850 130 385 m/s²)</p>
<p class="center"><math><mfrac><mn>5󱹬324 444󱹬301 513</mn><mn>322 545󱹬201 312</mn></mfrac></math> × <math><msup><mrow><mo>(</mo><mfrac><mn>41</mn><mn>2 130</mn></mfrac><mo>)</mo></mrow><mn>2</mn></msup></math> = <math><mfrac><mn>1󱹬415 503󱹬524 325</mn><mn>150󱹬223 042󱹬430 000</mn></mfrac></math><br/>= 0󱹮005 333󱹬324 241󱹬020 132 m
<br/>(decimal <math><mfrac><mn>3.747.405.725</mn><mn>144.545.641.776</mn></mfrac></math> = 0,025 925 414 830 613 m)</p>
<p>Isso significa que o pada é também a distância que, na Terra, em média, um objeto percorre numa queda livre de duração de um anuga, devido a aceleração da gravidade, que é de 1 pad/ang² (veja mais na página das unidades de aceleração).</p>
<p></p>
<p>Referências:</p>
<p id="reference_1"><sup>1</sup> <a href="https://primelmetrology.atlassian.net/wiki/x/pAB9">Metrologia Primel - Segunda Realidade Mundana: Aceleração devido à Gravidade da Terra</a>
</p>
<p></p>
`,
    'option-units-pad-pada': 'pada – pad',
    'option-decimal-units-pad-meter': 'metro – m',
    'option-decimal-units-pad-mile': 'milha – ml',
    'option-decimal-units-pad-yard': 'jarda – yd',
    'option-decimal-units-pad-foot': 'pé – ft',
    'option-decimal-units-pad-inch': 'polegada – in',

    'option-units-ktr-ketra': 'quetra – ktr',
    'option-units-ktr-sq-pada': 'pada quad. – pad²',
    'option-decimal-units-ktr-sq-meter': 'metro quad. – m²',
    'option-decimal-units-ktr-are': 'are - a',
    'option-decimal-units-ktr-acre': 'acre - ac',
    'option-decimal-units-ktr-sq-mile': 'milha quad. – ml²',
    'option-decimal-units-ktr-sq-yard': 'jarda quad. – yd²',
    'option-decimal-units-ktr-sq-foot': 'pé quad. – ft²',
    'option-decimal-units-ktr-sq-inch': 'polegada quad. – in²',

    'option-units-ayt-aytan': 'aitã – ayt',

    'option-decimal-units-prd-prd': 'parídis',
    'option-decimal-units-prd-tau_rad': 'τ radianos',
    'option-decimal-units-prd-pi_rad': 'π radianos',
    'option-decimal-units-prd-rad': 'radianos',
    'option-decimal-units-prd-deg': 'graus',
    'option-decimal-units-prd-arcmin': 'minutos',
    'option-decimal-units-prd-arcsec': 'segundos',
    'option-decimal-units-prd-turn': 'voltas',
    'option-decimal-units-prd-gon': 'gradianos (gon)',
};

export { sezimal_calculator_pt_text };
