<template>
  <section>
    <form @submit.prevent="validateBeforeSubmit" method="post">
      <template v-if="!sucess">
        <b-field
          label="Email"
          :type="{'is-danger': errors.has('Email')}"
          :message="errors.first('Email')"
        >
          <b-input type="text" v-model="email" name="Email" v-validate="'required|email'" />
        </b-field>
        <hr />
        <button
          type="submit"
          class="button is-primary is-outlined is-medium is-rounded is-fullwidth"
        >Enviar</button>
      </template>
      <div v-else class="column has-text-centered">
        <h1>Um link para redefinir sua senha será enviado para seu email</h1>
        <hr />
      </div>
      <div class="column has-text-centered">
        <nuxt-link
          class="voltar is-primary is-inverted"
          to="/auth/login"
          exact-active-class="is-active"
        >Voltar</nuxt-link>
      </div>
    </form>
  </section>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      email: null,
      sucess: false
    }
  },
  methods: {
    ...mapActions({
      recuperarSenha: "login/resetPassword"
    }),
    async resetPassword() {
      try {
       this.recuperarSenha(this.email)
          .then(response => {
            this.$buefy.toast.open({
              message: 'Recuperação de senha enviada para email com successo!',
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
              message: 'Email não encontrado.',
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
      } catch (e) {
        console.log(e)
      }
    },

    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.resetPassword()
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
