<template>
  <div class="container">
    <div class="columns is-desktop">
      <div v-for="item in list" :key="item.objectId" class="column" :class="isBusca ? 'is-one-third is-full-mobile' : 'is-half'">
        <CardDemanda
          :demanda="item"
          :ong="ong"
          :isCarrinho="false"
        />
      </div>
    </div>
  </div>
</template>

<script>
import CardDemanda from '../molecules/CardDemanda'

import { mapActions, mapGetters, mapState } from 'vuex'
export default {
  props: {
    isBusca: Boolean,
    list: Array
  },
  components: {
    CardDemanda
  },
  async asyncData() {
    return {}
  },
  computed: {
    ...mapState('carrinho', ['ong'])
  },
  methods: {
    ...mapActions('busca', ['fetchBusca', 'buscar'])
  },
  async asyncData () {
    this.fetchBusca()
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

