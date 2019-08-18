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
  mounted() {
    this.fetchOngs()
    console.log(this.$store.state.ongs.ongs)
  }
}
</script>

<style lang="scss">
</style>

