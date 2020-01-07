<template>
  <div class="create_account">
    <title>注册邀请码</title>
    <form action="/orca/admin/account/create" method="post">
        管理员密码：<input type="password" name="password" placeholder="请输入管理员密码"><br><br>
        <input type="account" name="account" placeholder="请输入创建用户名"><br><br>
        <input type="phone" name="phone" placeholder="请输入手机号码"><br><br>
        <input type="accountPassword" name="accountPassword" placeholder="请输入创建密码"><br><br>
        <input type="submit" value="创建用户">
    </form>
  </div>
</template>

<script>
export default {
  name: 'CreateAccount',
  data () {
    return {
      msg: 'create account'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
