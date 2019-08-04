<template>
    <div class="columns is-multiline">
      <div v-for="item in list" :key="item.id" class="column is-half">
        <CardOng :titulo="item.titulo" :quantidade="item.quantidade" :ong="item.ong" />
      </div>
    </div>
</template>

<script>

import CardOng from '../molecules/Card'

export default {
  components: {
    CardOng
  },
  async asyncData() {
    return {}
  },
  computed: {
    list () {
      return this.$store.state.busca.list
    }
  },
  mounted() {
  }
}
</script>

<style>
.columns {
  width: 100%;
}
</style>

