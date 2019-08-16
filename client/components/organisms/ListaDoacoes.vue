<template>
  <section>
    <b-table :data="data" ref="table" :default-sort="['demanda', 'asc']">
      <template slot-scope="props">
        <b-table-column
          field="demanda"
          :visible="columnsVisible['demanda'].display"
          :label="columnsVisible['demanda'].title"
          sortable
        >{{ props.row.demanda }}</b-table-column>

        <b-table-column
          field="doador"
          :visible="columnsVisible['doador'].display"
          :label="columnsVisible['doador'].title"
          sortable
          centered
        >{{ props.row.doador }}</b-table-column>

        <b-table-column
          field="quantidade"
          :visible="columnsVisible['quantidade'].display"
          :label="columnsVisible['quantidade'].title"
          sortable
          centered
        >{{ props.row.quantidade }}</b-table-column>

        <b-table-column
          field="acao"
          :visible="columnsVisible['acao'].display"
          :label="columnsVisible['acao'].title"
          centered
        >
          <b-icon class="button is-danger is-outlined is-medium" icon="cancel"></b-icon>
          <b-icon class="button is-primary is-outlined is-medium" icon="check"></b-icon>
        </b-table-column>
      </template>
    </b-table>
  </section>
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          demanda: 'Arroz',
          quantidade: 2,
          doador: 'Ana'
        },
        {
          demanda: 'Feijao',
          quantidade: 3,
          doador: 'Igor'
        },
        {
          demanda: 'Livro',
          quantidade: 12,
          doador: 'Pedro'
        }
      ],
      columnsVisible: {
        demanda: { title: 'Demanda', display: true },
        quantidade: { title: 'Quantidade', display: true },
        doador: { title: 'Doador', display: true },
        acao: { title: 'Cancelar/Confirmar', display: true }
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