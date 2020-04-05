<template>
  <span>
    <b-tooltip class="is-success" label="Editar demanda" position="is-right">
      <b-button @click="isComponentModalActive = true" class="is-outlined is-success is-small">
        <b-icon icon="apps"></b-icon>
      </b-button>
    </b-tooltip>
    <b-modal :active.sync="isComponentModalActive" has-modal-card>
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Edição de Demanda</p>
          </header>
          <section class="modal-card-body">
            <b-field label="Título">
              <b-input type="text" v-model="demandaLocal.nome" placeholder="Açucar"></b-input>
            </b-field>
            <b-field label="Quantidade esperada">
              <b-input
                type="number"
                step="0.01"
                v-model="demandaLocal.quantidadeDesejada"
                placeholder="Quantidade esperada"
              ></b-input>
            </b-field>
            <b-field label="Quantidade alcançada">
              <b-input
                type="number"
                step="0.01"
                v-model="demandaLocal.quantidadeAlcancada"
                placeholder="Quantidade alcançada"
              ></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button is-primary is-fullwidth" @click="confirm">Confirmar</button>
          </footer>
        </div>
      </form>
    </b-modal>
  </span>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  props: { demanda: Object },
  data() {
    return {
      isComponentModalActive: false,
      demandaLocal: {
        nome: "",
        quantidadeAlcancada: 0,
        quantidadeDesejada: 0
      }
    };
  },
  async asyncData() {
    this.demandaLocal = JSON.parse(JSON.stringify(this.demanda));

  },
  methods: {
    ...mapActions('demandas', {
      changeDemanda: 'changeDemanda'
    }),
    async confirm() {
      console.log(this.demandaLocal)
      this.changeDemanda(this.demandaLocal)
    }
  }
};
</script>

<style scoped lang="scss">
.modal-card-body {
  text-align: initial;
}
</style>
