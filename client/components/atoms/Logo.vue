<template>
   <img
      class="logo"
      src="~assets/kara-logo.svg"
      alt="logo"
      :width=width
    />
</template>
<script>
export default {
  props: ['width']
}
</script>

<style lang="scss">
  .logo {
    padding: 10px 40px;
    margin: 0 auto;
    display: block;
  }
</style>
