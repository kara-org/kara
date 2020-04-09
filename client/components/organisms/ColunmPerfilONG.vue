<template>
  <div class="has-background-primary has-text-light is-scroll-y">
    <div class="card-content" style="text-align: center;">
      <h3 class="title is-size-5 has-text-light">{{ ong.nome }}</h3>
      <hr />
      <figure class="image is-128x128" style="margin: 0 auto">
        <img
          class="is-rounded"
          :src="
            ong.fotoDoPerfil != null
              ? ong.fotoDoPerfil.url
              : 'https://bulma.io/images/placeholders/128x128.png'
          "
        />
      </figure>
      <hr />
      <h3 class="title is-size-5 has-text-light">História</h3>
      <p>
        {{ ong.biografia }}
      </p>
      <hr />
      <template v-if="ong.enderecos && ong.enderecos[0]">
        <h3 class="title is-size-5 has-text-light">Endereço</h3>
        <p>
          {{ ong.enderecos[0] }}
        </p>
        <hr />
      </template>
      <h3 class="title is-size-5 has-text-light">Contato</h3>
      <template v-if="ong.linkParaContato && ong.linkParaContato != ''">
        <a target="_blank" :href="ong.linkParaContato">Link para Whatsapp</a>
        <br />
      </template>
      {{ ong.telefones[0] ? telefone(ong.telefones[0]) : '' }}
      <br />
      {{ ong.email ? ong.email : '' }}
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters({ ong: 'carrinho/ong' })
  },
  methods: {
    telefone(telefone) {
      if (telefone) {
        let last = telefone.length - 4;
        telefone = `(${telefone.substring(0, 2)}) ${telefone.substring(
          2,
          last
        )}-${telefone.substring(last)}`;
      }
      return telefone;
    }
  }
};
</script>
