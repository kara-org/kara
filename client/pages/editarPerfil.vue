<template>
  <section class="hero is-medium is-bold" v-if="isAuthenticated">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <article class="card is-rounded" style="width:600px">
            <div class="card-content">
              <p class="form-section-title">Edite suas informações</p>
              <hr />
              <CadastroDoadorForm :isCadastro="false" v-if="user.vinculo_ong" />
              <CadastroOngForm :isCadastro="false" v-else />
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import CadastroDoadorForm from '@/components/organisms/CadastroDoadorForm'
import CadastroOngForm from '@/components/organisms/CadastroOngForm'
import { mapGetters } from 'vuex'
export default {
  layout: 'default',
  components: {
    CadastroDoadorForm,
    CadastroOngForm
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
  padding-top: 8rem !important;
}
</style>
