<template>
  <div>

    <div class="tabs is-centered is-toggle is-toggle-rounded">
      <ul>
        <li @click="isDoador = true" :class="isDoador ? 'is-active' : 'is-d'">
          <a>
            <span>SOU DOADOR</span>
          </a>
        </li>
        <li @click="isDoador = false" :class="!isDoador ? 'is-active' : 'is-d'">
          <a>
            <span>SOU UMA ONG</span>
          </a>
        </li>
      </ul>
    </div>
    <section class="hero is-medium is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <article class="card is-rounded" style="width:600px">
              <div class="card-content">
                <p class="form-section-title">Crie uma conta {{isDoador ? 'para doador' : 'para ONG'}}</p>
                <CadastroDoadorForm :isCadastro="true" :isDoador="true" v-if="isDoador" />
                <CadastroOngForm :isCadastro="true" v-else />
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import CadastroDoadorForm from '@/components/organisms/CadastroDoadorForm'
import CadastroOngForm from '@/components/organisms/CadastroOngForm'

export default {
  layout: 'default',
  components: {
    CadastroDoadorForm,
    CadastroOngForm
  },
  data() {
    return {
      isDoador: true
    }
  }
}
</script>

<style lang="scss" scoped>
.tabs {
  padding-top: 8rem;
}
.hero-body {
  padding-top: 0rem !important;
}
.logo {
  padding: 10px 40px;
}
</style>
