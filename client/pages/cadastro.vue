<template>
  <div>

    <div class="tabs is-centered is-toggle is-toggle-rounded">
      <ul>
<<<<<<< HEAD
        <li @click="doador = true" :class="doador ? 'is-active' : 'is-d'">
=======
        <li @click="isDoador = true" :class="isDoador ? 'is-active' : 'is-d'">
>>>>>>> d78a4427b1576989999991981258c61b76a4a967
          <a>
            <span>SOU DOADOR</span>
          </a>
        </li>
<<<<<<< HEAD
        <li @click="doador = false" :class="!doador ? 'is-active' : 'is-d'">
=======
        <li @click="isDoador = false" :class="!isDoador ? 'is-active' : 'is-d'">
>>>>>>> d78a4427b1576989999991981258c61b76a4a967
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
<<<<<<< HEAD
                <h1 class="title">
                  <img class="logo" src="~assets/kara-negativo.png" alt="logo" width="400" />
                </h1>
                <hr />
                <CadastroDoadorForm v-if="doador" />
=======
                <CadastroDoadorForm v-if="isDoador" />
>>>>>>> d78a4427b1576989999991981258c61b76a4a967
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
<<<<<<< HEAD
      doador: true
=======
      isDoador: true
>>>>>>> d78a4427b1576989999991981258c61b76a4a967
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
