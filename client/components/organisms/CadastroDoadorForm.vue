<template>
  <section>
    <form v-if="!sucess" @submit.prevent="validateBeforeSubmit" method="post">
      <div class="block has-text-centered">
        <b-radio v-model="pessoaFisica" :native-value="true" ref="fis" type="is-black">Física</b-radio>
        <b-radio v-model="pessoaFisica" :native-value="false" ref="jur" type="is-black">Juridíca</b-radio>
      </div>
      <hr />
      <b-field
        label="Nome/Razão social"
        :type="{'is-danger': errors.has('Nome')}"
        :message="errors.first('Nome')"
      >
        <b-input
          type="text"
          v-model.trim="usuario.nome_completo"
          name="Nome"
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
            type="text"
            v-model.trim="usuario.cpf_cnpj"
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
            type="text"
            v-model.trim="usuario.cpf_cnpj"
            maxlength="18"
            v-cleave="masks.cnpj"
            name="CNPJ"
            v-validate="{required: !pessoaFisica, cnpj:!pessoaFisica}"
          ></b-input>
        </b-field>
      </div>
      <b-field
        label="Telefone"
        :type="{'is-danger': errors.has('Telefone')}"
        :message="errors.first('Telefone')"
      >
        <b-input
          type="text"
          v-model.trim="usuario.telefone.numero"
          v-cleave="masks.phone"
          maxlength="15"
          name="Telefone"
          v-validate="'required|phone'"
        ></b-input>
      </b-field>
      <b-checkbox v-model="usuario.telefone.whatsapp" type="is-black">
        Whatsapp?
        <img width="15" src="~assets/wpp-icon.png" />
      </b-checkbox>
      <b-field
        label="Email"
        :type="{'is-danger': errors.has('Email')}"
        :message="errors.first('Email')"
      >
        <b-input
          type="text"
          v-model.trim="usuario.email"
          name="Email"
          v-validate="'required|email'"
        />
      </b-field>
      <b-field
        label="Senha"
        :type="{'is-danger': errors.has('Senha')}"
        :message="errors.first('Senha')"
      >
        <b-input
          type="password"
          name="Senha"
          v-model="usuario.password"
          v-validate="'required|min:8'"
          ref="Senha"
        />
      </b-field>
      <b-field
        label="Confirme sua senha"
        :type="{'is-danger': errors.has('Confirmação')}"
        :message="errors.first('Confirmação')"
      >
        <b-input
          v-validate="'required|confirmed:Senha'"
          name="Confirmação"
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
import cleave from '@/plugins/cleave-directive.js'
export default {
  data() {
    return {
      usuario: {
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
      sucess: false, //toremove
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
  methods: {
    async register() {
      try {
        await this.$UsuarioService.create(this.usuario).catch(err => {
          console.error(err)
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
        /* this.$router.push('/') */
      } catch (e) {
        this.error = e.response.data.message
      }
    },
    validateBeforeSubmit() {
      console.log(this.pessoaFisica)
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
