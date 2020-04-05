<template>
  <div class="columns has-margin is-fullheight">
    <MenuLateral />
    <section class="column is-main-content hero is-medium is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns has-no-margin is-centered">
            <article class="card is-rounded" style="width:300px">
              <div class="card-content">
                <p class="form-section-title">Cadastre uma demanda</p>
                <CadastroDemandaForm :demanda="demanda" :isCadastro="false" />
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import CadastroDemandaForm from '@/components/organisms/CadastroDemandaForm';
import MenuLateral from '@/components/organisms/MenuLateral';

export default {
  layout: 'default',
  components: {
    CadastroDemandaForm,
    MenuLateral
  },
  methods: {
    ...mapActions('demandas', {
      fetchDemanda: 'fetchDemanda'
    })
  },
  computed: {
    ...mapGetters({ demanda: 'demandas/demanda' })
  },
  mounted() {
    this.fetchDemanda(this.$route.params.id);
  }
};
</script>

<style lang="scss" scoped>
.hero-body {
  padding-top: 1em !important;
}
.has-margin {
  margin: 10px;
}
</style>
