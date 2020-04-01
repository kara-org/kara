<template>
  <b-menu class="column is-2 is-hidden-mobile">
    <b-menu-list label="Doador">
      <b-menu-item icon="account" label="Perfil" tag="router-link" to="/doador/editar"></b-menu-item>
      <b-menu-item icon="receipt" label="Minhas Doações" tag="router-link" to="/doador/doacoes"></b-menu-item>
    </b-menu-list>
    <b-menu-list v-if="!isDoador" label="ONG">
      <b-menu-item icon="group" label="Perfil" tag="router-link" to="/ong/editar"></b-menu-item>
      <b-menu-item
        v-if="!isDoador"
        icon="plus"
        label="Cadastrar Demanda"
        tag="router-link"
        to="/ong/demandas/cadastro"
      ></b-menu-item>
      <b-menu-item
        v-if="!isDoador"
        icon="receipt"
        label="Demandas"
        tag="router-link"
        to="/ong/demandas"
      ></b-menu-item>
      <b-menu-item icon="receipt" label="Doações" tag="router-link" to="/ong/doacoes"></b-menu-item>
    </b-menu-list>
  </b-menu>
</template>
<script>
export default {
  computed: {
    isDoador() {
      return !this.$store.state.login.usuario.ong
    }
  }
}
</script>
