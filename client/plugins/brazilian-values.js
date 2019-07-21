import Vue from 'vue'
import BrazilianValues from 'brazilian-values'

Vue.use(BrazilianValues, {
    inject: true,
    fieldsBagName: 'brazilianValues',
});