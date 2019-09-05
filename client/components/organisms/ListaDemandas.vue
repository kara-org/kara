<template>
  <section>
    <b-table class="table" :data="demandas" ref="table" :bordered="false" :striped="true">
      <template slot-scope="props">
        <b-table-column
          field="descricao"
          :visible="columnsVisible['descricao'].display"
          :label="columnsVisible['descricao'].title"
          centered
        >{{ props.row.descricao }}</b-table-column>
        <b-table-column
          field="quantidade_solicitada"
          :visible="columnsVisible['quantidade_solicitada'].display"
          :label="columnsVisible['quantidade_solicitada'].title"
          centered
        >{{ props.row.quantidade_solicitada }}</b-table-column>

        <b-table-column
          field="quantidade_alcancada"
          :visible="columnsVisible['quantidade_alcancada'].display"
          :label="columnsVisible['quantidade_alcancada'].title"
          centered
        >{{ !props.row.quantidade_alcancada ? 0 : props.row.quantidade_alcancada }}</b-table-column>

        <b-table-column
          field="restante"
          :visible="columnsVisible['restante'].display"
          :label="columnsVisible['restante'].title"
          centered
        >{{ qtdRestante(props.row.quantidade_solicitada, props.row.quantidade_alcancada)}}</b-table-column>

        <b-table-column
          field="acao"
          :visible="columnsVisible['acao'].display"
          :label="columnsVisible['acao'].title"
          centered
        >
          <template v-if="props.row.ativo">
            <EditarModal :demanda="props.row" />
            <b-tooltip class="is-danger" label="Inativar demanda" position="is-right">
              <b-button
                class="is-danger is-outlined is-small"
                @click="confirm(props.row.id, 'inativar')"
              >
                <b-icon icon="cancel"></b-icon>
              </b-button>
            </b-tooltip>
          </template>
          <span v-else class="tag is-danger">INATIVA</span>
          <!--<b-tooltip v-else class="is-success" label="Reativar demanda" position="is-right">
            <b-button
              disabled
              class="is-success is-outlined is-small"
              @click="confirm(props.row.id, 'reativar')"
            >
              <b-icon icon="replay"></b-icon>
            </b-button>
          </b-tooltip>-->
        </b-table-column>
        <b-table-column
          :visible="columnsVisible['progresso'].display"
          :label="columnsVisible['progresso'].title"
          centered
        >
          <span
            class="tag is-success"
          >{{ Math.round(( !props.row.quantidade_alcancada ? 0 : props.row.quantidade_alcancada / props.row.quantidade_solicitada) * 100) }}%</span>
        </b-table-column>
      </template>
    </b-table>
  </section>
</template>

<script>
import EditarModal from '@/components/molecules/EditarDemandaModal.vue'
import { mapActions, mapGetters } from 'vuex'
export default {
  components: { EditarModal },
  async mounted() {
    await this.fetchDemandasOng(this.$auth.user.ong.id)
  },
  computed: {
    user() {
      this.$auth.user
    },
    demandas() {
      return this.$store.state.demandas.list
    }
  },
  methods: {
    ...mapGetters({ demandas: 'demandas/demandas' }),
    qtdRestante(qtdSolicitada, qtdAlcancada) {
      var restante = qtdSolicitada - qtdAlcancada
      return restante >= 0 ? restante : 0
    },
    ...mapActions('demandas', [
      'fetchDemandasOng',
      'changeDemanda',
      'deleteDemanda'
    ]),
    async confirm(id, acao) {
      this.$dialog.confirm({
        message: `Tem certeza que deseja ${acao} essa demanda?`,
        confirmText: 'Sim',
        cancelText: 'Não',

        onConfirm: async () => {
          if (acao == 'inativar') {
            await this.deleteDemanda(id)
            await this.fetchDemandasOng(this.user.ong.id)
          } else {
            await this.changeDemanda(id, { ativo: true })
            await this.fetchDemandasOng(this.user.ong.id)
          }
        }
      })
    }
  },
  data() {
    return {
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

<style lang="scss">
.table {
  overflow-x: hidden;
  max-height: 400px;
  overflow-y: auto;
}
</style>