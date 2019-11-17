import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import FastTracking from '../views/FastTracking.vue'
import Menu from '../views/Menu.vue'
import Impact from '../views/Impact.vue'
import Catalogue from '../views/Catalogue.vue'

Vue.use(VueRouter)

const baseUrl = "http://localhost:8081/api";
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    props: { baseUrl: baseUrl },
    children: [
      {
        path: '/',
        name: 'menu',
        component: Menu,
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
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    props: { baseUrl: baseUrl }
  }
]

const router = new VueRouter({
  routes
})

export default router