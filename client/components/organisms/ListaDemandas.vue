<template>
  <section>
    <b-table :data="data" ref="table" :default-sort="['nome', 'asc']">
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
          sortable
          centered
        >{{ props.row.restante }}</b-table-column>
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
          <EditarModal :text="Editar"/>
          <b-icon class="button is-danger is-medium" icon="cancel"></b-icon>
          <b-icon class="button is-success is-medium" icon="check"></b-icon>
        </b-table-column>
      </template>
    </b-table>
  </section>
</template>

<script>
import EditarModal from '@/components/molecules/EditarDemandaModal.vue'
export default {
  components: { EditarModal },
  data() {
    return {
      data: [
        {
          nome: 'Arroz',
          esperado: 442,
          doado: 131,
          restante: 301
        },
        {
          nome: 'Feijao',
          esperado: 255,
          doado: 88,
          restante: 167
        },
        {
          nome: 'Livro',
          esperado: 1155,
          doado: 434,
          restante: 721
        }
      ],
      columnsVisible: {
        nome: { title: 'Nome', display: true },
        esperado: { title: 'Esperado', display: true },
        doado: { title: 'Doado', display: true },
        restante: { title: 'Restante', display: true },
        acao: { title: 'Editar/Cancelar/Finalizar', display: true },
        progresso: { title: 'Progresso', display: true }
      }
    }
  },
  methods: {
    toggle(row) {
      this.$refs.table.toggleDetails(row)
    }
  }
}
</script>