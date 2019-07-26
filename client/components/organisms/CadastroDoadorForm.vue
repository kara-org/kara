<template>
  <section>
    <form v-if="!success" @submit.prevent="validateBeforeSubmit" method="post">
      <div class="block has-text-centered" v-if="isCadastro">
        <b-radio v-model="pessoaFisica" :native-value="true" type="is-black">Física</b-radio>
        <b-radio v-model="pessoaFisica" :native-value="false" type="is-black">Juridíca</b-radio>
      </div>
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
            v-model.trim="doador.cpf_cnpj"
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
            v-model.trim="doador.cpf_cnpj"
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
          v-model.trim="doador.telefone.numero"
          v-cleave="masks.phone"
          maxlength="15"
          name="telefone"
          v-validate="'required|phone'"
        ></b-input>
      </b-field>
      <b-checkbox v-model="doador.telefone.whatsapp" type="is-black">
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
            to="/login"
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
    <div v-else-if="isCadastro" class="column has-text-centered">
      <h1>Cadastro realizado com successo! Será enviada uma confirmação para seu email.</h1>
      <hr />
    </div>
    <div v-else-if="!isCadastro" class="column has-text-centered">
      <h1>Atualização realizada com successo! Será enviada uma confirmação para seu email.</h1>
      <hr />
    </div>
  </section>
</template>
<script>
import cleave from '@/plugins/cleave-directive.js'
export default {
  props: {
    isCadastro: Boolean,
    isDoador: Boolean,
    usuarioEditar: Object
  },
  data() {
    return {
      doador: {
        nome_completo: null,
        cpf_cnpj: null,
        telefone: {
          numero: null,
          whatsapp: false
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
  created() {
    !this.isCadastro ? (this.doador = this.usuarioEditar) : this.doador
  },
  methods: {
    async register() {
      try {
        await this.$UsuarioService
          .create({
            email: 'emily@gmail.com',
            password: 'senha123',
            nome_completo: 'Emily Stefany Barros',
            ativo: true,
            ultimo_login: '2019-07-24T22:39:02.543520Z',
            cpf: '924.670.669-24',
            vinculo_ong: false,
            endereco: {
              id: 1,
              logradouro: 'Rua das aboboras 2',
              bairro: 'Leguminosas',
              cidade: 'Aracaju',
              estado: 'Sergipe',
              numero: 2,
              principal: true
            },
            telefone: [
              {
                numero: 11111111111,
                whatsapp: true
              }
            ]
          })
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
    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.register()
          return
        }
        this.$toast.open({
          message: 'Formulário inválido, verifique os campos em vermelho',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
    }
  }
}
</script>