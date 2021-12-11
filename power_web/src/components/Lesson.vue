<template>
  <div class="lesson">
    用户名：<input type="text" name="name" placeholder="请输入创建用户名" v-model="name"><br><br>
    手机号：<input type="text" name="phone" placeholder="请输入手机号码" v-model="phone"><br><br>
    <button @click="fRegister">创建用户</button>
    <p></p>
    手机号：<input type="text" name="phone" placeholder="手机号码模糊查询" v-model="phone"><br><br>
    <button @click="fSearchStudent(0)">搜索账户</button>
    <button @click="fSearchStudent(-1)">上一页</button>
    <button @click="fSearchStudent(1)">下一页</button>
    <table frame="hsides" id="users" align="center">
      <tr>
        <th>id</th> <th>姓名</th> <th>手机号</th> <th>加入时间</th> <th>上次上课时间</th>
      </tr>
    </table>
    <p>{{num}}</p>
  </div>
</template>

<script>
import { register, searchStudent } from '../api/index'

export default {
  name: 'Lesson',
  data () {
    return {
      num: 1,
      students: 0
    }
  },
  methods: {
    fRegister: function () {
      if (this.name === '' || this.phone === '' || length(this.phone) === 0) {
        alert('输入内容有误')
        return
      }
      const data = { name: this.name, phone: this.phone }
      register(data).then((response) => {
        response.json().then((res) => {
          if (res.statusCode === 200) {
            alert(res.data.msg)
          }
        })
      })
    },
    fSearchStudent: function (offset) {
      this.num += offset
      if (this.num < 1) {
        alert('页数异常')
        this.num = 1
        return
      }
      const data = { keyword: this.phone, pageSize: 10, pageNum: this.num }
      searchStudent(data).then((response) => {
        response.json().then((res) => {
          if (res.statusCode === 200) {
            var users = res.data.page
            var userTable = document.getElementById('users')
            for (var i = 0; i < this.students; i++) {
              userTable.deleteRow(-1)
            }
            this.students = 0
            for (var u of users) {
              var line = userTable.insertRow(-1)
              var name = line.insertCell(-1)
              var phone = line.insertCell(-1)
              var ctime = line.insertCell(-1)
              var last = line.insertCell(-1)
              name.innerHTML = u.name
              phone.innerHTML = u.phone
              ctime.innerHTML = u.ctime
              last.innerHTML = u.utime
              console.log(u)
              this.students += 1
            }
          } else {
            alert(res.message)
          }
        })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
