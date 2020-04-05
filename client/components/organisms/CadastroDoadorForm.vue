<template>
  <section>
    <form v-if="!success" @submit.prevent="validateBeforeSubmit" method="post">
      <hr />
      <b-field
        label="Nome"
        :type="{'is-danger': errors.has('nome')}"
        :message="errors.first('nome')"
      >
        <b-input type="text" v-model.trim="usuario.nome" name="nome" v-validate="'required'"></b-input>
      </b-field>
      <b-field
        label="Telefone"
        :type="{'is-danger': errors.has('telefone')}"
        :message="errors.first('telefone')"
      >
        <b-input
          type="text"
          v-model.trim="usuario.telefones[0]"
          v-cleave="phoneMask"
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
        <b-input
          type="text"
          v-model.trim="usuario.email"
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
            v-model="usuario.password"
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
      <button type="submit" class="button is-primary is-outlined is-medium is-rounded is-fullwidth">
        Confirmar
        <b-loading :is-full-page="true" :active.sync="isLoading" :can-cancel="false"></b-loading>
      </button>
      <div class="column has-text-centered">
        <nuxt-link
          class="voltar is-primary is-inverted"
          to="/"
          exact-active-class="is-active"
        >Voltar</nuxt-link>
      </div>
    </form>
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
import cleave from '@/plugins/cleave-directive.js';
import { ErrorBag } from 'vee-validate';
import { mapActions, mapGetters } from 'vuex';

export default {
  props: {
    isCadastro: Boolean,
    isDoador: Boolean
  },
  data() {
    return {
      usuario: {
        email: null,
        password: null,
        nome: null,
        telefones: [null]
      },
      passwordConfirm: null,
      success: false,
      phoneMask: {
        delimiters: ['(', ')', ' ', '-'],
        blocks: [0, 2, 0, 4, 5],
        numericOnly: true
      },
      isLoading: null
    };
  },

  computed: {
    ...mapGetters({ user: 'login/usuario' })
  },

  mounted() {
    if (!this.isCadastro) {
      this.usuario = { ...this.user };
    }
  },

  methods: {
    ...mapActions({ signUpParse: 'login/signUp', updateParse: 'login/update' }),
    async register() {
      await this.signUpParse({
        email: this.usuario.email,
        password: this.usuario.password,
        nome: this.usuario.nome,
        telefones: this.usuario.telefones
      })
        .then(response => {
          this.$buefy.toast.open({
            message: 'Cadastro realizado com successo!',
            type: 'is-success',
            position: 'is-top'
          });
          this.$router.push('/');
        })
        .catch(err => {
          //console.error(this.errors)
          console.log(err);
          if (err.code == 202) {
            err.message = 'Usuário com este email já existe';
          }
          this.$buefy.toast.open({
            message: err.message,
            type: 'is-danger',
            position: 'is-bottom'
          });
        });
      this.isLoading = false;
    },

    async patch() {
      await this.updateParse({
        email: this.usuario.email,
        nome: this.usuario.nome,
        telefones: this.usuario.telefones
      })
        .then(response => {
          this.$buefy.toast.open({
            message: 'Alteração realizada com successo!',
            type: 'is-success',
            position: 'is-top'
          });
        })
        .catch(err => {
          console.log(err);
          if (err.code == 202) {
            err.message = 'Usuário com este email já existe';
          }
          this.$buefy.toast.open({
            message: err.message,
            type: 'is-danger',
            position: 'is-bottom'
          });
        });
      this.success = true;
      this.isLoading = false;
    },

    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.usuario.telefones[0] = this.usuario.telefones[0].replace(
            /\D/g,
            ''
          );
          this.isLoading = true;
          return this.isCadastro ? this.register() : this.patch();
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
<style lang="scss" scoped>
.profile-image {
  border-radius: 50% !important;
  width: 128px;
  height: 128px;
  object-fit: cover;
}
</style>
