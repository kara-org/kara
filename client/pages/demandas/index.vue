<template>
  <section class="section">
    <section>
        <b-field grouped group-multiline>
            <b-select v-model="defaultSortDirection">
                <option value="asc">Default sort direction: ASC</option>
                <option value="desc">Default sort direction: DESC</option>
            </b-select>
            <b-select v-model="perPage" :disabled="!isPaginated">
                <option value="5">5 per page</option>
                <option value="10">10 per page</option>
                <option value="15">15 per page</option>
                <option value="20">20 per page</option>
            </b-select>
            <div class="control">
                <button class="button" @click="currentPage = 2" :disabled="!isPaginated">Set page to 2</button>
            </div>
            <div class="control is-flex">
                <b-switch v-model="isPaginated">Paginated</b-switch>
            </div>
            <div class="control is-flex">
                <b-switch v-model="isPaginationSimple" :disabled="!isPaginated">Simple pagination</b-switch>
            </div>
            <b-select v-model="paginationPosition" :disabled="!isPaginated">
                <option value="bottom">bottom pagination</option>
                <option value="top">top pagination</option>
                <option value="both">both</option>
            </b-select>
        </b-field>

        <b-table
            :data="data"
            :paginated="isPaginated"
            :per-page="perPage"
            :current-page.sync="currentPage"
            :pagination-simple="isPaginationSimple"
            :pagination-position="paginationPosition"
            :default-sort-direction="defaultSortDirection"
            default-sort="user.first_name"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page">

            <template slot-scope="props">
                <b-table-column field="id" label="ID" width="40" sortable numeric>
                    {{ props.row.id }}
                </b-table-column>

                <b-table-column field="nome" label="Nome do produto" sortable>
                    {{ props.row.nome }}
                </b-table-column>

                <b-table-column field="quantidade" label="Last Name" sortable>
                    {{ props.row.quantidade }}
                </b-table-column>

                <b-table-column field="date" label="Prazo" sortable centered>
                    <span class="tag is-success">
                        {{ new Date(props.row.date).toLocaleDateString() }}
                    </span>
                </b-table-column>

                <b-table-column label="Gender">
                    <b-icon pack="fas"
                        :icon="props.row.gender === 'Male' ? 'mars' : 'venus'">
                    </b-icon>
                    {{ props.row.gender }}
                </b-table-column>
            </template>
        </b-table>
    </section>
  </section>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  layout: 'inside',
  middleware: 'auth',
  async data () {
    return {
      data: await this.$store.ongs.state.demandas
    }
  },
  beforeCreate () {
    this.fetchDemandas()
  },
  methods: {
    ...mapActions('ongs', ['fetchDemandas'])
  },
}
</script>
