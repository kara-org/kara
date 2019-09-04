<template>
  <b-menu class="column is-2 is-hidden-mobile">
    <b-menu-list label="Perfil">
      <b-menu-item icon="account" label="Usuário" tag="router-link" to="/editarPerfil"></b-menu-item>
      <b-menu-item v-if="!isDoador" icon="group" label="ONG" tag="router-link" to="/editarOng"></b-menu-item>
    </b-menu-list>
    <b-menu-list label="Demandas">
      <b-menu-item
        v-if="!isDoador"
        icon="plus"
        label="Cadastrar Demanda"
        tag="router-link"
        to="/cadastroDemanda"
      ></b-menu-item>
      <b-menu-item
        v-if="!isDoador"
        icon="receipt"
        label="Demandas"
        tag="router-link"
        to="/gerenciarDemandas"
      ></b-menu-item>
      <b-menu-item icon="receipt" label="Doações" tag="router-link" to="/gerenciarDoacoes"></b-menu-item>
    </b-menu-list>
  </b-menu>
</template>
<script>
export default {
  computed: {
    isDoador() {
      return !this.$auth.user.vinculo_ong
    }
  }
}
</script>