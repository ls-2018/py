<template>
  <el-row :gutter="16">
    <el-col :span="8" v-for="(item, index) in groupList" :key="index">
      <group-card :group="item"></group-card>
    </el-col>
  </el-row>
</template>

<script>
import { getCommunityGroups } from '../api/api'
import cookie from '../store/cookie'
import GroupCard from '../components/GroupCard'

export default {
  name: 'MyGroups',
  components: { GroupCard },
  data () {
    return {
      userid: null,
      groupList: []
    }
  },
  methods: {
    obtainGroupList (userid) {
      getCommunityGroups({ params: { userid: userid } }).then(
        (response) => {
          this.groupList = response.data
        }
      ).catch((error) => {
        console.log(error.response)
      })
    }
  },
  mounted () {
    this.userId = cookie.getCookie('userid')
    if (this.userId) {
      this.obtainGroupList(this.userId)
    }
  }
}
</script>

<style scoped>

</style>
