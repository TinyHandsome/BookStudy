<template>
  <footer>
    <ul>
      <!-- <li>
        <router-link to="/films">电影</router-link>
      </li>
      <li>
        <router-link to="/cinemas">影院</router-link>
      </li>
      <li>
        <router-link to="/center">我的</router-link>
      </li> -->
      <router-link to="/films" custom v-slot="{ navigate, isActive }">
        <li @click="navigate" :class="isActive ? 'kerwinactive' : ''">
          <i class="iconfont icon-Dyanjing"></i>
          <span>电影</span>
        </li>
      </router-link>
      <router-link to="/cinemas" custom v-slot="{ navigate, isActive }">
        <li @click="navigate" :class="isActive ? 'kerwinactive' : ''">
          <i class="iconfont icon-anquan"></i>
          <span>影院</span>
        </li>
      </router-link>
      <router-link to="/center" custom v-slot="{ navigate, isActive }">
        <li @click="navigate" :class="isActive ? 'kerwinactive' : ''">
          <i class="iconfont icon-aixin"></i>
          <span>我的</span>
        </li>
      </router-link>

      <!-- <li><a href="/#/films">电影</a></li>
      <li><a href="/#/cinemas">影院</a></li>
      <li><a href="/#/center">我的</a></li> -->
    </ul>
  </footer>
</template>

<style lang="scss" scoped>
footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 3.0625rem;
  background: white;
  z-index: 100;

  ul {
    display: flex;
    li {
      flex: 1;
      line-height: 1.5625rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      i {
        font-size: 20px;
      }
      span {
        font-size: 16px;
      }
    }
  }

  .kerwinactive {
    color: red;
    font-weight: bold;
  }
}
</style>
