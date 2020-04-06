<template>
  <div>
    <section class="hero is-fullheight-with-navbar">
      <div class="hero-body banner">
        <div class="container">
          <h1 class="title"><span>  Obrigado!</span></h1>
          <p>Para concluir a doação entre em contato com a ong {{ ong.nome }}</p>
          <p>Use esse link para falar direto com um colaborador pelo whatsapp <a :href="ong.linkParaContato" >clique aqui</a></p>
          <b-button class="btn-ver" tag="nuxt-link"
                type="button is-primary is-outlined is-rounded"
                to="/doador/doacoes/">Ver minhas Doações</b-button>

        </div>
      </div>
    </section>
    <section >
    </section>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'HomePage',
  computed: {
    ong(){
      return this.$store.state.ongs.ong
    }
  },
  methods: {
    ...mapActions("ongs", ["fetchOng"])
  },
  created: function() {
    this.fetchOng(this.$route.params.idOng);
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

.is-completeheight {
  height: 100%;
}
.btn-ver{
  margin-top: 20px;
  margin-left: -5px;
}
</style>
