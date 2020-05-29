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
          <h2 class="title is-4  has-text-centered is-primary">ONGs</h2>
          <p class="has-text-centered">
            <small
              >Busque por itens, caso não encontre, veja nossas sugestões abaixo
            </small>
          </p>
          <div class="container">
            <div class="columns is-desktop">
              <div
                v-for="item in list"
                :key="item.objectId"
                class="column"
                :class="'is-one-third is-full-mobile'"
              >
                <CardOng :ong="item" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section></section>
  </div>
</template>

<script>
import CardOng from '../components/molecules/CardOng';
import Buscar from '../components/molecules/BuscarForm';
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'HomePage',
  components: {
    CardOng,
    Buscar
  },
  computed: {
    ...mapGetters({ list: 'busca/list' })
  },
  methods: {
    ...mapActions('busca', ['fetchBuscaOng'])
  },
  created: function() {
    this.fetchBuscaOng();
  }
};
</script>
<style>
.columns {
  display: flex;
  flex-wrap: wrap;
  margin: 10px !important;
}
.columns .column {
  padding: 5px;
}
</style>
