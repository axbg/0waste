import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import Toasted from 'vue-toasted';
import axios from 'axios';

const Options = {
  duration: 1500,
  singleton: true,
  position: 'bottom-center'
};

Vue.config.productionTip = false
Vue.use(VueMaterial)
Vue.use(Toasted, Options)
Vue.prototype.$axios = axios;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
