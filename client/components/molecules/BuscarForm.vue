<template>
  <div>
    <h1 class="title">Encontre uma {{ tipo }} e faça sua doação!</h1>
    <b-field class="filtro">
      <b-select v-model="tipo" placeholder="Tipo da busca" size="is-large">
        <option value="demanda">Demanda</option>
        <option value="ONG">ONG</option>
      </b-select>

      <b-input
        :expanded="true"
        placeholder="Digite aqui sua busca"
        size="is-large"
        type="search"
        v-model="palavraChave"
        @keyup.enter.native="send"
      ></b-input>
      <b-button class="is-primary" size="is-large" @click="send" icon="magnify" :loading="loading">Buscar</b-button>
    </b-field>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  props: {
    to: {
      type: String,
      default: null
    },
  },
   data () {
    return {
      palavraChave: '',
      tipo: 'demanda',
    }
  },
  methods: {
    ...mapActions('global', ['startLoading']),
    ...mapActions('busca', ['fetchBusca', 'buscar']),
    send () {
      this.startLoading()
      this.fetchBusca({ tipo: this.tipo, palavraChave: this.palavraChave})

      if (this.to)
        this.$router.push(this.to)
    }
  },
  computed: {
    loading () {
      return this.$store.state.global.loading
    }

  },
  watch: {
    palavraChave () {
      this.buscar({ tipo: this.tipo, palavraChave: this.palavraChave})
    }
  },
  created () {
    if (!this.$store.state.busca.list.length)
      this.fetchBusca({ tipo: this.tipo, palavraChave: this.palavraChave})
    this.palavraChave =  this.$store.state.busca.searchTerm
  }
}
</script>
<style lang="scss" scoped>

.filtro input {
  border-radius: 50px;
}
.button {
  border-top-right-radius: 25px;
  border-bottom-right-radius: 25px;
  border-top-left-radius: 0px;
  border-bottom-left-radius: 0px;
}

.title,
.subtitle {
  color: $white;
  span {
    background: $primary;
    font-weight: bold;
    padding: 5px;
  }
}

</style>

