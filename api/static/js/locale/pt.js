
const sezimal_calculator_pt_text = {
    'title': 'Calculadora Sezimal',

    //
    // Unidades
    //
    'td-shastadari-units': 'Unidades de Medida Xastadári',
    'optgroup-units-instructions': 'Instruções',
    'option-units-units': 'Unidades Xastadári',
    'option-units-prefixes': 'Prefixos Xastadári',
    'optgroup-units-mechanics': 'Mecânica',
    'option-units-ang': 'Tempo',
    'option-units-avt': 'Frequência',
    'option-units-pad': 'Comprimento',
    'option-units-kex': 'Área',
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

    'label-unit-sezimal': 'Sezimal',
    'label-unit-decimal': 'Decimal',
    'optgroup-units-generic-s-i': 'S.I.',
    'optgroup-units-generic-non-s-i': 'Outras',
    'optgroup-units-generic-us-uk': 'EUA/Reino Unido',
    'optgroup-units-generic-us': 'EUA',
    'optgroup-units-generic-uk': 'Reino Unido',
    'optgroup-units-generic-us-fluid': 'EUA - volume líq.',
    'optgroup-units-generic-us-dry': 'EUA - volume seco',
    'optgroup-units-generic-uk-fluid': 'Reino Unido - líq.',

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
<p style="text-align: center;"><span style="color: #9E9E9E;">5.</span><span style="font-size: 12pt; font-weight: bold;">55:55:55</span><span style="color: #9E9E9E;">:55:55</span></p>
<p style="text-align: center;"><span style="color: #9E9E9E;">   5 .  </span><span style="font-size: 12pt; font-weight: bold;">55 :   55 :     55</span><span style="color: #9E9E9E;"> :    55 :   55</span></p>
<p style="text-align: center;"><span style="color: #9E9E9E;">dina . </span><span style="font-size: 12pt; font-weight: bold;">uta : poxa : agrima</span><span style="color: #9E9E9E;"> : anuga : boda</span></p>
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
`,
    'optgroup-units-ang-common': 'Comum/civil',
    'option-units-ang-dina': 'dina = dia',
    'option-units-ang-uta': 'uta ~ hora',
    'option-units-ang-posha': 'poxa ~ minuto',
    'option-units-ang-agrima': 'agrima ~ segundo',
    'option-units-ang-anuga': 'anuga ~ cent. seg.',
    'option-units-ang-boda': 'boda ~ mil. seg.',
    'optgroup-units-ang-dina': 'Dina/dia',
    'option-units-ang-din': 'din = dia',
    // 'option-units-ang-edin': 'edin',
    // 'option-units-ang-ddin': 'ddin = uta',
    // 'option-units-ang-tdin': 'tdin',
    'option-units-ang-cdin': 'cdin = poxa',
    // 'option-units-ang-pdin': 'pdin',
    // 'option-units-ang-xdin': 'xdin = agrima',
    // 'option-units-ang-xedin': 'xedin',
    // 'option-units-ang-xddin': 'xddin = anuga',
    // 'option-units-ang-xtdin': 'xtdin',
    // 'option-units-ang-xcdin': 'xcdin = boda',
    // 'optgroup-units-ang-anuga': 'Anuga',
    'option-units-ang-XDang': 'XDang = dina/dia',
    // 'option-units-ang-XEang': 'XEang',
    // 'option-units-ang-Xang': 'Xang = uta',
    // 'option-units-ang-Pang': 'Pang',
    'option-units-ang-Cang': 'Cang = poxa',
    // 'option-units-ang-Tang': 'Tang',
    // 'option-units-ang-Dang': 'Dang = agrima',
    // 'option-units-ang-Eang': 'Eang',
    // 'option-units-ang-ang': 'ang',
    // 'option-units-ang-eang': 'eang',
    // 'option-units-ang-dang': 'dang = boda',
    // 'option-units-ang-tang': 'tang',
    // 'option-units-ang-cang': 'cang',
    // 'option-units-ang-pang': 'pang',
    // 'option-units-ang-xang': 'xang',
    'optgroup-decimal-units-ang-common': 'Comum/civil',
    'option-decimal-units-ang-day': 'dia',
    'option-decimal-units-ang-hour': 'hora',
    'option-decimal-units-ang-minute': 'minuto',
    'option-decimal-units-ang-second': 'segundo',

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
};

export { sezimal_calculator_pt_text };
