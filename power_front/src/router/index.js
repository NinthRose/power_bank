import Vue from 'vue'
import Router from 'vue-router'
import CreateAccount from '@/components/CreateAccount'
import Login from '@/components/Login'
import ResetAccount from '@/components/ResetAccount'
import SearchAccount from '@/components/SearchAccount'

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
    },
    {
      path: '/resetAccount',
      name: 'ResetAccount',
      component: ResetAccount
    },
    {
      path: '/searchAccount',
      name: 'SearchAccount',
      component: SearchAccount
    }
  ]
})
