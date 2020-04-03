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
            <h1 class="title is-4  has-text-centered is-primary">Demandas</h1>
            <p class="has-text-centered"><small >Busque por itens, caso não encontre, veja nossas sugestões abaixo </small></p>
            <ListagemCards :list="list" :isBusca="true"/>
        </div>
      </div>
    </section>
    <section></section>
  </div>
</template>

<script>
import ListagemCards from '../components/organisms/ListagemCards'
import Buscar from '../components/molecules/BuscarForm'
import { mapActions } from 'vuex';

export default {
  name: 'HomePage',
  components: {
    ListagemCards,
    Buscar
  },
  computed: {
    list (){
      return this.$store.state.busca.list
    }
  },
  methods: {
    ...mapActions('carrinho', ['limparCarrinho'])
  },
  mounted: function() {
    this.limparCarrinho()
  }
}
</script>
<style>
</style>
