<template>
  <article class="has-background-white">
    <h1 class="title is-size-5 has-text-centered">Demandas selecionadas</h1>
    <b-button
      @click="send"
      class="is-primary is-fullwidth is-rounded is-stick-botton"
      size="is-medium"
      fullwidth="true"
      icon="magnify"
      >Finalizar doação</b-button
    >
    <br />
    <div class="columns">
      <p v-if="demandas && demandas.length == 0">
        Demandas aparecerão aqui a medida que você for selecionando.
      </p>
    </div>
    <div class="cards is-scroll-y">
      <div v-for="item in demandas" :key="item.objectId" class="column is-full">
        <CardDemanda
          :demanda="item.demanda"
          :ong="ong"
          :isCarrinho="true"
          :quantidadePrometida="item.quantidadePrometida"
        />
      </div>
    </div>
  </article>
</template>

<script>
import CardDemanda from '../molecules/CardDemanda';
import { mapGetters, mapActions } from 'vuex';

export default {
  components: {
    CardDemanda
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters({ demandas: 'carrinho/itensNoCarrinho', ong: 'carrinho/ong' })
  },
  methods: {
    ...mapActions('carrinho', ['sendDoacao']),
    send() {
      this.sendDoacao()
        .then(() => {
          this.$buefy.toast.open({
            message: 'Obrigado pela doação!',
            type: 'is-success',
            position: 'is-top'
          });
          this.$router.push(`/doador/contato/${this.ong.objectId}`);
        })
        .catch(err => {
          if (err.code === 142)
            err.message = 'É necessário estar logado para realizar uma doação';
          console.log(err.message);
          this.$buefy.toast.open({
            message: err.message,
            type: 'is-danger',
            position: 'is-bottom'
          });
        });
    }
  }
};
</script>

<style lang="css" scoped>
.is-stick-botton{
  position: sticky;
  bottom: 0;
}
</style>
