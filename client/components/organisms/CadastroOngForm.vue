<template>
  <section>
    <form v-if="!sucess" @submit.prevent="validateBeforeSubmit" method="post">
      <b-field
        label="Razão social"
        :type="{'is-danger': errors.has('razão social')}"
        :message="errors.first('razão social')"
      >
        <b-input
          type="text"
          v-model.trim="ong.nome_completo"
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
          v-model.trim="ong.cpf_cnpj"
          maxlength="18"
          name="CNPJ"
          v-validate="'required|cnpj'"
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
          v-model.trim="ong.telefones[0]"
          maxlength="15"
          name="telefone"
          v-validate="'required|phone'"
        ></b-input>
      </b-field>
      <b-field
        label="Email"
        :type="{'is-danger': errors.has('email')}"
        :message="errors.first('email')"
      >
        <b-input type="text" v-model.trim="ong.email" name="email" v-validate="'required|email'" />
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
            v-model="ong.password"
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
      <EnderecoForm :endereco="ong.endereco" :submitted="submitted" />
      <hr />
      <b-field
        label="Biografia da ONG"
        :type="{'is-danger': errors.has('biografia')}"
        :message="errors.first('biografia')"
      >
        <b-input
          type="textarea"
          maxlength="200"
          v-model.trim="ong.biografia"
          name="biografia"
          v-validate="'required'"
        ></b-input>
      </b-field>
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
export default {
  components: { EnderecoForm },
  props: {
    isCadastro: Boolean
  },
  data() {
    return {
      ong: {
        nome_completo: null,
        cpf_cnpj: '',
        telefones: [],
        email: null,
        password: null,
        biografia: null,
        endereco: {
          cep: null,
          logradouro: null,
          numero: null,
          complemento: null,
          bairro: null,
          localidade: null,
          uf: null,
          validAdress: null
        }
      },
      passwordConfirm: null,
      sucess: false, //toremove
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
        }
      }
    }
  },
  created() {
    !this.isCadastro ? this.getOng() : {}
  },
  methods: {
    async getOng() {
      this.ong = await this.$OngService.get('id')
    },
    async register() {
      try {
        console.log(this.ong)
        await this.$OngService
          .create({
            cnpj: '111111111111',
            historia: 'bb',
            usuario: {
              email: 'emily@hotmail.com',
              password: 'senha123',
              nome_completo: 'Emily Stefany Barros',
              ativo: true,
              ultimo_login: '2019-07-24T22:39:02.543520Z',
              cpf: '924.670.669-24',
              vinculo_ong: true,
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
            }
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
    //todo
    validateBeforeSubmit() {
      this.submitted = true
      var interval = setInterval(() => {
        if (this.ong.endereco.validAdress != null) {
          if (!this.ong.endereco.validAdress) {
            this.ong.endereco.validAdress = null
            this.submitted = false
          }
          this.$validator.validateAll().then(result => {
            if (result && this.ong.endereco.validAdress) {
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
