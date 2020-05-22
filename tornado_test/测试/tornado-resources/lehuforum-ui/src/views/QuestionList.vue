<template>
    <el-row :gutter="16" class="mt8">
      <el-col :span="18" class="mt8">
        <el-card class="categories">
          <el-button round size="small" @click="handleSelectCategory('所有分类')">所有分类</el-button>
          <el-button round size="small" v-for="(item, index) in categories" :key="index"
                     @click="handleSelectCategory(item)">{{item}}</el-button>
          <hr/>
          <el-button round size="small" @click="handleSelectOrder('默认排序')">默认排序</el-button>
          <el-button size="small" round @click="handleSelectOrder('new')">最新发布</el-button>
          <el-button size="small" round @click="handleSelectOrder('hot')">最火问题</el-button>
        </el-card>
        <el-row class="mt8">
          <question-card v-for="(item, index) in questionList" :key="index" :question="item"></question-card>
        </el-row>
      </el-col>
      <el-col :span="6" class="mt8">
        <el-card>
          <el-button type="primary" icon="el-icon-share" @click="handleCreateQuestion">发布问题</el-button>
        </el-card>
      </el-col>
    </el-row>
</template>

<script>
import { getQuestionList } from '../api/api'
import QuestionCard from '../components/QuestionCard'
export default {
  name: 'QuestionList',
  components: { QuestionCard },
  data () {
    return {
      categories: ['Django专题', 'Tornado专题', 'Flask专题', 'Python专题', 'Element专题', 'PyTorch专题'],
      questionList: [],
      category: null,
      order: null
    }
  },
  methods: {
    handleCreateQuestion () {
      this.$router.push({ name: 'question_create' })
    },
    obtainQuestions (category, order) {
      getQuestionList({ params: { ctg: category, order: order } }).then(
        (response) => {
          this.questionList = response.data
        }
      ).catch((error) => {
        console.log(error.response)
      })
    },
    handleSelectCategory (category) {
      this.category = category === '所有分类' ? null : category
      this.obtainQuestions(this.category, this.order)
    },
    handleSelectOrder (order) {
      this.order = order === '默认排序' ? null : order
      this.obtainQuestions(this.category, this.order)
    }
  },
  mounted () {
    this.obtainQuestions(this.category, this.order)
  }
}
</script>

<style scoped>
.mt8 {
  margin-top: 8px;
}
</style>
