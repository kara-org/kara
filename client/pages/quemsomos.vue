<template>
  <div>
    <section class="hero is-fullheight-with-navbar">
      <div class="hero-body banner">
        <div class="container">
          <div class="columns">
            <div class="column is-completeheight">
              <h1 class="title">
                Quem somos
              </h1>
              <p>
                A plataforma Kara doações é uma tecnologia de impacto social que
                busca fornecer as organizações sociais (popularmente conhecidas
                como ONG's). Uma solução para gerenciar suas doações e campanhas
                de arrecadação de produtos.
              </p>
            </div>
            <div class="column is-completeheight">
              <iframe
                id="vimeo-iframe"
                src="https://player.vimeo.com/video/398071197"
                width="640"
                height="360"
                frameborder="0"
                allow="autoplay; fullscreen"
                allowfullscreen
              ></iframe>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'HomePage',
  computed: {},
  methods: {},
  mounted() {
    var iframe = document.getElementById('vimeo-iframe');
    iframe.style.height = '360px';
  }
};
</script>
<style lang="scss" scoped>
.is-completeheight {
  height: 100vh;
}

iframe {
  height: none;
}

iframe .player .vp-title .vp-title-header .headers {
  display: none;
}
</style>
