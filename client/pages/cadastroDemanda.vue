<template>
<div class="columns is-fullheight">
  <MenuLateral />
  <section class="column is-main-content hero is-medium is-bold">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <article class="card is-rounded" style="width:600px">
            <div class="card-content">
              <p class="form-section-title">Cadastre uma demanda</p>
              <CadastroDemandaForm :isCadastro="true" />
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</div>
</template>

<script>
import CadastroDemandaForm from '@/components/organisms/CadastroDemandaForm'
import MenuLateral from '@/components/organisms/MenuLateral'

export default {
  layout: 'default',
  components: {
    CadastroDemandaForm,
    MenuLateral
  }
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
