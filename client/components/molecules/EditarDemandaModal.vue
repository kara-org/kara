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
              <b-input type="text" v-model="titulo" placeholder="Açucar"></b-input>
            </b-field>
            <b-field label="Quantidade esperada">
              <b-input type="number" step="0.01" v-model="quantidade_solicitada" placeholder="Quantidade esperada"></b-input>
            </b-field>
            <b-field label="Quantidade alcançada">
              <b-input type="number" step="0.01" v-model="quantidade_alcancada" placeholder="Quantidade alcançada"></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button is-primary is-fullwidth" @click="confirm()">Confirmar</button>
          </footer>
        </div>
      </form>
    </b-modal>
  </span>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  props: { demanda: Object },
  data() {
    return {
      isComponentModalActive: false,
      quantidade_alcancada: null,
      quantidade_solicitada: null,
      titulo: null
    }
  },
  mounted() {
    this.titulo = this.demanda.descricao
    this.quantidade_solicitada = this.demanda.quantidade_solicitada
    this.quantidade_alcancada = this.demanda.quantidade_alcancada
  },
  methods: {
    async confirm() {
      this.$axios.$patch(`/demanda/${this.demanda.id}/`, {
        quantidade_solicitada: this.quantidade_solicitada,
        quantidade_alcancada: this.quantidade_alcancada,
        descricao: this.titulo
      })
      this.isComponentModalActive = false
    }
  }
}
</script>

<style scoped lang="scss">
.modal-card-body {
  text-align: initial;
}
</style>