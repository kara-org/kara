<template>
  <div>
    <NavBar :items="items" />
    <section class="main-content">
      <nuxt />
    </section>
  </div>
</template>

<script>
import NavBar from '../components/organisms/NavBar';
import { mapActions } from 'vuex';
export default {
  components: {
    NavBar
  },
  created() {
    this.fetchCurrentUser();
  },
  data() {
    return {
      items: [
        {
          title: 'INÍCIO',
          icon: 'home',
          to: { name: 'index' }
        },
        {
          title: 'QUEM SOMOS',
          icon: 'lightbulb',
          to: { name: 'quemsomos' }
        },
        {
          title: 'DEMANDAS',
          icon: 'lightbulb',
          to: { name: 'busca' }
        },
        {
          title: 'ONGS',
          icon: 'lightbulb',
          to: { name: 'ongs' }
        }
      ]
    };
  },
  methods: {
    ...mapActions({
      fetchCurrentUser: 'login/fetch'
    })
  }
};
</script>

<style lang="scss">
.navbar {
  color: $primary;

  .navbar-brand {
    padding: 10px;
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
