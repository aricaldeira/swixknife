
const sezimal_calculator_pt_text = {
    'title': 'Calculadora Sezimal',
    'button-sezimal-clear': 'Z',
    'button-decimal-clear': 'Z',
    // 'button-base-ten': 'dec',
    // 'button-base-six': 'sez',
    'translation-txt': 'ext',
    'translation-nif': 'nife',

    'translation-sezimal-calculator': 'Calculadora Sezimal',
    'label-sezimal-locale': 'Defina o locale para a formatação dos números',
    'label-sezimal-places': 'Defina a quantidade de casas sezimais',
    'label-sezimal-angle': 'Defina a conversão de unidades de ângulo<br/>para as funções trigonométricas',
    'translation-sezimal-units': 'Unidades de Medida Xastadári',
    'label-sezimal-units': 'Escolha qual unidade você deseja converter<br/>de ou para as unidades Xastadári,<br/>e veja as explicações e orientações<br/>sobre cada unidade',

    'translation-display-mod': 'mód',
    'translation-display-turn': 'volta',
    // 'translation-display-deg': '°',
    // 'translation-display-arcmin': '′',
    // 'translation-display-arcsec': '″',
    // 'translation-display-gon': 'gon',
    // 'translation-display-rad': 'rad',
    // 'translation-display-tau_rad': 'τ rad',
    // 'translation-display-pi_rad': 'π rad',
    'translation-display-deg2': 'grau²',

    'button-sezimal-sin': 'sen',
    // 'button-sezimal-cos': 'cos',
    // 'button-sezimal-tan': 'tan',
    'button-decimal-sin': 'sen',
    // 'button-decimal-cos': 'cos',
    // 'button-decimal-tan': 'tan',

    'translation-display-sin': 'sen',
    'translation-display-asin': 'asen',
    // 'translation-display-csc': 'csc',
    // 'translation-display-acsc': 'acsc',
    // 'translation-display-cos': 'cos',
    // 'translation-display-acos': 'acos',
    // 'translation-display-sec': 'sec',
    // 'translation-display-asec': 'asec',
    // 'translation-display-tan': 'tan',
    // 'translation-display-atan': 'atan',
    // 'translation-display-cot': 'cot',
    // 'translation-display-acot': 'acot',

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
    <li>[ mdl ◕ ° ] - unidades de medida de ângulos para as funções trigonométricas sezimais e decimais;</li><br/>
    <li>[ ⬢ ] - unidades e prefixos Xastadári convertidos de ou para unidades e prefixo do Sistema Internacional de Medidas (e algumas unidades tradicionais fora do SI);</li><br/>
    <li>[ 0󱹮3 ] - em quantos dígitos depois do separador sezimais o resultado vai ser arredondado; a precisão em base decimal vai ser ajustada baseada na precisão da base sezimal;</li><br/>
</ul>
<h2>Notação usada</h2>
<ul>
    <li>Nomes dos números - 0 zero; 1 um; 2 dois; 3 três; 4 quatro; 5 cinco; 10 seis; 11 sete; 12 oito; 13 nove; 14 dez; 15 onze; 20 doze; 21 doze e um; 22 doze e dois; 23 doze e três; 24 doze e quatro; 25 doze e cinco; 30 tresseis; 40 quasseis; 50 quinseis; 100 nife (da língua ndom <i>nif</i> para trinta e seis); 1󱹭000 arda (do sânscrito अर्ध <i>ardha</i> para meio, metade, para metade de seis dígitos); 10󱹭000 seis arda; 100󱹭000 nife arda; 1󱹬000󱹭000 xadara (do sânscrito षडार <i>ṣaḍāra</i> para um grupo de seis, ou um hexágono); de xadara se segue 10󱹬000󱹭000 seis xadara, 100󱹬000󱹭000 nife xadara, 1󱹭000󱹬000󱹭000 arda xadara (em escala longa, como em português europeu), 10󱹭000󱹬000󱹭000 seis arda xadara, 100󱹭000󱹬000󱹭000 nife arda xadara, dixadara 1󱹬000󱹭000󱹬000󱹭000 (<i>di</i> do sânscrito द्वि <i>dvi</i> para dois); trixadara para 10³⁰ (<i>tri</i> do sânscrito त्रि <i>tri</i> para três); tcharxadara para 10⁴⁰ (<i>tchar</i> do sânscrito चतुर् <i>catur</i> para quatro); panxadara para 10⁵⁰ (<i>pan</i> do sânscrito पञ्चन् <i>pañcan</i>, cinco); xaxadara para 10¹⁰⁰ (<i>xa</i> do sânscrito षष् <i>ṣaṣ</i> para seis); use a função de números por extenso para saber como ler qualquer número sezimal</li><br/>
    <li>Separador sezimal 󱹮 - uma barra em forma de agulha, apontando para cima, que se inicia sobre a linha base da escrita, pelo meio da altura X da fonte, e se extende para baixo até o ponto mais baixo dos descendentes da fonte; seu código Unicode é U+F1E6E; compare o separador sezimal com a vírgula e o ponto: ,󱹮.</li><br/>
    <li>Separador periódico 󱹯 „ ‥  - dobrando o separador fracionário (sezimal ou decimal) resulta no separador periódico; por exemplo, a fração sezimal 1⁄5 pode ser escrita 0󱹯1 (0󱹮1̅) = 0󱹮111...; 1⁄11 0󱹯05 = 0󱹮0̅5̅ = 0󱹮050󱹭505...; a fração decimal 1⁄3 0„3 (0,3̅) = 0,333...; decimal 1⁄12 0,08„3 (0,083̅) = 0.083 333...; esse último exemplo, se o separador periódico, é ambíguo: é só o 3 que se repete, ou 08333? Para o separador periódico num único caracter(como neste aplicativo), os códigos Unicode são 󱹯 U+F1E6F, „ U+201E e ‥ U+2025; o separador periódico sezimal se parece com um sinal de idem ".</li><br/>
    <li>Separador de arda ⍽ - o espaço inseparável estreito, código Unicode U+202F, é usado para marcar o primeiro grupo de três dígitos<!--, contando a partir do dígito mais à direita-->, à esquerda e à direita do separador sezimal, e, a partir daí, a cada grupo de seis dígitos, na prática se alternando com o separador de xadara;</li><br/>
    <li>Separador de xadara 󱹬 - tem a mesma forma básica do separador sezimal, com um sexto do tamanho, apontando para baixo, se extendendo para baixo a partir do ponto mais alto da fonte usada, e marca a posição dos xadaras a cada grupo de seis dígitos nos números sezimais, tanto à esquerda quanto à direita do separador sezimal, contando sempre a partir do dígito mais à direita; seu código Unicode é U+F1E6C; compare o separador de xadara com o apóstrofe reto/aspas simples reta e com a letra modificadora linha vertical 'ˈ󱹬;</li><br/>
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

    'optgroup-units-base': '13 unidades fundamentais',
    'option-units-ang': 'Tempo – ang',
    'option-units-pad': 'Comprimento – pad',
    'option-units-drv': 'Massa – drv',
    'option-units-gtk': 'Temperatura absoluta – gtk',
    'option-units-dar': 'Corrente elétrica – dar',
    'option-units-mdl': 'Ângulo plano – mdl',
    'option-units-gol': 'Ângulo sólido – gol',
    'option-units-pkx': 'Intensidade luminosa – pkx',
    'option-units-bht': 'Quantidade de substância – bht',

    'optgroup-units-derived': 'Unidades derivadas',
    'option-units-avt': 'Frequência – avt',
    'option-units-ktr': 'Área – ktr',
    'option-units-ayt': 'Volume – ayt',
    'option-units-veg': 'Velocidade – veg',
    'option-units-tvr': 'Aceleração – tvr',
    'option-units-gnt': 'Densidade – gnt',
    'option-units-bar': 'Força/peso – bar',
    'option-units-pdn': 'Pressão – pdn',
    'option-units-vrc': 'Energia/trabalho – vrc',
    'option-units-xkt': 'Potência – xkt',
    'option-units-svg': 'Momento linear – svg',
    'option-units-agh': 'Ação – agh',
    // 'option-units-pbv': 'Influência',
    // 'option-units-tnv': 'Tensão',
    // 'option-units-upr': 'Intensidade',
    // 'option-units-nad': 'Viscosidade dinâmica',
    // 'option-units-bum': 'Viscosidade cinética',

    'option-units-tap': 'Temperatura comum – tap',
    'option-units-agn': 'Capacidade térmica ‐ agn',
    'option-units-idn': 'Calor específico – idn',
    // 'option-units-tln': 'Capacidade térmica por volume',

    'option-units-vdt': 'Carga elétrica – vdt',
    'option-units-atr': 'Diferença de potencial el. – atr',
    'option-units-vrd': 'Resistência el. – vrd',
    'option-units-vht': 'Condutância el. – vht',
    // 'option-units-upp': 'Indutância el. – upp',
    'option-units-dry': 'Capacitância el. – dry',
    'option-units-pvh': 'Fluxo magnético – pvh',
    'option-units-vtr': 'Dens. do fluxo magético – vtr',
    'option-units-dpk': 'Fluxo luminoso – dpk',
    'option-units-dxt': 'Rendimento luminoso – dxt',
    'option-units-dul': 'Massa atômica – dul',

    'optgroup-units-others': 'Outras unidades',
    'option-units-spn': 'Proporção – spn',
    'option-units-atk': 'Armazenagem de dados – atk',
    'option-units-pvn': 'Vel. de transm. de dados – pvn',

    'label-prefix-sezimal': 'Prefixo sezimal',
    'label-prefix-sezimal-angle': 'Prefixo sezimal',
    'label-unit-sezimal': 'Unidade sezimal',
    'label-prefix-decimal': 'Prefixo decimal',
    'label-prefix-decimal-angle': 'Prefixo decimal',
    'label-prefix-decimal-binary': 'Prefixo decimal/binário',
    'label-unit-decimal': 'Unidade decimal',
    'optgroup-units-generic-shastadari': 'Xastadári',
    'optgroup-units-generic-s-i': 'S.I.',
    'optgroup-units-generic-others': 'Outras',
    'optgroup-units-generic-imp-us': 'Reino Unido (imperial)/EUA',
    'optgroup-units-generic-us': 'EUA',
    'optgroup-units-generic-imp': 'Reino Unido (imperial)',
    'optgroup-units-generic-us-fluid': 'EUA - volume líq.',
    'optgroup-units-generic-us-dry': 'EUA - volume seco',
    'optgroup-units-generic-imp-fluid': 'Reino Unido (imperial)',

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

    'optgroup-units-ang-common': 'Comum/civil',
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

    'option-units-pad-pada': 'pada – pad',
    'option-decimal-units-pad-metre': 'metro – m',
    'option-decimal-units-pad-mile': 'milha – ml',
    'option-decimal-units-pad-yard': 'jarda – yd',
    'option-decimal-units-pad-foot': 'pé – ft',
    'option-decimal-units-pad-inch': 'polegada – in',

    'option-units-drv-dravya': 'drávia ‐ drv',
    'option-decimal-units-drv-ton': 'tonelada ‐ ton',
    'option-decimal-units-drv-gram': 'grama ‐ g',
    'option-decimal-units-drv-dalton': 'dalton ‐ Da',
    'option-decimal-units-drv-gr': 'grão ‐ gr',
    'option-decimal-units-drv-dwt': 'pennyweight ‐ dwt',
    'option-decimal-units-drv-ozt': 'onça troy ‐ ozt',
    'option-decimal-units-drv-lbt': 'libra troy ‐ lbt',
    'option-decimal-units-drv-dr': 'dracma ‐ dr',
    'option-decimal-units-drv-oz': 'onça ‐ oz',
    'option-decimal-units-drv-lb': 'libra ‐ lb',
    'option-decimal-units-drv-st': 'stone ‐ st',
    'option-decimal-units-drv-sl': 'slug ‐ sl',
    'option-decimal-units-drv-US-qr': 'quarto curto ‐ US qr',
    'option-decimal-units-drv-US-cwt': 'hundredweight curto ‐ US cwt',
    'option-decimal-units-drv-US-ton': 'tonelada curta ‐ US ton',
    'option-decimal-units-drv-imp-qr': 'quarto longo ‐ imp. qr',
    'option-decimal-units-drv-imp-cwt': 'hundredweight longo ‐ imp. cwt',
    'option-decimal-units-drv-imp-ton': 'tonelada longa ‐ imp. ton',

    'option-units-gtk-gatika': 'gatica ‐ gtk',
    'option-units-tap-tapa': 'tapa ‐ tap',
    'option-decimal-units-gtk-kelvin': 'kelvin ‐ K',
    'option-decimal-units-gtk-celsius': 'grau Celsius ‐ °C',
    'option-decimal-units-gtk-fahrenheit': 'grau Fahrenheit ‐ °F',
    'option-decimal-units-gtk-rankine': 'grau Rankine – °R',

    'option-sezimal-units-mdl-mandala': 'mandala ‐ mdl',
    'option-decimal-units-mdl-tau_rad': 'τ radianos',
    'option-decimal-units-mdl-pi_rad': 'π radianos',
    'option-decimal-units-mdl-rad': 'radiano',
    'option-decimal-units-mdl-deg': 'grau',
    'option-decimal-units-mdl-arcmin': 'minuto',
    'option-decimal-units-mdl-arcsec': 'segundo',
    'option-decimal-units-mdl-turn': 'volta',
    'option-decimal-units-mdl-gon': 'gradiano (gon)',

    'option-sezimal-units-gol-gola': 'gola ‐ gol',
    'option-decimal-units-gol-sterradian': 'esferorradiano ‐ sr',
    'option-decimal-units-gol-spat': 'espaço ‐ spat',
    'option-decimal-units-gol-deg2': 'graus ao quadrado – grau²',

    'option-units-pkx-prakasha': 'pracaxa ‐ pkx',
    'option-decimal-units-pkx-candela': 'candela ‐ cd',

    'option-units-bht-bahuta': 'barruta ‐ bht',
    'option-decimal-units-bht-mole': 'mol ‐ mol',

    'option-units-avt-avriti': 'avríti – avt',
    'option-decimal-units-avt-hertz': 'Hertz – Hz',
    'option-decimal-units-avt-rpm': 'rpm',

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
    'option-units-ayt-cb-pada': 'pada cúbico – pad³',
    'option-decimal-units-ayt-cb-metre': 'metro cúbico ‐ m³',
    'option-decimal-units-ayt-litre': 'litro ‐ L',
    'option-decimal-units-ayt-cb-mile': 'milha cúbica ‐ ml³',
    'option-decimal-units-ayt-cb-yard': 'jarda cúbica ‐ yd³',
    'option-decimal-units-ayt-cb-foot': 'pé cúbico ‐ ft³',
    'option-decimal-units-ayt-cb-inch': 'polegada cúbica ‐ in³',

    'translation-display-US-fl-dr': 'fl dr EUA',
    'translation-display-US-tsp': 'cc EUA',
    'translation-display-US-tbsp': 'cs EUA',
    'translation-display-US-fl-oz': 'fl oz EUA',
    'translation-display-US-cup': 'xíc EUA',
    'translation-display-US-pt': 'pt EUA',
    'translation-display-US-qt': 'qt EUA',
    'translation-display-US-gal': 'gal EUA',
    'translation-display-US-pt-dry': 'pt (seco)',
    'translation-display-US-qt-dry': 'qt (seco)',
    'translation-display-US-gal-dry': 'gal (seco)',
    'translation-display-US-pk-dry': 'pk (seco)',
    'translation-display-US-bu-dry': 'bu (seco)',

    'translation-display-imp-fl-dr': 'fl dr imp.',
    'translation-display-imp-fl-oz': 'fl oz imp.',
    'translation-display-imp-pt': 'pt imp.',
    'translation-display-imp-qt': 'qt imp.',
    'translation-display-imp-gal': 'gal imp.',

    'option-decimal-units-ayt-imp-fl-dr': 'dracma ‐ fl dr imp.',
    'option-decimal-units-ayt-imp-fl-oz': 'onça ‐ fl oz imp.',
    'option-decimal-units-ayt-imp-pt': 'pinta ‐ pt imp.',
    'option-decimal-units-ayt-imp-qt': 'quarto ‐ imp. qt',
    'option-decimal-units-ayt-imp-gal': 'galão ‐ gal imp.',

    'option-decimal-units-ayt-us-fl-dr': 'dracma ‐ fl dr EUA',
    'option-decimal-units-ayt-us-tsp': 'colher de chá ‐ cc EUA',
    'option-decimal-units-ayt-us-tbsp': 'colher de sopa ‐ cs EUA',
    'option-decimal-units-ayt-us-fl-oz': 'onça ‐ fl oz EUA',
    'option-decimal-units-ayt-us-cup': 'xícara ‐ xíc EUA',
    'option-decimal-units-ayt-us-pt': 'pinta ‐ pt EUA',
    'option-decimal-units-ayt-us-qt': 'quarto ‐ qt EUA',
    'option-decimal-units-ayt-us-gal': 'galão ‐ gal EUA',

    'option-decimal-units-ayt-us-pt-dry': 'pinta ‐ pt (seco) EUA',
    'option-decimal-units-ayt-us-qt-dry': 'quarto ‐ qt (seco) EUA',
    'option-decimal-units-ayt-us-gal-dry': 'galão ‐ gal (seco) EUA',
    'option-decimal-units-ayt-us-pk-dry': 'peque ‐ pk (seco) EUA',
    'option-decimal-units-ayt-us-bu-dry': 'buxel ‐ bu (seco) EUA',

    'option-units-veg-vega': 'vega – veg',
    'option-decimal-units-veg-mh': 'metros por hora ‐ m/h',
    'option-decimal-units-veg-ms': 'metros por segundo ‐ m/s',
    'option-decimal-units-veg-mph': 'milhas por hora ‐ mph',
    'option-decimal-units-veg-fps': 'pés por segundo ‐ fps',
    'option-decimal-units-veg-kn': 'nós ‐ kn',
    'option-decimal-units-veg-c': 'velocidade da luz ‐ c',

};

export { sezimal_calculator_pt_text };
