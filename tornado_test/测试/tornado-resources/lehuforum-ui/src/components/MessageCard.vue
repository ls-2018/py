<template>
  <el-card class="msg-card" :body-style="{ padding: '8px 16px' }">
    <el-row :gutter="16" v-if="message">
      <el-col :span="1">
        <el-avatar size="medium" :src="message.sender.head_url"></el-avatar>
      </el-col>
      <el-col :span="23">
        <h5 class="info">{{ message.sender.nick_name }} {{message.msg_type}} 你的{{subject}} 【{{message.parent}}】</h5>
      </el-col>
    </el-row>
    <p v-if="message" class="msg">{{message.msg_type}}内容： {{message.message}}</p>
  </el-card>
</template>

<script>
export default {
  name: 'MessageCard',
  props: {
    message: null
  },
  computed: {
    subject () {
      return this.message.msg_type === '评论' ? '帖子' : '问题'
    }
  }
}
</script>

<style scoped>
  .msg-card {
    margin-bottom: 8px;
  }
  .info {
    padding: 0;
    margin: 10px;
  }
  .msg {
    margin-left: 16px;
  }
</style>
