<template>
  <div class="create_account">
        管理员密码：<input type="password" name="key" placeholder="请输入管理员密码" v-model="key"><br><br>
        手机号：<input type="text" name="phone" placeholder="请输入手机号码" v-model="phone"><br><br>
        用户名：<input type="text" name="name" placeholder="请输入重置名（为空不重置）" v-model="name"><br><br>
        密码鉴：<input type="password" name="password" placeholder="请输入重置密码（为空不重置）" v-model="password"><br><br>
    <button @click="fResetAccount">重置账户</button>
  </div>
</template>

<script>
import { resetAccount } from '../api/index'

export default {
  name: 'ResetAccount',
  methods: {
    fResetAccount: function () {
      const data = { key: this.key, name: this.name, phone: this.phone, password: this.password }
      resetAccount(data).then((response) => {
        if (response.statusCode === 200) {
          alert('账户信息重置成功' + response.message)
        } else {
          const info = response.$data
          console.log(response)
          console.log(response.message)
          console.log(info)
          alert(info)
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
