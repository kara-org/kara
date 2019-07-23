<template>
  <div>
    <nav
      class="navbar header is-white"
      role="navigation"
      aria-label="main navigation"
    >
    <div class="nav-container container">
      <div class="navbar-brand">
        <a
          class="navbar-item"
          href="/"
        >
          <img
            src="~assets/kara-negativo.png"
            alt="Buefy"
            height="28"
          >
        </a>

        <div class="navbar-burger">
          <span />
          <span />
          <span />
        </div>
      </div>
      <div class="navbar-menu">
        <div class="navbar-start">
          <a
              class="navbar-item"
              v-for="(item, key) of items"
              :key="key"
            >
              <nuxt-link
                :to="item.to"
                exact-active-class="is-active"
              >
                <b-icon :icon="item.icon" /> {{ item.title }}
              </nuxt-link>
            </a>
        </div>
        <div class="navbar-end">
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
      </div>
    </div>

    </nav>

    <section class="main-content">
        <nuxt />
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          title: 'Home',
          icon: 'home',
          to: { name: 'index' }
        },
        {
          title: 'Inspire',
          icon: 'lightbulb',
          to: { name: 'inspire' }
        }
      ]
    }
  }
}
</script>

<style lang="scss">

.navbar {
  color: $primary;

  .navbar-brand {
    padding: 10px
  }
  

  &::after {
    background: linear-gradient(-87deg, rgba(26,188,156, 0.8) 0%,  rgba(46,204,113,0.8) 100%);
    bottom: 0;
    content: '';
    height: 3px;
    position: absolute;
    width: 100%;
  }
}
</style>
