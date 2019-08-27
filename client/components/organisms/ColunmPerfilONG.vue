<template>
  <div class="has-background-primary has-text-light is-scroll-y">
    <div class="card-content" style="text-align: center;">
      <h3 class="title is-size-5 has-text-light">{{ ong.nome }}</h3>
      <hr />
      <figure class="image is-128x128" style="margin: 0 auto">
        <img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" />
      </figure>
      <hr />
      <h3 class="title is-size-5 has-text-light">História</h3>
      <p>
        {{ ong.historia }}
      </p>
      <hr />
      <h3 class="title is-size-5 has-text-light">Endereço</h3>
      <p>Rua Maria Miralda dos Santos, nº 4. Parque Ilza, Av. Central C Dois, Nossa Sra. do Socorro - SE, 49160-000.</p>
      <hr />
      <h3 class="title is-size-5 has-text-light">Contato</h3>
      <p>
        Telefone: 3248-1413
        <br />Email: almir@mail.com.br
      </p>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    ong () {
      return this.$store.state.carrinho.ong
    }
  }
}
</script>
