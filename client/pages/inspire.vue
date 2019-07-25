<template>
  <section class="section">
    <h2 class="title is-3 has-text-grey">
      "Just start  <b-icon
        icon="rocket"
        size="is-large"
      />"
    </h2>
    <h3 class="subtitle is-6 has-text-grey">
      {{ ip }}
    </h3>
  </section>
</template>

<script>
export default {
  middleware: 'auth',
  data () {
    return {
      ip: ''
    }
  },
  methods: {
  },
  mounted: async function () {
    this.ip = await this.$OngService.index()
  }
}
</script>
