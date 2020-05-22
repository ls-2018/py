<template>
<div>
  <el-menu
    :default-active="activeIndex"
    mode="horizontal"
    @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b">
    <el-menu-item index="1">乐乎论坛</el-menu-item>
    <el-menu-item index="2">乐乎小组</el-menu-item>
    <el-menu-item index="3">乐乎问答</el-menu-item>
    <el-submenu index="4" v-if="isLogin">
      <template slot="title">个人中心</template>
      <el-menu-item index="center">个人主页</el-menu-item>
      <el-menu-item index="settings">设置</el-menu-item>
      <el-menu-item index="logout">退出</el-menu-item>
    </el-submenu>
    <el-menu-item index="5" v-if="isLogin===false">注册</el-menu-item>
    <el-menu-item index="6" v-if="isLogin===false">登录</el-menu-item>
  </el-menu>
</div>
</template>

<script>
import cookie from '../store/cookie'
export default {
  name: 'TopNav',
  data () {
    return {
      activeIndex: '1',
      isLogin: false
    }
  },
  methods: {
    logOut () {
      cookie.delCookie('token')
      cookie.delCookie('username')
      cookie.delCookie('userid')
      // 存储,更新 store
      this.$store.dispatch('setInfo')
      this.isLogin = false
    },
    handleSelect (key, keyPath) {
      console.log(key)
      if (key === '1') {
        this.$router.push('/')
      }
      if (key === '2') {
        this.$router.push('/groups')
      }
      if (key === '3') {
        this.$router.push({ name: 'question_list' })
      }
      if (key === 'settings') {
        this.$router.push({ name: 'user_info' })
      }
      if (key === 'center') {
        this.$router.push({ name: 'user_center' })
      }
      if (key === 'logout') {
        this.logOut()
        // 跳转到登录
        this.$router.push({ name: 'login' })
      }
      if (key === '5') {
        this.$router.push('/regist')
      }
      if (key === '6') {
        this.$router.push('/login')
      }
    }
  },
  mounted () {
    if (cookie.getCookie('token') && cookie.getCookie('userid')) {
      this.isLogin = true
    } else {
      this.isLogin = false
    }
  }
}
</script>

<style scoped>

</style>
