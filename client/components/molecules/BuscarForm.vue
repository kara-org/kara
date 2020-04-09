<template>
  <div>
    <h2 class="title">Encontre {{ tipo }} e faça sua doação!</h2>
    <b-field grouped group-multiline position="is-centered" class="filtro">
      <!-- <b-select v-model="tipo" placeholder="Tipo da busca" size="is-large">
        <option value="demandas">Demanda</option>
        <option value="ongs" disabled>ONG</option>
      </b-select>-->

      <b-input
        :expanded="true"
        placeholder="Digite aqui sua busca"
        size="is-large"
        type="search"
        class="filtro"
        v-model="palavraChave"
        @keyup.enter.native="send"
      ></b-input>
      <p class="control">
        <b-button
          class="button is-primary"
          size="is-large"
          @click="send"
          icon="magnify"
          :loading="loading"
          >Buscar</b-button
        >
      </p>
    </b-field>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  props: {
    to: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      palavraChave: '',
      tipo: 'demandas'
    };
  },
  methods: {
    ...mapActions('global', ['startLoading']),
    ...mapActions('busca', ['fetchBusca', 'buscar']),
    send() {
      //this.startLoading()
      //this.fetchBusca(this.tipo)
      this.buscar({ tipo: this.tipo, palavraChave: this.palavraChave });

      if (this.to) this.$router.push(this.to);
    }
  },
  computed: {
    ...mapGetters(
      { loading: 'global/loading' },
      { searchTerm: 'busca/searchTerm' },
      { list: 'busca/list' }
    )
  },
  watch: {
    palavraChave() {
      this.buscar({ tipo: this.tipo, palavraChave: this.palavraChave });
    },
    searchTerm() {
      this.palavraChave = this.searchTerm != null ? this.searchTerm : '';
    },
    list() {
      if (!this.list.length) this.fetchBusca(this.tipo);
    }
  }
};
</script>
<style lang="scss" scoped>
.filtro input {
  border-radius: 50px;
}
.button {
  border-top-right-radius: 25px;
  border-bottom-right-radius: 25px;
  border-top-left-radius: 25px;
  border-bottom-left-radius: 25px;
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

@media only screen and (max-width: 768px) {
  .button {
    width: 100%;
    padding: auto 30px;
    border-top-left-radius: 25px;
    border-bottom-left-radius: 25px;
  }
}
</style>
