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
            <nuxt-link
              class="navbar-item"
              v-for="(item, key) of items"
              :key="key"
              :to="item.to"
              exact-active-class="is-active"
            >
              <b-icon :icon="item.icon" /> {{ item.title }}
            </nuxt-link>
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
