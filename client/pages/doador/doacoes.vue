<template>
  <div class="columns is-fullheight">
    <MenuLateral :isDoador="true" />
    <section class="column is-main-content hero is-medium is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <article class="card is-rounded" style="width:800px">
              <div class="card-content">
                <p class="form-section-title">Doações marcadas</p>
                <hr />
                <ListaDoacoes :isDoador="true" />
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import ListaDoacoes from '@/components/organisms/ListaDoacoes'
import MenuLateral from '@/components/organisms/MenuLateral'
export default {
  layout: 'default',
  components: {
    ListaDoacoes,
    MenuLateral
  },
}
</script>

<style lang="scss" scoped>
.hero-body {
  padding-top: 1em !important;
}
.columns div {
  margin: 10px !important;
}
</style>
