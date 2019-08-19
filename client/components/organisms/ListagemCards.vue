<template>
  <div class="container">
    <div class="columns is-multiline">
      <div v-for="item in list" :key="item.id" class="column" :class="isBusca ? 'is-one-third' : 'is-half'">
        <CardOng
          :demanda="item"
          :isCarrinho="false"
        />
      </div>
    </div>
  </div>
</template>

<script>
import CardOng from '../molecules/CardDemanda'

import { mapActions, mapGetters } from 'vuex'
export default {
  props: {
    isBusca: Boolean,
    list: Array
  },
  components: {
    CardOng
  },
  async asyncData() {
    return {}
  },
  computed: {
  },
  methods: {
    ...mapActions('busca', ['fetchBusca', 'buscar'])
  },
  mounted () {
  }
}
</script>

<style lang="scss" scoped>
.columns {
  display: flex;
  flex-wrap: wrap;
  margin: 10px!important;
}
.columns .column {
  padding: 5px;
}
</style>

