<template>
  <article class="card">
    <h1 class="title is-size-5 has-text-centered">Demandas selecionadas</h1>
    <div class="columns">
      <p v-if="demandas.length<1">Demandas aparecerão aqui a medida que você for selecionando.</p>
    </div>
    <div v-for="item in demandas" :key="item.id" class="column is-full">
      <CardOng
        :titulo="item.titulo"
        :quantidade="item.quantidade"
        :ongTitulo="item.ong.titulo"
        :ongId="item.ong.id"
        :isCarrinho="true"
      />
    </div>
  </article>
</template>

<script>
import CardOng from '../molecules/CardDemanda'
export default {
  components: {
    CardOng
  },
  data() {
    return {
      demandas: [
        {
          titulo: 'Feijão',
          quantidade: 23,
          ong: {
            id: 1,
            titulo: 'ALMIR DO PICOLÉ'
          }
        },
        {
          titulo: 'Arroz',
          quantidade: 13,
          ong: {
            id: 1,
            titulo: 'ALMIR DO PICOLÉ'
          }
        },
        {
          titulo: 'Sal',
          quantidade: 5,
          ong: {
            id: 1,
            titulo: 'ALMIR DO PICOLÉ'
          }
        },
        {
          titulo: 'Água',
          quantidade: 19,
          ong: {
            id: 1,
            titulo: 'ALMIR DO PICOLÉ'
          }
        }
      ]
    }
  }
}
</script>