import Cookies from 'js-cookie'
import { getLanguage } from '@/lang/index'

const state = {
    language: getLanguage(),
}

const mutations ={
    setLanguage: (state, language) => {
        state.language = language
        Cookies.set('language', language)
    },
}

const actions={
    setLanguage({ commit }, language) {
        commit('setLanguage', language)
    },
}


export default {
    namespaced: true,
    state,
    mutations,
    actions
}
