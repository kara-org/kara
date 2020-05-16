<template>
  <div>
    <section class="hero is-medium is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-flex is-vcentered is-centered">
            <div class="column is-narrow">
              <figure class="image is-256x256">
                <v-lazy-image class="is-rounded is-max-256x256 " :src="ong.fotoDoPerfil && ong.fotoDoPerfil.url" />
              </figure>
            </div>
            <div class="column is-4 is-flex">
              <div class="hero is-vcentered">
                <div class="content">
                  <p class="title ">{{ ong.nome }}</p>
                  <p class="subtitle">{{ ong.email }}</p>
                  <p>
                    {{ ong.biografia }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="hero is-medium is-bold">
      <ListagemCards :list="demandas" />
    </section>
  </div>
</template>

<script>
import PerfilONG from '@/components/organisms/ColunmPerfilONG';
import ListagemCards from '@/components/organisms/ListagemCards';
import CarrinhoONG from '@/components/organisms/ColunmCarrinhoONG';
import VLazyImage from 'v-lazy-image';

import { mapState, mapActions } from 'vuex';

export default {
  components: {
    VLazyImage,
    PerfilONG,
    ListagemCards,
    CarrinhoONG
  },
  created: async function() {
    const ong = await this.fetchOngSlug(this.$route.params.slug);
    this.fetchDemandasOng(ong.id);
  },
  data() {
    return {};
  },
  computed: {
    ...mapState('ongs', ['ong']),
    ...mapState('demandas', { demandas: 'list' })
  },
  methods: {
    ...mapActions('ongs', ['fetchOngSlug']),
    ...mapActions('demandas', ['fetchDemandasOng'])
  }
};
</script>

<style lang="scss">
.columns {
  margin: 5px;
}
.is-max-256x256{
  max-width: 256px;
  max-height: 256px;
}
</style>
