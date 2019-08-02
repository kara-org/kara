<template>
  <div>
    <NavBar :items=items />
    <section class="container main-content columns">
      <MenuLateral class="column is-one-quarter"/>
      <nuxt />
    </section>
  </div>
</template>

<script>
import NavBar from '../components/organisms/NavBar'
import MenuLateral from '../components/organisms/MenuLateral'
export default {
  components: {
    NavBar,
    MenuLateral
  },
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
</style>
