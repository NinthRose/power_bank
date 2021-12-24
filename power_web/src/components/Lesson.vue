<template>
  <div class="lesson">
    <input type="text" name="phone" placeholder="请输入手机号" v-model="phone">
    <input type="number" name="num" v-model="num" min="1" max="1000">
    <input type="radio" name="type" value="personal" v-model="type" />私教
    <input type="radio" name="type" value="lesson" v-model="type" />正课
    <input type="radio" name="type" value="free" v-model="type" />复习课
    <button @click="add">买课</button>
    <button @click="update(true)">退课</button>
    <button @click="update(false)">上课</button>
    <br/>
    <button @click="search(0)">账单</button>
    <button @click="search(-1)">上一页</button>
    <button @click="search(1)">下一页</button>
    <br/>
    搜索结果：{{res_num}}条课程记录，当页结果：{{lessons}}条；剩余课程: {{personal_num}}节私教课，{{lesson_num}}节正课，{{free_num}}节复习课
    <br/>
    <table frame="hsides" id="lessons" align="center">
      <tr>
        <th>充值时间</th> <th>消费</th> <th>退课</th> <th>课程类型</th>
      </tr>
    </table>
    <p>{{page_num}}</p>
  </div>
</template>

<script>
import { addLesson, searchLesson, updateLesson } from '../api/index'
export default {
  name: 'Lesson',
  data () {
    return {
      page_num: 1,
      lessons: 0,
      res_num: 0,
      personal_num: 0,
      lesson_num: 0,
      free_num: 0
    }
  },
  methods: {
    search: function (offset) {
      this.page_num += offset
      if (this.page_num < 1) {
        alert('页数异常')
        this.page_num = 1
        return
      }
      const data = { phone: this.phone, pageSize: 15, pageNum: this.page_num }
      searchLesson(data).then((response) => {
        response.json().then((res) => {
          if (res.statusCode === 200) {
            this.res_num = res.data.num
            this.personal_num = res.data.rest[0]
            this.lesson_num = res.data.rest[1]
            this.free_num = res.data.rest[2]
            var lessons = res.data.lessons
            var userTable = document.getElementById('lessons')
            if (lessons.length === 0) {
              if (this.res_num === 0) {
                alert('查不到相关信息')
              } else if (offset === 0) {
                this.page_num = 1
                searchLesson(0)
              } else {
                alert('该页内容为空')
                this.page_num -= 1
              }
              return
            }
            for (var i = 0; i < this.lessons; i++) {
              userTable.deleteRow(-1)
            }
            this.lessons = 0
            for (var l of lessons) {
              var line = userTable.insertRow(-1)
              var date = line.insertCell(-1)
              date.innerHTML = l.date
              var conduct = line.insertCell(-1)
              conduct.innerHTML = l.conduct
              var refund = line.insertCell(-1)
              refund.innerHTML = l.refund
              var type = line.insertCell(-1)
              type.innerHTML = l.type
              // console.log(u)
              this.lessons += 1
            }
          } else {
            alert(res.message)
          }
        })
      })
    },
    add: function () {
      if (this.type === '') {
        alert('请选择课程类型')
        return
      }
      const data = {phone: this.phone, num: this.num, type: this.type}
      console.log(this.type)
      addLesson(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
        })
      })
    },
    update: function (refund) {
      const data = {phone: this.phone, num: this.num, refund: refund, type: this.type}
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
