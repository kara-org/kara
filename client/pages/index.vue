<template>
  <div>
    <section class="hero is-fullheight-with-navbar">
      <div class="hero-body banner">
        <video
          autoplay
          loop
          muted
          class="banner__video"
          poster=""
        >
          <source src="~assets/video/video-bg.mp4" type="video/mp4" />
        </video>
        <div class="container">
          <h2 class="subtitle">
            <span>Ajude o próximo</span>
          </h2>
          <Buscar to="busca" />
        </div>
      </div>
    </section>
    <section class="hero is-fullheight">
      <div class="hero-body">
        <div class="container">
          <div class="level">
            <ListagemOngs :list="list" :isBusca="true"/>
          </div>
        </div>
      </div>
    </section>
    <section></section>
  </div>
</template>

<script>
import ListagemOngs from '../components/organisms/ListagemCards'
import Buscar from '../components/molecules/BuscarForm'

export default {
  name: 'HomePage',
  components: {
    ListagemOngs,
    Buscar
  },
  computed: {
    list (){
      return this.$store.state.busca.list
    }
  },
  created: function() {}
}
</script>
<style lang="scss" scoped>


.title,
.subtitle {
  color: $white;
  span {
    background: $primary;
    font-weight: bold;
    padding: 5px;
  }
}

.banner {
  position: relative;
  overflow: hidden;
  background: rgba(0, 0, 0, 0.5)
    url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAADCAYAAABWKLW/AAAAF0lEQVQIW2NkYGD4z8DAwMgAI0AMDA4AI3EBBCKrOnQAAAAASUVORK5CYII=');
  color: #fff;

  .container {
    max-width: 75%;
  }
}

.banner__video {
  position: absolute;
  top: 50%;
  left: 50%;
  width: auto;
  min-width: 100%;
  height: auto;
  min-height: 100%;
  transform: translateX(-50%) translateY(-50%);
  z-index: -1;
}
</style>
