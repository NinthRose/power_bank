import Vue from 'vue'
import Router from 'vue-router'
import CreateAccount from '@/components/CreateAccount'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'CreateAccount',
      component: CreateAccount
    }
  ]
})
