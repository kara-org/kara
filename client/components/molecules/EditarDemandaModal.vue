<template>
  <span>
    <a @click="isComponentModalActive = true">
      <b-tooltip class="is-success" label="Editar demanda" position="is-right">
        <b-button class="is-outlined is-success is-small">
          <b-icon icon="settings"></b-icon>
        </b-button>
      </b-tooltip>
    </a>
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
            <b-field label="Quantidade">
              <b-input type="number" v-model="quantidade" placeholder="Quantidade esperada"></b-input>
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
      quantidade: null,
      titulo: null
    }
  },
  mounted() {
    this.titulo = this.demanda.descricao
    this.quantidade = this.demanda.quantidade_solicitada
  },
  methods: {
    async confirm() {
      this.$axios.$patch(`/demanda/${this.demanda.id}/`, {
        quantidade_solicitada: this.quantidade,
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