import Vue from 'vue'
import ViaCep from 'vue-viacep'

Vue.use(ViaCep, {
  inject: true,
  fieldsBagName: 'viaCep',
});