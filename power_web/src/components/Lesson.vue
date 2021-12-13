<template>
  <div class="lesson">
    <input type="text" name="phone" placeholder="请输入手机号" v-model="phone">
    <input type="number" name="num" v-model="num" min="1" max="1000">
    <button @click="add">买课</button>
    <button @click="update(true)">退课</button>
    <button @click="update(false)">上课</button>

  </div>
</template>

<script>
import { addLesson, updateLesson } from '../api/index'
export default {
  name: 'Lesson',
  methods: {
    add: function () {
      const data = {phone: this.phone, num: this.num}
      addLesson(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
        })
      })
    },
    update: function (refund) {
      const data = {phone: this.phone, num: this.num, refund: refund}
      updateLesson(data).then((response) => {
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
