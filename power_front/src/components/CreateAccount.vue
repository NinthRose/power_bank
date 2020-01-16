<template>
  <div class="create_account">
    管理员密码：<input type="password" name="key" placeholder="请输入管理员密码" v-model="key"><br><br>
    用户名：<input type="text" name="name" placeholder="请输入创建用户名" v-model="name"><br><br>
    手机号：<input type="text" name="phone" placeholder="请输入手机号码" v-model="phone"><br><br>
    密码鉴：<input type="password" name="password" placeholder="请输入创建密码（默认为后四位）" v-model="password"><br><br>
    <button @click="fRegister">创建用户</button>
  </div>
</template>

<script>
import { register } from '../api/index'

export default {
  name: 'CreateAccount',
  methods: {
    fRegister: function () {
      const data = { key: this.key, name: this.name, phone: this.phone, password: this.password }
      register(data).then((response) => {
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
