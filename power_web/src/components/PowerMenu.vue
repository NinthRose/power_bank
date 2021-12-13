<template>
  <div id="power-menu">
    <router-link to="/student">
     <button class="student">学生</button>
    </router-link>
    <router-link to="/lesson">
     <button class="lesson">课程</button>
    </router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'PowerMenu'
}
</script>

<style>
</style>
