<template>
<body class="columns is-fullheight">
  <MenuLateral />
  <section class="column is-main-content hero is-medium is-bold" style="align-items:center;">
    <div class="hero-body">
      <article class="card is-rounded" style="width:600px">
        <div class="card-content">
          <p class="form-section-title">Edite os dados da ONG</p>
          <CadastroOngForm :isCadastro="false" />
        </div>
      </article>
    </div>
  </section>
</body>
</template>

<script>
import CadastroOngForm from '@/components/organisms/CadastroOngForm'
import MenuLateral from '@/components/organisms/MenuLateral'
export default {
  layout: 'default',
  components: {
    CadastroOngForm,
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
