import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Student from '@/components/Student'
import Lesson from '@/components/Lesson'
import PowerMenu from '@/components/PowerMenu'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    }, {
      path: '/powerMenu',
      name: 'PowerMenu',
      component: PowerMenu,
      children: [{
        path: '/student',
        component: Student
      }, {
        path: '/lesson',
        component: Lesson
      }]
    }
  ]
})
