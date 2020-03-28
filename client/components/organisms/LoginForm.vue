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
          v-validate="'required|min:4'"
        />
      </b-field>
      <div class="level has-text-centered">
        <nuxt-link
          class="is-primary is-inverted"
          to="/esqueciSenha"
          exact-active-class="is-active"
        >Esqueci minha senha</nuxt-link>
        <br />
        <nuxt-link
          class="is-primary is-inverted"
          to="/auth/cadastro"
          exact-active-class="is-active"
        >Não sou cadastrado</nuxt-link>
      </div>
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
import LoginService from "../../services/LoginService";

export default {
  data() {
    return {
      email: null,
      password: null,
      loginService: null
    };
  },
  mounted() {
    this.loginService = new LoginService();
  },
  methods: {
    async login() {
      await this.loginService.login(this.email, this.password).catch(err => {
        console.log(err.response)
        if (!err.response) {
          err.message = 'Servidor desconectado';
        } else if (err.response.status === 400) {
          err.message =
            'Login ou senha inválidos, confira os dados e tente novamente';
        }

        this.$buefy.toast.open({
          message: err.message,
          type: 'is-danger',
          position: 'is-bottom'
        });
        return;
      });
    },

    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.login();
          return;
        }
        this.$buefy.toast.open({
          message: 'Formulário inválido, verifique os campos em vermelho',
          type: 'is-danger',
          position: 'is-bottom'
        });
      });
    }
  }
};
</script>
