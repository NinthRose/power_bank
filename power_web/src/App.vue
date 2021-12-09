<template>
  <div id="app">
    <img src="./assets/logo.jpeg">
    <p></p>
    管理员密码：<input type="password" name="key" placeholder="请输入管理员密码" v-model="key"><br><br>
    <router-link to="/login">
     <button @click="fLogin" class="login">登录</button>
    </router-link>
    <router-link to="/logout">
     <button @click="fLogout" class="logout">登出</button>
    </router-link>
    <router-view/>
  </div>
</template>

<script>
import { login, logout } from './api/index'

export default {
  name: 'App',
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
img {
  width: 1%;
  height: 1%;
  top: 5%;
  left: 5%;
  border-left: 5%;
}

button:checked {
  display: none;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
