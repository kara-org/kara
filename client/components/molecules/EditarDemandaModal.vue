<template>
  <span>
    <a @click="isComponentModalActive = true">
      <b-tooltip class="is-success" label="Editar demanda" position="is-right">
        <b-icon class="button is-medium is-outlined is-success" icon="settings"></b-icon>
      </b-tooltip>
    </a>
    <b-modal :active.sync="isComponentModalActive" has-modal-card>
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Edição de Demanda</p>
          </header>
          <section class="modal-card-body">
            <b-field label="Nome">
              <b-input type="text" v-model="nome" placeholder="Açucar" required></b-input>
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
      quantidade: 1,
      nome: '',
      categoria: '',
      dataInicio: '',
      dataFim: ''
    }
  },
  mounted() {
    this.quantidade = this.demanda.quantidade
    this.nome = this.demanda.nome
    this.categoria = this.demanda.categoria
    this.dataInicio = this.demanda.dataInicio
    this.dataFim = this.demanda.dataFim
  },
  methods: {
    confirm() {
      if (this.quantidade > 0) {
        this.demanda.quantidade = this.quantidade
        this.demanda.esperado = this.quantidade
      }
      if (!this.nome) {
        this.demanda.nome = this.nome
      }
      if (!this.categoria) {
        this.demanda.categoria = this.categoria
      }
      if (!this.dataInicio) {
        this.demanda.dataInicio = this.dataInicio
      }
      if (!this.dataFim) {
        this.demanda.dataFim = this.dataFim
      }
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