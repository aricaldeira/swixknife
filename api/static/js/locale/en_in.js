
import { sezimal_calculator_en_gb_text } from './en_gb.js';

const sezimal_calculator_en_in_text = Object.assign({}, sezimal_calculator_en_gb_text, {
    'help-setting': sezimal_calculator_en_text['help-setting'].replaceAll('£', '₹').replaceAll('pounds', 'rupees').replaceAll('pence', 'paise'),
});

export { sezimal_calculator_en_in_text };
