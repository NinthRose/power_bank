<template>
    <div class="loginCon">
        <div class="loginContainer">
            <div class="iconBg"></div>
            <div id="loginBox" v-if="!showReg">
                <div class="logo"></div>
                <form>
                    <div class="userName">
                        <i class="in-lbl el-icon-user"></i>
                        <input type="text" v-focus v-model="form.username" name="userName" @focus="focusHandle"
                               @keyup.13="loginHandle" placeholder="请输入用户名"/>
                    </div>
                    <div class="passWord">
                        <i class="in-lbl el-icon-lock"></i>
                        <input type="password" v-model="form.password" name="userName" @focus="focusHandle"
                               @keyup.13="loginHandle" placeholder="请输入密码"/>
                    </div>
                    <div class="operate"><span class="tips" v-if="showTips">{{tipsTxt}}</span></div>
                    <div class="login-btn-main">
                         <div class="loginBtn btn-item" @click="loginHandle">登录</div>
                    </div>
                </form>
                <div class="forgerPassword">
                    <router-link tag="span"  to="/resetPassword">忘记密码？</router-link>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapActions } from 'vuex'
import { login } from '../api/index'

export default {
  data () {
    return {
      showTips: false,
      tipsTxt: null,
      form: {
        username: null,
        password: null
      },
      showReg: false,
      loading: null
    }
  },
  mounted () {
    if (document.querySelector('.el-loading-mask')) {
      document.body.removeChild(document.querySelector('.el-loading-mask'))
    }
  },
  methods: {
    ...mapActions('projectManage', ['addProjectAction']),
    ...mapActions('projectList', ['selectedProjectIndexAction', 'selectedProjectIdAction', 'loadRecentProjectAction', 'getProgectInfoAction']),
    focusHandle () {
      this.showTips = false
      this.tipsTxt = ''
    },
    loginHandle () {
      const { utils } = this
      // const _self = this
      const name = this.form.username
      if (!utils.Tools.isEmpty(this.form.username) && !utils.Tools.isEmpty(this.form.password)) {
        login({ user_id: name, password: this.form.password }).then((response) => {
          sessionStorage.setItem('projectId', '')
          if (response.data.stateCode === 200) {
            this.showTips = false
            // utils.Tools.setCookie('sessionId', response.data.result);
            // utils.Tools.setCookie('user_id',name);
            // 跳转首页
            this.loadRecentProject()
          } else if (response.data.stateCode === 301) {
            this.showTips = false
            // utils.Tools.setCookie('sessionId', response.data.result);
            // utils.Tools.setCookie('user_id', _self.form.username);
            this.$message({
              message: response.data.message,
              type: 'success'
            })
            this.loadRecentProject()
          } else {
            this.showTips = true
            this.tipsTxt = response.data.message
            utils.$('#loginBox').removeClass().addClass('shake animated')
              .one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
                utils.$(this).removeClass()
              })
          }
        })
      } else if (utils.Tools.isEmpty(this.form.username)) {
        this.showTips = true
        this.tipsTxt = '用户名不能为空'
        utils.$('#loginBox').removeClass().addClass('shake animated')
          .one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
            utils.$(this).removeClass()
          })
      } else if (utils.Tools.isEmpty(this.form.password)) {
        this.showTips = true
        this.tipsTxt = '密码不能为空'
        utils.$('#loginBox').removeClass().addClass('shake animated')
          .one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
            utils.$(this).removeClass()
          })
      }
    },
    selectedRow (index, item) {
      this.selectedProjectIndexAction(index)
      this.selectedProjectIdAction(item.project_id)
      sessionStorage.setItem('projectId', item.project_id)
      localStorage.setItem('project_info', JSON.stringify(item))
      this.$router.push('/task')
    },
    loadRecentProject () {
      this.loadRecentProjectAction({}).then((response) => {
        if (response.stateCode === 200) {
          if (response.result.length > 0) {
            this.selectedRow(0, response.result[0])
            this.getProgectInfoAction(response.result[0].project_id)
          } else {
            this.getProjectItem()
          }
        }
      })
    },
    getProjectItem () {
      this.addProjectAction({
        operation: 'view',
        page: 1,
        num: 1
      }).then((response) => {
        if (response.stateCode === 200) {
          if (response.result.project_list.length > 0) {
            this.selectedRow(0, response.result.project_list[0])
          } else {
            this.$router.push('/projectList')
          }
        } else {
          this.$message({
            type: 'error',
            message: response.message
          })
        }
      })
    }
  }
}
</script>
<style>
    .el-tabs__header{
        margin: 0 0 10px;
    }
    .loginCon .el-tabs__item {
        padding: 0 15px;
        height: 30px;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        line-height: 30px;
        display: inline-block;
        list-style: none;
        font-size: 12px;
        font-weight: 500;
        color: #303133;
        position: relative;
    }

</style>
