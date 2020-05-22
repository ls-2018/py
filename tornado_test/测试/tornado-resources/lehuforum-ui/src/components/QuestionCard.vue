<template>
  <el-card :body-style="{ padding: '0px' }" class="mb-16" shadow="hover">
    <el-row :gutter="16">
      <el-col :span="6">
        <img :src="question.image" class="image">
      </el-col>
      <el-col :span="18">
        <p class="title">{{question.title}}</p>
        <div class="bottom clearfix">
          <p class="info">类别： <el-badge type="warning" :value="question.category"></el-badge></p>
          <p class="info">{{question.user.nick_name}} 发布于 {{question.add_time.split('T')[0]}}
            <el-button type="text" class="button" @click="handleQuestionDetail">查看详情</el-button>
          </p>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: 'QuestionCard',
  props: {
    question: Object
  },
  data () {
    return {
      currentDate: new Date()
    }
  },
  methods: {
    handleQuestionDetail () {
      this.$router.push({ name: 'question_detail', params: { id: this.question.id } })
    }
  }
}
</script>

<style scoped>
  .mb-16 {
    margin-bottom: 16px;
  }
  .title {
    font-family: "Microsoft JhengHei";
    font-size: 18px;
  }
  .info {
    font-size: 15px;
    color: #303030;
  }

  .bottom {
    margin-top: 8px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    height: 120px;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }
</style>
