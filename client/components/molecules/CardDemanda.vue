<template>
  <transition name="fade" appear>
    <div class="box">
      <div class="card-content">
        <p class="title is-4 heading" style="font-weight: bold!important;">{{ demanda.descricao }}</p>
        <p class="is-size-5 heading">
          <!-- <nuxt-link :to="`/ong/${ demanda && demanda.ong && demanda.ong.id }`" exact-active-class="is-active">{{ demanda && demanda.ong && demanda.ong.nome }}</nuxt-link> -->
        </p>
        <p class="is-size-5 heading">
          Restam
          <strong>{{ qtdRestante(demanda.quantidade_solicitada, demanda.quantidade_alcancada) }}</strong>
          para a meta
        </p>
        <div class="level-right" v-if="!isCarrinho">
          <DoarModal :text="'Doar'" :id="1" :item="demanda" />
        </div>
        <div class="level" v-else>
          <button class="delete is-medium" @click="remover">Remover</button>
          <DoarModal :text="'Editar'" />
        </div>
      </div>
    </div>
  </transition>
</template>
<script>
import DoarModal from '@/components/molecules/DoarModal.vue'
import { mapActions } from 'vuex'

export default {
  components: { DoarModal },
  props: ['demanda', 'isCarrinho'],
  methods: {
    qtdRestante(qtdSolicitada, qtdAlcancada) {
      var restante = qtdSolicitada - qtdAlcancada
      return restante >= 0 ? restante : 0
    },
    ...mapActions('carrinho', ['removerItemNoCarrinho']),
    remover: function() {
      this.$dialog.confirm({
        message: 'Tem certeza que deseja remover este item?',
        confirmText: 'Sim',
        onConfirm: () => {
          this.removerItemNoCarrinho(this.demanda)
        }
      })
    }
  }
}
</script>
<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.7s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.heading {
  font-size: 1.5rem;
}
</style>
