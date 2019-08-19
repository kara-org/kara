<template>
  <section>
    <b-table
      :data="data"
      ref="table"
      :paginated="isPaginated"
      :per-page="perPage"
      :current-page.sync="currentPage"
      :pagination-position="paginationPosition"
    >
      <template slot-scope="fProps">
        <b-table :data="fProps.row.itens_doacao">
          <template slot-scope="props">
            <b-table-column
              field="demanda"
              :visible="columnsVisible['demanda'].display"
              :label="columnsVisible['demanda'].title"
              centered
            >{{ props.row.demanda_id }}</b-table-column>
            <b-table-column
              field="data"
              :visible="columnsVisible['data'].display"
              :label="columnsVisible['data'].title"
              centered
            >
              <span
                class="tag is-success"
              >{{ new Date(fProps.row.data_agendamento).toLocaleDateString() }}</span>
            </b-table-column>

            <b-table-column
              field="doador"
              :visible="columnsVisible['doador'].display"
              :label="columnsVisible['doador'].title"
              centered
            >{{ fProps.row.usuario }}</b-table-column>

            <b-table-column
              field="ong"
              :visible="columnsVisible['ong'].display"
              :label="columnsVisible['ong'].title"
              centered
            >{{ fProps.row.usuario }}</b-table-column>

            <b-table-column
              field="prometido"
              :visible="columnsVisible['prometido'].display"
              :label="columnsVisible['prometido'].title"
              centered
            >{{ props.row.quantidade_prometida }}</b-table-column>
            <b-table-column
              field="efetivado"
              :visible="columnsVisible['efetivado'].display"
              :label="columnsVisible['efetivado'].title"
              centered
            >{{ !props.row.quantidade_efetivada ? 0 : props.row.quantidade_efetivada }}</b-table-column>

            <b-table-column
              field="acao"
              :visible="columnsVisible['acao'].display"
              :label="columnsVisible['acao'].title"
              centered
            >
              <template v-if="props.row.status_id==3">
                <EditarModal v-if="isDoador" :doacao="props.row" />
                <b-tooltip class="is-danger" label="Cancelar doação" position="is-right">
                  <b-button
                    class="is-danger is-outlined is-small"
                    @click="confirm(props.row.id, 'cancelar')"
                  >
                    <b-icon icon="cancel"></b-icon>
                  </b-button>
                </b-tooltip>
                <b-tooltip
                  v-if="!isDoador"
                  class="is-success"
                  label="Confirmar doação"
                  position="is-right"
                >
                  <b-button
                    class="is-success is-outlined is-small"
                    @click="confirm(props.row.id, 'confirmar')"
                  >
                    <b-icon icon="check"></b-icon>
                  </b-button>
                </b-tooltip>
              </template>

              <span v-else-if="props.row.status_id==1" class="tag is-success">CONFIRMADA</span>
              <span v-else class="tag is-danger">CANCELADA</span>
            </b-table-column>
          </template>
        </b-table>
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
  async mounted() {
    if (this.isDoador) {
      this.data = await this.$axios.$get(`/doador/${1}/doacoes/`)
      console.log(this.data)
    } else {
      this.data = await this.$axios.$get(`/ong/${1}/doacoes/`)
      console.log(this.data)
    }
  },
  methods: {
    prettyDate(date) {
      date = new Date(date)
      return date.getDate() + '/' + date.getMonth() + '/' + date.getFullYear()
    },
    async confirm(id, acao) {
      this.$dialog.confirm({
        message: `Tem certeza que deseja ${acao} essa doação?`,
        confirmText: 'Sim',
        cancelText: 'Não',

        onConfirm: () => {
          if (acao == 'cancelar') {
            //this.$axios.$post(`/doacao/${id}/confirmar`)
            //this.mounted()
          } else {
            //this.$axios.$post(`/doacao/${id}/cancelar`)
            //this.mounted()
          }
        }
      })
    }
  },
  data() {
    return {
      data: [],
      columnsVisible: {
        demanda: { title: 'Demanda', display: true },
        efetivado: { title: 'Efetivado', display: true },
        prometido: { title: 'Prometido', display: true },
        doador: { title: 'Doador', display: this.isDoador ? false : true },
        ong: { title: 'ONG', display: this.isDoador ? true : false },
        data: { title: 'Data agendada', display: true },
        acao: { title: 'Ação', display: true }
      },
      isPaginated: true,
      paginationPosition: 'bottom',
      currentPage: 1,
      perPage: 1
    }
  }
}
</script>