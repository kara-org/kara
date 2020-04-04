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
      <p>{{ ong.historia }}</p>
      <hr />
      <h3 class="title is-size-5 has-text-light">Endereço</h3>
      <p>{{formataEndereco(ong.endereco)}}</p>
      <hr />
      <h3 class="title is-size-5 has-text-light">Contato</h3>
      <p>
        Telefone: {{formataTelefone(ong.telefone[0].numero)}}
        <br />
        Email: {{email}}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    ong() {
      return this.$store.state.carrinho.ong
    },
    email() {
      return this.$auth.user.email
    }
  },
  methods: {
    formataTelefone(telefone) {
      return (
        '(' +
        telefone.substring(0, 2) +
        ') ' +
        telefone.substring(2, 6) +
        '-' +
        telefone.substring(6)
      )
    },
    formataEndereco(endereco) {
      return (
        endereco.logradouro +
        ', ' +
        endereco.numero +
        ', ' +
        endereco.bairro +
        ', ' +
        endereco.cidade +
        ' - ' +
        endereco.estado
      )
    }
  }
}
</script>
