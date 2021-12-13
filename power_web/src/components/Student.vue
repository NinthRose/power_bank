<template>
  <div class="student">
    用户名：<input type="text" name="name" placeholder="请输入创建用户名" v-model="name">
    手机号：<input type="text" name="phone" placeholder="请输入手机号码" v-model="phone">
    <button @click="fRegister">创建用户</button>
    手机号：<input type="text" name="keyword" placeholder="手机号码模糊查询" v-model="keyword">
    <button @click="fSearchStudent(0)">搜索账户</button>
    <br/>
    <br/>
    <button @click="fSearchStudent(-1)">上一页</button>
    <button @click="fSearchStudent(1)">下一页</button>
    搜索结果：{{res_num}}条，当页结果：{{students}}条
    <br/>
    <table frame="hsides" id="users" align="center">
      <tr>
        <th>姓名</th> <th>手机号</th> <th>加入时间</th> <th>上次上课时间</th> <th>所有课程</th> <th>剩余课程</th>
      </tr>
    </table>
    <p>{{num}}</p>
  </div>
</template>

<script>
import { register, searchStudent } from '../api/index'

export default {
  name: 'Student',
  data () {
    return {
      num: 1,
      students: 0,
      res_num: 0
    }
  },
  methods: {
    fRegister: function () {
      if (this.name === '' || this.phone === '' || this.phone.length !== 11) {
        alert('输入内容有误')
        return
      }
      const data = { name: this.name, phone: this.phone }
      register(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
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
      const data = { keyword: this.keyword, pageSize: 10, pageNum: this.num }
      searchStudent(data).then((response) => {
        response.json().then((res) => {
          if (res.statusCode === 200) {
            this.res_num = res.data.num
            var users = res.data.users
            var userTable = document.getElementById('users')
            if (users.length === 0) {
              if (this.res_num === 0) {
                alert('查不到相关信息')
              } else if (offset === 0) {
                this.num = 1
                searchStudent(0)
              } else {
                alert('该页内容为空')
                this.num -= 1
              }
              return
            }
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
              var all = line.insertCell(-1)
              var rest = line.insertCell(-1)
              name.innerHTML = u.name
              phone.innerHTML = u.phone
              ctime.innerHTML = u.ctime
              last.innerHTML = u.utime
              all.innerHTML = u.all
              rest.innerHTML = u.rest
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
table {
  border-spacing: 10px 5px
}
</style>
