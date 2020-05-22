<template>
  <el-row>
    <h2>用户个人中心</h2>
    <hr/>
    <el-row :gutter="24">
      <el-col :span="4">
        <el-menu
          @select="handleSelect"
          default-active="myposts"
          class="el-menu-vertical-demo">
          <el-menu-item index="postcomments">
            <i class="el-icon-menu"></i>
            <span slot="title">收到的帖子评论</span>
          </el-menu-item>
          <el-menu-item index="myquestions">
            <i class="el-icon-menu"></i>
            <span slot="title">我发布的问题</span>
          </el-menu-item>
          <el-menu-item index="myanswers">
            <i class="el-icon-menu"></i>
            <span slot="title">收到的问题回答</span>
          </el-menu-item>
          <el-menu-item index="mygroups">
            <i class="el-icon-menu"></i>
            <span slot="title">我创建的小组</span>
          </el-menu-item>
          <el-menu-item index="myapplys">
            <i class="el-icon-menu"></i>
            <span slot="title">收到的加入请求</span>
          </el-menu-item>
        </el-menu>
      </el-col>
      <el-col :span="20">
        <router-view/>
      </el-col>
    </el-row>
  </el-row>
</template>

<script>
export default {
  name: 'UserCenter',
  methods: {
    handleSelect (key, keyPath) {
      console.log(key)
      if (key === 'postcomments') {
        this.$router.push({ name: 'my_postcomments' })
      }
      if (key === 'myquestions') {
        this.$router.push({ name: 'my_questions' })
      }
      if (key === 'myanswers') {
        this.$router.push({ name: 'my_answers' })
      }
      if (key === 'mygroups') {
        this.$router.push({ name: 'my_groups' })
      }
      if (key === 'myapplys') {
        this.$router.push({ name: 'my_applys' })
      }
    }
  }
}
</script>

<style scoped>

</style>
