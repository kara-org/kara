<template>
  <div>
    <div class="buttons-auth" v-if="!isAuthenticated">
      <div class="navbar-item">
        <nuxt-link
          class="button is-primary is-outlined is-rounded"
          to="/login"
          exact-active-class="is-active"
        >
          <!-- <b-icon :icon="item.icon" /> {{ item.title }} -->
          Entrar
        </nuxt-link>
      </div>
      <div class="navbar-item">
        <nuxt-link
          class="button is-primary is-rounded"
          to="/cadastro"
          exact-active-class="is-active"
        >
          <!-- <b-icon :icon="item.icon" /> {{ item.title }} -->
          Cadastre-se
        </nuxt-link>
      </div>
    </div>
    <div class="perfil-auth navbar-item media" v-else>
      <figure class="image media-left is-32x32">
        <img class="is-rounded" :src="user.foto" />
      </figure>
      <div class="media-content">
        <span>
          <small>Bem vindo!</small>
        </span>
        <span>
          <strong>{{ userName }}</strong>
        </span>
      </div>
      <div class="media-right">
        <a href="#" class="nav-link" @click="logout">sair</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
     user: { nome_completo: '' }
    }
  },
  computed: {
    isAuthenticated() {
      return this.$auth.loggedIn
    },
    userName() {
      return this.user.nome_completo.split(' ')[0]
    }
  },
  methods: {
    logout: function() {
      this.$dialog.confirm({
        message: 'Deseja mesmo Sair?',
        confirmText: 'Sim',
        onConfirm: () => {
          this.$auth.logout()
          this.$router.push('/')
          this.$toast.open('Logout Realizado com sucesso')
        }
      })
    }
  },
  mounted () {
    this.user = this.$auth.user
  }
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

