<template>
  <section>
    <form v-if="!success" @submit.prevent="validateBeforeSubmit" method="post">
      <hr />
      <b-field
        label="Nome"
        :type="{'is-danger': errors.has('nome')}"
        :message="errors.first('nome')"
      >
        <b-input type="text" v-model.trim="demanda.nome" name="nome" v-validate="'required'"></b-input>
      </b-field>
      <b-field
        label="Categoria"
        :type="{'is-danger': errors.has('categoria')}"
        :message="errors.first('categoria')"
      >
        <b-input
          type="text"
          v-model.trim="demanda.categoria"
          name="categoria"
          v-validate="'required'"
        />
      </b-field>
      <b-field
        label="Quantidade"
        :type="{'is-danger': errors.has('quantidade')}"
        :message="errors.first('quantidade')"
      >
        <b-input
          type="number"
          v-model.number="demanda.quantidade"
          name="quantidade"
          v-validate="'required'"
        ></b-input>
      </b-field>
      <b-field
        label="Data de inicio"
        :type="{'is-danger': errors.has('data inicio')}"
        :message="errors.first('data inicio')"
      >
        <b-datepicker
          placeholder="Selecione uma data..."
          v-model="demanda.data_inicio"
          :min-date="demanda.minDate"
          :max-date="demanda.maxDate"
          name="data inicio"
          v-validate="'required'"
        ></b-datepicker>
      </b-field>
      <b-field
        label="Data final"
        :type="{'is-danger': errors.has('data final')}"
        :message="errors.first('data final')"
      >
        <b-datepicker
          placeholder="Selecione uma data..."
          v-model="demanda.data_fim"
          :min-date="demanda.minDate"
          :max-date="demanda.maxDate"
          name="data final"
          v-validate="'required'"
        ></b-datepicker>
      </b-field>
      <hr />
      <button
        type="submit"
        class="button is-primary is-outlined is-medium is-rounded is-fullwidth"
      >Confirmar</button>
      <div class="column has-text-centered">
        <nuxt-link
          class="voltar is-primary is-inverted"
          to="/"
          exact-active-class="is-active"
        >Voltar</nuxt-link>
      </div>
    </form>
    <div v-else class="column has-text-centered">
      <h1>Produto cadastrado com successo.</h1>
      <hr />
    </div>
  </section>
</template>
<script>
import cleave from '@/plugins/cleave-directive.js'
export default {
  props: {
    isCadastro: Boolean
  },
  data() {
    const today = new Date()
    return {
      demanda: {
        nome: null,
        descricao: null,
        quantidade: null,
        data_inicio: null,
        data_fim: null,
        minDate: new Date(
          today.getFullYear(),
          today.getMonth(),
          today.getDate()
        ),
        maxDate: new Date(
          today.getFullYear() + 1,
          today.getMonth(),
          today.getDate()
        )
      },
      success: false
    }
  },
  created() {
    !this.isCadastro ? this.getDoador() : {}
  },
  methods: {
    async createDemanda() {
      try {
        await this.$UsuarioService.create({}).catch(err => {
          if (!err.response) {
            err.message = 'Servidor desconectado'
          } else if (err.response.status === 400) {
            err.message = err.response.data.non_field_errors[0]
          }
          this.$toast.open({
            message: err.message,
            type: 'is-danger',
            position: 'is-bottom'
          })
        })
        this.success = true
      } catch (e) {
        this.error = e.response.data.message
      }
    },
    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.register()
          return
        }
        this.$toast.open({
          message: 'Formulário inválido, verifique os campos em vermelho',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
    }
  }
}
</script>