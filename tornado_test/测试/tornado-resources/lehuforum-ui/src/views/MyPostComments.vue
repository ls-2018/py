<template>
  <el-row>
    <message-card v-for="(item,index) in commentsList" :key="index" :message="item"></message-card>
  </el-row>
</template>

<script>
import { getUserMessages } from '../api/api'
import MessageCard from '../components/MessageCard'
export default {
  name: 'MyPostComments',
  components: { MessageCard },
  data () {
    return {
      commentsList: [],
      msg_type: 1
    }
  },
  methods: {
    obtainCommentList () {
      getUserMessages({ params: { msg_type: this.msg_type } }).then(
        (response) => {
          this.commentsList = response.data
          console.log(this.commentsList)
        }
      ).catch((error) => {
        console.log(error.response)
      })
    }
  },
  mounted () {
    this.obtainCommentList()
  }
}
</script>

<style scoped>

</style>
