<template>
  <div class="columns  has-background-primary is-paddingless">
    <PerfilONG class="column is-one-fifth" />
    <div class="column is-three-fifth has-text-white">
      <br>
      <p class="is-size-5 has-text-weight-bold has-text-centered">Outras demandas dessa ONG</p>
      <p class="has-text-weight-white has-text-centered"><small>Você pode adicionar outros produtos para sua doação</small></p>
      <br>
      <ListagemCards :list="list" class="is-scroll-y" :isBusca="false" />
    </div>
    <CarrinhoONG class="column is-one-fifth" />
  </div>
</template>

<script>

import PerfilONG from '../components/organisms/ColunmPerfilONG'
import ListagemCards from '../components/organisms/ListagemCards'
import CarrinhoONG from '../components/organisms/ColunmCarrinhoONG'

export default {
  components: {
    PerfilONG,
    ListagemCards,
    CarrinhoONG
  },
  data() {
    return {}
  },
  computed: {
    list () {
      return this.$store.state.carrinho.ong.itens
    }
  },
}
</script>

<style lang="scss">
.columns {
  margin: 5px;
}
</style>
