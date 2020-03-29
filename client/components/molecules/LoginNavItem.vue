<template>
  <div>
    <div class="buttons-auth" v-show="!isAuthenticated">
      <div class="navbar-item">
        <nuxt-link
          class="button is-primary is-outlined is-rounded"
          to="/auth/login"
          exact-active-class="is-active"
        >Entrar</nuxt-link>
      </div>
      <div class="navbar-item">
        <nuxt-link
          class="button is-primary is-rounded"
          to="/auth/cadastro"
          exact-active-class="is-active"
        >
          <!-- <b-icon :icon="item.icon" /> {{ item.title }} -->
          Cadastre-se
        </nuxt-link>
      </div>
    </div>
    <div class="perfil-auth navbar-item media" v-show="isAuthenticated">
      <figure class="image media-left is-32x32">
        <img class="is-rounded" :src="isAuthenticated ? user.foto : null" />
      </figure>
      <div class="media-content">
        <span>
          <small>Bem vindo!</small>
        </span>
        <span>
          <strong>{{ userName }}</strong>
        </span>
      </div>
      <div class="navbar-item" />
      <div class="navbar-item" v-show="vinculoOng">
        <nuxt-link
          class="button is-primary is-outlined is-rounded"
          :to="`/ong/demandas`"
          exact-active-class="is-active"
        >Gerenciamento</nuxt-link>
      </div>
      <div class="navbar-item" v-show="!vinculoOng">
        <nuxt-link
          class="button is-primary is-outlined is-rounded"
          :to="`/doador/editar`"
          exact-active-class="is-active"
        >Perfil</nuxt-link>
      </div>
      <div class="media-right">
        <a href="#" class="nav-link" @click="logout">sair</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      return this.$auth.loggedIn
    },
    user() {
      return this.$auth.user
    },
    userName() {
      return this.isAuthenticated ? this.user.nome_completo.split(' ')[0] : null
    },
    vinculoOng() {
      return this.isAuthenticated ? this.user.vinculo_ong : null
    }
  },
  methods: {
    logout: function() {
      this.$buefy.dialog.confirm({
        message: 'Deseja mesmo sair?',
        confirmText: 'Sim',
        onConfirm: () => {
          this.$auth.logout()
          this.$router.push('/')
          this.$buefy.toast.open('Logout realizado com sucesso')
        }
      })
    }
  },
}
</script>

<style lang="scss">
.buttons-auth {
  display: flex;
  height: 100%;
}
.perfil-auth {
  img {
    width: auto;
  }

  .media-content {
    display: flex;
    flex-direction: column;
  }
}
</style>

