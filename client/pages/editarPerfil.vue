<template>
<div class="columns is-fullheight">
  <MenuLateral :isDoador="!this.$auth.user.vinculo_ong" />
  <section class="column is-main-content hero is-medium is-bold" style="align-items:center;">
    <div class="hero-body">
      <article class="card is-rounded" style="width:600px">
        <div class="card-content">
          <p class="form-section-title">Edite suas informações</p>
          <CadastroDoadorForm :isCadastro="false" />
        </div>
      </article>
    </div>
  </section>
</div>
</template>

<script>
import CadastroDoadorForm from '@/components/organisms/CadastroDoadorForm'
import MenuLateral from '@/components/organisms/MenuLateral'
export default {
  layout: 'default',
  components: {
    CadastroDoadorForm,
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
