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
          field="ong"
          :visible="columnsVisible['ong'].display"
          :label="columnsVisible['ong'].title"
          sortable
          centered
        >{{ props.row.ong }}</b-table-column>

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
          <EditarModal :doacao="props.row" />
          <b-tooltip class="is-danger" label="Cancelar doação" position="is-right">
            <b-icon class="button is-danger is-outlined is-medium" icon="cancel"></b-icon>
          </b-tooltip>
          <b-tooltip
            v-if="!isDoador"
            class="is-success"
            label="Confirmar doação"
            position="is-right"
          >
            <b-icon class="button is-success is-outlined is-medium" icon="check"></b-icon>
          </b-tooltip>
        </b-table-column>
      </template>
    </b-table>
  </section>
</template>

<script>
import EditarModal from '@/components/molecules/EditarDoacaoModal.vue'
export default {
  components: { EditarModal },
  props: {
    isDoador: Boolean
  },
  data() {
    return {
      data: [
        {
          demanda: 'Arroz',
          quantidade: 2,
          ong: 'Canastra',
          doador: 'Ana'
        },
        {
          demanda: 'Feijao',
          quantidade: 3,
          ong: 'Associação Católica Bom Pastor',
          doador: 'Igor'
        },
        {
          demanda: 'Livro',
          quantidade: 12,
          ong: 'Almir do Picolé',
          doador: 'Pedro'
        }
      ],
      columnsVisible: {
        demanda: { title: 'Demanda', display: true },
        quantidade: { title: 'Quantidade', display: true },
        doador: { title: 'Doador', display: this.isDoador ? false : true },
        ong: { title: 'ONG', display: this.isDoador ? true : false },
        acao: { title: 'Ação', display: true }
      }
    }
  }
}
</script>