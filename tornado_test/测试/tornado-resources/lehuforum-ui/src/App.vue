<template>
  <div id="app">
    <el-row>
      <el-col :span="3"><div style="width: 100%;height: 1px"></div></el-col>
      <el-col :span="18">
        <div id="nav">
          <top-nav></top-nav>
        </div>
        <router-view/>
      </el-col>
      <el-col :span="3"></el-col>
    </el-row>
  </div>
</template>

<script>
import TopNav from './views/TopNav'
export default {
  name: 'App',
  components: { TopNav }
}
</script>

<style lang="less">
</style>
