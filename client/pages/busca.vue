<template>
  <div>
    <section class="hero is-degrade-primary">
      <div class="hero-body banner">
        <div class="container">
          <Buscar />
        </div>
      </div>
    </section>
    <section class="hero">
      <div class="hero-body">
        <div class="container">
          <h1 class="title is-4">Demandas</h1>
          <div class="level">
            <ListagemOngs />
          </div>
        </div>
      </div>
    </section>
    <section></section>
  </div>
</template>

<script>
import ListagemOngs from '../components/organisms/ListagemCards'
import Buscar from '../components/molecules/BuscarForm'

export default {
  name: 'HomePage',
  components: {
    ListagemOngs,
    Buscar
  },
  created: function() {}
}
</script>
<style>
</style>
