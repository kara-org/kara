<template>
  <section>
    <form v-if="!success" @submit.prevent="validateBeforeSubmit" method="post">
      <hr />
      <b-field
        label="Título"
        :type="{'is-danger': errors.has('titulo')}"
        :message="errors.first('titulo')"
      >
        <b-input type="text" v-model.trim="demanda.descricao" name="titulo" v-validate="'required'"></b-input>
      </b-field>
      <div class="columns">
        <div class="column is-half">
          <b-field
            label="Categoria"
            :type="{'is-danger': errors.has('categoria')}"
            :message="errors.first('categoria')"
          >
            <b-select
              v-model="demanda.id_categoria"
              placeholder="Selecione uma categoria"
              name="categoria"
              v-validate="'required'"
            >
              <option :value="1">Alimentos</option>
              <option :value="2">Roupas</option>
              <option :value="3">Utilitários</option>
            </b-select>
          </b-field>
          <b-field
            label="Quantidade"
            :type="{'is-danger': errors.has('quantidade')}"
            :message="errors.first('quantidade')"
          >
            <b-numberinput
              v-model.number="demanda.quantidade_solicitada"
              name="quantidade"
              min="1"
              v-validate="'required'"
            ></b-numberinput>
          </b-field>
        </div>
        <div class="column is-half">
          <b-field
            label="Data de inicio"
            :type="{'is-danger': errors.has('data inicio')}"
            :message="errors.first('data inicio')"
          >
            <b-datepicker
              placeholder="Selecione uma data..."
              v-model="data_inicio"
              name="data inicio"
              v-validate="'required'"
              :month-names="meses"
            ></b-datepicker>
          </b-field>
          <b-field
            label="Data final"
            :type="{'is-danger': errors.has('data final')}"
            :message="errors.first('data final')"
          >
            <b-datepicker
              placeholder="Selecione uma data..."
              v-model="data_fim"
              name="data final"
              v-validate="'required'"
              :month-names="meses"
            ></b-datepicker>
          </b-field>
        </div>
      </div>
      <hr />
      <button
        type="submit"
        class="button is-primary is-outlined is-medium is-rounded is-fullwidth"
      >Confirmar</button>
    </form>
    <div v-else class="column has-text-centered">
      <hr />
      <h1>Produto cadastrado com successo.</h1>
      <hr />
      <div class="column has-text-centered">
        <button @click="reset()" class="button is-primary is-outlined is-medium is-rounded">Voltar</button>
      </div>
    </div>
  </section>
</template>
<script>
import cleave from '@/plugins/cleave-directive.js'
export default {
  data() {
    return {
      meses: [
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro'
      ],
      demanda: {
        id_categoria: null,
        descricao: null,
        quantidade_solicitada: null,
        data_inicio: null,
        data_fim: null
      },
      success: false,
      data_inicio: null,
      data_fim: null
    }
  },
  methods: {
    reset() {
      this.success = false
      this.demanda.data_inicio = null
      this.demanda.data_fim = null
    },
    dateConvert(date) {
      return date.getFullYear() + '-' + date.getMonth() + '-' + date.getDate()
    },
    async createDemanda() {
      this.demanda.data_inicio = this.dateConvert(this.data_inicio)
      this.demanda.data_fim = this.dateConvert(this.data_fim)
      try {
        await this.$axios
          .$post(`/ong/${1}/demandas/`, this.demanda)
          .then(response => {
            this.$toast.open({
              message: 'Cadastro realizado com successo!',
              type: 'is-success',
              position: 'is-top'
            })
            this.success = true
          })
          .catch(err => {
            if (!err.response) {
              err.message = 'Servidor desconectado'
            } else if (err.response.status === 400) {
              if (err.response.data.non_field_errors)
                err.message = err.response.data.non_field_errors[0]
            }
            this.$toast.open({
              message: err.message,
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
      } catch (e) {
        this.error = e.response.data.message
      }
    },
    validateBeforeSubmit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          this.createDemanda()
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