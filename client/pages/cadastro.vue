<template>
  <div>
    <div class="tabs is-centered is-toggle is-toggle-rounded">
      <ul>
        <li @click="pessoaFisica = true" :class="pessoaFisica ? 'is-active' : 'is-d'">
          <a>
            <span>DOADOR</span>
          </a>
        </li>
        <li @click="pessoaFisica = false" :class="!pessoaFisica ? 'is-active' : 'is-d'">
          <a>
            <span>ONG</span>
          </a>
        </li>
      </ul>
    </div>
    <section class="hero is-medium is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <article class="card is-rounded" style="width:400px">
              <div class="card-content">
                <h1 class="title">
                  <img class="logo" src="~assets/kara-negativo.png" alt="logo" width="400" />
                </h1>
                <hr />
                <CadastroDoadorForm v-if="pessoaFisica" />
                <CadastroOngForm v-else />
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
      pessoaFisica: true
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
