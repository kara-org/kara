<template>
  <section>
    <form v-if="!success" @submit.prevent="validateBeforeSubmit" method="post">
      <h1 class="title is-5 has-text-centered">Dados da ONG</h1>
      <b-field
        label="Nome da ong"
        :type="{'is-danger': errors.has('nome_da_ong')}"
        :message="errors.first('nome_da_ong')"
      >
        <b-input
          type="text"
          v-model.trim="ong.nome_da_ong"
          name="nome_da_ong"
          v-validate="'required'"
        ></b-input>
      </b-field>
      <hr />
      <h1 class="title is-5 has-text-centered">Responsável</h1>
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
import { mapActions } from 'vuex';

export default {
  props: {
    isCadastro: Boolean,
    isDoador: Boolean
  },
  data() {
    return {
      ong: {
        nome_da_ong: null
      },
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
      }
    };
  },

  mounted() {},

  created() {
    if (!this.isCadastro) {
      this.usuario = this.$store.state.login.usuario;
    }
  },

  methods: {
    ...mapActions({ signUpParse: 'login/signUp', updateParse: 'login/update' }),
    async register() {
      try {
        await this.signUpParse({
          email: this.usuario.email,
          password: this.usuario.password,
          nome: this.usuario.nome,
          telefones: this.usuario.telefones,
          nomeDaOng: this.nome_da_ong
        })
          .then(response => {
            this.$buefy.toast.open({
              message: 'Cadastro realizado com successo!',
              type: 'is-success',
              position: 'is-top'
            });
            this.$router.push('/auth/login');
          })
          .catch(err => {
            console.log(err);
            if (!err.response) {
              err.message = 'Servidor desconectado';
            } else if (err.code === 202) {
              err.message = 'Usuário com este email já existe';
            } else if (err.code === 101) {
              if (err.response.data.non_field_errors)
                err.message = err.response.data.non_field_errors[0];
            }
            this.$buefy.toast.open({
              message: err.message,
              type: 'is-danger',
              position: 'is-bottom'
            });
          });
      } catch (e) {
        console.log(e);
        //this.error = e.response.data.message;
      }
    },

    async patch() {
      try {
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
            //console.error(this.errors)
            console.log(err);
            if (!err.response) {
              err.message = 'Servidor desconectado';
            } else if (err.response.data.mensagem.email != null) {
              err.message = 'Usuário com este email já existe';
            } else if (err.response.status === 400) {
              if (err.response.data.non_field_errors)
                err.message = err.response.data.non_field_errors[0];
            }
            this.$buefy.toast.open({
              message: err.message,
              type: 'is-danger',
              position: 'is-bottom'
            });
          });
        this.success = true;
      } catch (e) {
        console.log(e);
        //this.error = e.response.data.message;
      }
    },

    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.usuario.telefones[0] = this.usuario.telefones[0].replace(
            /\D/g,
            ''
          );
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
