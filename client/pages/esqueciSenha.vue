<template>
  <section class="hero is-fullheight is-medium is-bold">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <article class="card is-rounded" style="width:400px">
            <div class="card-content">
              <h1 class="title">
                <Logo width="250" />
              </h1>
              <ForgotForm />
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import ForgotForm from '../components/organisms/ForgotForm'
import Logo from '../components/atoms/Logo'
export default {
  layout: 'default',
  components: {
    ForgotForm,
    Logo
  }
}
</script>


<style lang="scss" scoped>
.logo {
  padding: 10px 40px;
}

.hero-body {
  padding-top: 5em !important;
}

</style>
