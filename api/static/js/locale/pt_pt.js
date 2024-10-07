
import { sezimal_calculator_pt_text } from './pt.js';

const sezimal_calculator_pt_pt_text = Object.assign({}, sezimal_calculator_pt_text, {
    'option-decimal-units-gol-sterradian': 'esterradianos – sr',
    'option-decimal-units-bht-mole': 'moles – mol',
    'option-decimal-units-bar-dyn': 'dines – dyn',
    'option-decimal-units-vrc-ev': 'eletrões-volt – eV',
    'help-setting': sezimal_calculator_pt_text['help-setting'].replaceAll('R$', '€').replaceAll('reais󱹶', 'euros󱹶').replaceAll('reais;', 'euros;').replaceAll('centavos', 'cêntimos'),
});

export { sezimal_calculator_pt_pt_text };
