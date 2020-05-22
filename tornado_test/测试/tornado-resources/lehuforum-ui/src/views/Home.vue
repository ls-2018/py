<template>
  <div class="home">
    <el-row :gutter="20">
      <el-col :span="3"><div style="height: 1px;width: 100%"></div></el-col>
      <el-col :span="18">
        <img alt="Vue logo" src="../assets/logo.png">
        <HelloWorld msg="欢迎来到乐乎论坛！"/>
      </el-col>
      <el-col :span="3"><div style="height: 1px;width: 100%"></div></el-col>
    </el-row>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
}
</script>

<style>
  .home {
    text-align: center;
  }
</style>
