<template>
  <transition name="fade" appear>
    <div class="card">
      <div class="card-content">
        <p class="title is-6">{{titulo}}</p>
        <p class="heading">
          <nuxt-link :to="'/ong/'+ongId" exact-active-class="is-active">{{ ongTitulo }}</nuxt-link>
        </p>
        <p class="heading">
          Fatam
          <strong>{{ quantidade }}</strong>
        </p>
        <div class="level-right" v-if="!isCarrinho">
          <DoarModal :text="'Doar'" />
        </div>

        <div class="level" v-else>
          <button class="delete is-small" @click="remover">Remover</button>
          <DoarModal :text="'Editar'" />
        </div>
      </div>
    </div>
  </transition>
</template>
<script>
import DoarModal from '@/components/molecules/DoarModal.vue'
export default {
  components: { DoarModal },
  props: [
    'imagem',
    'titulo',
    'quantidade',
    'ongId',
    'ongTitulo',
    'to',
    'isCarrinho'
  ],
  methods: {
    remover: function() {
      this.$dialog.confirm({
        message: 'Tem certeza que deseja remover este item?',
        confirmText: 'Sim',
        onConfirm: () => {
        }
      })
    }
  }
}
</script>
<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.7s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
