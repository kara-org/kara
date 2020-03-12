<template>
  <span>
    <b-tooltip class="is-success" label="Editar doação" position="is-right">
      <b-button @click="isComponentModalActive = true" class="is-outlined is-success is-small">
        <b-icon icon="settings"></b-icon>
      </b-button>
    </b-tooltip>
    <b-modal :active.sync="isComponentModalActive" has-modal-card>
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Edição de Doação</p>
          </header>
          <section class="modal-card-body">
            <b-field label="Quantidade">
              <b-input type="number" v-model="quantidade" placeholder="Quantidade a doar" required></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button" type="button" @click="isComponentModalActive = false">Cancelar</button>
            <button class="button is-primary" @click="confirm()">Confirmar</button>
          </footer>
        </div>
      </form>
    </b-modal>
  </span>
</template>

<script>
export default {
  props: { doacao: Object },
  data() {
    return {
      isComponentModalActive: false,
      quantidade: null
    }
  },
  mounted() {
    this.quantidade = this.doacao.quantidade_prometida

  },
  methods: {
    async confirm() {
      if (this.quantidade && this.quantidade > 0) {
        console.log(
          await this.$axios.$patch(`/item/${this.doacao.id}/`, {
            quantidade_prometida: this.quantidade
          })
        )
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
