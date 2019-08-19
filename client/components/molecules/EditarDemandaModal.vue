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
              <b-input type="text" v-model="titulo" placeholder="Açucar" required></b-input>
            </b-field>
            <b-field label="Categoria">
              <b-input type="text" v-model="categoria" placeholder="Alimentos" required></b-input>
            </b-field>
            <b-field label="Quantidade">
              <b-input type="number" v-model="quantidade" placeholder="Quantidade a doar" required></b-input>
            </b-field>
            <b-field label="Data de inicio">
              <b-input type="text" v-model="dataInicio" placeholder="15/08/2019" required></b-input>
            </b-field>
            <b-field label="Data de finalização">
              <b-input type="text" v-model="dataFim" placeholder="21/09/2019" required></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button" @click="isComponentModalActive = false">Cancelar</button>
            <button class="button is-primary" @click="confirm()">Confirmar</button>
          </footer>
        </div>
      </form>
    </b-modal>
  </span>
</template>

<script>
export default {
  props: { demanda: Object },
  data() {
    return {
      isComponentModalActive: false,
      quantidade: null,
      titulo: null,
      categoria: null,
      dataInicio: null,
      dataFim: null
    }
  },
  mounted() {
    this.quantidade = this.demanda.quantidade_solicitada
    this.titulo = this.demanda.descricao
    this.categoria = this.demanda.categoria
    this.dataInicio = this.demanda.data_inicio
    this.dataFim = this.demanda.data_fim
  },
  methods: {
    async confirm() {
      if (this.quantidade && this.quantidade > 0) {
        this.demanda.quantidade_solicitada = this.quantidade
      }
      if (this.titulo) {
        this.demanda.descricao = this.titulo
      }
      if (this.categoria) {
        this.demanda.categoria = this.categoria
      }
      if (this.dataInicio) {
        this.demanda.data_inicio = this.dataInicio
      }
      if (this.dataFim) {
        this.demanda.data_fim = this.dataFim
      }
      console.log(
        await this.$axios.$put(`/demanda/${this.demanda.id}/`, this.demanda)
      )
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