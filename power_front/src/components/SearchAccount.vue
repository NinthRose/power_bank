<template>
  <div class="create_account">
        手机号：<input type="text" name="phone" placeholder="手机号码模糊查询" v-model="phone"><br><br>
        <p>{{num}}</p>
    <button @click="fSearchAccount(0)">搜索账户</button>
    <button @click="fSearchAccount(-1)">上一页</button>
    <button @click="fSearchAccount(1)">下一页</button>
    <table frame="hsides" id="users" align="center">
    <tr>
        <th>姓名</th>
        <th>手机号</th>
        <th>加入时间</th>
        <th>上次登录时间</th>
    </tr>
</table>
  </div>
</template>

<script>
import { searchAccount } from '../api/index'

export default {
  name: 'SearchAccount',
  data () {
    return {
      num: 1,
      lineNum: 0
    }
  },
  methods: {
    fSearchAccount: function (offset) {
      this.num += offset
      if (this.num < 1) {
        alert('页数异常')
        this.num = 1
        return
      }
      const data = { keyword: this.phone, pageSize: 10, pageNum: this.num }
      searchAccount(data).then((response) => {
        response.json().then((res) => {
          if (res.statusCode === 200) {
            var users = res.data.page
            var userTable = document.getElementById('users')
            for (var i = 0; i < this.lineNum; i++) {
              userTable.deleteRow(-1)
            }
            this.lineNum = 0
            for (var u of users) {
              var line = userTable.insertRow(-1)
              var name = line.insertCell(-1)
              var phone = line.insertCell(-1)
              var ctime = line.insertCell(-1)
              var lastLogin = line.insertCell(-1)
              name.innerHTML = u.name
              phone.innerHTML = u.phone
              ctime.innerHTML = u.ctime
              lastLogin.innerHTML = u.last_login
              console.log(u)
              this.lineNum += 1
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
