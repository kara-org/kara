<template>
  <section>
    <b-table :data="data" ref="table">
      <template slot-scope="props">
        <b-table-column
          field="nome"
          :visible="columnsVisible['nome'].display"
          :label="columnsVisible['nome'].title"
          sortable
        >{{ props.row.nome }}</b-table-column>
        <b-table-column
          field="esperado"
          :visible="columnsVisible['esperado'].display"
          :label="columnsVisible['esperado'].title"
          sortable
          centered
        >{{ props.row.esperado }}</b-table-column>

        <b-table-column
          field="doado"
          :visible="columnsVisible['doado'].display"
          :label="columnsVisible['doado'].title"
          sortable
          centered
        >{{ props.row.doado }}</b-table-column>

        <b-table-column
          field="restante"
          :visible="columnsVisible['restante'].display"
          :label="columnsVisible['restante'].title"
          centered
        >{{ props.row.esperado - props.row.doado }}</b-table-column>
        <b-table-column
          :visible="columnsVisible['progresso'].display"
          :label="columnsVisible['progresso'].title"
          centered
        >
          <span
            class="tag is-success"
          >{{ Math.round(( props.row.doado / props.row.esperado) * 100) }}%</span>
        </b-table-column>

        <b-table-column
          field="acao"
          :visible="columnsVisible['acao'].display"
          :label="columnsVisible['acao'].title"
          centered
        >
          <EditarModal :demanda="props.row" />
          <b-tooltip class="is-danger" label="Cancelar demanda" position="is-right">
            <b-icon class="button is-danger is-outlined is-medium" icon="cancel"></b-icon>
          </b-tooltip>
          <b-tooltip class="is-success" label="Finalizar demanda" position="is-right">
            <b-icon class="button is-success is-outlined is-medium" icon="check"></b-icon>
          </b-tooltip>
        </b-table-column>
      </template>
    </b-table>
  </section>
</template>

<script>
import EditarModal from '@/components/molecules/EditarDemandaModal.vue'
import { mapActions } from 'vuex'
export default {
  components: { EditarModal },
  async mounted() {
    this.fetchDemandas()
    this.data = await this.$store.state.ongs.demandas
    console.log(this.data)
  },
  methods: {
    ...mapActions('ongs', ['fetchDemandas'])
  },
  data() {
    return {
      data: [],
      columnsVisible: {
        nome: { title: 'Nome', display: true },
        esperado: { title: 'Esperado', display: true },
        doado: { title: 'Doado', display: true },
        restante: { title: 'Restante', display: true },
        acao: { title: 'Editar/Cancelar/Finalizar', display: true },
        progresso: { title: 'Progresso', display: true }
      }
    }
  }
}
</script>