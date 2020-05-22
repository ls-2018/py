<template>
  <el-row>
    <h3 v-if="post">{{post.title}}</h3>
    <p v-if="post">
      <el-badge type="warning" :value="post.user.nick_name"></el-badge>
      发布于 <span>{{post.add_time}}</span>
      <span style="margin-left: 32px"> 评论数量: {{post.comment_nums}}</span>
    </p>
    <hr/>
    <div v-if="post" v-html="post.content"></div>
    <hr/>
    <div v-if="post">
      <el-form :model="form" ref="ruleForm" :rules="rules">
        <el-form-item label="帖子ID" prop="post_id" hidden>
          <el-input type="number" v-model="form.post_id" readonly autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="评论内容" prop="content">
          <el-input type="textarea" :rows="4" :maxlength="255" :minlength="6"
                    v-model="form.content" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')" class="ml-60">提交评论</el-button>
          <el-button @click="resetForm('ruleForm')">重置表单</el-button>
        </el-form-item>
      </el-form>
    </div>
    <hr/>
    <div v-if="post">
      <h5>当前贴子的评论列表: {{commentList.length}} 条</h5>
      <comment-card v-for="(item,index) in commentList" :key="index" :comment="item"></comment-card>
    </div>
  </el-row>
</template>

<script>
import { getPostDetail, createPostComment, getPostComments } from '../api/api'
import CommentCard from '../components/CommentCard'
export default {
  name: 'PostDetail',
  components: { CommentCard },
  data () {
    return {
      postId: 0,
      groupId: 0,
      post: null,
      commentList: [],
      form: {
        post_id: 0,
        content: ''
      },
      rules: {
        post_id: [
          { required: true, message: '帖子ID不能为空！', trigger: 'blur' }
        ],
        content: [
          { required: true, message: '评论内容不能为空！', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    obtainPost () {
      getPostDetail({ post_id: this.postId }).then(
        (response) => {
          this.post = response.data
        }
      ).catch((error) => {
        console.log(error.response.data)
      })
    },
    obtainPostComments (postId) {
      getPostComments({ post_id: postId }).then(
        (response) => {
          this.commentList = response.data
        }
      )
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          createPostComment({ post_id: this.form.post_id, content: this.form.content }).then(
            (response) => {
              console.log(response.data)
              this.obtainPostComments(this.postId)
            }
          ).catch((error) => {
            console.log(error.response.data)
          })
        } else {
          alert('表单内容有误！')
          return false
        }
      })
    },
    resetForm (formName) {
      // this.$refs[formName].resetFields()
      this.form.content = ''
    }
  },
  mounted () {
    this.postId = this.$route.params.pid
    this.groupId = this.$route.params.id
    this.obtainPost()
    this.form.post_id = this.postId
    this.obtainPostComments(this.postId)
  }
}
</script>

<style scoped>

</style>
