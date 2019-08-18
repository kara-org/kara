<template>
  <div class="columns">
    <PerfilONG class="column is-one-fifth" />
    <div class="column is-three-fifth">
      <h1 class="title is-5 has-text-centered">Demandas de Almir do Picolé</h1>
      <ListagemCards :isBusca="false" />
    </div>
    <CarrinhoONG class="column is-one-fifth" />
  </div>
</template>

<script>
import PerfilONG from '../components/organisms/ColunmPerfilONG'
import ListagemCards from '../components/organisms/ListagemCards.vue'
import CarrinhoONG from '../components/organisms/ColunmCarrinhoONG'
export default {
  components: {
    PerfilONG,
    ListagemCards,
    CarrinhoONG
  },
  data() {
    return {}
  }
}
</script>

<style lang="scss">
.columns {
  margin: 5px;
}
</style>
