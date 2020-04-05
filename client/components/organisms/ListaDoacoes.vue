<template>
  <section>
    <b-table
      :data="doacoes"
      ref="table"
      :paginated="true"
      :per-page="5"
      :show-detail-icon="true"
      pagination-position="bottom"
      detail-key="objectId"
      detailed
    >
      <template slot-scope="columnDoacoes">
        <b-table-column v-if="isDoador" field="ong" label="ONG" centered>
          <span>{{ columnDoacoes.row.ong.nome }}</span>
        </b-table-column>
        <b-table-column
          v-else
          field="doador"
          :visible="columnsVisible['doador'].display"
          :label="columnsVisible['doador'].title"
          centered
          >{{ nome(columnDoacoes.row.user.nome) }}</b-table-column
        >
        <b-table-column field="telefone" label="Telefone" centered>{{
          telefone(columnDoacoes.row)
        }}</b-table-column>
        <b-table-column field="email" label="Email" centered>{{
          email(columnDoacoes.row)
        }}</b-table-column>

        <b-table-column
          field="situacao"
          :visible="columnsVisible['situacao'].display"
          :label="columnsVisible['situacao'].title"
          centered
        >
          <span
            :class="
              getTagStatusDoacao(getStatusDoacao(columnDoacoes.row.demandas))
            "
            >{{ getStatusDoacao(columnDoacoes.row.demandas) }}</span
          >
        </b-table-column>
      </template>
      <template slot="detail" slot-scope="columnDoacoes">
        <b-table :data="columnDoacoes.row.demandas">
          <template slot-scope="columnItemDoacao">
            <b-table-column
              field="demanda"
              :visible="columnsVisible['demanda'].display"
              :label="columnsVisible['demanda'].title"
              centered
              >{{ columnItemDoacao.row.demanda.nome }}</b-table-column
            >
            <b-table-column
              field="prometido"
              :visible="columnsVisible['prometido'].display"
              :label="columnsVisible['prometido'].title"
              centered
              >{{ columnItemDoacao.row.quantidadePrometida }}</b-table-column
            >
            <b-table-column
              field="efetivado"
              :visible="columnsVisible['efetivado'].display"
              :label="columnsVisible['efetivado'].title"
              centered
              >{{
                !columnItemDoacao.row.quantidadeEfetivada
                  ? 0
                  : columnItemDoacao.row.quantidadeEfetivada
              }}</b-table-column
            >

            <b-table-column
              field="acao"
              :visible="columnsVisible['acao'].display"
              :label="columnsVisible['acao'].title"
              centered
            >
              <span v-if="columnItemDoacao.row.entregue" class="tag is-success"
                >ENTREGUE</span
              >
              <span
                v-else-if="columnItemDoacao.row.cancelado"
                class="tag is-danger"
                >CANCELADA</span
              >
              <template v-else>
                <EditarModal v-if="isDoador" :doacao="columnItemDoacao.row" />
                <b-tooltip
                  class="is-danger"
                  label="Cancelar doação"
                  position="is-right"
                >
                  <b-button
                    class="is-danger is-outlined is-small"
                    @click="cancel(columnItemDoacao.row.objectId)"
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
                  <DoarModal
                    text="Confirmar"
                    :idOng="columnItemDoacao.row.demanda.ong.objectId"
                    :item="columnItemDoacao.row"
                  />
                </b-tooltip>
              </template>
            </b-table-column>
          </template>
        </b-table>
      </template>
    </b-table>
  </section>
</template>

<script>
import DoarModal from '@/components/molecules/DoarModal.vue';
import EditarModal from '@/components/molecules/EditarDoacaoModal.vue';
import { mapActions, mapGetters } from 'vuex';
export default {
  components: { EditarModal, DoarModal },
  props: {
    isDoador: Boolean
  },
  computed: {
    ...mapGetters({ doacoes: 'doacoes/doacoes', user: 'login/usuario' })
  },
  mounted() {
    if (this.isDoador) this.fetchDoacoesDoador(this.user.objectId);
    else this.fetchDoacoesOng(this.user.ong.objectId);
  },
  methods: {
    nome(nome) {
      let nomes = nome.split(' ');
      return nomes[0] + (nomes.length > 1 ? ' ' + nomes[nomes.length - 1] : '');
    },
    telefone(doacao) {
      let telefone;
      if (this.isDoador) telefone = doacao.ong.telefones[0];
      if (!this.isDoador) telefone = doacao.user.telefones[0];

      if (telefone) {
        let last = telefone.length - 4;
        telefone = `(${telefone.substring(0, 2)}) ${telefone.substring(
          2,
          last
        )}-${telefone.substring(last)}`;
      }
      return telefone;
    },
    email(doacao) {
      if (this.isDoador) return doacao.ong.email;
      if (!this.isDoador)
        return doacao.user.email ? doacao.user.email : doacao.user.username;
    },
    getStatusDoacao(itensDoacao) {
      let status = 'CANCELADA';
      itensDoacao.forEach(item => {
        if (item.entregue) status = 'ENTREGUE';
        if (!item.cancelado && !item.entregue) return (status = 'PENDENTE');
      });
      return status;
    },
    getTagStatusDoacao(status) {
      switch (status) {
        case 'PENDENTE':
          return 'tag';
          break;
        case 'CANCELADA':
          return 'tag is-danger';
          break;
        default:
          return 'tag is-success';
          break;
      }
    },
    ...mapActions('doacoes', [
      'fetchDoacoesDoador',
      'fetchDoacoesOng',
      'changeItemDoacao',
      'deleteItemDoacao',
      'confirmaItemDoacao'
    ]),
    toggle(row) {
      this.$refs.table.toggleDetails(row);
    },
    prettyDate(date) {
      date = new Date(date);
      return date.getDate() + '/' + date.getMonth() + '/' + date.getFullYear();
    },
    async cancel(objectId) {
      this.$buefy.dialog.confirm({
        message: `Tem certeza que deseja cancelar este item?`,
        confirmText: 'Sim',
        cancelText: 'Não',

        onConfirm: async () => {
          await this.deleteItemDoacao(objectId);
          if (this.isDoador) await this.fetchDoacoesDoador(this.user.objectId);
          else await this.fetchDoacoesOng(this.user.ong.objectId);
        }
      });
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
        situacao: { title: 'Situação', display: true },
        acao: { title: 'Ação', display: true }
      }
    };
  }
};
</script>
<style lang="scss" scoped></style>
