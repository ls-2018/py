<template>
  <div>
    <h1>注册页面</h1>
    <hr/>
    <el-row :gutter="20">
      <el-col :span="7"><div style="height: 1px;width: 100%"></div></el-col>
      <el-col :span="10">
        <el-card>
          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="手机号" prop="mobile">
              <el-input v-model="ruleForm.mobile"></el-input>
            </el-form-item>
            <el-form-item label="验证码" prop="code">
              <el-row :gutter="8">
                <el-col :span="16"><el-input v-model="ruleForm.code"></el-input></el-col>
                <el-col :span="6"><el-button @click="obtainCode('ruleForm')">获取验证码</el-button></el-col>
              </el-row>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input type="password" v-model="ruleForm.password" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPassword">
              <el-input type="password" v-model="ruleForm.checkPassword" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
              <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
      <el-col :span="7"><div style="height: 1px;width: 100%"></div></el-col>
    </el-row>
  </div>
</template>

<script>
import { getVerifyCode, registUser } from '../api/api'
export default {
  name: 'Register',
  data () {
    let checkCode = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('验证码不能为空'))
      }
      setTimeout(() => {
        if (value.length !== 4) {
          callback(new Error('验证码的长度必须为4位'))
        } else {
          callback()
        }
      }, 10)
    }
    let checkMobile = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('手机号不能为空'))
      }
      setTimeout(() => {
        if (value.length !== 11) {
          callback(new Error('手机号码长度必须为11位'))
        } else {
          callback()
        }
      }, 10)
    }
    let validatePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.ruleForm.checkPassword !== '') {
          this.$refs.ruleForm.validateField('checkPassword')
        }
        callback()
      }
    }
    let validatePassword2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      codeObtained: false,
      ruleForm: {
        mobile: '',
        password: '',
        checkPassword: '',
        code: ''
      },
      rules: {
        password: [
          { validator: validatePassword, trigger: 'blur' }
        ],
        checkPassword: [
          { validator: validatePassword2, trigger: 'blur' }
        ],
        code: [
          { validator: checkCode, trigger: 'blur' }
        ],
        mobile: [
          { validator: checkMobile, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          registUser({
            mobile: this.ruleForm.mobile,
            code: this.ruleForm.code,
            password: this.ruleForm.password
          }).then((response) => {
            console.log(response.data)
            this.$router.push({ name: 'home' })
          }).catch((err) => {
            if (err.response.status === 400) {
              if (err.response.data.code) {
                this.$message({ message: err.response.data.code, type: 'error' })
              } else if (err.response.data.mobile) {
                this.$message({ message: err.response.data.mobile, type: 'error' })
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
    },
    obtainCode (formName) {
      if (this.codeObtained) {
        setTimeout(() => {
          this.$message({ message: '每隔5分钟才能再次发送短信验证码!', type: 'warning' })
          this.codeObtained = false
        }, 300000)
      }
      if (!this.codeObtained && this.ruleForm.mobile !== '') {
        this.codeObtained = true
        getVerifyCode({
          mobile: this.ruleForm.mobile
        }).then((response) => {
          console.log(response)
          this.$message({ message: '短信验证码已发送!', type: 'success' })
        }).catch(function (error) {
          console.log(error)
          this.$message({ message: '短信验证码发送失败!', type: 'error' })
        })
      } else {
        this.$message({ message: '请输入手机号码！!', type: 'error' })
      }
    }
  }
}
</script>

<style scoped>

</style>
