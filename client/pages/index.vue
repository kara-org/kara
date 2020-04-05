<template>
  <div>
    <section class="hero is-fullheight-with-navbar video">
      <div class="hero-video">
        <video
          autoplay
          loop
          muted

          poster=""
        >
          <source src="~assets/video/video-bg.mp4" type="video/mp4" />
        </video>
      </div>
      <div class="hero-body banner">
        <div class="container">
          <h2 class="subtitle">
            <span>Ajude o próximo</span>
          </h2>
          <Buscar to="busca" />
        </div>
      </div>
    </section>
    <section class="section sobre">
      <div class="container">
        <div class="columns">
          <div class="column is-full">
            <h1 class="title is-primary is-size-2 has-text-centered">Como funciona</h1>
          </div>
        </div>
        <div class="columns is-vcentered">
          <div class="column is-half">
            <figure class="image">
              <img src="~assets/sobre/acesso.svg">
            </figure>
          </div>
          <div class="column">
            <div class="hero is-completeheight">
              <div class="hero-body">
                <div class="container">
                  <h2 class="is-size-4 is-2 has-text-dark">
                    <div class="tag is-size-6 is-primary">1</div><p>Primeiro, você precisa buscar uma demanda na nossa barra de busca, experimente digitar "Arroz" e clicar no botão buscar</p>
                  </h2>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="columns is-vcentered">
            <div class="column">
              <div class="hero is-completeheight">
                <div class="hero-body">
                  <div class="container">
                    <h2 class="is-size-4 is-2 has-text-dark is-centered">
                      <div class="tag is-size-6 is-primary">2</div><p>  Inicie uma conversa por telefone ou email para combinar o encontro com a ONG</p>
                    </h2>
                  </div>
                </div>
              </div>
            </div>
            <div class="column is-half">
              <figure class="image">
                <img src="~assets/sobre/combine.svg">
              </figure>
            </div>
        </div>
        <div class="columns is-vcentered">
          <div class="column is-half">
            <figure class="image">
              <img src="~assets/sobre/entrega.svg">
            </figure>
          </div>
          <div class="column">
            <div class="hero is-completeheight">
              <div class="hero-body">
                <div class="container is-vcentered">
                  <h2 class="is-size-4 is-2 has-text-dark">
                    <div class="tag is-size-6 is-primary">3</div><p> Agora é só entregar sua doação e aproveitar pra conhecer o projeto que você está apoiando! </p>
                  </h2>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section >
    </section>
  </div>
</template>

<script>
import Buscar from '../components/molecules/BuscarForm'
import { mapActions } from 'vuex'

export default {
  name: 'HomePage',
  components: {
    Buscar
  },
  computed: {
  },
  methods: {
     ...mapActions('busca', ['fetchBusca']),
  },
  created: function() {
    this.fetchBusca()
  }
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
.is-completeheight {
  height: 100%;
}
</style>
