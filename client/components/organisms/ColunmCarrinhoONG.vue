<template>
  <article class="card is-rounded">
    <div class="card-content">
      <h class="title is-size-5">Demandas selecionadas</h>
      <hr />

      <p v-if="demandas.length<1">Demandas aparecerão aqui a medida que você for selecionando.</p>
    </div>
    <div v-for="(item, key) of demandas" :key="key" class="card">
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <p class="title is-4">{{item.nome}}</p>
            <p class="subtitle is-6">Acaba em {{item.data}}</p>
          </div>
        </div>
        <div class="content">
          <p>{{item.progresso}}% concluído</p>
        </div>
      </div>
    </div>
  </article>
</template>

<script>
export default {
  data() {
    return {
      demandas: [
        { nome: 'Feijão', progresso: 23, data: '10/10/2019' },
        { nome: 'Arroz', progresso: 13, data: '31/21/2019' },
        { nome: 'Sal', progresso: 5, data: '22/09/2019' },
        { nome: 'Água', progresso: 19, data: '14/02/2019' }
      ]
    }
  }
}
</script>
<style lang="scss">
.card-content {
  text-align: -webkit-center;
}
.card-content p {
  text-align: justify;
}
</style>