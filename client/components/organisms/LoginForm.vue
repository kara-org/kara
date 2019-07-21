<template>
  <section>
    <form @submit.prevent="validateBeforeSubmit" method="post">
      <b-field
        label="Email"
        :type="{'is-danger': errors.has('Email')}"
        :message="errors.first('Email')"
      >
        <b-input type="text" v-model="email" name="Email" v-validate="'required|email'" />
      </b-field>

      <b-field
        label="Senha"
        :type="{'is-danger': errors.has('Senha')}"
        :message="errors.first('Senha')"
      >
        <b-input
          type="password"
          name="Senha"
          password-reveal
          v-model="password"
          v-validate="'required|min:8'"
        />
      </b-field>
      <hr />
      <div class="column has-text-centered">
        <span>Esqueceu a senha?</span>
        <nuxt-link
          class="is-primary is-inverted"
          to="/esqueciSenha"
          exact-active-class="is-active"
        >Resete sua senha</nuxt-link>
        <br />
        <span>Não é usuário?</span>
        <nuxt-link
          class="is-primary is-inverted"
          to="/cadastro"
          exact-active-class="is-active"
        >Cadastre-se</nuxt-link>
      </div>
      <hr />
      <button
        type="submit"
        class="button is-primary is-outlined is-medium is-rounded is-fullwidth"
      >Entrar</button>
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
export default {
  data() {
    return {
      email: null,
      password: null
    }
  },
  methods: {
    async login() {
      try {
        this.$auth
          .loginWith('local', {
            data: {
              email: this.email,
              password: this.password
            }
          })
          .catch(err => {
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
        // this.$router.push('/')
      } catch (e) {
        this.$toast.open({
          message: e.response.data.message,
          type: 'is-danger',
          position: 'is-bottom'
        })

        return
      }
    },

    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.login()
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
