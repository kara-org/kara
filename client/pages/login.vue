<template>
  <section class="hero is-fullheight is-medium  is-bold">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <article class="card is-rounded" style="width:400px">
            <div class="card-content">
              <h1 class="title">
                <img
                  class="logo"
                  src="~assets/kara-negativo.png"
                  alt="logo"
                  width="400"
                />                
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
import LoginForm from '../components/organisms/LoginForm'
export default {
  layout: 'empty',
  components: {
    LoginForm
  }
}
</script>


<style lang="scss" scoped>
  .logo {
    padding: 10px 40px;
  }
</style>
