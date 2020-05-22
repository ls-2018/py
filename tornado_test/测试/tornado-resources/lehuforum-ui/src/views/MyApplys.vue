<template>
  <el-row>
    <apply-card v-for="(item,index) in applysList" :key="index" :apply="item"></apply-card>
  </el-row>
</template>

<script>
import { getUserApplys } from '../api/api'
import ApplyCard from '../components/ApplyCard'
export default {
  name: 'MyApplys',
  components: { ApplyCard },
  data () {
    return {
      applysList: []
    }
  },
  methods: {
    obtainApplysList () {
      getUserApplys({}).then(
        (response) => {
          this.applysList = response.data
          console.log(this.applysList)
        }
      ).catch((error) => {
        console.log(error.response)
      })
    }
  },
  mounted () {
    this.obtainApplysList()
  }
}
</script>

<style scoped>

</style>
