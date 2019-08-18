export default {
    namespaced: true,
    state() {
        return {
            demandas: [
            ],
        }
    },
    mutations: {
        adicionarDemanda(state, payload) {
            state.demandas.push(payload)
        },
    },
    actions: {
        adicionarDemanda(context, payload) {
            setTimeout(() => {
                context.commit('adicionarDemanda', payload)
            }, 200)
        }
    }
}