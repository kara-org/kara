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
              <b-numberinput v-model.number="quantidade" name="quantidade" required></b-numberinput>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button" type="button" @click="isComponentModalActive = false">Cancelar</button>
            <button class="button is-primary" type="button" @click="confirm">Confirmar</button>
          </footer>
        </div>
      </form>
    </b-modal>
  </span>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  props: { doacao: Object },
  data() {
    return {
      isComponentModalActive: false,
      quantidade: 1.0
    };
  },
  computed: {
    ...mapGetters({ user: 'login/usuario' })
  },
  mounted() {
    this.quantidade = this.doacao.quantidadePrometida;
  },
  methods: {
    ...mapActions('doacoes', ['changeItemDoacao', 'fetchDoacoesDoador']),
    async confirm() {
      if (this.quantidade && this.quantidade > 0) {
        await this.changeItemDoacao({
          objectId: this.doacao.objectId,
          quantidadePrometida: this.quantidade
        });
        await this.fetchDoacoesDoador(this.user.objectId);
      }
      this.isComponentModalActive = false;
    }
  }
};
</script>

<style scoped lang="scss">
.modal-card-body {
  text-align: initial;
}
</style>
