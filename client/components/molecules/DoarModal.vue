<template>
  <section>
    <b-tooltip
      v-if="text === 'Confirmar'"
      class="is-success"
      label="Confirmar doação"
      position="is-right"
    >
      <b-button class="is-success is-outlined is-small" @click="isComponentModalActive = true">
        <b-icon icon="check"></b-icon>
      </b-button>
    </b-tooltip>
    <button
      v-else
      class="button is-primary is-medium"
      @click="isComponentModalActive = true"
    >{{text}}</button>
    <b-modal :active.sync="isComponentModalActive" has-modal-card>
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Item Doação</p>
          </header>
          <section class="modal-card-body">
            <b-field label="Quantidade">
              <b-input
                type="number"
                min="0.5"
                step=".5"
                v-model="quantidade"
                placeholder="Quantidade a doar"
                required
              ></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button" type="button" @click="isComponentModalActive = false">Cancelar</button>
            <button class="button is-primary" type="button" @click="confirmado">Confirmar</button>
          </footer>
        </div>
      </form>
    </b-modal>
  </section>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  props: {
    text: {
      type: String,
      required: true
    },
    id: {
      type: Number
    },
    item: {
      type: Object
    },
    idOng: {
      type: Number
    }
  },
  data() {
    return {
      isComponentModalActive: false,
      quantidade: 1.0
    }
  },
  computed: {
    ...mapGetters({ carrinhoVazio: 'carrinho/isEmpty' })
  },
  methods: {
    ...mapActions('carrinho', ['fetchOng', 'adicionarItemNoCarrinho']),
    ...mapActions('doacoes', ['confirmaItemDoacao', 'fetchDoacoesOng']),
    confirmado() {
      if (this.text === 'Confirmar') {
        this.$axios
          .$post(`/item/${this.id}/confirmar/`, {
            quantidade_efetivada: this.quantidade
          })
          .then(response => {
            this.fetchDoacoesOng(this.idOng)
          })
      } else {
        this.fetchOng(this.idOng)
        this.adicionarItemNoCarrinho({
          demanda: this.item,
          quantidade_prometida: this.quantidade
        })
        if (this.carrinhoVazio) this.$router.push('/carrinho')
      }
      this.isComponentModalActive = false
    }
  }
}
</script>
