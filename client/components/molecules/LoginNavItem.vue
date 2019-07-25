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
        <nuxt-link class="button is-primary is-rounded" to="/cadastro" exact-active-class="is-active">
          <!-- <b-icon :icon="item.icon" /> {{ item.title }} -->
          Cadastre-se
        </nuxt-link>
      </div>
    </div>
    <div class="perfil-auth navbar-item media" v-else >
      <figure class="image media-left is-32x32">
        <img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
      </figure>
      <div class="media-content">
        <strong>John Smith</strong> <small>@johnsmith</small>
      </div>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    data () {
      return {
        user: {}
      }
    },
    computed: {
      isAuthenticated () {
        return this.$auth.loggedIn
      },
      user () {
        return this.$auth.user
      }
    },
}
</script>
