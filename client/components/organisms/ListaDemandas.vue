<template>
  <section>
    <b-table class="table" :data="demandas" ref="table" :bordered="false" :striped="true">
      <template slot-scope="props">
        <b-table-column
          field="nome"
          :visible="columnsVisible['nome'].display"
          :label="columnsVisible['nome'].title"
          centered
        >{{ props.row.nome }}</b-table-column>
        <b-table-column
          field="quantidadeDesejada"
          :visible="columnsVisible['quantidadeDesejada'].display"
          :label="columnsVisible['quantidadeDesejada'].title"
          centered
        >{{ props.row.quantidadeDesejada }}</b-table-column>

        <b-table-column
          field="quantidadeAlcancada"
          :visible="columnsVisible['quantidadeAlcancada'].display"
          :label="columnsVisible['quantidadeAlcancada'].title"
          centered
        >{{ !props.row.quantidadeAlcancada ? 0 : props.row.quantidadeAlcancada }}</b-table-column>

        <b-table-column
          field="restante"
          :visible="columnsVisible['restante'].display"
          :label="columnsVisible['restante'].title"
          centered
        >{{ qtdRestante(props.row.quantidadeDesejada, props.row.quantidadeAlcancada)}}</b-table-column>

        <b-table-column
          field="acao"
          :visible="columnsVisible['acao'].display"
          :label="columnsVisible['acao'].title"
          centered
        >
          <template v-if="props.row.ativo">
            <nuxt-link
              :to="`/ong/demandas/editar/${props.row.objectId}`"
              exact-active-class="is-outlined is-success is-small"
            >
              <b-icon icon="settings"></b-icon>
            </nuxt-link>
            <b-tooltip class="is-danger" label="Inativar demanda" position="is-right">
              <b-button
                class="is-danger is-outlined is-small"
                @click="inativar(props.row)"
              >
                <b-icon icon="cancel"></b-icon>
              </b-button>
            </b-tooltip>
          </template>
          <!-- <span v-else class="tag is-danger">INATIVA</span> -->
          <b-tooltip v-else class="is-info" label="Reativar demanda" position="is-right">
            <b-button
              class="is-info is-outlined is-small"
              @click="inativar(props.row)"
            >
              <b-icon icon="replay"></b-icon>
            </b-button>
          </b-tooltip>
        </b-table-column>
        <b-table-column
          :visible="columnsVisible['progresso'].display"
          :label="columnsVisible['progresso'].title"
          centered
        >
          <span
            class="tag is-success"
          >{{ Math.round(( !props.row.quantidadeAlcancada ? 0 : props.row.quantidadeAlcancada / props.row.quantidadeDesejada) * 100) }}%</span>
        </b-table-column>
      </template>
    </b-table>
  </section>
</template>

<script>
import EditarModal from '@/components/molecules/EditarDemandaModal.vue';
import { mapActions, mapGetters } from 'vuex';
export default {
  components: { EditarModal },
  props: {
    demandas: Array
  },
  computed: {
    ...mapGetters({ user: 'login/usuario' })
  },
  methods: {
    qtdRestante(qtdSolicitada, qtdAlcancada) {
      var restante = qtdSolicitada - qtdAlcancada;
      return restante >= 0 ? restante : 0;
    },
    ...mapActions('demandas', [
      'fetchDemandasOng',
      'changeDemanda',
      'inativaAtiva'
    ]),
    async inativar(demanda) {
      this.$buefy.dialog.confirm({
        message: `Tem certeza que deseja inativar essa demanda?`,
        confirmText: 'Sim',
        cancelText: 'Não',

        onConfirm: async () => {
          await this.inativaAtiva(demanda);
          await this.fetchDemandasOng();
        }
      });
    }
  },
  data() {
    return {
      columnsVisible: {
        nome: { title: 'Título', display: true },
        quantidadeDesejada: { title: 'Esperado', display: true },
        quantidadeAlcancada: { title: 'Doado', display: true },
        restante: { title: 'Restante', display: true },
        acao: { title: 'Ação', display: true },
        progresso: { title: 'Progresso', display: true }
      },
      isPaginated: true,
      paginationPosition: 'bottom',
      currentPage: 1,
      perPage: 5,
      isPaginationSimple: true
    };
  }
};
</script>

<style lang="scss">
.table {
  overflow-x: hidden;
  max-height: 400px;
  overflow-y: auto;
}
</style>
