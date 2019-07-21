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
          to="/login"
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
      sucess: false
    }
  },
  methods: {
    async resetPassword() {
      setTimeout(() => {
        this.sucess = true
      }, 1000)
    },

    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.resetPassword()
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
