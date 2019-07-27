<template>
  <section>
    <form v-if="!success" @submit.prevent="validateBeforeSubmit" method="post">
      <b-field
        label="Razão social"
        :type="{'is-danger': errors.has('razão social')}"
        :message="errors.first('razão social')"
      >
        <b-input
          type="text"
          v-model.trim="ong.razao_social"
          name="razão social"
          v-validate="'required'"
        ></b-input>
      </b-field>
      <b-field
        label="CNPJ"
        v-cleave="masks.cnpj"
        :type="{'is-danger': errors.has('CNPJ')}"
        :message="errors.first('CNPJ')"
      >
        <b-input
          :disabled="!isCadastro"
          type="text"
          v-model.trim="ong.cnpj"
          maxlength="18"
          name="CNPJ"
          v-validate="'required|cnpj'"
        ></b-input>
      </b-field>
      <b-field
        label="Biografia da ONG"
        :type="{'is-danger': errors.has('biografia')}"
        :message="errors.first('biografia')"
      >
        <b-input
          type="textarea"
          maxlength="200"
          v-model.trim="ong.historia"
          name="biografia"
          v-validate="'required'"
        ></b-input>
      </b-field>
      <hr />
      <h1 class="title is-5 has-text-centered">Responsável</h1>
      <b-field
        label="Nome"
        :type="{'is-danger': errors.has('nome')}"
        :message="errors.first('nome')"
      >
        <b-input
          type="text"
          v-model.trim="ong.usuario.nome_completo"
          name="nome"
          v-validate="'required'"
        ></b-input>
      </b-field>
      <b-field
        label="CPF"
        v-cleave="masks.cpf"
        :type="{'is-danger': errors.has('CPF')}"
        :message="errors.first('CPF')"
      >
        <b-input
          :disabled="!isCadastro"
          type="text"
          v-model.trim="ong.usuario.cpf"
          maxlength="18"
          name="CPF"
          v-validate="'required|cpf'"
        ></b-input>
      </b-field>
      <b-field
        label="Telefone"
        v-cleave="masks.phone"
        :type="{'is-danger': errors.has('telefone')}"
        :message="errors.first('telefone')"
      >
        <b-input
          type="text"
          v-model.trim="ong.usuario.telefone[0].numero"
          maxlength="15"
          name="telefone"
          v-validate="'required|phone'"
        ></b-input>
      </b-field>
      <b-checkbox v-model="ong.usuario.telefone[0].whatsapp" type="is-black">
        Whatsapp?
        <img width="15" src="~assets/wpp-icon.png" />
      </b-checkbox>
      <b-field
        label="Email"
        :type="{'is-danger': errors.has('email')}"
        :message="errors.first('email')"
      >
        <b-input
          type="text"
          v-model.trim="ong.usuario.email"
          name="email"
          v-validate="'required|email'"
        />
      </b-field>
      <template v-if="isCadastro">
        <b-field
          label="Senha"
          :type="{'is-danger': errors.has('senha')}"
          :message="errors.first('senha')"
        >
          <b-input
            type="password"
            name="senha"
            v-model="ong.usuario.password"
            v-validate="'required|min:8'"
            ref="senha"
          />
        </b-field>
        <b-field
          label="Confirme sua senha"
          :type="{'is-danger': errors.has('confirmação')}"
          :message="errors.first('confirmação')"
        >
          <b-input
            v-validate="'required|confirmed:senha'"
            v-model="passwordConfirm"
            name="confirmação"
            type="password"
            data-vv-as="senha"
          />
        </b-field>
      </template>
      <hr />
      <EnderecoForm :endereco="ong.usuario.endereco" :submitted="submitted" />
      <hr />
      <div class="column has-text-centered" v-if="isCadastro">
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
    <div v-else-if="isCadastro" class="column has-text-centered">
      <h1>Cadastro realizado com sucesso! Será enviada uma confirmação para seu email.</h1>
      <hr />
    </div>
    <div v-else class="column has-text-centered">
      <h1>Atualização realizada com sucesso! Será enviada uma confirmação para seu email.</h1>
      <hr />
    </div>
  </section>
</template>

<script>
import ViaCep from 'vue-viacep'
import EnderecoForm from '@/components/molecules/EnderecoForm.vue'
import cleave from '@/plugins/cleave-directive.js'
import { mapGetters } from 'vuex'
export default {
  components: { EnderecoForm },
  props: {
    isCadastro: Boolean
  },
  data() {
    return {
      ong: {
        razao_social: null,
        cnpj: null,
        historia: null,
        usuario: {
          email: null,
          password: null,
          nome_completo: null,
          ativo: true,
          ultimo_login: '2019-07-24T22:39:02.543520Z',
          cpf: null,
          vinculo_ong: true,
          endereco: {
            id: 2,
            logradouro: null,
            bairro: null,
            cidade: null,
            estado: null,
            numero: null,
            principal: true,
            validAdress: null
          },
          telefone: [
            {
              numero: null,
              whatsapp: false
            }
          ]
        }
      },
      passwordConfirm: null,
      success: false, //toremove
      submitted: false,
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
        },
        cpf: {
          delimiters: ['.', '.', '-'],
          blocks: [3, 3, 3, 2],
          numericOnly: true
        },
      }
    }
  },
  computed: {
    user() {
      return this.$auth.user
    }
  },
  mounted() {
    !this.isCadastro ? this.getOng() : {}
  },
  methods: {
    async register() {
      var num = this.ong.usuario.telefone[0].numero
      this.ong.usuario.telefone[0].numero = Number.parseInt(num.replace(/\D/g, ''))
      try {
        await this.$axios
          .post('ong/create/', this.ong)
          .catch(err => {
            if (!err.response) {
              err.message = 'Servidor desconectado'
            } else if (err.response.status === 400) {
              err.message = err.response.data.non_field_errors[0]
            }
            this.$toast.open({
              message: err.message,
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
        this.success = true
      } catch (e) {
        this.error = e.response.data.message
      }
    },
    //todo
    validateBeforeSubmit() {
      this.submitted = true
      var interval = setInterval(() => {
        if (this.ong.usuario.endereco.validAdress != null) {
          if (!this.ong.usuario.endereco.validAdress) {
            this.ong.usuario.endereco.validAdress = null
            this.submitted = false
          }
          this.$validator.validateAll().then(result => {
            if (result && this.ong.usuario.endereco.validAdress) {
              this.register()
              return
            } else {
              this.submitted = false
              this.$toast.open({
                message: 'Formulário inválido, verifique os campos em vermelho',
                type: 'is-danger',
                position: 'is-bottom'
              })
            }
          })
          clearInterval(interval)
        }
      }, 500)
    }
  }
}
</script>
