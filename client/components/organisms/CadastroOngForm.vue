<template>
  <section>
    <form v-if="!sucess" @submit.prevent="validateBeforeSubmit" method="post">
      <b-field
        label="Razão social"
        :type="{'is-danger': errors.has('Razão social')}"
        :message="errors.first('Razão social')"
      >
        <b-input type="text" v-model.trim="razaoSocial" name="Razão social" v-validate="'required'"></b-input>
      </b-field>
      <b-field
        label="CNPJ"
        v-cleave="masks.cnpj"
        :type="{'is-danger': errors.has('CNPJ')}"
        :message="errors.first('CNPJ')"
      >
        <b-input
          type="text"
          v-model.trim="cpnj"
          maxlength="18"
          name="CNPJ"
          v-validate="'required|cnpj'"
        ></b-input>
      </b-field>
      <b-field
        label="Telefone"
        v-cleave="masks.phone"
        :type="{'is-danger': errors.has('Telefone')}"
        :message="errors.first('Telefone')"
      >
        <b-input
          type="text"
          v-model.trim="phoneNumbers[0]"
          maxlength="15"
          name="Telefone"
          v-validate="'required|phone'"
        ></b-input>
      </b-field>
      <b-field
        label="Email"
        :type="{'is-danger': errors.has('Email')}"
        :message="errors.first('Email')"
      >
        <b-input type="text" v-model.trim="email" name="Email" v-validate="'required|email'" />
      </b-field>
      <b-field
        label="Senha"
        :type="{'is-danger': errors.has('senha')}"
        :message="errors.first('senha')"
      >
        <b-input
          type="password"
          name="senha"
          v-model="password"
          v-validate="'required|min:8'"
          ref="senha"
        />
      </b-field>
      <b-field
        label="Confirme sua senha"
        :type="{'is-danger': errors.has('Confirmação')}"
        :message="errors.first('Confirmação')"
      >
        <b-input
          v-validate="'required|confirmed:senha'"
          v-model="passwordConfirm"
          name="Confirmação"
          type="password"
          data-vv-as="senha"
        />
      </b-field>
      <hr />
      <EnderecoForm :endereco="endereco" :submitted="submitted" />
      <hr />
      <b-field
        label="Descrição da ONG"
        :type="{'is-danger': errors.has('Descrição')}"
        :message="errors.first('Descrição')"
      >
        <b-input
          type="textarea"
          maxlength="200"
          v-model.trim="descricao"
          name="Descrição"
          v-validate="'required'"
        ></b-input>
      </b-field>
      <hr />
      <div class="column has-text-centered">
        Já tem um cadastro?
        <nuxt-link
          class="is-primary is-inverted"
          to="/login"
          exact-active-class="is-active"
        >Logue-se</nuxt-link>
      </div>
      <hr />

      <button
        type="submit"
        class="button is-primary is-outlined is-medium is-rounded is-fullwidth"
      >Confirmar</button>
      <div class="column has-text-centered">
        <nuxt-link
          class="voltar is-primary is-inverted"
          to="/"
          exact-active-class="is-active"
        >Voltar</nuxt-link>
      </div>
    </form>
    <div v-else class="column has-text-centered">
      <h1>Cadastro realizado com sucesso! Será enviada uma confirmação para seu email.</h1>
      <hr />
    </div>
  </section>
</template>

<script>
import ViaCep from 'vue-viacep'
import EnderecoForm from '@/components/organisms/EnderecoForm.vue'
import cleave from '@/plugins/cleave-directive.js'
export default {
  components: { EnderecoForm },
  data() {
    return {
      razaoSocial: null,
      cpnj: '',
      phoneNumbers: [],
      email: null,
      password: null,
      passwordConfirm: null,
      descricao: null,
      sucess: false, //toremove
      submitted: false,
      endereco: {
        cep: null,
        logradouro: null,
        numero: null,
        complemento: null,
        bairro: null,
        localidade: null,
        uf: null,
        validAdress: null
      },
      masks: {
        phone: {
          delimiters: ['(', ')', ' ', '-'],
          blocks: [0, 2, 0, 4, 4],
          numericOnly: true
        },
        cnpj: {
          delimiters: ['.', '.', '/', '-'],
          blocks: [2, 3, 3, 4, 2],
          numericOnly: true
        }
      }
    }
  },
  methods: {
    async register() {
      setTimeout(() => {
        this.sucess = true
      }, 1000)
    },
    //todo
    validateBeforeSubmit() {
      this.submitted = true
      var interval = setInterval(() => {
        console.log('dasdas')
        if (this.endereco.validAdress != null) {
          if (!this.endereco.validAdress) {
            this.endereco.validAdress = null
            this.submitted = false
          } else {
            this.$validator.validateAll().then(result => {
              if (result && this.endereco.validAdress) {
                this.register()
                return
              } else {
                this.submitted = false
                this.$toast.open({
                  message:
                    'Formulário inválido, verifique os campos em vermelho',
                  type: 'is-danger',
                  position: 'is-bottom'
                })
              }
            })
          }
          clearInterval(interval)
        }
      }, 500)
    }
  }
}
</script>
