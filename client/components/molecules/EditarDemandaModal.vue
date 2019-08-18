<template>
  <span>
    <a @click="isComponentModalActive = true">
      <b-icon class="button is-medium" icon="menu"></b-icon>
    </a>
    <b-modal :active.sync="isComponentModalActive" has-modal-card>
      <form action>
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Edição de Demanda</p>
          </header>
          <section class="modal-card-body">
            <b-field label="Nome">
              <b-input type="text" v-model="nome" placeholder="Açucar" required></b-input>
            </b-field>
            <b-field label="Categoria">
              <b-input type="text" v-model="categoria" placeholder="Alimentos" required></b-input>
            </b-field>
            <b-field label="Quantidade">
              <b-input type="number" v-model="quantidade" placeholder="Quantidade a doar" required></b-input>
            </b-field>
            <b-field label="Data de inicio">
              <b-input type="text" v-model="dataInicio" placeholder="15/08/2019" required></b-input>
            </b-field>
            <b-field label="Data de finalização">
              <b-input type="text" v-model="dataFim" placeholder="21/09/2019" required></b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <button class="button" type="button" @click="isComponentModalActive = false">Cancelar</button>
            <button class="button is-primary">Confirmar</button>
          </footer>
        </div>
      </form>
    </b-modal>
  </span>
</template>

<script>
export default {
  data() {
    return {
      isComponentModalActive: false,
      quantidade: 1,
      nome: '',
      categoria: '',
      dataInicio: '22/07/2019',
      dataFim: '22/08/2019'
    }
  }
}
</script>

<style scoped lang="scss">
  .modal-card-body{
    text-align: initial;
  }
</style>