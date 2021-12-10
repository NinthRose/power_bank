<template>
  <div id="app">
    <router-link to="/login">
      <img src="./assets/logo.jpeg">
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
