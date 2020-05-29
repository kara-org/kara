<template>
  <transition name="fade" appear>
    <div class="box">
      <div class="card-content">
        <article class="media">
          <figure class="media-left">
            <p class="image is-64x64">
              <img :src="ong.fotoDoPerfil && ong.fotoDoPerfil.url" />
            </p>
          </figure>
          <div class="media-content">
            <div class="content">
              <p class="title is-4 heading" style="margin-bottom: 8px">
                <strong> {{ ong.nome }}</strong>
              </p>
            </div>
            <div class="level">
              <div class="level-left">
                <div class="level-item">
                  <nuxt-link
                    :to="'/ong/' + ong.slug"
                    exact-active-class="is-active"
                    >Ver perfil da ONG</nuxt-link
                  >
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>
    </div>
  </transition>
</template>
<script>
import { mapActions } from 'vuex';

export default {
  props: ['ong'],
  computed: {},
  methods: {}
};
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
