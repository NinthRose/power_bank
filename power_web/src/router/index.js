import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Logout from '@/components/Logout'
import Student from '@/components/Student'
import Source from '@/components/Source'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    },
    {
      path: '/student',
      name: 'Student',
      component: Student
    },
    {
      path: '/source',
      name: 'Source',
      component: Source
    }
  ]
})
