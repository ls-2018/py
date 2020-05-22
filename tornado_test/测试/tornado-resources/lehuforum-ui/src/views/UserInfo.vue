<template>
  <el-row>
    <h2>用户个人信息</h2>
    <hr/>
    <el-row :gutter="24">
      <el-col :span="3"><div style="width: 100%;height: 1px"></div></el-col>
      <el-col :span="12">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
          <el-form-item label="登陆账号">
            <el-input v-model="ruleForm.mobile" readonly ></el-input>
          </el-form-item>
          <el-form-item label="用户昵称" prop="nick_name">
            <el-input v-model="ruleForm.nick_name"></el-input>
          </el-form-item>
          <el-form-item label="用户地址" prop="address">
            <el-input v-model="ruleForm.address"></el-input>
          </el-form-item>
          <el-form-item label="用户性别" prop="gender">
            <el-radio-group v-model="ruleForm.gender">
              <el-radio label="male">男</el-radio>
              <el-radio label="female">女</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="个人简介" prop="desc">
            <el-input type="textarea" :rows="3" v-model="ruleForm.desc"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">提交表单</el-button>
            <el-button @click="resetForm('ruleForm')">重置表单</el-button>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="9" style="text-align: center">
        <el-upload
          class="avatar-uploader"
          name="avatar"
          :auto-upload="true"
          action="http://127.0.0.1:9001/avatar/"
          :headers="headers"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload">
          <div class="el-upload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </div>
        </el-upload>
        <h4>用户头像</h4>
      </el-col>
    </el-row>
    <h2>用户修改密码</h2>
    <hr/>
    <el-row :gutter="24">
      <el-col :span="3"><div style="width: 100%;height: 1px"></div></el-col>
      <el-col :span="12">
        <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="100px">
          <el-form-item label="旧密码" prop="oldPassword">
            <el-input type="password" v-model="ruleForm2.oldPassword" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="新密码" prop="newPassword">
            <el-input type="password" v-model="ruleForm2.newPassword" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="checkPassword">
            <el-input type="password" v-model="ruleForm2.checkPassword" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm2('ruleForm2')">提交修改</el-button>
            <el-button @click="resetForm2('ruleForm2')">重置表单</el-button>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="9"><div style="width: 100%;height: 1px"></div></el-col>
    </el-row>
  </el-row>
</template>

<script>
import cookie from '../store/cookie'
import { getUserProfile, changeUserProfile, getUserAvatar, changeUserPassword } from '../api/api'
export default {
  name: 'UserInfo',
  data () {
    let validatePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入新密码'))
      } else {
        if (this.ruleForm.checkPassword !== '') {
          this.$refs.ruleForm2.validateField('checkPassword')
        }
        callback()
      }
    }
    let validatePassword2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm2.newPassword) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      ruleForm: {
        id: '',
        mobile: '',
        nick_name: '',
        address: '',
        gender: '',
        desc: ''
      },
      rules: {
        mobile: [
          { required: true, message: '请输入手机号', trigger: 'blur' }
        ],
        nick_name: [
          { required: true, message: '请输入昵称', trigger: 'blur' }
        ],
        address: [
          { required: true, message: '请输入地址信息', trigger: 'blur' }
        ],
        gender: [
          { required: true, message: '请选择性别', trigger: 'change' }
        ],
        desc: [
          { required: true, message: '请填写个人简介', trigger: 'blur' }
        ]
      },
      imageUrl: '',
      headers: {
        Authorization: cookie.getCookie('token')
      },
      ruleForm2: {
        oldPassword: '',
        newPassword: '',
        checkPassword: ''
      },
      rules2: {
        oldPassword: [
          { required: true, message: '请输入旧密码', trigger: 'blur' }
        ],
        newPassword: [
          { validator: validatePassword, trigger: 'blur' }
        ],
        checkPassword: [
          { validator: validatePassword2, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          changeUserProfile(this.ruleForm).then(
            (response) => {
              this.ruleForm = response.data
              this.$message({ message: '用户信息修改成功!', type: 'success' })
            }
          ).catch((error) => {
            console.log(error.response)
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
    obtainUserInfo () {
      getUserProfile({}).then(
        (response) => {
          this.ruleForm = response.data
        }
      ).catch((error) => {
        console.log(error.response)
      })
    },
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg' || file.type === 'image/jpg' || file.type === 'image/png'
      const isLt1M = file.size / 1024 / 1024 < 1

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG/JPEG/PNG 格式!')
      }
      if (!isLt1M) {
        this.$message.error('上传头像图片大小不能超过 1MB!')
      }
      return isJPG && isLt1M
    },
    obtainUserAvatar () {
      getUserAvatar({}).then(
        (response) => {
          this.imageUrl = response.data.avatarUrl
        }
      ).catch((error) => {
        this.imageUrl = ''
        console.log(error.response)
      })
    },
    submitForm2 (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          changeUserPassword(this.ruleForm2).then(
            (response) => {
              console.log(response.data)
              this.$message({ message: '用户密码修改成功!', type: 'success' })
            }
          ).catch((error) => {
            if (error.response.status === 400) {
              // console.log(error.response)
              if (error.response.data.oldPassword) {
                alert(error.response.data.oldPassword)
              }
              if (error.response.data.checkPassword) {
                alert(error.response.data.checkPassword)
              }
            }
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm2 (formName) {
      this.$refs[formName].resetFields()
    }
  },
  mounted () {
    this.obtainUserInfo()
    this.obtainUserAvatar()
  }
}
</script>

<style scoped>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
