import Vue from 'vue'
import VeeValidate, { Validator } from 'vee-validate'
import br from "vee-validate/dist/locale/pt_BR";
import { isCNPJ, isCPF, isCEP } from 'brazilian-values'

Validator.localize({ pt_BR: br });

Validator.extend('cpf', {
    getMessage: field => 'O campo ' + field + ' deve ser um CPF válido.',
    validate: value => isCPF(value)
});

Validator.extend('cnpj', {
    getMessage: field => 'O campo ' + field + ' deve ser um CNPJ válido.',
    validate: value => isCNPJ(value)
});

Validator.extend('cep', {
    getMessage: field => 'O campo ' + field + ' deve ser um CEP válido.',
    validate: value => isCEP(value)
});

Validator.extend('phone', {
    getMessage: field => 'O campo ' + field + ' deve ser um Telefone válido.',
    validate: value => isPhone(value)
});

function isPhone(tel) {
    var exp = /\(\d{2}\)\ \d{4}\-\d{4,5}/
    var length = tel.length != 11 && tel.length != 10
    return !exp.test(tel) && length ? false : true
}

Vue.use(VeeValidate, { locale: 'pt_BR' });