
const sezimal_calculator_bz_text = {
    'title': 'Kawkuladora Sezimal',
    'button-sezimal-clear': 'Z',
    'button-decimal-clear': 'Z',
    'button-base-ten': 'des',
    // 'button-base-six': 'sez',

    //
    // Unidadis
    //
    'td-shastadari-units': 'Unidadis di Medida Xastadari',
    'optgroup-units-instructions': 'Instrusoyns',
    'option-units-units': 'Unidadis Xastadari',
    'option-units-prefixes': 'Prefiksus Xastadari',
    'optgroup-units-mechanics': 'Mekânika',
    'option-units-ang': 'Tenpu',
    'option-units-avt': 'Frekwensya',
    'option-units-pad': 'Konprimentu',
    'option-units-kex': 'Arya',
    'option-units-ayt': 'Volumi',
    'option-units-veg': 'Velosidadi',
    'option-units-tvr': 'Aselerasawn',
    'option-units-drv': 'Masa',
    'option-units-gan': 'Densidadi',
    'option-units-bar': 'Forsa/pezu',
    'option-units-dab': 'Presawn',
    'option-units-kry': 'Enerjia/trabalyu',
    'option-units-xat': 'Potensya',
    // 'option-units-svg': 'Momentu',
    // 'option-units-pkp': 'Asawn',
    // 'option-units-pbv': 'Influensya',
    // 'option-units-tnv': 'Tensawn',
    // 'option-units-upr': 'Intensidadi',
    // 'option-units-nad': 'Viskozidadi dinâmika',
    // 'option-units-bum': 'Viskozidadi sinétika',
    'optgroup-units-thermodynamics': 'Tèrmudinâmika',
    'option-units-tap': 'Tenperatura komun',
    'option-units-gtk': 'Tenperatura tèrmudinâmika',
    'option-units-agn': 'Kapasidadi térmika',
    'option-units-idn': 'Kapasidadi térmika pur masa',
    'option-units-tln': 'Kapasidadi térmika pur volumi',
    'optgroup-units-electromagnetism': 'Elètrumaginetismu',
    'option-units-avx': 'Karga el.',
    'option-units-dar': 'Korrenti el.',
    'option-units-vbv': 'Diferensa di potensiaw el.',
    'option-units-ptr': 'Rezistensya el.',
    'option-units-cln': 'Kondutansya el.',
    'option-units-prk': 'Indutansya el.',
    'option-units-smi': 'Kapasitansya el.',
    'option-units-abv': 'Fluksu mag.',
    'option-units-vtr': 'Densidadi du fluksu mag.',
    'optgroup-units-angle': 'Ângulu',
    'option-units-prd': 'Ângulu planu',
    'option-units-gol': 'Ângulu sólidu',
    'optgroup-units-proportion': 'Proporsawn',
    'option-units-prt': 'Proporsawn',
    'optgroup-units-data-information': 'Dadus/informasawn',
    'option-units-atk': 'Armazenajen',
    'option-units-pvn': 'Velosidadi',

    'label-unit-sezimal': 'Sezimaw',
    'label-unit-decimal': 'Desimaw',
    'optgroup-units-generic-s-i': 'S.I.',
    'optgroup-units-generic-non-s-i': 'Otras',
    'optgroup-units-generic-us-uk': 'EUA/Reynu Unidu',
    'optgroup-units-generic-us': 'EUA',
    'optgroup-units-generic-uk': 'Reynu Unidu',
    'optgroup-units-generic-us-fluid': 'EUA - volumi lík.',
    'optgroup-units-generic-us-dry': 'EUA - volumi seku',
    'optgroup-units-generic-uk-fluid': 'Reynu Unidu - lík.',

    'unit-ang-explanation': `
<br/>
<p>U tenpu siviw è divididu in sêys unidadis; un dia è divididu di fòrma regular in sestus, i esis sestus sawn agrupadus in subunidadis, da seginti maneyra:</p>
<ul>
    <li>u dina, sínbolu din, korrespondenti aw dia mesmu;</li>
    <li>u uta, sínbolu uta, korrespondenti as duas primeyras divizoyns/sestus, kun valor máys prósimu da òra;</li>
    <li>u poxa (pôxa, não póxa), sínbolu pox, korrespondenti as duas prósimas divizoyns/sestus, kun valor máys prósimu du minutu;</li>
    <li>u agrima, sínbolu agm, korrespondenti as duas divizoyns/sestus segintis, kun valor máys prósimu du segundu;</li>
    <li>u anuga, sínbolu ang, korrespondenti as prósimas duas divizoyns/sestus, kun valor máys prósimu du sentézimu di segundu (sentisegundu);</li>
    <li>u boda (bôda, nawn bòda), sínbolu bod, korrespondenti as duas úwtimas divizoyns/sestus, kun valor máys prósimu du milézimu di segundu (milisegundu);</li>
</ul>
<p>Intawn, un dia è dividu:</p>
<p style="text-align: center;"><span style="color: #9E9E9E;">5.</span><span style="font-size: 12pt; font-weight: bold;">55:55:55</span><span style="color: #9E9E9E;">:55:55</span></p>
<p style="text-align: center;"><span style="color: #9E9E9E;">   5 .  </span><span style="font-size: 12pt; font-weight: bold;">55 :   55 :     55</span><span style="color: #9E9E9E;"> :    55 :   55</span></p>
<p style="text-align: center;"><span style="color: #9E9E9E;">dina . </span><span style="font-size: 12pt; font-weight: bold;">uta : poxa : agrima</span><span style="color: #9E9E9E;"> : anuga : boda</span></p>
<p>Pra uzu sientífiku, a unidadi bazi di tenpu è u anuga, pur isu, todas as otras unidadis ki derivam da dimensawn tenpu, in awguma fòrma, uzam u anuga nas suas definisoyns.</p>
<p>Us prefiksus pòden ser uzadus kun kawkèr uma das unidadis di tenpu, i a konversawn entri as unidadis i us prefiksus è a seginti:</p>
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
    'optgroup-units-ang-common': 'Komun/siviw',
    'option-units-ang-dina': 'dina = dia',
    'option-units-ang-uta': 'uta ~ òra',
    'option-units-ang-posha': 'poxa ~ minutu',
    'option-units-ang-agrima': 'agrima ~ segundu',
    'option-units-ang-anuga': 'anuga ~ sent. seg.',
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
    'optgroup-decimal-units-ang-common': 'Komun/siviw',
    'option-decimal-units-ang-day': 'dia',
    'option-decimal-units-ang-hour': 'òra',
    'option-decimal-units-ang-minute': 'minutu',
    'option-decimal-units-ang-second': 'segundu',

    'unit-avt-explanation': `
<br/>
<p>Frekwensya è rejistrada uzandu a unidadi avrita, sínbolu avt, ki reprezenta eventus, siklus, okorrensyas etc. pur anuga (a unidadi bazi di tenpu).</p>
<p>Uma propriedadi interesanti di todas as unidadis ki envòwven tenpu in sezimaw è ki è bastanti sinplis a konversawn das varyas unidadis di tenpu komun/siviw i u anuga:</p>
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
        <td style="text-align: center;">Davt</td>
        <td style="text-align: center;">avt</td>
        <td style="text-align: center;">davt</td>
        <td style="text-align: center;">cavt</td>
        <td style="text-align: center;">xavt</td>
        <td style="text-align: center;">xdavt</td>
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

export { sezimal_calculator_bz_text };
