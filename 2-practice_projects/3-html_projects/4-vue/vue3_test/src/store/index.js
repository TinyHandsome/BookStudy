import { createStore } from 'vuex'

export default createStore({
  state: {
    isTabbarShow: true,
  },
  getters: {
  },
  mutations: {
    hide(state) {
      state.isTabbarShow = false
    },
    show(state) {
      state.isTabbarShow = true
    }
  },
  actions: {
  },
  modules: {
  }
})
