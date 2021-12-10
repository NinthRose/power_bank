<template>
  <div id="app">
    管理员密码：<input type="password" name="key" placeholder="请输入管理员密码" v-model="key"><br><br>
    <router-link to="/powerMenu">
     <button @click="fLogin" class="login">登录</button>
    </router-link>
    <router-link to="/">
     <button @click="fLogout" class="logout">登出</button>
    </router-link>
  </div>
</template>

<script>
import { login, logout } from '../api/index'

export default {
  name: 'Login',
  methods: {
    fLogin: function () {
      const data = { password: this.key }
      login(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
        })
      })
    },
    fLogout: function () {
      const data = { key: this.key }
      logout(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
        })
      })
    }
  }
}
</script>

<style>
</style>
