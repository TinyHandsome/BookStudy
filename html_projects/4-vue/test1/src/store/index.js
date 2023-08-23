import Vue from 'vue'
import Vuex from 'vuex'
import http from "@/util/http";
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState({
    reducer: (state) => {
      return {
        cityId: state.cityId,
        cityName: state.cityName
      }
    }
  })],
  // 公共状态
  state: {
    cityId: '310100',
    cityName: '上海',
    cinemaList: [],
    isTabbarShow: true,
  },
  getters: {
  },
  // 改变状态的方法：统一管理，被devtools记录了状态的修改
  mutations: {
    changeCityName(state, cityName) {
      // console.log(cityName);
      state.cityName = cityName
    },
    changeCityId(state, cityId) {
      state.cityId = cityId
    },
    changeCinemaData(state, data) {
      state.cinemaList = data
    },
    clearCinema(state) {
      state.cinemaList = []
    },

    show(state) {
      state.isTabbarShow = true
    },
    hide(state) {
      state.isTabbarShow = false
    }
  },
  // 支持异步和同步
  actions: {
    getCinemaData(store, cityId) {
      // console.log("get-actions");
      return http({
        url: `/gateway?cityId=${cityId}&ticketFlag=1&k=4312294`,
        headers: {
          "X-Host": "mall.film-ticket.cinema.list",
        },
      }).then((res) => {
        // console.log(res.data.data.cinemas);
        // this.cinemaList = res.data.data.cinemas;

        // this.$nextTick(() => {
        //   new BetterScroll(".box", {
        //     scrollbar: {
        //       fade: true,
        //     },
        //   });
        // });
        store.commit("changeCinemaData", res.data.data.cinemas)
      });
    }
  },
  modules: {
  }
})
