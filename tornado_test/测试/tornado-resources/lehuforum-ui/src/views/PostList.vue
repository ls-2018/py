<template>
    <el-row>
      <el-card>
        <el-button type="text" class="btn-order" @click="handlePostList('add_time')">所有帖子</el-button>
        <el-button type="text" class="btn-order" @click="handlePostList('-add_time')">最新帖子</el-button>
        <el-button type="text" class="btn-order" @click="handlePostList('excellent')">精华帖子</el-button>
      </el-card>
      <post-card v-for="(item,index) in postList" :key="index" :post="item" :group-id="groupId" class="mt8"></post-card>
    </el-row>
</template>

<script>
import { getPostList } from '../api/api'
import PostCard from '../components/PostCard'
export default {
  name: 'PostList',
  components: { PostCard },
  data () {
    return {
      groupId: 0,
      order: null,
      excellent: null,
      postList: []
    }
  },
  methods: {
    obtainPostList () {
      getPostList({ params: { group_id: this.groupId, order: this.order, excellent: this.excellent } }).then(
        (response) => {
          this.postList = response.data
          console.log(this.postList)
        }
      ).catch((error) => {
        if (error.response.status === 403) {
          alert('当前没有权限查看帖子列表，请等待你的加入申请被批准！')
        }
        console.log(error.response.data)
      })
    },
    handlePostList (param) {
      if (param === 'add_time') {
        this.order = null
        this.excellent = null
      }
      if (param === '-add_time') {
        this.order = '-add_time'
        this.excellent = null
      }
      if (param === 'excellent') {
        this.excellent = 'excellent'
        this.order = '-add_time'
      }
      this.obtainPostList()
    }
  },
  mounted () {
    this.groupId = this.$route.params.id
    this.order = this.$route.params.order === '-add_time' ? '-add_time' : null
    this.excellent = null
    this.obtainPostList()
  }
}
</script>

<style scoped>
  .mt8 {
    margin-top: 8px;
  }
  .btn-order {
    margin: 0 16px;
    padding: 3px 0
  }
</style>
