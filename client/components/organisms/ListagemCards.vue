<template>
  <div class="container">
    <div class="columns is-multiline">
      <div v-for="item in list" :key="item.id" class="column" :class="isBusca ? 'is-one-third' : 'is-half'">
        <CardOng
          :titulo="item.titulo"
          :quantidade="item.quantidade"
          :ongTitulo="item.ong.titulo"
          :ongId="item.ong.id"
          :isCarrinho="false"
        />
      </div>
      <div v-for="item in list" :key="item.id"  class="column" :class="isBusca ? 'is-one-third' : 'is-half'">
        <CardOng
          :titulo="item.titulo"
          :quantidade="item.quantidade"
          :ongTitulo="item.ong.titulo"
          :ongId="item.ong.id"
          :isCarrinho="false"
        />
      </div>
      <div v-for="item in list" :key="item.id"  class="column" :class="isBusca ? 'is-one-third' : 'is-half'">
        <CardOng
          :titulo="item.titulo"
          :quantidade="item.quantidade"
          :ongTitulo="item.ong.titulo"
          :ongId="item.ong.id"
          :isCarrinho="false"
        />
      </div>
    </div>
  </div>
</template>

<script>
import CardOng from '../molecules/CardDemanda'

import { mapActions } from 'vuex'
export default {
  props: {
    isBusca: Boolean
  },
  components: {
    CardOng
  },
  async asyncData() {
    return {}
  },
  computed: {
    list() {
      if (!this.$store.state.busca.list.length)
        this.fetchBusca({
          tipo: 'demanda',
          palavraChave: 'this.palavraChave'
        })
      var list = this.$store.state.busca.list
      return list != null ? list : this.$store.state.busca.default
    }
  },
  methods: {
    ...mapActions('busca', ['fetchBusca', 'buscar'])
  },
  mounted() {}
}
</script>

<style>
.columns {
  display: flex;
  flex-wrap: wrap;
  margin: 10px!important;
}
.columns .column {
  padding: 5px;
}
</style>

