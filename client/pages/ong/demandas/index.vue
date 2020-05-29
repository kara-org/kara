<template>
  <div class="columns is-fullheight">
    <MenuLateral />
    <section class="column is-main-content hero is-medium is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <article class="card is-rounded" style="width:800px">
              <div class="card-content">
                <p class="form-section-title">Demandas da ONG</p>
                <hr />
                <ListaDemandas :demandas="demandas" />
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

import ListaDemandas from '@/components/organisms/ListaDemandas';
import MenuLateral from '@/components/organisms/MenuLateral';

export default {
  middleware: 'auth',
  layout: 'default',
  components: {
    ListaDemandas,
    MenuLateral
  },
  computed:{
    ...mapGetters({ demandas: 'demandas/demandas', user: 'login/usuario' })
  },
  methods: {
    ...mapActions('demandas', [
      'fetchDemandasOng',
      'changeDemanda',
      'deleteDemanda'
    ])
  },
  async mounted (){
    this.fetchDemandasOng(this.user.objectId)
  }
};
</script>

<style lang="scss" scoped>
.hero-body {
  padding-top: 1em !important;
}
.columns div {
  margin: 10px !important;
}
</style>
