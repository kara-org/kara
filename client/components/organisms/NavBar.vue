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
            src="~assets/kara-logo.svg"
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
          <LoginNavItem />
        </div>
      </div>
    </div>
    </nav>
  </div>
</template>
<script>
import LoginNavItem from '../molecules/LoginNavItem'
export default {
  components: {
    LoginNavItem
  },
  props: ['items'],
  asyncData () {
    return {

    }
  }
}
</script>
