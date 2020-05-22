<template>
  <el-row>
    <question-card v-for="(item, index) in questionList" :key="index" :question="item"></question-card>
  </el-row>
</template>

<script>
import { getQuestionList } from '../api/api'
import cookie from '../store/cookie'
import QuestionCard from '../components/QuestionCard'

export default {
  name: 'MyQuestions',
  components: { QuestionCard },
  data () {
    return {
      userId: null,
      questionList: []
    }
  },
  methods: {
    obtainQuestionList (userid) {
      getQuestionList({ params: { userid: userid } }).then(
        (response) => {
          this.questionList = response.data
        }
      ).catch((error) => {
        console.log(error.response)
      })
    }
  },
  mounted () {
    this.userId = cookie.getCookie('userid')
    if (this.userId) {
      this.obtainQuestionList(this.userId)
    }
  }
}
</script>

<style scoped>

</style>
