<template>
  <div class="sources">
        管理员密码：<input type="password" name="password" placeholder="管理员密码" v-model="password"><br><br>
        用户手机号：<input type="text" name="phone" placeholder="用户手机号" v-model="phone"><br><br>
        添加课程数量：<input type="number" name="num_add" placeholder="请输入添加课程数量" min=1 v-model="num_add"><br><br>
    <button @click="fAddSource">添加课程</button><br><br>
        使用课程数量：<input type="number" name="num_consume" placeholder="请输入使用课程数量" min=1 v-model="num_consume"><br><br>
    <button @click="fConsumeSource">使用课程</button><br><br>
    <p>{{num}}</p>
    <button @click="fStatisticSource(0)">课程使用信息</button>
    <button @click="fStatisticSource(-1)">上一页</button>
    <button @click="fStatisticSource(1)">下一页</button>
    <p>总课程{{total}}, 使用课程{{used}}，剩余课程：{{last}}</p>
    <table frame="hsides" id="sources" align="center">
    <tr>
        <th>充值时间</th>
        <th>使用时间</th>
    </tr>
  </div>
</template>

<script>
import { addSource, consumeSource, statisticSource } from '../api/index'

export default {
  name: 'Login',
  data () {
    return {
      num: 1,
      tatol: 0,
      used: 0,
      last: 0,
      lineNum: 0
    }
  },
  methods: {
    fAddSource: function () {
      if (this.password === '') {
        alert('需要管理员密码')
      }
      const data = { num: this.num_add, password: this.password, phone: this.phone }
      addSource(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
        })
      })
    },
    fConsumeSource: function () {
      if (this.password === '') {
        alert('需要管理员密码')
      }
      const data = { num: this.num_consume, password: this.password, phone: this.phone }
      consumeSource(data).then((response) => {
        response.json().then((res) => {
          alert(res.message)
        })
      })
    },
    fStatisticSource: function (offset) {
      this.num += offset
      if (this.num < 1) {
        alert('页数异常')
        this.num = 1
        return
      }
      const data = { pageSize: 10, pageNum: this.num, phone: this.phone }
      statisticSource(data).then((response) => {
        response.json().then((res) => {
          if (res.statusCode === 200) {
            this.total = res.data.total
            this.used = res.data.used
            this.last = res.data.last
            var sources = res.data.sources
            var userTable = document.getElementById('sources')
            for (var i = 0; i < this.lineNum; i++) {
              userTable.deleteRow(-1)
            }
            this.lineNum = 0
            for (var s of sources) {
              var line = userTable.insertRow(-1)
              var ctime = line.insertCell(-1)
              var stime = line.insertCell(-1)
              ctime.innerHTML = s.ctime
              stime.innerHTML = s.stime
              console.log(s)
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
