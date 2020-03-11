<template>
  <section>
    <form v-if="!success" @submit.prevent="validateBeforeSubmit" method="post">
      <hr />
      <b-field
        label="Razão social"
        :type="{'is-danger': errors.has('razão social')}"
        :message="errors.first('razão social')"
      >
        <b-input type="text" v-model.trim="ong.nome" name="razão social" v-validate="'required'"></b-input>
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
          v-validate="'cnpj'"
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
      <template v-if="isCadastro">
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
            v-model.trim="ong.telefone[0].numero"
            maxlength="15"
            name="telefone"
            v-validate="'required|phone'"
          ></b-input>
        </b-field>
        <b-checkbox v-model="ong.telefone[0].whatsapp" type="is-black">
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
        <b-field
          label="Senha"
          :type="{'is-danger': errors.has('senha')}"
          :message="errors.first('senha')"
        >
          <b-input
            type="password"
            name="senha"
            v-model="ong.usuario.password"
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
            v-model="passwordConfirm"
            name="confirmação"
            type="password"
            data-vv-as="senha"
          />
        </b-field>
        <hr />
      </template>
      <template v-if="isCadastro">
        <EnderecoForm :endereco="ong.endereco" :submitted="submitted" />
        <hr />
      </template>
      <div class="has-text-centered" style="margin: 10px;" v-if="isCadastro">
        Já tem um cadastro?
        <nuxt-link
          class="is-primary is-inverted"
          to="/auth/login"
          exact-active-class="is-active"
        >Logue-se</nuxt-link>
      </div>
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
      <h1>Cadastro realizado com sucesso!</h1>
      <hr />
    </div>
    <div v-else class="column has-text-centered">
      <h1>Atualização realizada com sucesso!</h1>
      <hr />
      <button
        class="button is-primary is-outlined is-rounded"
        @click="success=false"
        exact-active-class="is-active"
      >Voltar</button>
    </div>
  </section>
</template>

<script>
import ViaCep from 'vue-viacep'
import EnderecoForm from '@/components/molecules/EnderecoForm.vue'
import cleave from '@/plugins/cleave-directive.js'
import { mapActions } from 'vuex'
export default {
  components: { EnderecoForm },
  props: {
    isCadastro: Boolean
  },
  data() {
    return {
      ong: {
        nome: null,
        cnpj: null,
        historia: null,
        email: null,
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
        ],
        usuario: {
          email: null,
          password: null,
          nome_completo: null,
          cpf: null,
          vinculo_ong: true,
          telefone: [
            {
              numero: null,
              whatsapp: false
            }
          ]
        }
      },
      passwordConfirm: null,
      success: false,
      submitted: false,
      masks: {
        phone: {
          delimiters: ['(', ')', ' ', '-'],
          blocks: [0, 2, 0, 4, 5],
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
        }
      }
    }
  },
  computed: {
    user() {
      return this.$auth.user
    }
  },
  async mounted() {
    if (this.user && this.user.ong) {
      this.ong.id = this.user.ong.id
      this.ong.nome = this.user.ong.nome
      this.ong.cnpj = this.user.ong.cnpj
      this.ong.historia = this.user.ong.historia
    }
  },
  methods: {
    ...mapActions('ongs', ['fetchPerfilOng']),
    async register() {
      try {
        await this.$OngService
          .create(this.ong)
          .then(response => {
            this.$buefy.toast.open({
              message: 'Cadastro realizado com successo!',
              type: 'is-success',
              position: 'is-top'
            })
            this.$router.push('/auth/login')
          })
          .catch(err => {
            if (!err.response) {
              err.message = 'Servidor desconectado'
            } else if (err.response.status === 400) {
              if (err.response.data.non_field_errors) {
                err.message = err.response.data.non_field_errors[0]
              } else if (err.response.data.usuario) {
                Object.keys(err.response.data.usuario).forEach(key => {
                  this.$buefy.toast.open({
                    message: err.response.data.usuario[key][0],
                    type: 'is-danger',
                    position: 'is-bottom'
                  })
                })
                return
              }
            }
            this.$buefy.toast.open({
              message: err.response.data.message,
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
      } catch (e) {
        this.error = e.response.data.message
      }
    },
    async change() {
      try {
        await this.$OngService
          .update(this.ong.id, {
            nome: this.ong.nome,
            historia: this.ong.historia
          })
          .then(response => {
            this.$buefy.toast.open({
              message: 'Atualização realizada com successo!',
              type: 'is-success',
              position: 'is-top'
            })
            this.success = true
            // this.$router.push('/ong/editar')
          })
          .catch(err => {
            if (!err.response) {
              err.message = 'Servidor desconectado'
            } else if (err.response.status === 400) {
              if (err.response.data.non_field_errors)
                err.message = err.response.data.non_field_errors[0]
            }
            this.$buefy.toast.open({
              message: err.response.data.message,
              type: 'is-danger',
              position: 'is-bottom'
            })
            this.success = false
          })
      } catch (e) {
        this.error = e.response.data.message
      }
    },
    //TODO
    validateBeforeSubmit() {
      this.submitted = true
      if (!this.isCadastro) {
        this.$validator.validateAll().then(result => {
          if (result) {
            this.change()
            return
          } else {
            this.submitted = false
            this.$buefy.toast.open({
              message: 'Formulário inválido, verifique os campos em vermelho',
              type: 'is-danger',
              position: 'is-bottom'
            })
          }
        })
      } else
        var interval = setInterval(() => {
          if (this.ong.endereco.validAdress != null) {
            if (!this.ong.endereco.validAdress) {
              this.ong.endereco.validAdress = null
              this.submitted = false
            }
            this.$validator.validateAll().then(result => {
              if (result && this.ong.endereco.validAdress) {
                this.ong.telefone[0].numero = this.ong.telefone[0].numero.replace(
                  /\D/g,
                  ''
                )
                this.ong.usuario.telefone[0].numero = this.ong.telefone[0].numero
                this.ong.cnpj = this.ong.cnpj.replace(/\D/g, '')
                this.isCadastro ? this.register() : this.change()
                return
              } else {
                this.submitted = false
                this.$buefy.toast.open({
                  message:
                    'Formulário inválido, verifique os campos em vermelho',
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

<style lang="scss" scoped>
.profile-image {
  border-radius: 50% !important;
  width: 128px;
  height: 128px;
  object-fit: cover;
}
</style>
