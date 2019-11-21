<template>
  <section>
    <form @submit.prevent="validateBeforeSubmit" method="post">
      <template v-if="isCadastro">
        <b-field class="has-text-centered">
          <b-switch
            type="is-black"
            v-model="pessoaFisica"
          >{{ pessoaFisica ? "Pessoa Física" : "Pessoa Juridíca" }}</b-switch>
        </b-field>
      </template>
      <hr />
      <b-field class="file is-centered" style="margin:10px;">
        <b-upload v-model="doador.foto">
          <img
            class="profile-image"
            :src="doador.foto != null ? loadFoto() : 'https://bulma.io/images/placeholders/128x128.png'"
          />
        </b-upload>
      </b-field>
      <hr />
      <b-field
        label="Nome/Razão social"
        :type="{'is-danger': errors.has('nome')}"
        :message="errors.first('nome')"
      >
        <b-input
          type="text"
          v-model.trim="doador.nome_completo"
          name="nome"
          v-validate="'required'"
        ></b-input>
      </b-field>
      <div v-show="pessoaFisica">
        <b-field
          label="CPF"
          :type="{'is-danger': errors.has('CPF')}"
          :message="errors.first('CPF')"
        >
          <b-input
            :disabled="!isCadastro"
            type="text"
            v-model.trim="doador.cpf"
            name="CPF"
            v-cleave="masks.cpf"
            maxlength="14"
            v-validate="{required: pessoaFisica, cpf: pessoaFisica}"
          ></b-input>
        </b-field>
      </div>
      <div v-show="!pessoaFisica">
        <b-field
          label="CNPJ"
          :type="{'is-danger': errors.has('CNPJ')}"
          :message="errors.first('CNPJ')"
        >
          <b-input
            :disabled="!isCadastro"
            type="text"
            v-model.trim="doador.cpf"
            maxlength="18"
            v-cleave="masks.cnpj"
            name="CNPJ"
            v-validate="{required: !pessoaFisica, cnpj:!pessoaFisica}"
          ></b-input>
        </b-field>
      </div>
      <b-field
        label="Telefone"
        :type="{'is-danger': errors.has('telefone')}"
        :message="errors.first('telefone')"
      >
        <b-input
          type="text"
          v-model.trim="doador.telefone[0].numero"
          v-cleave="masks.phone"
          maxlength="15"
          name="telefone"
          v-validate="'required|phone'"
        ></b-input>
      </b-field>
      <b-checkbox v-model="doador.telefone[0].whatsapp" type="is-black">
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
          v-model.trim="doador.email"
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
            v-model="doador.password"
            v-validate="'required|min:4'"
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
            name="confirmação"
            type="password"
            v-model="passwordConfirm"
          />
        </b-field>
        <hr />
        <div class="column has-text-centered">
          Já tem um cadastro?
          <nuxt-link
            class="is-primary is-inverted"
            to="/auth/login"
            exact-active-class="is-active"
          >Logue-se</nuxt-link>
        </div>
      </template>
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
  </section>
</template>
<script>
import cleave from '@/plugins/cleave-directive.js'
import { ErrorBag } from 'vee-validate'

export default {
  props: {
    isCadastro: Boolean,
    isDoador: Boolean
  },
  data() {
    return {
      doador: {
        foto: null,
        nome_completo: null,
        cpf: null,
        ativo: true,
        vinculo_ong: false,
        ultimo_login: '2019-07-24T22:39:02.543520Z',
        telefone: [
          {
            numero: null,
            whatsapp: false
          }
        ],
        endereco: {
          cep: '49000000',
          logradouro: 'logradouro',
          bairro: 'bairro',
          cidade: 'cidade',
          estado: 'estado',
          numero: 2,
          principal: true
        },
        email: null,
        password: null
      },
      pessoaFisica: true,
      passwordConfirm: null,
      success: false, //toremove
      masks: {
        cpf: {
          delimiters: ['.', '.', '-'],
          blocks: [3, 3, 3, 2],
          numericOnly: true
        },
        phone: {
          delimiters: ['(', ')', ' ', '-'],
          blocks: [0, 2, 0, 4, 5],
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
  created() {
    if (!this.isCadastro) {
      this.doador = JSON.parse(JSON.stringify(this.$auth.user))
    }
  },
  methods: {
    loadFoto() {
      return URL.createObjectURL(this.doador.foto)
    },
    async patch() {
      try {
        await this.$axios
          .patch(`/usuario/${this.$auth.user.id}/`, {
            nome_completo: this.doador.nome_completo,
            //telefone: this.doador.telefone,
            email: this.doador.email
            //foto: this.doador.foto
          })
          .then(response => {
            this.$buefy.toast.open({
              message: 'Atualização realizada com successo!',
              type: 'is-success',
              position: 'is-top'
            })
            this.$router.push('/editarPerfil')
          })
          .catch(err => {
            if (!err.response) {
              err.message = 'Servidor desconectado'
            } else if (err.response.status === 400) {
              if (err.response.data.non_field_errors)
                err.message = err.response.data.non_field_errors[0]
            }
            this.$buefy.toast.open({
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
    async register() {
      try {
        await this.$axios
          .post('usuario/', this.doador)
          .then(response => {
            this.$buefy.toast.open({
              message: 'Cadastro realizado com successo!',
              type: 'is-success',
              position: 'is-top'
            })
            this.$router.push('/auth/login')
          })
          .catch(err => {
            console.error(this.errors)
            if (!err.response) {
              err.message = 'Servidor desconectado'
            } else if (err.response.data.mensagem.email != null) {
              err.message = "Usuário com este email já existe"
            } else if (err.response.status === 400) {
              if (err.response.data.non_field_errors)
                err.message = err.response.data.non_field_errors[0]
            }
            this.$buefy.toast.open({
              message: err.message,
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
      } catch (e) {
        this.error = e.response.data.message
      }
    },

    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.doador.telefone[0].numero = this.doador.telefone[0].numero.replace(
            /\D/g,
            ''
          )
          this.doador.cpf = this.doador.cpf.replace(/\D/g, '')
          this.isCadastro ? this.register() : this.patch()

          return
        }
        this.$buefy.toast.open({
          message: 'Formulário inválido, verifique os campos em vermelho',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
    }
  }
}
</script>
<style lang="scss" scoped>
.profile-image {
  border-radius: 50% !important;
  width: 128px;
  height: 128px;
  object-fit: cover;
}
</style>
