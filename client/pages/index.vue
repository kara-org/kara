<template>
  <div>
    <section class="hero is-fullheight-with-navbar">
      <div class="hero-body banner">
        <video
          autoplay
          loop
          muted
          class="banner__video"
          poster="https://pawelgrzybek.com/photos/2015-12-06-codepen.jpg"
        >
          <!-- <source src="https://pawelgrzybek.com/photos/2015-12-06-codepen.webm" type="video/webm"> -->
          <!-- <source src="https://pawelgrzybek.com/photos/2015-12-06-codepen.mp4" type="video/mp4"> -->
          <source src="~assets/video/video-bg.mp4" type="video/mp4" />
        </video>
        <div class="container">
          <h2 class="subtitle"> <span> Ajude o próximo</span></h2>
          <h1 class="title">Encontre uma ONG e faça sua doação!</h1>
          <b-field class="filtro">
            <b-input
              :expanded="true"
              icon="magnify"
              placeholder="Buscar..."
              size="is-large"
              type="search"
            ></b-input>
            <b-button class="is-primary" size="is-large">Buscar</b-button>
          </b-field>
        </div>
      </div>
    </section>
    <section class="hero is-fullheight">
      <ListagemOngs />
    </section>
  </div>
</template>

<script>
import ListagemOngs from '../components/organisms/ListagemOngs'

export default {
  name: 'HomePage',
  components: {
    ListagemOngs
  },
  created: function() {
  }
}
</script>
<style lang="scss" scoped>
.filtro input {
  border-radius: 50px;
}
.button {
  border-top-right-radius: 25px;
  border-bottom-right-radius: 25px;
  border-top-left-radius: 0px;
  border-bottom-left-radius: 0px;
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
