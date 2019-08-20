<template>
  <section>
    <b-table
      :data="data"
      ref="table"
      :paginated="isPaginated"
      :per-page="perPage"
      :current-page.sync="currentPage"
      :pagination-position="paginationPosition"
      :pagination-simple="isPaginationSimple"
    >
      <template slot-scope="props">
        <b-table-column
          field="descricao"
          :visible="columnsVisible['descricao'].display"
          :label="columnsVisible['descricao'].title"
          sortable
        >{{ props.row.descricao }}</b-table-column>
        <b-table-column
          field="quantidade_solicitada"
          :visible="columnsVisible['quantidade_solicitada'].display"
          :label="columnsVisible['quantidade_solicitada'].title"
          sortable
          centered
        >{{ props.row.quantidade_solicitada }}</b-table-column>

        <b-table-column
          field="quantidade_alcancada"
          :visible="columnsVisible['quantidade_alcancada'].display"
          :label="columnsVisible['quantidade_alcancada'].title"
          sortable
          centered
        >{{ !props.row.quantidade_alcancada ? 0 : props.row.quantidade_alcancada }}</b-table-column>

        <b-table-column
          field="restante"
          :visible="columnsVisible['restante'].display"
          :label="columnsVisible['restante'].title"
          centered
        >{{ props.row.quantidade_solicitada - (!props.row.quantidade_alcancada ? 0 : props.row.quantidade_alcancada) }}</b-table-column>
        <b-table-column
          :visible="columnsVisible['progresso'].display"
          :label="columnsVisible['progresso'].title"
          centered
        >
          <span
            class="tag is-success"
          >{{ Math.round(( !props.row.quantidade_alcancada ? 0 : props.row.quantidade_alcancada / props.row.quantidade_solicitada) * 100) }}%</span>
        </b-table-column>
        <b-table-column
          field="acao"
          :visible="columnsVisible['acao'].display"
          :label="columnsVisible['acao'].title"
          centered
        >
          <EditarModal :demanda="props.row" />
          <b-tooltip
            v-if="props.row.ativo"
            class="is-danger"
            label="Inativar demanda"
            position="is-right"
          >
            <b-button
              class="is-danger is-outlined is-small"
              @click="confirm(props.row.id, 'inativar')"
            >
              <b-icon icon="cancel"></b-icon>
            </b-button>
          </b-tooltip>
          <b-tooltip v-else class="is-success" label="Reativar demanda" position="is-right">
            <b-button disabled
              class="is-success is-outlined is-small"
              @click="confirm(props.row.id, 'reativar')"
            >
              <b-icon icon="replay"></b-icon>
            </b-button>
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
    this.data = await this.$axios.$get(`/ong/${1}/demandas/`)
    console.log(this.data)
  },
  methods: {
    /* async reativar(id) {
      this.$axios.$patch(`/demanda/${id}/`, { ativo: true })
      this.data = await this.$axios.$get(`/ong/${1}/demandas/`)
    },
    async inativar(id) {
      this.$axios.$delete(`/demanda/${id}/cancelar`)
      this.data = await this.$axios.$get(`/ong/${1}/demandas/`)
    }, */
    async confirm(id, acao) {
      this.$dialog.confirm({
        message: `Tem certeza que deseja ${acao} essa demanda?`,
        confirmText: 'Sim',
        cancelText: 'Não',

        onConfirm: () => {
          if (acao == 'inativar') {
            this.$axios.$delete(`/demanda/${id}/cancelar`)
          } else {
            this.$axios.$patch(`/demanda/${id}/`, { ativo: true })
          }
        }
      })
    }
  },
  data() {
    return {
      data: [],
      columnsVisible: {
        descricao: { title: 'Título', display: true },
        quantidade_solicitada: { title: 'Esperado', display: true },
        quantidade_alcancada: { title: 'Doado', display: true },
        restante: { title: 'Restante', display: true },
        acao: { title: 'Ação', display: true },
        progresso: { title: 'Progresso', display: true }
      },
      isPaginated: true,
      paginationPosition: 'bottom',
      currentPage: 1,
      perPage: 5,
      isPaginationSimple: true
    }
  }
}
</script>