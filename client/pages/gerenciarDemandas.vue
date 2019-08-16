<template>
<body class="columns is-fullheight">
  <MenuLateral />
  <section class="column is-main-content hero is-medium is-bold">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <article class="card is-rounded" style="width:800px">
            <div class="card-content">
              <p class="form-section-title">Demandas da ONG</p>
              <hr />
              <ListaDemandas />
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</body>
</template>

<script>
import ListaDemandas from '@/components/organisms/ListaDemandas'
import MenuLateral from '@/components/organisms/MenuLateral'

export default {
  layout: 'default',
  components: {
    ListaDemandas,
    MenuLateral
  }
}
</script>

<style lang="scss" scoped>
.hero-body {
  padding-top: 1em !important;
}
body {
  margin: 10px !important;
}
</style>
