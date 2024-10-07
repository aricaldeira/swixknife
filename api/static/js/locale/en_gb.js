
import { sezimal_calculator_en_text } from './en.js';

const sezimal_calculator_en_gb_text = Object.assign({}, sezimal_calculator_en_text, {
    'help-setting': sezimal_calculator_en_text['help-setting'].replaceAll('€', '£').replaceAll('euros', 'pounds').replaceAll('cents', 'pence'),
});

export { sezimal_calculator_en_gb_text };
