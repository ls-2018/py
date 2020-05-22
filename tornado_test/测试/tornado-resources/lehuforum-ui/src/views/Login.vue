<template>
  <div>
    <h1>登录页面</h1>
    <hr/>
    <el-row :gutter="24">
      <el-col :span="8"><div style="height: 1px;width: 100%"></div></el-col>
      <el-col :span="8">
        <el-card>
          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="手机号" prop="mobile">
              <el-input type="text" v-model="ruleForm.mobile"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input type="password" v-model="ruleForm.password" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
              <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
      <el-col :span="8"><div style="height: 1px;width: 100%"></div></el-col>
    </el-row>
  </div>
</template>

<script>
import { loginUser } from '../api/api'
import cookie from '../store/cookie'

export default {
  name: 'Login',
  data () {
    return {
      ruleForm: {
        mobile: '',
        password: ''
      },
      rules: {
        mobile: [
          { required: true, message: '请输入电话号码', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          loginUser({ 'mobile': this.ruleForm.mobile, 'password': this.ruleForm.password }).then(
            (response) => {
              console.log(response.data)
              cookie.setCookie('username', response.data.nick_name, 7)
              cookie.setCookie('userid', response.data.user_id, 7)
              cookie.setCookie('token', response.data.token, 7)
              // 存储,更新 store
              this.$store.dispatch('setInfo')
              // 刷新跳转到当前页
              this.$router.go(0)
              // 跳转到首页
              this.$router.push({ name: 'home' })
            }
          ).catch((error) => {
            console.log(error.response)
            if (error.response.status === 400) {
              if (error.response.data.password) {
                this.$message({ message: error.response.data.password, type: 'error' })
              } else if (error.response.data.mobile) {
                this.$message({ message: error.response.data.mobile, type: 'error' })
              }
            }
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style scoped>

</style>
