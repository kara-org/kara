<template>
<body class="columns is-fullheight">
  <MenuLateral />
  <section class="column is-main-content hero is-medium is-bold" v-if="isAuthenticated">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <article class="card is-rounded" style="width:600px">
            <div class="card-content">
              <p class="form-section-title">Edite suas informações</p>
              <CadastroDoadorForm :isCadastro="false" />
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</body>
</template>

<script>
import CadastroDoadorForm from '@/components/organisms/CadastroDoadorForm'
import CadastroOngForm from '@/components/organisms/CadastroOngForm'
import MenuLateral from '@/components/organisms/MenuLateral'
export default {
  layout: 'default',
  components: {
    CadastroDoadorForm,
    CadastroOngForm,
    MenuLateral
  },
  computed: {
    isAuthenticated() {
      return this.$auth.loggedIn
    },
    user() {
      return this.$auth.user
    }
  }
}
</script>

<style lang="scss" scoped>
.hero-body {
  padding-top: 2em !important;
}
body {
  margin: 10px !important;
}
</style>
