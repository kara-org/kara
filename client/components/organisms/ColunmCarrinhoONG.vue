<template>
  <article class="has-background-white">
    <h1 class="title is-size-5 has-text-centered">Demandas selecionadas</h1>
    <b-button  @click="send" class="is-primary is-fullwidth is-rounded is-stick-botton" size="is-medium" fullwidth="true"  icon="magnify">Finalizar doação</b-button>
    <br>
    <div class="columns">
      <p v-if="demandas && demandas.length == 0 ">Demandas aparecerão aqui a medida que você for selecionando.</p>
    </div>
    <div class="cards is-scroll-y">
      <div v-for="item in demandas" :key="item.id" class="column is-full">
        <CardDemanda
          :demanda="item.demanda"
          :ong="ong"
          :isCarrinho="true"
          :quantidadePrometida="item.quantidade_prometida"
        />
      </div>
    </div>
  </article>
</template>

<script>
import CardDemanda from '../molecules/CardDemanda'
import { mapGetters, mapActions, mapState } from 'vuex'

export default {
  components: {
    CardDemanda
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters({ demandas: 'carrinho/itensNoCarrinho' }),
    ...mapState('carrinho', ['ong'])
  },
  methods: {
    ...mapActions('carrinho', ['sendDoacao']),
    send(){
      this.sendDoacao().then(() => {
        this.$toast.open({
            message: "Obrigado pela doação!",
            type: 'is-success',
            position: 'is-top'
          })
      })
      this.$router.push('/gerenciarDoacoes')
    }
  }
}
</script>

<style lang="css" scoped>
.is-stick-botton{
  position: sticky;
  bottom: 0;
}
</style>
