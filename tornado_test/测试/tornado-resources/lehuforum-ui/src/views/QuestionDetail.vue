<template>
  <el-row>
    <h3 v-if="question">{{question.title}}</h3>
    <p v-if="question">
      <el-badge type="warning" :value="question.user.nick_name"></el-badge>
      发布于 <span>{{question.add_time}}</span>
      <span style="margin-left: 32px"> 答案数量: {{question.answer_nums}}</span>
    </p>
    <hr/>
    <el-row v-if="question" v-html="question.content"></el-row>
    <hr/>
    <el-row v-if="question">
      <el-form :model="form" ref="ruleForm" :rules="rules">
        <el-form-item label="问题ID" prop="question_id" hidden>
          <el-input type="number" v-model="form.question_id" readonly autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="回答内容" prop="content">
          <el-input type="textarea" :rows="4" :maxlength="255" :minlength="6"
                    v-model="form.content" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')" class="ml-60">提交答案</el-button>
          <el-button @click="resetForm('ruleForm')">重置表单</el-button>
        </el-form-item>
      </el-form>
    </el-row>
    <hr/>
    <el-row v-if="question">
      <h5>当前问题的所有答案：{{answerList.length}} 条</h5>
      <answer-card v-for="(item,index) in answerList" :key="index" :answer="item" ></answer-card>
    </el-row>
  </el-row>
</template>

<script>
import { getQuestionDetail, createAnswer, getAnswers } from '../api/api'
import AnswerCard from '../components/AnswerCard'
export default {
  name: 'QuestionDetail',
  components: { AnswerCard },
  data () {
    return {
      question: null,
      questionId: 0,
      form: {
        question_id: 0,
        content: ''
      },
      rules: {
        question_id: [
          { required: true, message: '问题ID不能为空！', trigger: 'blur' }
        ],
        content: [
          { required: true, message: '回答内容不能为空！', trigger: 'blur' }
        ]
      },
      answerList: []
    }
  },
  methods: {
    obtainQuestionDetail (questionId) {
      getQuestionDetail({ question_id: questionId }).then(
        (response) => {
          this.question = response.data
        }
      ).catch((error) => {
        console.log(error.response)
      })
    },
    obtainAnswerList (questionId) {
      getAnswers({ question_id: questionId }).then(
        (response) => {
          this.answerList = response.data
        }
      ).catch((error) => {
        console.log(error.response)
      })
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          createAnswer({ question_id: this.form.question_id, content: this.form.content }).then(
            (response) => {
              console.log(response.data)
              this.obtainAnswerList(this.questionId)
            }
          ).catch((error) => {
            console.log(error.response)
          })
        } else {
          alert('表单内容有误！')
          return false
        }
      })
    },
    resetForm (formName) {
      // this.$refs[formName].resetFields()
      this.form.content = ''
    }
  },
  mounted () {
    this.questionId = this.$route.params.id
    this.form.question_id = this.questionId
    this.obtainQuestionDetail(this.questionId)
    this.obtainAnswerList(this.questionId)
  }
}
</script>

<style scoped>

</style>
