<template>
  <div class="create_account">
    <title>注册邀请码</title>
    <form action="/powerBank/admin/account/create" method="post">
        管理员密码：<input type="password" name="key" placeholder="请输入管理员密码"><br><br>
        用户名：<input type="text" name="name" placeholder="请输入创建用户名"><br><br>
        手机号：<input type="text" name="phone" placeholder="请输入手机号码"><br><br>
        密码鉴：<input type="password" name="password" placeholder="请输入创建密码（默认为后四位）"><br><br>
        <input type="submit" value="创建用户">
    <p>{{info}}</p>
    </form>
  </div>
</template>

<script>
import { register } from '../api/index'

export default {
  name: 'CreateAccount',
  methods: {
    fRegister: function () {
      const data = { key: this.key, name: this.phone, phone: this.phone, password: this.form.password }
      register(data).then((response) => {
        this.info = '注册成功'
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
