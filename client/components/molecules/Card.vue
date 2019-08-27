<template>
  <transition name="fade" appear>
    <div class="box">
      <div class="media">
        <div v-if="imagem" class>
          <figure class="media-left">
            <p class="image is-64x64">
              <img :src="imagem" alt="Ong" />
            </p>
          </figure>
        </div>
        <div class="media-content">
          <div class="content">
            <nav class="level">
              <div class="level-item has-text-centered">
                <div>
                  <p class="title" style="margin-bottom: 10px;">{{ titulo }}</p>
                  <p class="heading">
                    para
                    <nuxt-link :to="'/ong/'+ongId" exact-active-class="is-active">{{ ongTitulo }}</nuxt-link>
                  </p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Ainda precisamos de</p>
                  <p class="title" style="margin-bottom: 10px;">{{ quantidade }}</p>
                  <p class="heanding">Para atingir a meta</p>
                </div>
              </div>
            </nav>
          </div>
        </div>
        <div class="media-right">
          <a href="/carrinho" class="card-footer-item button is-primary is-medium">Doar</a>
        </div>
      </div>
    </div>
  </transition>
</template>
<script>
export default {
  props: ['imagem', 'titulo', 'quantidade', 'ongId', 'ongTitulo', 'to']
}
</script>
<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .7s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
