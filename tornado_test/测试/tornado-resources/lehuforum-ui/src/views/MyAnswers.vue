<template>
  <el-row>
    <message-card v-for="(item,index) in answersList" :key="index" :message="item"></message-card>
  </el-row>
</template>

<script>
import { getUserMessages } from '../api/api'
import MessageCard from '../components/MessageCard'
export default {
  name: 'MyAnswers',
  components: { MessageCard },
  data () {
    return {
      answersList: [],
      msg_type: 2
    }
  },
  methods: {
    obtainAnswersListList () {
      getUserMessages({ params: { msg_type: this.msg_type } }).then(
        (response) => {
          this.answersList = response.data
          console.log(this.answersList)
        }
      ).catch((error) => {
        console.log(error.response)
      })
    }
  },
  mounted () {
    this.obtainAnswersListList()
  }
}
</script>

<style scoped>

</style>
