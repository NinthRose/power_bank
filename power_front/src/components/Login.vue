<template>
  <div class="create_account">
        手机号：<input type="text" name="phone" placeholder="请输入手机号码" v-model="phone"><br><br>
        密码：<input type="password" name="password" placeholder="请输入密码" v-model="password"><br><br>
    <button @click="fLogin">登录</button>
    <button @click="fLogout">登出</button>
  </div>
</template>

<script>
import { login, logout } from '../api/index'

export default {
  name: 'Login',
  methods: {
    fLogin: function () {
      const data = { phone: this.phone, password: this.password }
      login(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
        })
      })
    },
    fLogout: function () {
      const data = {}
      logout(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
        })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
