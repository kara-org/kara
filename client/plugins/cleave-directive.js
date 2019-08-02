import Vue from 'vue'
import Cleave from 'cleave.js'

const cleave = Vue.directive('cleave', {
    bind(el, binding) {
        const input = el.querySelector('input')
        input._vCleave = new Cleave(input, binding.value)
    },
    unbind(el) {
        const input = el.querySelector('input')
        input._vCleave.destroy()
    },
})
export default {
    directives: { cleave }
}