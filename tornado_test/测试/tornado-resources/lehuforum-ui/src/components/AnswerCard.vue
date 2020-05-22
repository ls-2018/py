<template>
  <el-card :body-style="{ padding: '0px' }" class="mb-8" shadow="hover">
    <el-row>
      <p class="info"><bold>{{answer.user.nick_name}}</bold> 回答于 {{answer.add_time.replace('T', '，')}}</p>
      <p class="content">{{answer.content}}</p>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: 'AnswerCard',
  props: {
    answer: Object
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
