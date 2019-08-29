<template>
  <div>
    <h1 class="title is-5 has-text-centered">Endereço</h1>
    <b-field label="CEP" :type="{'is-danger': errors.has('CEP')}" :message="errors.first('CEP')">
      <b-input
        type="text"
        @blur="cepEnter"
        v-model.trim="endereco.cep"
        v-cleave="maskCep"
        name="CEP"
        maxlength="9"
        v-validate="'required|cep'"
      ></b-input>
    </b-field>
    <b-field
      label="Logradouro"
      :type="{'is-danger': errors.has('logradouro')}"
      :message="errors.first('logradouro')"
    >
      <b-input
        type="text"
        v-model.trim="endereco.logradouro"
        name="logradouro"
        v-validate="'required'"
      ></b-input>
    </b-field>
    <b-field
      label="Número"
      :type="{'is-danger': errors.has('numero')}"
      :message="errors.first('numero')"
    >
      <b-input type="number" v-model.number="endereco.numero" name="numero" v-validate="'required'"></b-input>
    </b-field>
    <b-field
      label="Complemento"
      :type="{'is-danger': errors.has('complemento')}"
      :message="errors.first('complemento')"
    >
      <b-input
        type="text"
        v-model.trim="endereco.complemento"
        name="complemento"
        v-validate="'required'"
      ></b-input>
    </b-field>
    <b-field
      label="Bairro"
      :type="{'is-danger': errors.has('bairro')}"
      :message="errors.first('bairro')"
    >
      <b-input
        type="text"
        v-model.trim="endereco.bairro"
        name="bairro"
        v-validate="'required'"
      ></b-input>
    </b-field>
    <b-field
      label="Cidade"
      :type="{'is-danger': errors.has('cidade')}"
      :message="errors.first('cidade')"
    >
      <b-input
        type="text"
        v-model.trim="endereco.cidade"
        name="cidade"
        v-validate="'required'"
      ></b-input>
    </b-field>
    <b-field label="Estado" :type="{'is-danger': errors.has('estado')}" :message="errors.first('estado')">
      <b-input
        type="text"
        v-model.trim="endereco.estado"
        name="estado"
        v-validate="'required|alpha|length:2'"
      ></b-input>
    </b-field>
  </div>
</template>

<script>
export default {
  props: {
    endereco: Object,
    submitted: Boolean
  },
  data() {
    return {
      maskCep: {
        delimiters: ['-'],
        blocks: [5, 3],
        numericOnly: true
      }
    }
  },
  watch: {
    submitted() {
      if (this.submitted) {
        this.validateBeforeSubmit()
      }
    }
  },
  methods: {
    cepEnter() {
      var cep = this.endereco.cep

      if (cep != null && cep != '') {
        cep = cep.replace(/\D/g, '')

        var validacep = /^[0-9]{8}$/

        if (validacep.test(cep)) {
          this.$viaCep.buscarCep(cep).then(obj => {
            this.endereco.logradouro = obj.logradouro
            this.endereco.bairro = obj.bairro
            this.endereco.cidade = obj.localidade
            this.endereco.estado = obj.uf
          })
        }
      }
    },
    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.endereco.validAdress = true
        } else this.endereco.validAdress = false
      })
    }
  }
}
</script>