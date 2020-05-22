<template>
  <el-card :body-style="{ padding: '0px' }" class="mb-8" shadow="hover">
    <el-row>
      <p class="info">{{comment.user.nick_name}} 评论于 {{comment.add_time.replace('T', '，')}}</p>
      <p class="content">{{comment.content}}</p>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: 'CommentCard',
  props: {
    comment: Object
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>

<style scoped>
  .mb-8 {
    margin-bottom: 8px;
  }
  .content {
    font-family: "Microsoft JhengHei";
    font-size: 15px;
    margin-left: 32px;
  }
  .info {
    font-size: 15px;
    color: #303030;
  }
</style>
