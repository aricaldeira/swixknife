
const sezimal_calculator_en_text = {
    'title': 'Sezimal Calculator',
    'button-sezimal-clear': 'C',
    'button-decimal-clear': 'C',
    'button-base-ten': 'dec',
    'button-base-six': 'sez',

    //
    // Units
    //
    'td-shastadari-units': 'Shastadari Units of Measure',
    'optgroup-units-instructions': 'Instructions',
    'option-units-units': 'Shastari units',
    'option-units-prefixes': 'Shastari prefixes',
    'optgroup-units-mechanics': 'Mechanics',
    'option-units-ang': 'Time',
    'option-units-avt': 'Frequency',
    'option-units-pad': 'Length',
    'option-units-kex': 'Area',
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

    'label-unit-sezimal': 'Sezimal',
    'label-unit-decimal': 'Decimal',
    'optgroup-units-generic-s-i': 'S.I.',
    'optgroup-units-generic-non-s-i': 'Non-S.I.',
    'optgroup-units-generic-us-uk': 'US/UK',
    'optgroup-units-generic-us': 'US',
    'optgroup-units-generic-uk': 'UK',
    'optgroup-units-generic-us-fluid': 'US fluid',
    'optgroup-units-generic-us-dry': 'US dry',
    'optgroup-units-generic-uk-fluid': 'UK fluid',

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
<p style="text-align: center;"><span style="color: #9E9E9E;">5.</span><span style="font-size: 12pt; font-weight: bold;">55:55:55</span><span style="color: #9E9E9E;">:55:55</span></p>
<p style="text-align: center;"><span style="color: #9E9E9E;">   5 .  </span><span style="font-size: 12pt; font-weight: bold;">55 :    55 :     55</span><span style="color: #9E9E9E;"> :    55 :   55</span></p>
<p style="text-align: center;"><span style="color: #9E9E9E;">dina . </span><span style="font-size: 12pt; font-weight: bold;">uta : posha : agrima</span><span style="color: #9E9E9E;"> : anuga : boda</span></p>
<p>For science, the base unit of time is the anuga, so all other units that derive from time in any way use the anuga in their definitions.</p>
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
`,
    'optgroup-units-ang-common': 'Common/Civil',
    'option-units-ang-dina': 'dina = day',
    'option-units-ang-uta': 'uta ~ hour',
    'option-units-ang-posha': 'posha ~ minute',
    'option-units-ang-agrima': 'agrima ~ second',
    'option-units-ang-anuga': 'anuga ~ centisecond',
    'option-units-ang-boda': 'boda ~ millisecond',
    'optgroup-units-ang-dina': 'Dina/day',
    'option-units-ang-din': 'din = day',
    // 'option-units-ang-edin': 'edin',
    'option-units-ang-ddin': 'ddin = uta',
    // 'option-units-ang-tdin': 'tdin',
    'option-units-ang-cdin': 'cdin = posha',
    // 'option-units-ang-pdin': 'pdin',
    'option-units-ang-xdin': 'xdin = agrima',
    // 'option-units-ang-xedin': 'xedin',
    'option-units-ang-xddin': 'xddin = anuga',
    // 'option-units-ang-xtdin': 'xtdin',
    'option-units-ang-xcdin': 'xcdin = boda',
    'optgroup-units-ang-anuga': 'Anuga',
    'option-units-ang-XDang': 'XDang = dina/day',
    // 'option-units-ang-XEang': 'XEang',
    'option-units-ang-Xang': 'Xang = uta',
    // 'option-units-ang-Pang': 'Pang',
    'option-units-ang-Cang': 'Cang = posha',
    // 'option-units-ang-Tang': 'Tang',
    'option-units-ang-Dang': 'Dang = agrima',
    // 'option-units-ang-Eang': 'Eang',
    // 'option-units-ang-ang': 'ang',
    // 'option-units-ang-eang': 'eang',
    'option-units-ang-dang': 'dang = boda',
    // 'option-units-ang-tang': 'tang',
    // 'option-units-ang-cang': 'cang',
    // 'option-units-ang-pang': 'pang',
    // 'option-units-ang-xang': 'xang',
    'optgroup-decimal-units-ang-common': 'Common/civil',
    'option-decimal-units-ang-day': 'day',
    'option-decimal-units-ang-hour': 'hour',
    'option-decimal-units-ang-minute': 'minute',
    'option-decimal-units-ang-second': 'second',

    'unit-avt-explanation': `
<br/>
<p>Frequency is registered using the unit avrita (uh-VREE-tuh), símbolo avt, that represents events, cycles, ocurrences etc. per anuga (the base unit of time).</p>
<p>An interesting property of all units envolving time in sezimal, is that is }fairly easy to convert between the several units of civil time and the anuga:</p>
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
};

export { sezimal_calculator_en_text };
