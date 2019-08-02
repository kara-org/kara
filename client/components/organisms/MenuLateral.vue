<template>
  <b-menu>
    <b-menu-list label="Menu">
      <b-menu-item icon="information-outline" label="Dashboard" tag="router-link" to="/dashboard"></b-menu-item>
      <b-menu-item icon="information-outline" label="Doações" tag="router-link" to="/doacoes"></b-menu-item>
      <b-menu-item icon="information-outline" label="Demandas" tag="router-link" to="/demandas"></b-menu-item>
      <b-menu-item icon="account" label="Meus dados" tag="router-link" to="/perfil/edit"> </b-menu-item>
    </b-menu-list>
    <b-menu-list>
      <b-menu-item label="Expo" icon="link" tag="router-link" to="/expo"></b-menu-item>
    </b-menu-list>
    <b-menu-list label="Actions">
      <b-menu-item label="Logout"></b-menu-item>
    </b-menu-list>
  </b-menu>
</template>
