<template>
  <transition name="fade" appear>
    <div class="box">
      <div class="card-content">
        <p v-if="isCarrinho"> Entregar {{ quantidadePrometida }} de </p>
        <p class="title is-4 heading" style="margin-bottom: 8px"><strong> {{ demanda.nome }}</strong></p>
        <p style="text-transform: uppercase">
          <small>para <span class="has-text-primary"> {{ demanda && demanda.ong && demanda.ong.nome  ? demanda.ong.nome : ong.nome }} </span></small>
        </p>
        <p class="is-size-5 heading" v-if="!isCarrinho">
          Restam
          <strong>{{ quantidadeRestante }}</strong>
          para a meta
        </p>
        <div class="level-right" v-if="!isCarrinho">
          <DoarModal :text="'Doar'" :item="demanda" :idOng="demanda && demanda.ong && demanda.ong.objectId  ? demanda.ong.objectId : ong.objectId" />
        </div>
        <div class="level" v-else>
          <button class="delete is-medium" @click="remover">Remover</button>
          <DoarModal :text="'Editar'" :item="demanda" :idOng="demanda && demanda.ong && demanda.ong.objectId  ? demanda.ong.objectId : ong.objectId" />
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
  props: ['demanda', 'isCarrinho', 'ong', 'quantidadePrometida'],
  computed: {
    quantidadeRestante () {
      let restante = this.demanda.quantidadeDesejada - this.demanda.quantidadeAlcancada
      return restante >= 0 ? restante : 0
    }

  },
  methods: {
    ...mapActions('carrinho', ['removerItemNoCarrinho']),
    remover: function() {
      this.$buefy.dialog.confirm({
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
.box {
  height: 100%;
}
</style>
