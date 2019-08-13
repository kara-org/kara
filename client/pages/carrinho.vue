<template>
  <div class="columns">
    <PerfilONG class="column is-one-fifth" />
    <ListagemONG class="column auto" />
    <CarrinhoONG class="column is-one-fifth" />
  </div>
</template>

<script>
import PerfilONG from '../components/organisms/ColunmPerfilONG'
import ListagemONG from '../components/organisms/ColunmListagemONG'
import CarrinhoONG from '../components/organisms/ColunmCarrinhoONG'
export default {
  components: {
    PerfilONG,
    ListagemONG,
    CarrinhoONG
  },
  data() {
    return {}
  }
}
</script>

<style lang="scss">
.columns:last-child {
  margin: auto;
}
</style>
