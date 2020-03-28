import LoginService from "../services/LoginService";

let serviceUser = new LoginService();

export const state = () => ({
    usuario: {}
});

export const mutations = {
    SET(state, user) {
        state.usuario = user;
    }
};

export const actions = {
    async fetch({ commit }) {
        let user = await serviceUser.currentUser();
        commit("SET", user);
    }
};
