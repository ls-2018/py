<template>
    <el-card :body-style="{ padding: '8px' }"  shadow="hover">
      <h4>{{post.title}}</h4>
      <p>
        <el-badge type="warning" :value="post.user.nick_name"></el-badge>
        发布于 <span>{{post.add_time.split('T')[0]}}</span>
        <span style="margin-left: 32px"> 评论数量: {{post.comment_nums}}</span>
        <el-button style="float: right; padding: 3px 0" type="text" @click="handleSeeDetail">查看详情</el-button>
      </p>
    </el-card>
</template>

<script>
export default {
  name: 'PostCard',
  props: {
    post: Object,
    groupId: Number
  },
  methods: {
    handleSeeDetail () {
      this.$router.push({ name: 'post_detail', params: { id: this.groupId, pid: this.post.id } })
    }
  }
}
</script>

<style scoped>

</style>
