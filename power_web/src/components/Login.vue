<template>
  <div id="login">
    <form>
      管理员密码：<input type="password" name='password' placeholder="请输入管理员密码" v-model="password" autocomplete="off"><br><br>
    </form>
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
      const data = { password: this.password }
      login(data).then((response) => {
        response.json().then((res) => {
          if (res.statusCode !== 200) {
            this.$router.push('/login')
          }
          alert(res.message)
        })
      })
    },
    fLogout: function () {
      const data = { }
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
