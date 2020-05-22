<template>
    <el-row>
      <el-card>
        <el-form :model="form" ref="ruleForm" :rules="rules">
          <el-form-item label="小组名称" :label-width="formLabelWidth" hidden>
            <el-input type="text" v-model="form.group_name" readonly autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="小组ID" :label-width="formLabelWidth" prop="group_id" hidden>
            <el-input type="number" v-model="form.group_id" readonly autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="帖子标题" :label-width="formLabelWidth" prop="title">
            <el-input type="text" v-model="form.title" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="帖子内容" :label-width="formLabelWidth" prop="content">
<!--            <el-input type="textarea" :rows="20" :maxlength="500" :minlength="5"-->
<!--                      v-model="form.content" autocomplete="off"></el-input>-->
            <tinymce-editor v-model="form.content"></tinymce-editor>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')" class="ml-60">发表帖子</el-button>
            <el-button @click="resetForm('ruleForm')">重置表单</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-row>
</template>

<script>
import { createPost } from '../api/api'
import Editor from '@tinymce/tinymce-vue'
export default {
  name: 'PostCreate',
  components: {
    'tinymce-editor': Editor
  },
  data () {
    return {
      formLabelWidth: '80px',
      form: {
        group_name: '',
        group_id: 0,
        title: '',
        content: ''
      },
      rules: {
        group_id: [
          { required: true, message: '小组ID不能为空！', trigger: 'blur' }
        ],
        title: [
          { required: true, message: '帖子标题不能为空！', trigger: 'blur' }
        ],
        content: [
          { required: true, message: '帖子内容不能为空！', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          createPost({ group_id: this.form.group_id, title: this.form.title, content: this.form.content }).then(
            (response) => {
              console.log(response.data)
              this.$message({ message: '贴子发布成功!', type: 'success' })
              this.$router.push({ name: 'post_list', params: { id: this.form.group_id } })
            }
          ).catch((error) => {
            if (error.response.status === 400) {
              alert('表单错误！')
            }
            if (error.response.status === 404) {
              alert('小组不存在！')
            }
            if (error.response.status === 403) {
              alert('你在当前小组内没有发帖权限！')
            }
          })
        } else {
          alert('表单内容有误！')
          return false
        }
      })
    },
    resetForm (formName) {
      // this.$refs[formName].resetFields()
      this.form.title = ''
      this.form.content = ''
    }
  },
  created () {
    this.form.group_id = this.$route.params.id
    this.form.group_name = this.$route.params.name
  }
}
</script>

<style scoped>
  .ml-60 {
    margin-left: 60%;
  }
</style>
