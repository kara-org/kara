<template>
  <section class="hero is-medium is-bold">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <article class="card is-rounded" style="width:400px">
            <div class="card-content">
              <p class="form-section-title">Cadastre uma demanda</p>
              <CadastroDemandaForm :isCadastro="true" />
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import CadastroDemandaForm from '@/components/organisms/CadastroDemandaForm'

export default {
  layout: 'default',
  components: {
    CadastroDemandaForm
  }
}
</script>

<style lang="scss" scoped>
.hero-body {
  padding-top: 5em !important;
}
</style>
