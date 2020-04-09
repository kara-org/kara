<template>
  <div>
    <div class="card" v-for="(item, key) of ongs" :key="key">

    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  async asyncData() {
    return {

    }
  },
  computed: {
    ongs() {
      return this.$store.ongs
    }
  },
  methods: {
    ...mapActions('ongs', ['fetchOngs'])
  },
  async asyncData() {
    this.fetchOngs()
  }
}
</script>

<style lang="scss">
</style>

