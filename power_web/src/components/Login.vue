<template>
  <div id="app">
    <router-link to="/student">
      <button class="btn btn-default">学生</button>
    </router-link>
    <router-link to="/lesson">
     <button class="lesson">课程</button>
    </router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'Login'
}
</script>

<style>
</style>
