import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import FastTracking from '../views/FastTracking.vue'
import Impact from '../views/Impact.vue'
import Catalogue from '../views/Catalogue.vue'

Vue.use(VueRouter)

const baseUrl = "http://localhost:8081";
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    props: { baseUrl: baseUrl }
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    props: { baseUrl: baseUrl }
  },
  {
    path: '/fast',
    name: 'fast',
    component: FastTracking,
    props: { baseUrl: baseUrl }
  },
  {
    path: '/impact',
    name: 'impact',
    component: Impact,
    props: { baseUrl: baseUrl }
  },
  {
    path: '/catalogue',
    name: 'catalogue',
    component: Catalogue,
    props: { baseUrl: baseUrl }
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (localStorage.getItem("username")) {
    if (to.name === "login") {
      next("/")
    } else {
      next();
    }
  } else if (to.name === "login") {
    next();
  } else {
    next("/login");
  }
});

export default router