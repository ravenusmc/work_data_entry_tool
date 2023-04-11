import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index';
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/analyze',
    name: 'Analyze',
    component: () => import(/* webpackChunkName: "about" */ '../views/Analyze.vue')
  },
  {
    path: '/main',
    name: 'main',
    component: () => import(/* webpackChunkName: "about" */ '../views/Main.vue'),
    // beforeEnter: (to, from, next) => {
    //   if (store.state.common.loginFlag === false) {
    //     next('/login');
    //   } else {
    //     next();
    //   }
    // },
    // beforeRouteLeave: (to, from, next) => {
    //   if (store.state.common.loginFlag === false) {
    //     next('/login');
    //   } else {
    //     next();
    //   }
    // },
  },
  {
    path: '/sign_up',
    name: 'signup',
    component: () => import('../views/SignUp.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
