import Vue from 'vue'
import Router from 'vue-router'
import CreateAccount from '@/components/CreateAccount'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/createAccount',
      name: 'CreateAccount',
      component: CreateAccount
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
