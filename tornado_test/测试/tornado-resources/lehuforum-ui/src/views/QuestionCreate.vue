<template>
  <el-row>
    <h1>发布问题</h1>
    <hr/>
    <el-row>
      <el-col :span="2"><div style="height: 1px;width: 100%"></div></el-col>
      <el-col :span="20">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
          <el-form-item label="问题标题" prop="title">
            <el-input type="text" v-model="ruleForm.title"></el-input>
          </el-form-item>
          <el-form-item label="问题类别" prop="category">
            <el-select v-model="ruleForm.category" placeholder="请选择问题类别">
              <el-option v-for="(item, index) in categories" :key="index" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="封面图象">
            <input type="file" id="image" name="image" accept="image/png, image/jpeg, image/jpg" @change="changeImage($event)">
          </el-form-item>
          <el-form-item label="问题内容" prop="content">
<!--            <el-input type="textarea" v-model="ruleForm.content" :rows="4"></el-input>-->
            <tinymce-editor v-model="ruleForm.content"></tinymce-editor>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </el-row>
</template>

<script>
import { createQuestion } from '../api/api'
import Editor from '@tinymce/tinymce-vue'
export default {
  name: 'QuestionCreate',
  components: {
    'tinymce-editor': Editor
  },
  data () {
    return {
      categories: ['Django专题', 'Tornado专题', 'Flask专题', 'Python专题', 'Element专题', 'PyTorch专题'],
      ruleForm: {
        title: '',
        category: '',
        image: '',
        content: ''
      },
      rules: {
        title: [
          { required: true, message: '请输入问题标题', trigger: 'blur' },
          { min: 3, max: 200, message: '长度在 3 到 200 个字符', trigger: 'blur' }
        ],
        category: [
          { required: true, message: '请选择问题类别', trigger: 'blur' }
        ],
        content: [
          { required: true, message: '请填写问题内容', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    changeImage (evt) {
      this.ruleForm.image = evt.target.files[0]
      console.log(this.ruleForm.image)
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          if (this.ruleForm.image === '') {
            alert('请选择封面文件!')
            return false
          }
          let formData = new FormData()
          formData.append('title', this.ruleForm.title)
          formData.append('category', this.ruleForm.category)
          formData.append('content', this.ruleForm.content)
          formData.append('image', this.ruleForm.image)
          createQuestion(formData).then((response) => {
            console.log(response.data)
            this.$message({ message: '问题已发布成功！', type: 'success' })
            this.$router.push({ name: 'question_list' })
          }).catch((error) => {
            console.log(error.response.data)
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
