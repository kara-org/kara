<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <nuxt-link class="navbar-item" to="/" exact-active-class="is-active">
        <img src="~assets/kara-logo.svg" alt="kara" />
      </nuxt-link>
      <a role="button" class="navbar-burger" aria-label="menu" data-target="navMenu" aria-expanded="false">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu" id="navMenu">
      <div class="navbar-start">
        <nuxt-link
          v-for="(item, key) of items"
          :key="key"
          class="navbar-item"
          :to="item.to"
          exact-active-class="is-active"
        >
          <!-- <b-icon :icon="item.icon" /> -->
          {{ item.title }}
        </nuxt-link>
      </div>
      <div class="navbar-end">
        <LoginNavItem />
      </div>
    </div>
  </nav>
</template>
<script>
import LoginNavItem from '../molecules/LoginNavItem'
export default {
  props: ['items'],
  components: {
    LoginNavItem
  },
  asyncData() {
    return {}
  },
  mounted() {
    document.addEventListener('DOMContentLoaded', () => {
      // Get all "navbar-burger" elements
      const $navbarBurgers = Array.prototype.slice.call(
        document.querySelectorAll('.navbar-burger'),
        0
      )

      // Check if there are any navbar burgers
      if ($navbarBurgers.length > 0) {
        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
          el.addEventListener('click', () => {
            // Get the target from the "data-target" attribute
            const target = el.dataset.target
            const $target = document.getElementById(target)

            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle('is-active')
            $target.classList.toggle('is-active')
          })
        })
      }
    })
  }
}
</script>
<style lang="scss">
.navbar {
  color: $primary;
  justify-content: space-around;
  align-content: center;
  align-items: center;
  padding: 14px;

  .column {
    display: inline-flex;
    .navbar-item {
      color: $grey !important;
    }
  }
  b-navbar-item {
    img {
      max-height: 40px;
    }
  }

  &::after {
    background: linear-gradient(
      -87deg,
      rgba(26, 188, 156, 0.8) 0%,
      rgba(46, 204, 113, 0.8) 100%
    );
    bottom: 0;
    content: '';
    height: 3px;
    position: absolute;
    width: 100%;
  }
}
</style>
