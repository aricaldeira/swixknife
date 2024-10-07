
import { sezimal_calculator_en_text } from './en.js';

const sezimal_calculator_en_us_text = Object.assign({}, sezimal_calculator_en_text, {
    'help-setting': sezimal_calculator_en_text['help-setting'].replaceAll('€', '$').replaceAll('euro', 'dollar'),

    'optgroup-units-generic-imp-us': 'Customary/Imperial',
    'optgroup-units-generic-us': 'Customary',
    'optgroup-units-generic-us-fluid': 'Fluid',
    'optgroup-units-generic-us-dry': 'Dry',

    'option-decimal-prefix-deca': 'da – deca – 10¹',

    'option-decimal-units-pad-metre': 'meter – m',
    'option-decimal-units-ktr-sq-metre': 'sq. meter – m²',
    'option-decimal-units-ayt-cb-metre': 'cb. meter – m³',
    'option-decimal-units-ayt-litre': 'liter – L',

    'option-decimal-units-drv-US-qr': 'quarter – qr',
    'option-decimal-units-drv-US-cwt': 'hundredweight – cwt',
    'option-decimal-units-drv-US-ton': 'ton – ton',
    'option-decimal-units-drv-imp-qr': 'long quarter – qr',
    'option-decimal-units-drv-imp-cwt': 'long hundredweight – cwt',
    'option-decimal-units-drv-imp-ton': 'long ton – ton',

    'option-decimal-units-ayt-imp-fl-dr': 'fluid dram - imp. fl dr',
    'option-decimal-units-ayt-imp-fl-oz': 'fluid ounce - imp. fl oz',
    'option-decimal-units-ayt-imp-pt': 'pint - imp. pt',
    'option-decimal-units-ayt-imp-qt': 'quarter - imp. qt',
    'option-decimal-units-ayt-imp-gal': 'gallon - imp. gal',

    'option-decimal-units-ayt-us-fl-dr': 'dram  – fl dr',
    'option-decimal-units-ayt-us-tsp': 'tea spoon – tsp',
    'option-decimal-units-ayt-us-tbsp': 'table spoon – tbsp',
    'option-decimal-units-ayt-us-fl-oz': 'ounce - fl oz',
    'option-decimal-units-ayt-us-cup': 'cup – cup',
    'option-decimal-units-ayt-us-pt': 'pint – pt',
    'option-decimal-units-ayt-us-qt': 'quarter – qt',
    'option-decimal-units-ayt-us-gal': 'gallon – gal',
    'option-decimal-units-ayt-us-pt-dry': 'pint - pt (dry)',
    'option-decimal-units-ayt-us-qt-dry': 'quarter - qt (dry)',
    'option-decimal-units-ayt-us-gal-dry': 'gallon - gal (dry)',
    'option-decimal-units-ayt-us-pk-dry': 'peck - pk (dry)',
    'option-decimal-units-ayt-us-bu-dry': 'bushel - bu (dry)',

    'translation-display-US-fl-dr': 'fl dr',
    'translation-display-US-tsp': 'tsp',
    'translation-display-US-tbsp': 'tbsp',
    'translation-display-US-fl-oz': 'fl oz',
    'translation-display-US-cup': 'cup',
    'translation-display-US-pt': 'pt',
    'translation-display-US-qt': 'qt',
    'translation-display-US-gal': 'gal',
    'translation-display-US-pt-dry': 'pt (dry)',
    'translation-display-US-qt-dry': 'qt (dry)',
    'translation-display-US-gal-dry': 'gal (dry)',
    'translation-display-US-pk-dry': 'pk (dry)',
    'translation-display-US-bu-dry': 'bu (dry)',

    'translation-display-imp-fl-dr': 'imp. fl dr',
    'translation-display-imp-fl-oz': 'imp. fl oz',
    'translation-display-imp-pt': 'imp. pt',
    'translation-display-imp-qt': 'imp. qt',
    'translation-display-imp-gal': 'imp. gal',

    'option-decimal-units-veg-mh': 'meters per hour – m/h',
    'option-decimal-units-veg-ms': 'meters per second – m/s',

    'option-decimal-units-tvr-ms2': 'meters per sq. second – m/s²',

    'option-decimal-units-gnt-gm3': 'grams per cb. meter – g/m³',
    'option-decimal-units-gnt-gl': 'grams per liter – g/L',

    'option-decimal-units-bar-gms2': 'gram-meter per sq. second – g·m/s²',

    'option-decimal-units-pdn-mmhg': 'millimeters of mercury – mm Hg',

    'option-decimal-units-svg-gms': 'gram-meter per second – g·m/s',

    'option-decimal-units-clt-kml': 'kilometers per liter – km/L',
    'option-decimal-units-clt-l100km': 'liters per 100 kilometers – L/100 L',
    'option-decimal-units-clt-km20l': 'kilometers per 20 liters – km/20 L',
    'option-decimal-units-clt-usmpg': 'miles per gallon – mpg',
    'option-decimal-units-clt-impmpg': 'miles per imperial gallon – mpg imp.',

    'translation-display-US-mpg': 'mpg',
    'translation-display-imp-mpg': 'mpg imp.',
});

console.log('passou aqui', sezimal_calculator_en_us_text['help-setting']);

export { sezimal_calculator_en_us_text };
