<template>
  <div>
    <section class="hero is-degrade-primary">
      <div class="hero-body banner">
        <div class="container">
          <Buscar />
        </div>
      </div>
    </section>
    <section class="hero is-fullheight">
      <div class="hero-head">
        <div class="container">
          <h2 class="title is-4  has-text-centered is-primary">Demandas</h2>
          <p class="has-text-centered">
            <small
              >Busque por itens, caso não encontre, veja nossas sugestões abaixo
            </small>
          </p>
          <ListagemCards :list="list" :isBusca="true" />
        </div>
      </div>
    </section>
    <section></section>
  </div>
</template>

<script>
import ListagemCards from '../components/organisms/ListagemCards';
import Buscar from '../components/molecules/BuscarForm';
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'HomePage',
  components: {
    ListagemCards,
    Buscar
  },
  created() {
    this.fetchBusca();
  },
  computed: {
    ...mapGetters({ list: 'busca/list' })
  },
  methods: {
    ...mapActions('busca', ['fetchBusca']),
    ...mapActions('carrinho', ['limparCarrinho'])
  },
  mounted: function() {
    this.limparCarrinho();
  }
};
</script>
<style></style>
