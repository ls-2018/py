<template>
  <el-row class="mt8">
    <el-card :body-style="{ padding: '8px' }">
      <el-row :gutter="16">
        <el-col :span="6">
          <img v-if="group" :src="group.cover" class="cover">
        </el-col>
        <el-col :span="18">
          <h3 v-if="group">{{group.name}}</h3>
          <p v-if="group">【简介】: {{group.desc}}</p>
          <p v-if="group"><span style="margin-right: 16px">帖子：{{group.post_nums}}个</span>|
            <span style="margin-left: 16px">成员：{{group.member_nums}}人</span></p>
          <p>
            <el-button type="success" class="btn-view" @click="handlePostList('add_time')">查看所有帖子</el-button>
            <el-button type="primary" class="btn-pub" @click="handleCreatePost">发布新帖子</el-button>
          </p>
        </el-col>
      </el-row>
    </el-card>
    <el-row :gutter="16">
      <el-col :span="18">
        <el-row class="mt8">
          <router-view/>
        </el-row>
      </el-col>
      <el-col :span="6">
        <el-card class="mt8">
          <div slot="header">
            <span>小组公告</span>
            <el-button class="btn-pub" type="text">发布公告</el-button>
          </div>
          <div v-if="group">
            {{group.notice}}
          </div>
        </el-card>
      </el-col>
    </el-row>
  </el-row>
</template>

<script>
import { getSingleGroup } from '../api/api'
export default {
  name: 'GroupDetail',
  data () {
    return {
      group_id: 3,
      group: null
    }
  },
  methods: {
    obtainGroup (groupId) {
      getSingleGroup({ group_id: groupId }).then(
        (response) => {
          this.group = response.data
          console.log(this.group)
        }
      ).catch((error) => {
        console.log(error.response.data)
      })
    },
    handleCreatePost (groupId) {
      this.$router.push({ name: 'post_create', params: { id: this.group.id, name: this.group.name } })
    },
    handlePostList (order) {
      this.$router.push({ name: 'post_list', params: { id: this.group.id, order: order } })
    }
  },
  created () {
    this.group_id = this.$route.params.id
    this.obtainGroup(this.group_id)
  }
}
</script>

<style scoped>
  .mt8 {
    margin-top: 8px;
  }
  .cover {
    height: 180px;
    width: 100%;
  }
  .btn-pub {
    float: right;
    padding: 5px 0;
  }
  .btn-view {
    float: right;
    margin-left: 32px;
    padding: 5px 0;
  }
</style>
