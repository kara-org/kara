<template>
  <section>
    <button class="button is-primary is-medium" @click="isComponentModalActive = true">{{text}}</button>
    <b-modal :active.sync="isComponentModalActive" has-modal-card>
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Item Doação</p>
          </header>
          <section class="modal-card-body">
            <b-field label="Quantidade">
              <b-input type="number" :value="quantidade" placeholder="Quantidade a doar" required></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button" type="button" @click="isComponentModalActive = false">Cancelar</button>
            <button class="button is-primary"  type="button"  @click="confirmado">Confirmar</button>
          </footer>
        </div>
      </form>
    </b-modal>
  </section>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  props: {
    text: {
      type: String,
      required: true
    },
    idOng: {
      type: Number
    },
    item: {
      type: Object
    }
  },
  data() {
    return {
      isComponentModalActive: false,
      quantidade: 1
    }
  },
  computed:{
     ...mapGetters({ carrinhoVazio: 'carrinho/isEmpty' }),
  },
  methods: {
    ...mapActions('carrinho', ['fetchOng', 'adicionarItemNoCarrinho']),
    ...mapActions('busca', ['fetchOng', 'adicionarItemNoCarrinho']),
    confirmado () {
      this.isComponentModalActive = false
      this.fetchOng(1)
      this.adicionarItemNoCarrinho({ item: this.item, quantidade: this.quantidade })
      if (this.carrinhoVazio)

        this.$router.push('/carrinho')
    }
  }
}
</script>
