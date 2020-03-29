<template>
  <section>
    <b-table
      :data="doacoes"
      ref="table"
      :paginated="true"
      :per-page="5"
      :show-detail-icon="true"
      pagination-position="bottom"
      detail-key="id"
      detailed
    >
      <template slot-scope="fProps">
        <b-table-column field="id" label="ID Doação" centered>{{ fProps.row.id }}</b-table-column>

        <b-table-column v-if="isDoador" field="ong" label="ONG" centered>
          <span>{{ fProps && fProps.row.item_doacao[0]  && fProps.row.item_doacao[0].demanda.ong.nome }}</span>
        </b-table-column>
        <b-table-column
          v-else
          field="doador"
          :visible="columnsVisible['doador'].display"
          :label="columnsVisible['doador'].title"
          centered
        >{{ fProps.row.usuario.nome_completo }}</b-table-column>
        <b-table-column
          field="data"
          :visible="columnsVisible['data'].display"
          :label="columnsVisible['data'].title"
          centered
        >
          <span v-if="isDoacaoPendente(fProps.row.item_doacao)" class="tag">PENDENTE</span>
          <span
            v-else-if="isDoacaoCancelada(fProps.row.item_doacao)"
            class="tag is-danger"
          >CANCELADA</span>
          <span v-else class="tag is-success">ENTREGUE</span>
        </b-table-column>
      </template>
      <template slot="detail" slot-scope="fProps">
        <b-table :data="fProps.row.item_doacao">
          <template slot-scope="props">
            <b-table-column
              field="demanda"
              :visible="columnsVisible['demanda'].display"
              :label="columnsVisible['demanda'].title"
              centered
            >{{ props.row.demanda.descricao }}</b-table-column>
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
              <template v-if="props.row.status.codigo_status===1">
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
                  <DoarModal text="Confirmar" :id="props.row.id" :item="props.row"  />
                </b-tooltip>
              </template>

              <span v-else-if="props.row.status.codigo_status===3" class="tag is-success">ENTREGUE</span>
              <span v-else class="tag is-danger">CANCELADA</span>
            </b-table-column>
          </template>
        </b-table>
      </template>
    </b-table>
  </section>
</template>

<script>
import DoarModal from '@/components/molecules/DoarModal.vue'
import EditarModal from '@/components/molecules/EditarDoacaoModal.vue'
import { mapActions, mapGetters } from 'vuex'
export default {
  components: { EditarModal, DoarModal },
  props: {
    isDoador: Boolean,
  },
  computed: {
    user() {
      return this.$store.state.login.usuario;
    },
    ...mapGetters({ doacoes: 'doacoes/doacoes' })
  },

  async mounted() {
    if (this.isDoador) {
      await this.fetchDoacoesDoador(this.user.id)
    } else {
      await this.fetchDoacoesOng(this.user.ong.id)
    }
  },

  methods: {
    isDoacaoPendente(doacao) {
      for (let index = 0; index < doacao.length; index++) {
        if (doacao[index].status.codigo_status === 1) {
          return true
        }
      }
      return false
    },
    isDoacaoCancelada(doacao) {
      for (let index = 0; index < doacao.length; index++) {
        if (doacao[index].status.codigo_status !== 2) {
          return false
        }
      }
      return true
    },
    ...mapActions('doacoes', [
      'fetchDoacoesDoador',
      'fetchDoacoesOng',
      'changeItemDoacao',
      'deleteItemDoacao',
      'confirmaItemDoacao'
    ]),
    toggle(row) {
      this.$refs.table.toggleDetails(row)
    },
    prettyDate(date) {
      date = new Date(date)
      return date.getDate() + '/' + date.getMonth() + '/' + date.getFullYear()
    },
    async confirm(id, acao) {
      this.$buefy.dialog.confirm({

        message: `Tem certeza que deseja ${acao} essa doação?`,
        confirmText: 'Sim',
        cancelText: 'Não',

        onConfirm: async () => {
          if (acao == 'cancelar') {
            await this.deleteItemDoacao(id)
            if (this.isDoador) {
              await this.fetchDoacoesOng(this.user.ong.id)
            } else await this.fetchDoacoesDoador(this.user.id)
          } else {
            await this.confirmaItemDoacao(id)
          }
        }
      })
    }
  },
  data() {
    return {
      columnsVisible: {
        demanda: { title: 'Demanda', display: true },
        efetivado: { title: 'Efetivado', display: true },
        prometido: { title: 'Prometido', display: true },
        doador: { title: 'Doador', display: this.isDoador ? false : true },
        ong: { title: 'ONG', display: this.isDoador ? true : false },
        data: { title: 'Estado', display: true },
        acao: { title: 'Ação', display: true }
      }
    }
  }
}
</script>
<style lang="scss" scoped>
</style>
