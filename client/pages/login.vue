<template>
  <section class="hero is-fullheight is-medium  is-bold">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <article class="card is-rounded" style="width:400px">
            <div class="card-content">
              <h1 class="title">
                <Logo width="250" />
              </h1>
              <LoginForm />
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Logo from '../components/atoms/Logo'
import LoginForm from '../components/organisms/LoginForm'

export default {
  layout: 'empty',
  components: {
    LoginForm,
    Logo
  }
}
</script>


<style lang="scss" scoped>
  .hero-body {
    padding-top: 5em !important;
  }

</style>
