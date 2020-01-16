<template>
  <div id="app">
    <img src="./assets/logo.png">
    <p></p>
    <router-link to="/createAccount">
     <button class="btn btn-default">添加用户</button>
    </router-link>
    <router-link to="/login">
     <button class="btn btn-default">登录</button>
    </router-link>
    <router-link to="/searchAccount">
     <button class="btn btn-default">搜索</button>
    </router-link>
    <router-link to="/resetAccount">
     <button class="btn btn-default">重置账户</button>
    </router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
