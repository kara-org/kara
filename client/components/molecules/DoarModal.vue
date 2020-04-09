<template>
  <section>
    <b-tooltip
      v-if="text === 'Confirmar'"
      class="is-success"
      label="Confirmar doação"
      position="is-right"
    >
      <b-button
        class="is-success is-outlined is-small"
        @click="isComponentModalActive = true"
      >
        <b-icon icon="check"></b-icon>
      </b-button>
    </b-tooltip>
    <button
      v-else
      class="button is-primary is-medium"
      @click="isComponentModalActive = true"
    >
      {{ text }}
    </button>
    <b-modal :active.sync="isComponentModalActive" has-modal-card>
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Item Doação</p>
          </header>
          <section class="modal-card-body">
            <b-numberinput
              v-model.number="quantidade"
              name="quantidade"
              min="1"
              v-validate="'required'"
            ></b-numberinput>
          </section>
          <footer class="modal-card-foot">
            <button
              class="button"
              type="button"
              @click="isComponentModalActive = false"
            >
              Cancelar
            </button>
            <button class="button is-primary" type="button" @click="confirmado">
              Confirmar
            </button>
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
    item: {
      type: Object
    },
    idOng: {
      type: String
    }
  },
  data() {
    return {
      isComponentModalActive: false,
      quantidade: 1.0
    };
  },
  computed: {
    ...mapGetters({ carrinhoVazio: 'carrinho/isEmpty' })
  },
  methods: {
    ...mapGetters({ itensOng: 'busca/demandasPorOng' }),
    ...mapActions('carrinho', [
      'fetchOng',
      'fetchItens',
      'adicionarItemNoCarrinho',
      'alterarItemNoCarrinho'
    ]),
    ...mapActions('doacoes', ['confirmaItemDoacao', 'fetchDoacoesOng']),
    async confirmado() {
      if (this.text === 'Confirmar') {
        this.confirmaItemDoacao({
          objectId: this.item.objectId,
          quantidadeEfetivada: this.quantidade
        }).then(response => {
          this.fetchDoacoesOng(this.idOng);
        });
      } else if (this.text === 'Editar') {
        this.alterarItemNoCarrinho({
          demanda: this.item,
          quantidadePrometida: this.quantidade
        });
      } else {
        await this.fetchOng(this.item.ong.objectId);
        await this.fetchItens(this.itensOng()(this.item.ong.objectId));
        this.adicionarItemNoCarrinho({
          demanda: this.item,
          quantidadePrometida: this.quantidade
        });
        if (this.carrinhoVazio) this.$router.push('/carrinho');
      }
      this.isComponentModalActive = false;
    }
  }
};
</script>
