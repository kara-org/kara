<template>
  <section>
    <form v-if="!success" @submit.prevent="validateBeforeSubmit" method="post">
      <hr />
      <b-field
        label="Título"
        :type="{'is-danger': errors.has('titulo')}"
        :message="errors.first('titulo')"
      >
        <b-input type="text" v-model.trim="demanda.nome" name="titulo" v-validate="'required'"></b-input>
      </b-field>
      <b-field
        label="Categoria"
        :type="{'is-danger': errors.has('categoria')}"
        :message="errors.first('categoria')"
      >
        <b-select
          v-model="demanda.categoria"
          placeholder="Selecione uma categoria"
          name="categoria"
          v-validate="'required'"
        >
          <option :value="'Alimentos'">Alimentos</option>
          <option :value="'Roupas'">Roupas</option>
          <option :value="'Utilitários'">Utilitários</option>
        </b-select>
      </b-field>
      <b-field
        label="Quantidade"
        :type="{'is-danger': errors.has('quantidade')}"
        :message="errors.first('quantidade')"
      >
        <b-numberinput
          v-model.number="demanda.quantidadeDesejada"
          name="quantidade"
          min="1"
          v-validate="'required'"
        ></b-numberinput>
      </b-field>
      <hr />
      <button
        type="submit"
        class="button is-primary is-outlined is-medium is-rounded is-fullwidth"
      >Confirmar</button>
    </form>
    <div v-else class="column has-text-centered">
      <hr />
      <h1>Demanda cadastrada com successo.</h1>
      <hr />
      <div class="column has-text-centered">
        <button
          @click="success = false"
          class="button is-primary is-outlined is-medium is-rounded"
        >Voltar</button>
      </div>
    </div>
  </section>
</template>

<script>
import cleave from '@/plugins/cleave-directive.js';
import { mapActions, mapMutations } from 'vuex';
export default {
  props: {
    isCadastro: Boolean
  },
  data() {
    return {
      demanda: {
        categoria: null,
        nome: null,
        quantidadeDesejada: null,
        ong: null
      },
      success: false
    };
  },
  computed: {
    ong() {
      return this.$store.state.login.usuario.ong;
    }
  },
  methods: {
    ...mapMutations('demandas', ['SET_DEMANDA']),
    ...mapActions('demandas', ['createDemanda', 'updateDemanda']),
    async create() {
      this.demanda.ong = this.ong;
      let method;

      if (this.isCadastro) {
        method = this.createDemanda;
      } else {
        method = this.updateDemanda;
      }

      method({ ...this.demanda })
        .then(response => {
          this.$buefy.toast.open({
            message: 'Operação realizada com successo!',
            type: 'is-success',
            position: 'is-top'
          });
          this.success = true;
        })
        .catch(err => {
          console.log(err);
          if (!err.response) {
            err.message = 'Servidor desconectado';
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
    },
    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.create();
          return;
        }
        this.$buefy.toast.open({
          message: 'Formulário inválido, verifique os campos em vermelho',
          type: 'is-danger',
          position: 'is-bottom'
        });
      });
    }
  },
  created() {
    this.unsubscribe = this.$store.subscribe((mutation, state) => {
      if (mutation.type === 'demandas/SET_DEMANDA') {
        this.demanda = JSON.parse(JSON.stringify(state.demandas.demanda));
      }
    });
  },
  beforeDestroy() {
    this.unsubscribe();
  }
};
</script>
