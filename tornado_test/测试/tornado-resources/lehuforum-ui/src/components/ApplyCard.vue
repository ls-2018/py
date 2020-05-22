<template>
  <el-card class="msg-card" :body-style="{ padding: '8px 16px' }">
    <el-row :gutter="16" v-if="apply">
      <el-col :span="1">
        <el-avatar size="medium" :src="apply.user.head_url"></el-avatar>
      </el-col>
      <el-col :span="23">
        <h5 class="info">{{ apply.user.nick_name }} 申请加入 你的小组： 【{{apply.group}}】
          <small style="float: right">{{apply.add_time}}</small></h5>
      </el-col>
    </el-row>
    <p v-if="apply" class="msg">申请理由： {{apply.apply_reason}}</p>
    <p v-if="apply.status==='agree'" class="status">处理状态： <el-badge type="success" :value="apply.status"></el-badge></p>
    <p v-if="apply.status==='refuse'" class="status">处理状态： <el-badge type="danger" :value="apply.status"></el-badge></p>
    <el-row v-if="apply.status===null" class="status">
      <el-input v-if="showMsg" v-model="handleMsg" placeholder="请输入拒绝理由！"></el-input>
      <el-button size="small" type="success" @click="handleApplyProcess('agree')">同意</el-button>
      <el-button size="small" type="danger" @click="handleApplyProcess('refuse')">拒绝</el-button>
    </el-row>
  </el-card>
</template>

<script>
import { changeApplyStatus } from '../api/api'

export default {
  name: 'ApplyCard',
  props: {
    apply: null
  },
  data () {
    return {
      handleMsg: '',
      showMsg: false
    }
  },
  methods: {
    handleApplyProcess (status) {
      if (status === 'refuse') {
        this.showMsg = true
        if (this.handleMsg === '') {
          return
        }
      }
      if (status === 'agree') {
        this.showMsg = false
        this.handleMsg = ''
      }
      changeApplyStatus({ apply_id: this.apply.id, status: status, handle_msg: this.handleMsg }).then(
        (response) => {
          this.apply.status = status
        }
      ).catch((error) => {
        console.log(error.response)
      })
    }
  }
}
</script>

<style scoped>
  .msg-card {
    margin-bottom: 8px;
  }
  .info {
    padding: 0;
    margin: 10px;
  }
  .msg {
    margin-left: 16px;
  }
  .status {
    float: right;
    padding: 0;
    margin: 4px;
  }
</style>
